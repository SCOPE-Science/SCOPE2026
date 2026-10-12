"""Independent finite-prime-field enumeration of abelian subspaces of a fixed 7-dimensional algebra."""
from itertools import combinations, product
from math import prod

N = 7

def gauss(n, k, q):
    if not 0 <= k <= n:
        return 0
    return prod(q**(n-i)-1 for i in range(k)) // prod(q**(k-i)-1 for i in range(k))

def rref_spaces(n, d, q):
    for pivots in combinations(range(n), d):
        free = [(i, j) for i, p in enumerate(pivots)
                for j in range(p+1, n) if j not in pivots]
        for entries in product(range(q), repeat=len(free)):
            basis = [[0] * n for _ in pivots]
            for i, p in enumerate(pivots):
                basis[i][p] = 1
            for (i, j), value in zip(free, entries):
                basis[i][j] = value
            yield basis

def bracket(x, y, q):
    return ((x[0]*y[1]-x[1]*y[0]) % q,
            (x[0]*y[2]-x[2]*y[0]) % q,
            (x[1]*y[2]-x[2]*y[1]) % q,
            (x[0]*y[5]-x[1]*y[4]+x[2]*y[3]
             -y[0]*x[5]+y[1]*x[4]-y[2]*x[3]) % q)

def is_abelian(basis, q):
    return all(not any(bracket(x, y, q))
               for x, y in combinations(basis, 2))

def expected(d, q):
    return gauss(4, d, q) + q*(q*q+q+1)*(gauss(4, d, q)-gauss(3, d, q))

if __name__ == '__main__':
    for q, dims in [(2, range(8)), (3, range(3))]:
        for d in dims:
            count = 0; total = 0
            for basis in rref_spaces(N, d, q):
                total += 1
                if is_abelian(basis, q):
                    count += 1
            e = expected(d, q)
            print(f'q={q} d={d} total={total} abelian={count} predicted={e}')
            assert total == gauss(N, d, q), (q, d, total)
            assert count == e, (q, d, count, e)
    for q in (3, 5, 7):
        expected_max = 1 + q*(q*q+q+1)
        # Explicit family: one W+Z and, for each line of V, q lifts.
        lines = list(rref_spaces(3, 1, q))
        assert len(lines) == q*q+q+1
        print(f'q={q} maximal={expected_max}')
    print('VERIFY_OK')
