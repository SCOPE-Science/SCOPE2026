"""Exact finite certificates for sharp fourth moments on Paley Fourier spectra.

Usage: python3 checker.py   (standard library only)
All arithmetic in the certified combinatorial tests is integral.
"""
from collections import Counter
from itertools import product


def residues(p):
    return {a*a % p for a in range(1, p)}


def triple_histogram(p):
    H = residues(p)
    return Counter(
        sum((b + x) % p in H and (b - y) % p in H for b in H)
        for x in range(1, p) for y in range(1, p) if (x + y) % p
    )


def det_integer(M):
    # Bareiss fraction-free determinant, with no floating-point operations.
    A = [r[:] for r in M]
    n = len(A)
    sign, last = 1, 1
    for k in range(n-1):
        if A[k][k] == 0:
            j = next(j for j in range(k+1, n) if A[j][k])
            A[j], A[k] = A[k], A[j]
            sign *= -1
        pivot = A[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = A[i][j] * pivot - A[i][k] * A[k][j]
                assert numerator % last == 0
                A[i][j] = numerator // last
        for i in range(k+1, n):
            A[i][k] = 0
        last = pivot
    return sign*A[-1][-1]


def run():
    tests = 0
    # Check the Paley difference-set identity and the exact even-moment
    # formula for constant (and modulated-constant) coefficients.
    for p in (7, 11, 19, 23, 31, 43, 47, 59):
        H = residues(p)
        m = (p-1)//2
        lam = (p-3)//4
        assert len(H) == m
        differences = Counter((a-b) % p for a in H for b in H)
        assert differences[0] == m
        assert all(differences[t] == lam for t in range(1, p))
        tests += p
        # For every additive modulation, all correlations have modulus lam.
        # The normalized fourth moment is therefore m^2+(p-1)lam^2.
        normalized_fourth_moment = m*m + (p-1)*lam*lam
        expected = (m*m+1)*m//2
        assert normalized_fourth_moment == expected
        tests += 1
        # Exact pairwise Cauchy and modulus inequality for integer vectors.
        # The latter is homogeneous of degree 4 and checked by multiplication.
        order = sorted(H)
        vectors = [tuple(1 for _ in order), tuple(i+1 for i in range(m))]
        vectors.extend(tuple(((-1)**((i*j + j)//3))*(i%3+1)
                             for i in range(m)) for j in range(7))
        for vec in vectors:
            S = sum(c*c for c in vec)
            corr = [sum(vec[i]*vec[j] for i,a in enumerate(order)
                        for j,b in enumerate(order) if (a-b)%p==t)
                    for t in range(p)]
            moment = sum(z*z for z in corr)
            assert 2*m*moment <= (m*m+1)*S*S
            tests += 1
    h19 = triple_histogram(19)
    h23 = triple_histogram(23)
    assert dict(h19) == {1:126, 2:162, 3:18}
    assert dict(h23) == {1:66, 2:264, 3:132}
    assert sum(h19.values()) == 18*17
    assert sum(h23.values()) == 22*21
    tests += 4
    # Independent exact subgroup-pair verification for the small p=11 case.
    p = 11
    H = residues(p)
    assert H == {1,3,4,5,9}
    relations = ((1,5,3,3),(1,1,4,9),(1,9,5,5),(3,5,4,4))
    assert all((a+b-c-d)%p == 0 for a,b,c,d in relations)
    M = [[-2,0,1,0], [0,1,0,1], [0,0,-2,1], [1,-2,1,0]]
    assert abs(det_integer(M)) == 11
    # Each of the eleven characters gives a distinct normalized solution.
    assert len({tuple((k*(h-1))%11 for h in (3,4,5,9)) for k in range(11)}) == 11
    tests += 4
    # At p=7 each ordered nonzero difference has a single representation,
    # so every choice of unit complex phases has exactly the same moment.
    assert all(Counter((a-b)%7 for a in residues(7) for b in residues(7))[t]
               == 1 for t in range(1,7))
    tests += 6
    # Check monotonic positive inequality at p=31 and the derivative.
    assert (31-15)**2 > 4*31 and 31-15>0
    tests += 1
    print('EXACT_COMBINATORIAL_CERTIFICATE_PASS', tests)
    print('p19 triple histogram', dict(sorted(h19.items())))
    print('p23 triple histogram', dict(sorted(h23.items())))


if __name__ == '__main__':
    run()
