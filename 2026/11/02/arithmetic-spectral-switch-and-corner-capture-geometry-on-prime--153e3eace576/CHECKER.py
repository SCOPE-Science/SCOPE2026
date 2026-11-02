"""Exact modular linear-algebra checks for finite prime-sided quantum grids.

For integer hopping values the integer Krylov matrix has the same rank
as its column span over Q. A full rank modulo a prime is a rigorous lower
bound for the Q-rank; symbolic upper bounds are proved in RESULT.md.
If a modular rank matches a proved upper bound, it certifies the Q-rank.
"""

from math import isqrt

MODULI = (1000003, 1000033)


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def grid_edges(rows, cols, vertical, horizontal):
    edge_list = []
    for x in range(rows):
        for y in range(cols):
            i = x * cols + y
            if x + 1 < rows:
                edge_list.append((i, i + cols, vertical))
            if y + 1 < cols:
                edge_list.append((i, i + 1, horizontal))
    return edge_list


def rank_mod(vectors, modulus):
    pivots = {}
    for column in vectors:
        v = [z % modulus for z in column]
        while True:
            i = next((i for i, z in enumerate(v) if z), None)
            if i is None:
                break
            if i not in pivots:
                factor = pow(v[i], -1, modulus)
                pivots[i] = [(factor * z) % modulus for z in v]
                break
            c = v[i]
            basis = pivots[i]
            v = [(z - c * t) % modulus for z, t in zip(v, basis)]
    return len(pivots)


def krylov_rank(rows, cols, vertical, horizontal, sinks, modulus):
    n = rows * cols
    edges = grid_edges(rows, cols, vertical, horizontal)
    columns = []
    for sink in sinks:
        v = [0] * n
        v[sink] = 1
        for _ in range(n):
            columns.append(v)
            new = [0] * n
            for i, j, w in edges:
                new[i] = (new[i] + w * v[j]) % modulus
                new[j] = (new[j] + w * v[i]) % modulus
            v = new
    return rank_mod(columns, modulus)


def check(rows, cols, a, b, sinks, expected):
    observations = [krylov_rank(rows, cols, a, b, sinks, p) for p in MODULI]
    assert observations == [expected] * len(MODULI), (rows, cols, a, b, sinks, observations, expected)
    print(f"PASS {rows}x{cols} weights=({a},{b}) sinks={sinks} rank={expected} primes={MODULI}")


def main():
    for p in (5, 7, 11):
        assert prime(p)
        n = p - 1
        d = n // 2
        check(n, n, 1, 1, (0,), 2 * d * d + 1)
        check(n, n, 1, 1, (0, n * n - 1), 2 * d * d + 1)
        check(n, n, 1, 1, (0, n * (n - 1)), 3 * d * d - d + 2)
        check(n, n, 2, 3, (0,), n * n)
    for p, q, a, b in ((5, 7, 1, 1), (5, 7, 2, 3), (5, 11, 3, 5), (7, 11, 1, 2)):
        assert prime(p) and prime(q) and p != q
        check(p - 1, q - 1, a, b, (0,), (p - 1) * (q - 1))
    # Independent trace-Gram linear-algebra certificate:
    # G_{ab}=p-2 if a=b and -2 otherwise has eigenvalues 1,p,...,p.
    for p in (5, 7, 11, 13, 17):
        assert prime(p)
        d = (p - 1) // 2
        gram = [[(p - 2) if i == j else -2 for j in range(d)] for i in range(d)]
        assert all(sum(gram[i][j] for j in range(d)) == 1 for i in range(d))
        assert all(gram[i][i] - gram[i][0] == p for i in range(1, d))
    print('PASS trace-Gram identity and positive eigenvalues for five primes')
    # Exact symbolic P4 resonance at ratio sqrt(5), using pairs (a,b)=a+b*sqrt(5).
    # lambda_1=(1+sqrt5)/2, lambda_2=(-1+sqrt5)/2, lambda_3=(1-sqrt5)/2.
    l1=(1,1);l2=(-1,1);l3=(1,-1)  # doubled eigenvalues
    difference=(l1[0]-l2[0],l1[1]-l2[1])  # doubled lambda1-lambda2 = 2
    other=(l3[0]-l1[0],l3[1]-l1[1])  # doubled lambda3-lambda1 = -2sqrt5
    # sqrt5*(2) - 2sqrt5 = 0 exactly
    real=5*difference[1]+other[0]
    irrational=difference[0]+other[1]
    assert (real,irrational)==(0,0)
    print('PASS exact irrational-ratio collision at sqrt(5)')
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    main()
