#!/usr/bin/env python3
"""Exhaustive finite verification of a joint balance spectrum of de Bruijn cycles."""
from collections import Counter
from csv import DictReader
from pathlib import Path

ORDER = 5
EXPECTED = {(5, 6): 224, (6, 6): 304, (6, 7): 384,
            (7, 6): 48, (7, 7): 640, (7, 8): 224,
            (8, 8): 192, (8, 9): 32}
EXPECTED_ORBITS = {(5, 6): (8, 52), (6, 6): (0, 76),
                   (6, 7): (8, 92), (7, 6): (0, 12),
                   (7, 7): (0, 160), (7, 8): (12, 50),
                   (8, 8): (0, 48), (8, 9): (4, 6)}


def canonical(s):
    """Anchor at the unique zero-power factor (no generic orbit oracle)."""
    return min(s[i:] + s[:i] for i in range(len(s)))


def via_local_pairings(n):
    """Enumerate all possible incoming-to-outgoing pairings at each vertex."""
    N, vertices = 1 << n, 1 << (n - 1)
    incoming = [[] for _ in range(vertices)]
    for e in range(N):
        incoming[e & (vertices - 1)].append(e)
    out = set()
    for choice in range(1 << vertices):
        nxt = [-1] * N
        for v in range(vertices):
            t = (choice >> v) & 1
            nxt[incoming[v][0]] = 2 * v + t
            nxt[incoming[v][1]] = 2 * v + (1 - t)
        edge, used, bits = 0, set(), []
        for _ in range(N):
            if edge in used:
                break
            used.add(edge)
            bits.append(str(edge & 1))
            edge = nxt[edge]
        if len(bits) == N and edge == 0:
            out.add(canonical(''.join(bits)))
    return out


def via_eulerian_backtracking(n):
    """Independently visit every Euler circuit starting with the unique all-zero edge."""
    N, mask = 1 << n, (1 << (n - 1)) - 1
    found = set()
    # The word at each edge is the last bit of its n-bit edge label.
    def rec(v, used, bits):
        if used.bit_count() == N:
            if v == 0:
                found.add(canonical(''.join(bits)))
            return
        for b in (0, 1):
            edge = 2 * v + b
            if not (used >> edge) & 1:
                bits.append(str(b))
                rec(edge & mask, used | (1 << edge), bits)
                bits.pop()
    rec(0, 1, ['0'])
    return found


def direct_discrepancy(s):
    """Directly inspect every start and factor length on the circle."""
    N = len(s)
    diff = [2 * int(c) - 1 for c in s]
    mx = 0
    for i in range(N):
        acc = 0
        for L in range(N):
            acc += diff[(i + L) % N]
            mx = max(mx, abs(acc))
    return mx


def prefix_discrepancy(s):
    """Balanced-circle prefix-walk range formula."""
    x, vals = 0, [0]
    for c in s:
        x += 2 * int(c) - 1
        vals.append(x)
    assert x == 0
    return max(vals) - min(vals)


def abelian_peak_by_sets(s):
    """Each position and length independently forms a Parikh count."""
    N = len(s)
    peak = 0
    for L in range(1, N):
        sums = set()
        for i in range(N):
            sums.add(sum(int(s[(i + j) % N]) for j in range(L)))
        peak = max(peak, len(sums))
    return peak


def abelian_peak_by_sliding(s):
    """Second evaluation via sliding window extrema, not Parikh-set materialization."""
    N = len(s)
    bits = list(map(int, s))
    peak = 0
    for L in range(1, N):
        k = sum(bits[:L])
        lo = hi = k
        for i in range(1, N):
            k += bits[(i + L - 1) % N] - bits[i - 1]
            lo, hi = min(lo, k), max(hi, k)
        peak = max(peak, hi - lo + 1)
    return peak


def sym_orbit(s):
    complement = lambda t: ''.join('1' if c == '0' else '0' for c in t)
    return {canonical(t) for t in [s, s[::-1], complement(s), complement(s[::-1])]}


def run():
    a = via_local_pairings(ORDER)
    b = via_eulerian_backtracking(ORDER)
    assert len(a) == len(b) == 2048 and a == b
    joint = Counter()
    for s in sorted(a):
        assert len(s) == 32
        assert len({''.join(s[(i + j) % 32] for j in range(5)) for i in range(32)}) == 32
        d = prefix_discrepancy(s)
        assert d == direct_discrepancy(s)
        p = abelian_peak_by_sets(s)
        assert p == abelian_peak_by_sliding(s)
        assert p <= d + 1
        joint[(d, p)] += 1
    assert dict(joint) == EXPECTED
    orbits = Counter()
    covered = set()
    for s in sorted(a):
        if s in covered:
            continue
        orb = sym_orbit(s)
        assert orb <= a and len(orb) in (2, 4)
        covered |= orb
        orbits[(prefix_discrepancy(s), abelian_peak_by_sliding(s), len(orb))] += 1
    assert covered == a
    for cell, (two, four) in EXPECTED_ORBITS.items():
        assert orbits[cell + (2,)] == two
        assert orbits[cell + (4,)] == four
        assert 2 * two + 4 * four == EXPECTED[cell]
    assert sum(orbits.values()) == 528
    # Replay each machine-readable table row, including its concrete witness.
    with (Path(__file__).resolve().parent / 'spectrum.csv').open(newline='') as stream:
        csv_rows = list(DictReader(stream))
    assert len(csv_rows) == 8
    assert {(int(row['discrepancy']), int(row['peak_abelian_complexity'])) for row in csv_rows} == set(EXPECTED)
    for row in csv_rows:
        cell = int(row['discrepancy']), int(row['peak_abelian_complexity'])
        assert int(row['cycles']) == EXPECTED[cell]
        assert (int(row['symmetry_orbits_size_2']), int(row['symmetry_orbits_size_4'])) == EXPECTED_ORBITS[cell]
        witness = row['lexicographically_least_witness']
        assert witness in a and (prefix_discrepancy(witness), abelian_peak_by_sliding(witness)) == cell
        assert witness == min(s for s in a if (prefix_discrepancy(s), abelian_peak_by_sliding(s)) == cell)
    # Lower-order baseline, a cross-check against the canonical de Bruijn count.
    baseline = [1, 1, 2, 16, 2048]
    for n, cnt in zip(range(1, 6), baseline):
        assert len(via_local_pairings(n)) == cnt
    print('VERIFY_OK independent_euler_and_pairing_generators=2048 '
          'pairings_tested=65536 independent_discrepancy_algorithms=2 '
          'independent_abelian_peak_algorithms=2 rooted_windows_tested=2031616 '
          'joint_cells=8 symmetry_orbits=528 '
          'histogram=' + ','.join(f'{d}-{p}:{n}' for (d, p), n in sorted(joint.items())))

if __name__ == '__main__':
    run()
