#!/usr/bin/env python3
"""Exact exhaustive classification of spectra and tilings on Z/8 x Z/2.
No external libraries, numerical tolerances, or external data files.
Run: python3 verify.py
Coordinates x+8*y identify (x mod 8,y mod 2).
"""
from collections import Counter, defaultdict
from itertools import combinations
import json
from math import comb

N = 16
M = 1 << N
ALL_D = (1 << (N - 1)) - 1
SIZES = (1, 2, 4, 8, 16)
ALL_SIZES = tuple(range(1, N + 1))

def plus(x, y):
    return ((x % 8 + y % 8) % 8) + 8 * ((x // 8 + y // 8) % 2)

def minus(x, y):
    return ((x % 8 - y % 8) % 8) + 8 * ((x // 8 - y // 8) % 2)

def elements(mask):
    while mask:
        b = mask & -mask
        yield b.bit_length() - 1
        mask ^= b

def difference_mask(mask):
    points = list(elements(mask))
    result = 0
    for x in points:
        for y in points:
            if x != y:
                result |= 1 << (minus(x, y) - 1)
    return result

def zeros(mask):
    points = list(elements(mask))
    result = 0
    for frequency in range(1, N):
        counts = [0] * 8
        for point in points:
            counts[(frequency % 8 * (point % 8) +
                    4 * (frequency // 8) * (point // 8)) % 8] += 1
        if all(counts[i] == counts[i + 4] for i in range(4)):
            result |= 1 << (frequency - 1)
    return result

def zeta(hist):
    for j in range(N - 1):
        flag = 1 << j
        for s in range(1 << (N - 1)):
            if s & flag:
                hist[s] += hist[s ^ flag]

# Recurrence: differences of C ∪ {i} are old differences plus ±(i-j).
differences = [0] * M
for mask in range(1, M):
    pivot_bit = mask & -mask
    i = pivot_bit.bit_length() - 1
    rest = mask ^ pivot_bit
    d = differences[rest]
    for j in elements(rest):
        d |= (1 << (minus(i, j) - 1)) | (1 << (minus(j, i) - 1))
    differences[mask] = d

# Every Fourier-zero predicate uses exact Phi_8 divisibility, not floating point.
zero_sets = [0] * M
for mask in range(1, M):
    zero_sets[mask] = zeros(mask)

histograms = {k: [0] * (1 << (N - 1)) for k in ALL_SIZES}
for mask in range(1, M):
    k = mask.bit_count()
    histograms[k][differences[mask]] += 1
for k in ALL_SIZES:
    zeta(histograms[k])

spectra = [0] * M
tile_complements = [0] * M
profiles = {}
for k in SIZES:
    sdist = Counter()
    tdist = Counter()
    for mask in range(1, M):
        if mask.bit_count() != k:
            continue
        a = histograms[k][zero_sets[mask]]
        b = histograms[N // k][ALL_D ^ differences[mask]]
        assert (a > 0) == (b > 0)
        spectra[mask] = a
        tile_complements[mask] = b
        sdist[a] += 1
        tdist[b] += 1
    assert sum(sdist.values()) == comb(N, k)
    profiles[str(k)] = {
        'subsets': comb(N, k),
        'spectral_sets': sum(v for x, v in sdist.items() if x),
        'spectra_multiplicity': dict(sorted(sdist.items())),
        'tile_complement_multiplicity': dict(sorted(tdist.items()))
    }
# Exhaustively rule out every other cardinality without using a tiling theorem.
for k in ALL_SIZES:
    if k not in SIZES:
        assert all(histograms[k][zero_sets[mask]] == 0
                   for mask in range(1, M) if mask.bit_count() == k)
assert sum(z['spectral_sets'] for z in profiles.values()) == 1611
assert [profiles[str(k)]['spectral_sets'] for k in SIZES] == [16, 120, 732, 742, 1]

# Independent brute-force tests using direct sets of elements, not recurrence.
for mask in range(1, M):
    if mask.bit_count() in (1, 2, 4, 8, 16) and (mask <= 1024 or mask % 97 == 0):
        assert difference_mask(mask) == differences[mask]

freq_spectra = {k: [m for m in range(1, M) if m.bit_count() == k and spectra[m]] for k in SIZES}
for k in (2, 4, 8):
    test_sets = freq_spectra[k]
    bs = [b for b in range(1, M) if b.bit_count() == k]
    for a in test_sets:
        z = zero_sets[a]
        assert sum(1 for b in bs if differences[b] & ~z == 0) == spectra[a]

# All sixteen group automorphisms, followed by the sixteen translations.
automorphisms = []
for a in (1, 3, 5, 7):
    for b in (0, 1):
        for c in (0, 4):
            perm = [((a*x+c*y) % 8) + 8*((b*x+y) % 2)
                    for y in range(2) for x in range(8)]
            assert len(set(perm)) == N
            automorphisms.append(perm)
assert len(automorphisms) == 16
perms = [[plus(perm[x], t) for x in range(N)]
         for perm in automorphisms for t in range(N)]
assert len({tuple(p) for p in perms}) == 256

def image_of(mask, perm):
    result = 0
    for x in elements(mask):
        result |= 1 << perm[x]
    return result

orbits = {}
for k in SIZES:
    visited = set()
    records = []
    for mask in freq_spectra[k]:
        if mask in visited:
            continue
        orbit = {image_of(mask, perm) for perm in perms}
        assert orbit.isdisjoint(visited)
        assert len(orbit) <= 256
        assert all(spectra[other] == spectra[mask] and
                   tile_complements[other] == tile_complements[mask]
                   for other in orbit)
        visited.update(orbit)
        records.append({
            'representative_indices': list(elements(mask)),
            'affine_orbit_size': len(orbit),
            'number_of_spectra': spectra[mask],
            'number_of_tiling_complements': tile_complements[mask]
        })
    assert len(visited) == len(freq_spectra[k])
    records.sort(key=lambda x: (x['number_of_spectra'],
                                x['affine_orbit_size'],
                                x['representative_indices']))
    orbits[str(k)] = records
assert [len(orbits[str(k)]) for k in SIZES] == [1, 5, 17, 19, 1]
assert sum(map(len, orbits.values())) == 43

# Non-divisor cardinalities were excluded by exhaustive orthogonality testing.
output = {
    'group': 'Z/8 x Z/2',
    'total_nonempty_spectral_sets': 1611,
    'affine_orbit_count': 43,
    'profiles': profiles,
    'affine_orbits': orbits
}
print(json.dumps(output, sort_keys=True, indent=2))
