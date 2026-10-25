"""Exact arithmetic verification for the 24-cell harmonic sampling spectrum.

Usage: python verify_spectrum.py  (requires sympy 1.13 or newer).
"""
import itertools
import sympy as sp

V = []
for i, j in itertools.combinations(range(4), 2):
    for si, sj in itertools.product((-1, 1), repeat=2):
        v = [0]*4
        v[i], v[j] = si, sj
        V.append(tuple(v))
assert len(V) == 24 and len(set(V)) == 24
T = sp.Matrix(24,24, lambda i,j: sp.Rational(sum(x*y for x,y in zip(V[i],V[j])),2))
I=sp.eye(24)
J=sp.ones(24)
B=T.applyfunc(lambda z: int(z == sp.Rational(1,2)))
C=T.applyfunc(lambda z: int(z == 0))
R=T.applyfunc(lambda z: int(z == -1))
assert R*R==I and B*R==R*B and C*R==C
assert B*B==8*I+3*B+4*C+R*B
assert C*C==6*(I+R)+4*C
assert B*C==3*(B+R*B)
Pe=(I+R)/2
Po=(I-R)/2
P1=J/24
P2=(C+2*Pe)/8-P1
P9=(6*Pe-C)/8
P4=(B*Po+2*Po)/6
P8=Po-P4
P=[P1,P2,P9,P4,P8]
assert sum(P,sp.zeros(24))==I
for idx,X in enumerate(P):
    assert X*X==X
    for Y in P[idx+1:]:
        assert X*Y==sp.zeros(24)
assert [sp.trace(X) for X in P]==[1,2,9,4,8]

def spectrum(l):
    n=l+1
    a=sp.chebyshevu(l,sp.Rational(1,2))
    b=sp.chebyshevu(l,0)
    if l%2==0:
        return (2*n+16*a+6*b,2*n-8*a+6*b,2*n-2*b,0,0)
    return (0,0,0,2*n+8*a,2*n-4*a)

ranks=[]
for ell in range(49):
    n=ell+1
    S=T.applyfunc(lambda t: sp.chebyshevu(ell,t))
    vals=spectrum(ell)
    assert S==sum((v*p for v,p in zip(vals,P)),sp.zeros(24))
    assert S==S.T
    assert all(v>=0 for v in vals)
    rk=sum(int(bool(v>0))*m for v,m in zip(vals,(1,2,9,4,8)))
    ranks.append(rk)
assert ranks[:11]==[1,4,9,8,11,12,10,12,12,12,11]
assert all(r==12 for r in ranks[11:])
print('exact 24-cell class-algebra identities: PASS')
print('five orthogonal spectral projectors; multiplicities (1,2,9,4,8): PASS')
print('degree 0..48 exact Chebyshev spectrum and positivity: PASS')
print('low-degree ranks:',ranks[:11])
print('full parity interpolation for tested degrees 11..48: PASS')
print('the proof establishes the all-degree formula; finite checker is not an all-degree proof')
