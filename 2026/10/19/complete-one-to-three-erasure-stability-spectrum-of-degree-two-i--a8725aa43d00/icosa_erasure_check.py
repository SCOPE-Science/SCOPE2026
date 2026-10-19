"""Exact symbolic check for degree-two harmonic sampling on the icosahedron.
Run: python icosa_erasure_check.py  (requires SymPy).
No external data are required.
"""
from itertools import combinations, product
from collections import Counter
import sympy as S

r = S.sqrt(5)
phi = (1 + r) / 2
raw = []
for a,b in product([-1,1],repeat=2):
    raw += [S.Matrix([0,a,b*phi]), S.Matrix([a,b*phi,0]), S.Matrix([b*phi,0,a])]
assert len(raw)==12 and len(set(map(tuple,raw)))==12
norm2 = 1 + phi**2
V = [v / S.sqrt(norm2) for v in raw]
def simplify(x): return S.simplify(S.radsimp(x))
def dot(i,j): return simplify(V[i].dot(V[j]))
T = S.Matrix(12,12,lambda i,j:dot(i,j))
assert all(simplify(T[i,i]-1)==0 for i in range(12))
assert set(T).issubset({S.Integer(1),-S.Integer(1),1/r,-1/r})
# The first 9 spherical harmonics have addition kernel K_2(t)=1+3t+5P_2(t).
def K(t): return 1+3*t+S.Rational(5,2)*(3*t*t-1)
P = S.Matrix(12,12,lambda i,j:simplify(K(T[i,j])/12))
assert simplify(S.trace(P)-9)==0
assert all(simplify(x)==0 for x in P*P-P)
Q = S.eye(12)-P
assert simplify(S.trace(Q)-3)==0
assert all(simplify(x)==0 for x in Q*Q-Q)
# Verify exact fourth-order spherical moments, independently proving 4-design.
def dfodd(n):
    z=1
    for k in range(1,n+1,2):z*=k
    return z
for degree in range(6):
    for e0 in range(degree+1):
        for e1 in range(degree-e0+1):
            e2=degree-e0-e1
            ev=simplify(sum(v[0]**e0*v[1]**e1*v[2]**e2 for v in V)/12)
            if degree%2 or any(k%2 for k in (e0,e1,e2)):
                expected=S.Integer(0)
            else:
                half=degree//2
                expected=S.Rational(dfodd(e0-1)*dfodd(e1-1)*dfodd(e2-1),dfodd(2*half+1))
            assert simplify(ev-expected)==0,(e0,e1,e2,ev,expected)

# All one- and two-erasure minors are checked by exact invariants.
assert all(simplify(Q[i,i]-S.Rational(1,4))==0 for i in range(12))
pairclasses=Counter()
for E in combinations(range(12),2):
    i,j=E
    M=Q.extract(E,E)
    if T[i,j]==-1:
        label='opposite'
        expected=[S.Integer(0),S.Rational(1,2)]
    else:
        label='nonopposite'
        expected=[(1+1/r)/4,(1-1/r)/4]
    pairclasses[label]+=1
    assert simplify(S.trace(M)-sum(expected))==0
    assert simplify(M.det()-S.prod(expected))==0
assert pairclasses=={'opposite':6,'nonopposite':60},pairclasses
counts=Counter()
for E in combinations(range(12),3):
    pairdots=[T[i,j] for i,j in combinations(E,2)]
    if -1 in pairdots:
        label='antipodal'
    else:
        sign=simplify(S.prod(pairdots))
        label='product_positive' if sign>0 else 'product_negative'
    counts[label]+=1
    M=Q.extract(E,E)
    tr=simplify(S.trace(M)); det=simplify(M.det())
    c=1/r
    if label=='antipodal':
        eigen=[S.Integer(0),(3+S.sqrt(S.Rational(13,5)))/8,(3-S.sqrt(S.Rational(13,5)))/8]
    elif label=='product_positive':
        eigen=[(1-2*c)/4,(1+c)/4,(1+c)/4]
    else:
        eigen=[(1+2*c)/4,(1-c)/4,(1-c)/4]
    assert simplify(tr-sum(eigen))==0
    assert simplify(S.trace(M*M)-sum(t*t for t in eigen))==0
    assert simplify(det-S.prod(eigen))==0,(E,label,det,S.prod(eigen))
assert counts=={'antipodal':60,'product_positive':80,'product_negative':80},counts
print('design: degree 5; projector: rank 9; complement: rank 3')
print('three-erasure classes:',dict(counts))
print('r=1: 8 unit eigenvalues, 1/4')
print('r=2: opposite => 7 unit, 1/2, 0; otherwise 7 unit, (1+1/sqrt(5))/4, (1-1/sqrt(5))/4')
print('r=3: 6 unit, and the class-dependent triple displayed in the report')
print('all exact checks passed')
