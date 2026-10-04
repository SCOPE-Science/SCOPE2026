from itertools import combinations, product
from collections import Counter
from fractions import Fraction

def rank_mod(A, p):
    A = [[x % p for x in row] for row in A]
    m = len(A)
    n = len(A[0]) if m else 0
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c] % p), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][c], -1, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] % p:
                z = A[i][c] % p
                A[i] = [(A[i][j] - z * A[r][j]) % p for j in range(n)]
        r += 1
        if r == m:
            break
    return r

def alt_matrix(n, edges, values, p):
    A = [[0] * n for _ in range(n)]
    for (u, v), z in zip(edges, values):
        A[u][v] = z % p
        A[v][u] = (-z) % p
    return A

def rank_counts(n, edges, p):
    out = Counter()
    for values in product(range(p), repeat=len(edges)):
        r = rank_mod(alt_matrix(n, edges, values, p), p)
        assert r % 2 == 0
        out[r // 2] += 1
    assert sum(out.values()) == p ** len(edges)
    return out

def cone_edges(n, edges):
    return list(edges) + [(v, n) for v in range(n)]

def matrix_rank_count(a, b, r, q):
    if r < 0 or r > min(a, b):
        return 0
    if r == 0:
        return 1
    z = Fraction(1, 1)
    for j in range(r):
        z *= Fraction((q ** a - q ** j) * (q ** b - q ** j), q ** r - q ** j)
    assert z.denominator == 1
    return z.numerator

def tripartite_edges(a, b):
    # singleton part {0}, A={1,...,a}, B={a+1,...,a+b}
    edges = [(0, v) for v in range(1, a + b + 1)]
    edges += [(u, v) for u in range(1, a + 1)
                      for v in range(a + 1, a + b + 1)]
    return edges

# Exhaustive cone recurrence for every graph on <= 4 vertices.
for n in range(1, 5):
    possible = list(combinations(range(n), 2))
    for mask in range(1 << len(possible)):
        edges = [e for j, e in enumerate(possible) if (mask >> j) & 1]
        for q in (2, 3):
            old = rank_counts(n, edges, q)
            new = rank_counts(n + 1, cone_edges(n, edges), q)
            top = (n + 1) // 2 + 1
            for i in range(top + 1):
                expected = (q ** (2 * i)) * old.get(i, 0)
                if i >= 1:
                    expected += (q ** n - q ** (2 * i - 2)) * old.get(i - 1, 0)
                assert new.get(i, 0) == expected, (n, edges, q, i, new, old)

# Explicit complete-tripartite formula and character sum of squares.
for a in (1, 2):
    for b in (1, 2):
        n = 1 + a + b
        edges = tripartite_edges(a, b)
        for q in (2, 3):
            counts = rank_counts(n, edges, q)
            for r in range((n // 2) + 2):
                expected = (q ** (2 * r)) * matrix_rank_count(a, b, r, q)
                if r >= 1:
                    expected += (
                        q ** (a + b) - q ** (2 * r - 2)
                    ) * matrix_rank_count(a, b, r - 1, q)
                assert counts.get(r, 0) == expected, (a, b, q, r, counts, expected)

            # ch(r)=q^(n-2r)*rho_r and sum ch(r)*q^(2r)=|G|.
            sqsum = 0
            for r, rho in counts.items():
                ch = q ** (n - 2 * r) * rho
                sqsum += ch * q ** (2 * r)
            group_order = q ** (n + len(edges))
            assert sqsum == group_order, (a, b, q, sqsum, group_order)

print("VERIFY_OK")
