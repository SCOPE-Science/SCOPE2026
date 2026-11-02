"""Independent exhaustive checks for simultaneous square-one elements in incidence algebras.

Run: python verify.py ; requires Python 3 standard library only.
"""
from itertools import product


def predicted(n, edges, q, k):
    palette = 1 << k
    return sum(q ** sum(col[i] != col[j] for i, j in edges)
               for col in product(range(palette), repeat=n))


def actual(n, edges, q, maxk):
    positions = [(i, i) for i in range(n)] + list(edges)
    def to_matrix(vals):
        a = [[0] * n for _ in range(n)]
        for (i, j), v in zip(positions, vals):
            a[i][j] = v
        return tuple(tuple(row) for row in a)
    def mul(a, b):
        return tuple(tuple(sum(a[i][h] * b[h][j] for h in range(n)) % q
                     for j in range(n)) for i in range(n))
    unit = tuple(tuple(int(i == j) for j in range(n)) for i in range(n))
    invol = [a for vals in product(range(q), repeat=len(positions))
             if (a := to_matrix(vals)) and mul(a, a) == unit]
    commuting = [[mul(a, b) == mul(b, a) for b in invol] for a in invol]
    ret = [1, len(invol)]
    if maxk >= 2:
        ret.append(sum(map(sum, commuting)))
    if maxk >= 3:
        ret.append(sum(commuting[i][j] and commuting[i][k] and commuting[j][k]
                       for i in range(len(invol))
                       for j in range(len(invol))
                       for k in range(len(invol))))
    for k, observed in enumerate(ret):
        wanted = predicted(n, edges, q, k)
        assert observed == wanted, (n, edges, q, k, observed, wanted)
    return ret


def verify():
    cases = [
        ('two-chain', 2, [(0, 1)], 3, 3),
        ('three-chain', 3, [(0, 1), (0, 2), (1, 2)], 3, 3),
        ('vee', 3, [(0, 1), (0, 2)], 3, 3),
        ('inverted-vee', 3, [(0, 2), (1, 2)], 3, 3),
        ('two-disjoint-chains', 4, [(0, 1), (2, 3)], 3, 2),
        ('three-chain-q5', 3, [(0, 1), (0, 2), (1, 2)], 5, 2),
    ]
    for title, n, edges, q, maxk in cases:
        counts = actual(n, edges, q, maxk)
        print('EXHAUSTIVE_OK', title, 'q=', q, 'k=0..', maxk, counts)
    # Exact finite polynomial identity against finite-color enumeration.
    for n, edges in [
        (3, [(0, 1), (0, 2)]),
        (3, [(0, 1), (0, 2), (1, 2)]),
        (4, [(0, 1), (0, 2), (1, 3)]),
    ]:
        m = len(edges)
        for q in (3, 5, 7):
            for k in (0, 1, 2, 3):
                palette = 2 ** k
                graph_sum = 0
                for mask in range(1 << m):
                    adj = [set() for _ in range(n)]
                    for j, (u, v) in enumerate(edges):
                        if mask >> j & 1:
                            adj[u].add(v)
                            adj[v].add(u)
                    unseen = set(range(n))
                    comps = 0
                    while unseen:
                        comps += 1
                        stack = [unseen.pop()]
                        while stack:
                            for w in adj[stack.pop()] & unseen:
                                unseen.remove(w)
                                stack.append(w)
                    size = mask.bit_count()
                    graph_sum += q ** (m - size) * (1 - q) ** size * palette ** comps
                assert graph_sum == predicted(n, edges, q, k)
    print('POTTS_IDENTITY_OK 36')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
