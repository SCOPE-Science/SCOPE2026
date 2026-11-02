"""Independent entrywise checks of the finite-field sandwich square-zero census.

Run with Python 3: python3 verify.py. Does not require third-party packages.
The direct test explicitly evaluates X P X without using the block-counting proof.
"""
from itertools import product
from math import prod


def rank_matrix_count(a, b, u, q):
    if not (0 <= u <= min(a, b)):
        return 0
    top = prod(q**a - q**i for i in range(u)) * prod(q**b - q**i for i in range(u))
    bot = prod(q**u - q**i for i in range(u))
    assert top % bot == 0
    return top // bot


def formula(m, n, r, q):
    assert 1 <= m and 1 <= n and 0 <= r <= min(m, n) and q >= 2
    s, t = n - r, m - r
    ans = 0
    for j in range(r//2 + 1):
        # Flags im(A) <= ker(A), together with V/ker(A) ~= im(A).
        gl = prod(q**j - q**i for i in range(j))
        number_a = rank_matrix_count(r, j, j, q) * rank_matrix_count(r-j, j, j, q) // gl
        for u in range(min(r-2*j, s) + 1):
            ans += (number_a * q**(j*s)
                    * rank_matrix_count(r-2*j, s, u, q)
                    * q**(t*(r-j-u)))
    return ans * q**(s*t)


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def multiply(a, b, q):
    if q != 4:
        return a*b % q
    # F4 = F2[alpha]/(alpha^2 + alpha + 1); 2 denotes alpha.
    result = 0
    for i in (0, 1):
        for j in (0, 1):
            if (a >> i) & 1 and (b >> j) & 1:
                result ^= (1, 2, 3)[i+j]
    return result


def canonical_sandwich(n, m, r):
    return [[int(i == j and i < r) for j in range(m)] for i in range(n)]


def brute(m, n, p, q):
    assert len(p) == n and all(len(row) == m for row in p)
    result = 0
    for entries in product(range(q), repeat=m*n):
        x = [entries[i*n:(i+1)*n] for i in range(m)]
        square_zero = True
        # (XPX)[i,j] = sum_{a<n, b<m} X[i,a] P[a,b] X[b,j].
        for i in range(m):
            for j in range(n):
                z = 0
                for a in range(n):
                    for b in range(m):
                        z = add(z, multiply(multiply(x[i][a], p[a][b], q), x[b][j], q), q)
                if z:
                    square_zero = False
                    break
            if not square_zero:
                break
        result += square_zero
    return result


def test():
    cases = [(1,1,0,2),(1,2,1,2),(2,1,1,3),
             (2,2,1,2),(2,2,1,3),(2,2,2,2),
             (2,2,2,3),(2,2,1,4),(2,3,1,2),
             (3,2,1,2),(3,3,1,2),(3,3,2,2),
             (3,3,3,2),(2,3,2,2),(3,3,2,3),(3,3,3,3)]
    for m, n, r, q in cases:
        got = brute(m, n, canonical_sandwich(n, m, r), q)
        expected = formula(m, n, r, q)
        assert got == expected, (m, n, r, q, got, expected)
    # A noncanonical rank-one P: all entries 1, with independent evaluation.
    for q in (2,3,4):
        p = [[1,1],[1,1]]
        assert brute(2, 2, p, q) == formula(2,2,1,q)
    # Check the reduced rank-one component inclusion-exclusion formula.
    for m, n, q in ((2,2,2),(2,3,3),(3,3,4),(4,2,2)):
        reduced_union = q**((m-1)*n) + q**(m*(n-1)) - q**((m-1)*(n-1))
        assert formula(m,n,1,q) == reduced_union
    print('SANDWICH_SQUARE_ZERO_OK 19 exhaustive matrix cases; 4 component counts')


if __name__ == '__main__':
    test()
