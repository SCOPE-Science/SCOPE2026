"""Independent finite checks for Fermat-companion semigroup pseudo-Frobenius formula.

The universal classification is proved symbolically; these checks cover only
specified finite ranges and are not a proof for all n.
"""
from heapq import heappop, heappush


def shortest_apery(modulus, generators):
    d = [None] * modulus
    d[0] = 0
    heap = [(0, 0)]
    while heap:
        weight, residue = heappop(heap)
        if d[residue] != weight:
            continue
        for g in generators:
            r = (residue + g) % modulus
            v = weight + g
            if d[r] is None or v < d[r]:
                d[r] = v
                heappush(heap, (v, r))
    assert all(x is not None for x in d)
    return d


def greedy_counts(h, max_r):
    coins = [(1 << i) - 1 for i in range(1, h + 1)]
    out = []
    for r in range(max_r + 1):
        t, v = 0, r
        for c in coins[::-1]:
            q, v = divmod(v, c)
            t += q
        assert v == 0
        out.append(t)
    return out


def verify():
    lemma_tests = 0
    for h in range(1, 13):
        c = (1 << h) - 1
        counts = greedy_counts(h, 2 * c)
        local_maxima = [r for r in range(2 * c + 1)
                         if all(r + ((1 << i) - 1) > 2 * c
                                or counts[r + ((1 << i) - 1)] <= counts[r]
                                for i in range(1, h + 1))]
        assert local_maxima == list(range(2 * c - h + 1, 2 * c + 1)), (h, local_maxima)
        for q in range(h):
            assert counts[2 * c - q] == q + 2, (h, q)
        lemma_tests += len(counts)
    checks = 0
    for n in range(3, 12):
        a = (1 << n) + 1
        gens = [a] + [((1 << i) * (a + 1) - 1) for i in range(1, n)]
        w = shortest_apery(a, gens[1:])
        def member(z):
            return z >= 0 and z >= w[z % a]
        pf = sorted(w[r] - a for r in range(1, a)
                    if all(member(w[r] - a + g) for g in gens[1:]))
        target = sorted([a * a + 3 * a - 1] +
                        [a * a - a - 1 - j for j in range(4, n + 1)])
        assert pf == target, (n, pf, target)
        counts = greedy_counts(n - 1, a - 1)
        assert all(w[r] == (a + 1) * r + a * counts[r]
                   for r in range(a)), n
        checks += a
    print(f'PASS: {lemma_tests} greedy cutoff tests; '
          f'{checks} Apéry entries; n=3..11, h=1..12')

if __name__ == '__main__':
    verify()
