"""Exact forcing/anti-forcing census for perfect matchings of the four-cube.

Run with: python3 verify.py
Uses only the Python standard library; completes the full finite verification.
"""
from collections import Counter
from itertools import combinations, permutations

N = 16
V = tuple(range(N))
ADJ = tuple(tuple(v ^ (1 << b) for b in range(4)) for v in V)
EVEN = tuple(v for v in V if v.bit_count() % 2 == 0)
ODD = tuple(v for v in V if v.bit_count() % 2 == 1)


def enum_matchings():
    out = []
    def rec(mask, edges):
        if not mask:
            out.append(tuple(sorted(edges)))
            return
        v = (mask & -mask).bit_length() - 1
        for w in ADJ[v]:
            if mask & (1 << w):
                rec(mask ^ (1 << v) ^ (1 << w), edges + [(min(v,w), max(v,w))])
    rec((1 << N) - 1, [])
    return tuple(sorted(out))


def permanent_count():
    # Independently count all bipartite perfect matchings by subset DP.
    index = {v: j for j, v in enumerate(ODD)}
    dp = [0] * (1 << 8)
    dp[0] = 1
    for mask in range(1 << 8):
        row = mask.bit_count()
        if row == 8:
            continue
        for w in ADJ[EVEN[row]]:
            j = index[w]
            if not mask >> j & 1:
                dp[mask | (1 << j)] += dp[mask]
    return dp[-1]


def forcing_profile(matchings):
    # Complete search over the 2^8 subsets of each matching, testing uniqueness.
    ans = []
    for m in matchings:
        competing = [set(m) - set(n) for n in matchings if n != m]
        for size in range(9):
            wins = sum(all(not block.isdisjoint(s) for block in competing)
                       for s in map(frozenset, combinations(m, size)))
            if wins:
                ans.append((size, wins))
                break
    return tuple(ans)


def arc_table(m):
    matched = {v: k for k, pair in enumerate(m) for v in pair}
    arcs = [[0] * 8 for _ in range(8)]
    for u in EVEN:
        for v in ADJ[u]:
            i, j = matched[u], matched[v]
            if i != j:
                arcs[i][j] += 1
    assert sum(map(sum, arcs)) == 24
    return arcs


def anti_forcing_dp(m):
    # Maximum number of nonmatching directed arcs kept acyclic.
    arcs = arc_table(m)
    best = [-1000] * 256
    best[0] = 0
    for mask in range(1, 256):
        best[mask] = max(best[mask ^ (1 << j)] +
                         sum(arcs[i][j] for i in range(8)
                             if (mask ^ (1 << j)) & (1 << i))
                         for j in range(8) if mask & (1 << j))
    return 24 - best[255]


def anti_forcing_orders(m):
    # Independent algorithm: all 8! linear orders, for one representative/orbit.
    arcs = arc_table(m)
    maximum = 0
    for order in permutations(range(8)):
        rank = {v: i for i, v in enumerate(order)}
        forward = sum(arcs[i][j] for i in range(8) for j in range(8)
                      if rank[i] < rank[j])
        if forward > maximum:
            maximum = forward
    return 24 - maximum


def symmetry_orbits(matchings):
    locate = {m: i for i, m in enumerate(matchings)}
    seen = set()
    perms = tuple(permutations(range(4)))
    transformations = []
    for p in perms:
        base = [sum(((v >> k) & 1) << p[k] for k in range(4)) for v in V]
        for b in range(16):
            transformations.append(tuple(x ^ b for x in base))
    assert len(set(transformations)) == 384
    orbits = []
    for k, m in enumerate(matchings):
        if k in seen:
            continue
        orbit = set()
        for T in transformations:
            image = tuple(sorted((min(T[u], T[v]), max(T[u], T[v]))
                                 for u, v in m))
            orbit.add(locate[image])
        assert orbit.isdisjoint(seen)
        assert k in orbit
        seen.update(orbit)
        orbits.append((min(orbit), tuple(sorted(orbit))))
    assert len(seen) == 272
    return tuple(sorted(orbits, key=lambda p:(len(p[1]),p[0])))



def small_dimension_spectrum(d):
    # Direct independent enumeration for d=1,2,3; no Q4 helpers used.
    n = 1 << d
    edges = {u: [u ^ (1 << j) for j in range(d)] for u in range(n)}
    all_matchings = []
    def visit(left, chosen):
        if not left:
            all_matchings.append(tuple(chosen))
            return
        u = min(left)
        for v in edges[u]:
            if v in left:
                visit(left - {u,v}, chosen + [(u,v)])
    visit(set(range(n)), [])
    counts = Counter()
    for m in all_matchings:
        number = len(m)
        where = {u:j for j,e in enumerate(m) for u in e}
        arcs = [[0]*number for _ in range(number)]
        for u in range(n):
            if u.bit_count()%2 == 0:
                for v in edges[u]:
                    if where[u] != where[v]:
                        arcs[where[u]][where[v]] += 1
        dp = [0]*(1 << number)
        for mask in range(1, 1 << number):
            dp[mask] = max(dp[mask ^ (1 << j)] +
                           sum(arcs[i][j] for i in range(number)
                               if ((mask ^ (1 << j)) >> i) & 1)
                           for j in range(number) if (mask >> j) & 1)
        counts[sum(map(sum,arcs))-dp[-1]] += 1
    return counts

def main():
    assert small_dimension_spectrum(1) == {0:1}
    assert small_dimension_spectrum(2) == {1:2}
    assert small_dimension_spectrum(3) == {3:6,4:3}
    matches = enum_matchings()
    assert len(matches) == permanent_count() == 272
    forcing = forcing_profile(matches)
    af = tuple(anti_forcing_dp(m) for m in matches)
    assert Counter(k for k, z in forcing) == {4:272}
    assert Counter(af) == {8:196,10:72,12:4}
    orbits = symmetry_orbits(matches)
    assert len(orbits) == 8
    expected = [(4,12,2),(8,8,24),(12,8,12),(24,10,4),
                (32,8,18),(48,10,4),(48,8,8),(96,8,10)]
    actual = []
    for rep, inds in orbits:
        assert {af[k] for k in inds} == {af[rep]}
        assert {forcing[k] for k in inds} == {forcing[rep]}
        assert anti_forcing_orders(matches[rep]) == af[rep]
        actual.append((len(inds), af[rep], forcing[rep][1]))
    assert actual == expected, (actual, expected)
    assert sum(size for size, *_ in actual) == 272
    assert sum(size for size, a, c in actual if a == 12) == 4
    print('Q1,Q2,Q3 anti-forcing spectra: {0}, {1}, {3,4}')
    print('Q4 perfect matchings:', len(matches))
    print('forcing polynomial: 272 z^4')
    print('anti-forcing polynomial: 196 z^8 + 72 z^10 + 4 z^12')
    print('orbit size, anti-forcing number, number of minimum forcing sets:')
    for row in actual:
        print(*row)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
