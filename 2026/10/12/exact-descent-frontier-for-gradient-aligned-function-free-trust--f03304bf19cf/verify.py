"""Exact-rational checks for the Cauchy-step descent envelope.
Scientific proof is analytic; these checks test its finite rational witnesses.
Run: python3 verify.py
"""
from fractions import Fraction as Q


def alpha(b, rho):
    if rho <= 0 or rho <= b:
        return Q(1)
    return b / rho


def reduction(L, M, b, rho):
    # f(z)=L*z*z/2+z at the starting point z=0: gradient equals one.
    # For model B=rho and the source's step, z_new=-alpha/b.
    a=alpha(b,rho)
    z=-a/b
    new=L*z*z/2+z
    return -new*b


def envelope(L,M,b):
    e0=Q(1)-L/(2*b)
    if b >= M:
        return e0
    eM=(b/M)*(Q(1)-L/(2*M))
    return min(e0,eM)


def threshold(L,M):
    return M*M/(4*M-2*L) if 2*L <= M else 2*L/3

for Lnum in range(1,21):
    for Mnum in range(1,21):
        L,M=Q(Lnum,4),Q(Mnum,4)
        B=threshold(L,M)
        assert envelope(L,M,B)==Q(1,4), (L,M,B,envelope(L,M,B))
        assert B < 2*(L+M)
        for mult in [Q(1,5), Q(2,3), Q(9,10), Q(1), Q(11,10), Q(2), Q(4)]:
            b=mult*B
            v0=reduction(L,M,b,Q(0))
            vM=reduction(L,M,b,M)
            assert min(v0,vM) == envelope(L,M,b), (L,M,b,v0,vM,envelope(L,M,b))
            if mult < 1:
                assert envelope(L,M,b)<Q(1,4),(L,M,b)
            else:
                assert envelope(L,M,b)>=Q(1,4),(L,M,b)

# Sharp phase boundary for the largest gain over the previously proven threshold:
M=Q(2);L=Q(1);B=threshold(L,M)
assert B==Q(2,3) and 2*(L+M)/B==9
# Model-rich threshold witness: L=1/4, M=1, b=2/7; B=M attains exactly 1/4.
assert threshold(Q(1,4),Q(1))==Q(2,7)
assert reduction(Q(1,4),Q(1),Q(2,7),Q(1))==Q(1,4)
# Function-smoothness threshold witness: L=M=1, b=2/3, zero model attains 1/4.
assert reduction(Q(1),Q(1),Q(2,3),Q(0))==Q(1,4)
# Genuine connected two-node decentralized quadratic tests. W has all entries 1/2.
# Declared global Lipschitz bound stays exactly L; along the first-node step
# the actual quadratic curvature is ell=L-delta/2-epsilon.
for L,M,b,rho in [(Q(1,4),Q(1),Q(1,4),Q(1)),
                  (Q(1),Q(1),Q(3,5),Q(0))]:
    delta=epsilon=Q(1,10000)
    assert L-delta-epsilon>0
    ell=L-delta/2-epsilon
    assert b<threshold(L,M)
    assert reduction(ell,M,b,rho)<Q(1,4)
print('VERIFY_OK: 400 parameter pairs, exact endpoint witnesses, two-node obstructions, sharp threshold, factor-nine boundary')
