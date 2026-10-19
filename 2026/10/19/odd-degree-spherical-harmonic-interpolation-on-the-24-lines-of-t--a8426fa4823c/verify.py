"""Exact finite checks for harmonic sampling on the normalized F4 root lines.

Requires Python 3 and SymPy. The proof for all degrees is given separately.
"""
from itertools import combinations, product
from fractions import Fraction
import sympy as sp

short=[]
for i in range(4):
    x=[sp.Integer(0)]*4; x[i]=sp.Integer(1); short.append(tuple(x))
for signs in product((-1,1),repeat=3):
    short.append(tuple([sp.Rational(1,2)]+[sp.Rational(z,2) for z in signs]))
long_unscaled=[]
for i,j in combinations(range(4),2):
    for sign in (-1,1):
        x=[sp.Integer(0)]*4; x[i]=sp.Integer(1); x[j]=sp.Integer(sign)
        long_unscaled.append(tuple(x))

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def sign(x):return 1 if x>0 else (-1 if x<0 else 0)
def near_zero(M):return M == sp.zeros(*M.shape)

def within(points):
    return sp.Matrix([[int(sign(dot(a,b))) if i!=j else 0
                       for j,b in enumerate(points)] for i,a in enumerate(points)])
S=within(short); T=within(long_unscaled)
B=sp.Matrix([[int(sign(dot(x,y))) for y in long_unscaled] for x in short])
I=sp.eye(12)
assert len(short)==len(long_unscaled)==12
for P,pts in ((S,short),(T,long_unscaled)):
    assert near_zero(P*P-2*P-8*I)
    assert P.eigenvals()=={sp.Integer(4):4,sp.Integer(-2):8}
assert near_zero(S*B-4*B) and near_zero(B*T-4*B)
assert near_zero(B*B.T-3*(S+2*I))
assert near_zero(B.T*B-3*(T+2*I))
assert B.rank()==4

# Distinct angular classes: dot=0 or ±1/2 within each orbit,
# dot=0 or ±1/sqrt(2) across distinct orbits.
for points, length_sq in ((short,sp.Integer(1)),(long_unscaled,sp.Integer(2))):
    for i,j in combinations(range(12),2):
        assert dot(points[i],points[j])/length_sq in (0,sp.Rational(1,2),-sp.Rational(1,2))
for x in short:
    for y in long_unscaled:
        assert dot(x,y) in (0,1,-1)

# Full exact Chebyshev U_l Gram for ℓ odd with the long roots normalized.
long=[sp.Matrix(p)/sp.sqrt(2) for p in long_unscaled]
short_v=[sp.Matrix(p) for p in short]
X=short_v+long
for ell in range(1,42,2):
    n=ell+1
    eps=sp.simplify(sp.chebyshevu(ell,sp.Rational(1,2)))
    eta=sp.simplify(sp.sin(n*sp.pi/4))
    assert eps in (-1,0,1) and eta in (-1,0,1)
    a=n*eps; b=sp.simplify(n*sp.sqrt(2)*eta)
    G=sp.diag(*([sp.Integer(n*n)]*24))
    G[:12,:12] += a*S
    G[12:,12:] += a*T
    G[:12,12:] += b*B
    G[12:,:12] += b*B.T
    ev={}
    for value,mul in ((n*(n-2*eps),16),(n*(n+4*eps+6*eta),4),(n*(n+4*eps-6*eta),4)):
        ev[value]=ev.get(value,0)+mul
    actual={key:mul for key,mul in G.eigenvals().items()}
    assert actual==ev,(ell,actual,ev)
    assert all(z>=0 for z in actual)
    if ell<=11:
        predicted={1:4,3:16,5:20,7:24,9:20,11:24}[ell]
        assert 24-actual.get(sp.Integer(0),0)==predicted
    if ell>=11: assert 0 not in actual
    if ell%12==11: assert G==n*n*sp.eye(24)
    if ell in (7,11,13):
        direct=sp.Matrix([[sp.simplify(n*sp.chebyshevu(ell,sp.simplify(v.dot(w)))) for w in X] for v in X])
        assert near_zero(G-direct)
print('PASS: exact root geometry; signed adjacency identities; all harmonic Gram spectra for 21 odd degrees; direct normalized Gegenbauer kernels; rank reversal and arithmetic tightness.')
