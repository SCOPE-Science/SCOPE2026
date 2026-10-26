"""Reproduce certified arithmetic for a four-season two-habitat linear population system.

Python 3.9+ standard library only. All enclosures and comparisons are exact rationals.
"""
from fractions import Fraction as Q
from math import factorial
from itertools import permutations

I=((Q(1),Q(0)),(Q(0),Q(1)))
Z=((Q(0),Q(0)),(Q(0),Q(0)))
J=((Q(1),Q(1)),(Q(1),Q(1)))

def mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def add(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))

def scale(A,c):
    return tuple(tuple(c*z for z in row) for row in A)

def tr(A):
    return A[0][0]+A[1][1]

def product(Ms):
    C=I
    for A in Ms:
        C=mul(C,A)
    return C

def trunc_exp(A,N):
    C=I; S=I
    for k in range(1,N+1):
        C=scale(mul(C,A),Q(1,k))
        S=add(S,C)
    return S

def tail_bound(x,N):
    """Bound sum_{k>N} x**k/k! whenever x<N+2."""
    assert x>=0 and x<Q(N+2)
    return x**(N+1)/Q(factorial(N+1))/(1-x/Q(N+2))

def matrix_exp_bounds(A,N=60):
    # Entrywise nonnegative A, each row sum at most 28/5.
    R=Q(28,5)
    assert all(x>=0 for row in A for x in row)
    assert max(map(sum,A))<=R
    S=trunc_exp(A,N)
    return S,add(S,scale(J,tail_bound(R,N)))

def scalar_exp_bounds(x,N=120):
    s=Q(1); t=Q(1)
    for k in range(1,N+1):
        t*=x/Q(k);s+=t
    return s,s+tail_bound(x,N)

# Population model: m=1, beta=(1,-1,2,-2), mean isolated growth -2/5.
# Every phase lasts exactly 1 time unit.
B=[((Q(b)+Q(13,5),Q(1)),(Q(1),-Q(b)+Q(13,5))) for b in [1,-1,2,-2]]
E=[matrix_exp_bounds(X) for X in B]

def trace_bounds(p):
    return tr(product([E[i][0] for i in p])),tr(product([E[i][1] for i in p]))

# Since K = product exp(B_i), Floquet M=e^-16 K, det M=e^-56/5<1.
# Its leading eigenvalue exceeds 1 iff tr(K)>e^16+e^(24/5).
threshlo,threshhi=(scalar_exp_bounds(Q(16))[0]+scalar_exp_bounds(Q(24,5))[0],
                   scalar_exp_bounds(Q(16))[1]+scalar_exp_bounds(Q(24,5))[1])
low1,hi1=trace_bounds((0,1,2,3))
low2,hi2=trace_bounds((0,2,1,3))
assert Q(6436128)<low1<=hi1<Q(6436129)
assert Q(15910318)<low2<=hi2<Q(15910319)
assert Q(8886232)<threshlo<=threshhi<Q(8886233)
assert hi1<threshlo and low2>threshhi

# Additional exact finite checks of the four-factor trace identity for the
# traceless components. These are independent corroboration, not its proof.
for m in [Q(1,2),Q(1),Q(3)]:
    for bs in [(Q(1),Q(-1),Q(2),Q(-2)),
               (Q(0),Q(1,3),Q(5,2),Q(-4)),
               (Q(2),Q(2),Q(3),Q(4))]:
        X=[((b,m),(m,-b)) for b in bs]
        d=tr(product(X))-tr(product([X[0],X[2],X[1],X[3]]))
        assert d==4*m*m*(bs[0]-bs[3])*(bs[1]-bs[2])
        # Three symmetric factors admit all 3! trace permutations.
        for p in permutations(range(3)):
            assert tr(product([X[i] for i in p]))==tr(product(X[:3]))

# Distinctness of the three dihedral classes can also be checked exactly
# using the quartic polynomial trace in this instance.
bs=(Q(1),Q(-1),Q(2),Q(-2))
X=[((b,Q(1)),(Q(1),-b)) for b in bs]
classes={tr(product([X[i] for i in p])) for p in permutations(range(4))}
assert len(classes)==3
print('PASS: exact rational four-season extinction/growth certificate,')
print('      3-factor permutation symmetry and 4-factor trace identity tests.')
print('Bounds: tr K(1,2,3,4) in (6436128,6436129),')
print('        threshold in (8886232,8886233),')
print('        tr K(1,3,2,4) in (15910318,15910319).')
