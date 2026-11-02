"""Exact-arithmetic reproduction checks for the alternating-momentum theorem.

Run: python check_periodic_momentum.py
Requires only the Python standard library. The general proof is in RESULT.md;
these finite checks are supplementary and are not substituted for it.
"""
from fractions import Fraction as Q


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matrix(beta, z):
    return [[1 + beta - z, -beta], [Q(1), Q(0)]]


def parameters(b, c, z):
    M = mul(matrix(c, z), matrix(b, z))
    trace = M[0][0] + M[1][1]
    determinant = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    F = z*z - (2+b+c)*z + 2*(1+b*c)
    D = (1-b)**2 - 6*(1-b)*(1-c) + (1-c)**2
    assert trace == 1+b*c - (2+b+c)*z + z*z
    assert determinant == b*c
    assert 1+trace+determinant == F
    assert 1-trace+determinant == z*(2+b+c-z)
    assert 1-determinant > 0
    return F, D


def check():
    cases = 0
    B = [Q(0), Q(1,100), Q(1,10), Q(1,2), Q(4,5), Q(9,10), Q(93,100), Q(99,100)]
    Z = [Q(k,20) for k in range(1,101)]
    for b in B:
        for c in B:
            for z in Z:
                F, D = parameters(b,c,z)
                a = 2+b+c
                assert (0 < z < a and F > 0) == (z*(a-z) > 0 and F > 0)
                assert D == a*a-8*(1+b*c)
                # Positive F corresponds to the exact quadratic Schur condition,
                # with the two remaining Schur signs checked in parameters().
                cases += 1
    # Singular but convergent full step in a fixed coefficient is NOT asserted.
    # Two alternating individually stable fixed-coefficient recurrences diverge.
    b,c,z = Q(0), Q(9,10), Q(3,2)
    F,D = parameters(b,c,z)
    assert F < 0 and D > 0
    assert z < 2*(1+b) and z < 2*(1+c)
    xprev=x=Q(1)
    for k in range(36):
        beta = b if (k%2 == 0) else c
        xnext = (1+beta-z)*x-beta*xprev
        xprev,x=x,xnext
        if k%2 == 1:
            j=(k+1)//2
            assert x == Q(-11,10)**j
    # Arbitrarily small absolute contrast near unit momentum.
    for denominator in [8,10,100,1000,10000]:
        d = Q(1,denominator)
        b,c=1-7*d,1-d
        z=2-4*d
        F,D=parameters(b,c,z)
        assert D==8*d*d and F==-2*d*d
        assert 0<=b<c<1 and 0<z<2
        assert z<2*(1+b) and z<2*(1+c)
    print('EXACT_CHECKS_OK:',cases,'parameter triples, 36 recurrence updates, 5 contrasts')


if __name__ == '__main__':
    check()
