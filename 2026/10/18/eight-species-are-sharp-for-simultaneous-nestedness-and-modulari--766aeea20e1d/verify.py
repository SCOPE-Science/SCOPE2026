"""Exact exhaustive certificate for nestedness/modularity under bipartite swaps.
Python >= 3.9; standard library only. Run: python verify.py
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb


def graph(bits, p, a):
    rows = tuple(frozenset(j for j in range(a) if bits & (1 << (i * a + j))) for i in range(p))
    return rows


def connected(rows, a):
    p = len(rows)
    if any(not s for s in rows):
        return False
    reached = {0}
    queue = [0]
    while queue:
        u = queue.pop()
        if u < p:
            neighbors = (p + v for v in rows[u])
        else:
            neighbors = (i for i in range(p) if u - p in rows[i])
        for v in neighbors:
            if v not in reached:
                reached.add(v)
                queue.append(v)
    return len(reached) == p + a


def nestedness(rows, a):
    p = len(rows)
    cols = tuple(frozenset(i for i in range(p) if j in rows[i]) for j in range(a))
    pair_contributions = []
    for guild in (rows, cols):
        for u, v in combinations(guild, 2):
            lo = min(len(u), len(v))
            hi = max(len(u), len(v))
            if hi > lo and lo > 0:
                pair_contributions.append(Fraction(len(u & v), lo))
    return sum(pair_contributions, Fraction(0)) / (comb(p, 2) + comb(a, 2))


def modularity_num(rows, a):
    """Maximize Newman-Girvan Q; return exact integer 4m^2 Q.

    Partition dynamic program: each block containing the least vertex is
    enumerated exactly once, so every set partition is covered.
    """
    p = len(rows)
    n = p + a
    neighbors = [set() for _ in range(n)]
    for i, s in enumerate(rows):
        for j in s:
            neighbors[i].add(p + j)
            neighbors[p + j].add(i)
    m = sum(map(len, rows))
    deg = [len(x) for x in neighbors]
    ds = [0] * (1 << n)
    inside = [0] * (1 << n)
    weight = [0] * (1 << n)
    for mask in range(1, 1 << n):
        bit = mask & -mask
        v = bit.bit_length() - 1
        prev = mask ^ bit
        ds[mask] = ds[prev] + deg[v]
        inside[mask] = inside[prev] + sum((prev >> u) & 1 for u in neighbors[v])
        weight[mask] = 4 * m * inside[mask] - ds[mask] ** 2
    @lru_cache(None)
    def best(mask):
        if mask == 0:
            return (0, ())
        bit = mask & -mask
        optimum = None
        subset = mask
        while subset:
            if subset & bit:
                tailvalue, blocks = best(mask ^ subset)
                candidate = (weight[subset] + tailvalue, (subset,) + blocks)
                if optimum is None or candidate[0] > optimum[0]:
                    optimum = candidate
            subset = (subset - 1) & mask
        return optimum
    return best((1 << n) - 1)


def swap_neighbors(bits, p, a):
    """All degree-preserving two-by-two switches, with no duplicate switch choice."""
    for i, k in combinations(range(p), 2):
        for j, ell in combinations(range(a), 2):
            ij, iell, kj, kell = (1 << (x * a + y) for x, y in ((i, j), (i, ell), (k, j), (k, ell)))
            block = ij | iell | kj | kell
            pattern = bits & block
            if pattern == (ij | kell) or pattern == (iell | kj):
                yield bits ^ block


def exhaustive_small():
    totals = []
    for n in range(3, 8):
        for p in range(1, n // 2 + 1):
            a = n - p
            connected_bits = []
            scores = {}
            for bits in range(1 << (p * a)):
                if bits.bit_count() < n - 1:
                    continue
                rows = graph(bits, p, a)
                if connected(rows, a):
                    connected_bits.append(bits)
                    scores[bits] = (nestedness(rows, a), modularity_num(rows, a)[0])
            events = good = opposite = 0
            for bits in connected_bits:
                for nxt in swap_neighbors(bits, p, a):
                    if nxt not in scores:
                        continue
                    events += 1
                    dn = scores[nxt][0] - scores[bits][0]
                    dq = scores[nxt][1] - scores[bits][1]
                    if dn > 0 and dq > 0:
                        good += 1
                    if dn and dq and ((dn > 0) != (dq > 0)):
                        opposite += 1
            print(f'n={n} guilds={p}+{a} connected={len(connected_bits)} directed_swaps={events} coimprove={good} opposed={opposite}')
            assert good == 0
            totals.append((n, p, a, len(connected_bits), events, opposite))
    return totals


def brute_modularity(rows, a):
    """Independent unrestricted-growth-label partition enumeration for witness."""
    p = len(rows)
    n = p + a
    m = sum(map(len, rows))
    degrees = [len(s) for s in rows] + [sum(j in s for s in rows) for j in range(a)]
    adjacency = {(i, p+j) for i, s in enumerate(rows) for j in s}
    maximum = -10**9
    optimum = None
    count = 0
    def rec(labels, maxlabel):
        nonlocal maximum, optimum, count
        if len(labels) == n:
            count += 1
            group_degrees = [0] * (maxlabel+1)
            group_edges = [0] * (maxlabel+1)
            for i, k in enumerate(labels):
                group_degrees[k] += degrees[i]
            for i, j in adjacency:
                if labels[i] == labels[j]:
                    group_edges[labels[i]] += 1
            value = sum(4*m*e - d*d for e, d in zip(group_edges, group_degrees))
            if value > maximum:
                maximum, optimum = value, labels
            return
        for label in range(maxlabel + 2):
            rec(labels + (label,), max(maxlabel, label))
    rec((0,), 0)
    assert count == 4140
    return maximum, optimum, count


def witness():
    p, a = 3, 5
    before = ('01111', '10100', '11000')
    after = ('11101', '00110', '11000')
    def parse(lines):
        return tuple(frozenset(i for i, val in enumerate(s) if val == '1') for s in lines)
    u, v = parse(before), parse(after)
    assert connected(u, a) and connected(v, a)
    assert [len(x) for x in u] == [len(x) for x in v]
    assert [sum(j in s for s in u) for j in range(a)] == [sum(j in s for s in v) for j in range(a)]
    assert len({(i,j) for i,s in enumerate(u) for j in s} ^ {(i,j) for i,s in enumerate(v) for j in s}) == 4
    for tag, rows in [('before', u), ('after', v)]:
        N = nestedness(rows, a)
        max_integer, optimal_blocks = modularity_num(rows, a)
        brut, labels, n_partitions = brute_modularity(rows, a)
        assert max_integer == brut
        Q = Fraction(max_integer, 4 * sum(map(len, rows))**2)
        print(f'{tag} NODF={N} max_modularity={Q} integer={max_integer} example_optimal_labels={labels}; checked_partitions={n_partitions}')
    assert nestedness(v, a) - nestedness(u, a) == Fraction(1,26)
    assert modularity_num(v, a)[0] - modularity_num(u, a)[0] == 6
    print('witness differences: nestedness +1/26; modularity +3/128')

if __name__ == '__main__':
    exhaustive_small()
    witness()
    print('ALL CHECKS PASSED')
