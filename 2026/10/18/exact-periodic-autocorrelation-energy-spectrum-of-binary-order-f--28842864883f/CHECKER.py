"""Exact finite enumeration for periodic autocorrelation energy of binary order-5 de Bruijn cycles.

Only the Python standard library is needed. The pairing and depth-first engines
produce the 2048 cycles independently; neither assumes the target histogram.
"""
from collections import Counter
from fractions import Fraction
from statistics import mean

HISTOGRAM = {
    192:12,224:12,256:12,288:12,320:44,352:32,384:96,416:72,
    448:100,480:72,512:136,544:132,576:112,608:66,640:146,
    672:126,704:104,736:52,768:74,800:74,832:76,864:52,
    896:66,928:40,960:18,992:30,1024:26,1056:8,1088:32,
    1120:38,1152:16,1184:20,1216:18,1248:10,1280:20,
    1312:20,1344:12,1408:2,1440:8,1472:4,1504:8,1600:8,
    1632:4,1664:10,1696:8,1888:4,1952:4,
}


def cycles_by_pairings():
    # Vertices are 4-bit words v. Incoming 5-bit edges: v, v+16.
    # Outgoing edges: 2*v, 2*v+1. Each switch chooses one of the
    # two bijections between incoming and outgoing edges at v.
    for switches in range(1 << 16):
        successor = [0] * 32
        for v in range(16):
            flip = (switches >> v) & 1
            successor[v] = (v << 1) | flip
            successor[v + 16] = (v << 1) | (1 - flip)
        visited = 0
        edge = 0   # unique 00000 edge fixes cyclic rotation
        bits = []
        for _ in range(32):
            if (visited >> edge) & 1:
                break
            visited |= 1 << edge
            bits.append(edge >> 4)
            edge = successor[edge]
        if edge == 0 and visited == (1 << 32) - 1:
            yield tuple(bits)


def cycles_by_dfs():
    # Independent Euler-tour backtracking on 5-bit edges.
    bits = [0] * 32
    def rec(edge, used, depth):
        bits[depth] = edge >> 4
        used |= 1 << edge
        if depth == 31:
            if edge & 15 == 0:
                yield tuple(bits)
            return
        new_head = (edge & 15) << 1
        for next_edge in (new_head, new_head + 1):
            if not ((used >> next_edge) & 1):
                yield from rec(next_edge, used, depth + 1)
    yield from rec(0, 0, 0)


def is_debruijn_5(word):
    doubled = word + word
    return len(word) == 32 and len({tuple(doubled[i:i + 5]) for i in range(32)}) == 32


def corr_profile(word):
    # Direct signed cyclic correlation, no spectral transform assumptions.
    return [sum(1 if word[i] == word[(i + t) & 31] else -1 for i in range(32))
            for t in range(1, 32)]


def energy(word):
    return sum(r * r for r in corr_profile(word))


def rotated_canonical(word):
    return min(word[j:] + word[:j] for j in range(32))


def dihedral_complement_orbits(words):
    remaining = set(words)
    out = []
    while remaining:
        w = min(remaining)
        group = {rotated_canonical(tuple(v)) for v in (
            w, tuple(reversed(w)), tuple(1 - b for b in w),
            tuple(1 - b for b in reversed(w)))}
        assert group.issubset(remaining)
        out.append(group)
        remaining -= group
    return out


def main():
    A = list(cycles_by_pairings())
    B = list(cycles_by_dfs())
    assert len(A) == len(set(A)) == len(B) == len(set(B)) == 2048
    assert set(A) == set(B)
    assert all(is_debruijn_5(w) for w in A)
    hist = Counter(energy(w) for w in A)
    assert dict(hist) == HISTOGRAM
    assert sum(hist.values()) == 2048 and len(hist) == 47
    assert min(hist) == 192 and max(hist) == 1952
    assert all(k % 32 == 0 for k in hist)
    assert sum(e * count for e, count in hist.items()) == 1440256
    assert Fraction(sum(e * count for e, count in hist.items()), 2048) == Fraction(2813, 4)
    assert Fraction(sum(e * e * count for e, count in hist.items()), 2048) == 578100
    assert Fraction(578100) - Fraction(2813, 4) ** 2 == Fraction(1336631, 16)
    low = [w for w in A if energy(w) == 192]
    high = [w for w in A if energy(w) == 1952]
    assert len(low) == 12 and len(high) == 4
    assert sorted(map(len, dihedral_complement_orbits(low))) == [4, 4, 4]
    assert sorted(map(len, dihedral_complement_orbits(high))) == [4]
    max_lag = {w: max(abs(v) for v in corr_profile(w)) for w in A}
    assert sum(p <= 4 for p in max_lag.values()) == 12
    assert sum(p <= 8 for p in max_lag.values()) == 784
    # Matches all three *rounded* published average normalized RMS sidelobes.
    norm_rms = {w: (energy(w) / 31) ** .5 / 32 for w in A}
    assert round(mean(norm_rms.values()), 3) == .146
    assert round(mean(v for w, v in norm_rms.items() if max_lag[w] <= 8), 3) == .123
    assert round(mean(v for w, v in norm_rms.items() if max_lag[w] <= 4), 3) == .078
    # Elementary Fourier/periodic identities: all low shifts vanish.
    assert all(all(x == 0 for x in corr_profile(w)[:4]) for w in A)
    print('ORDER5_DEBRUIJN_ENERGY_PASS cycles=2048 switches=65536 energies=47 '
          'min=192:12 max=1952:4 mean=2813/4 variance=1336631/16')


if __name__ == '__main__':
    main()
