"""Independent exact Gröbner-chart smoothness and binomial-moment census.
Requires Python 3 and SymPy (tested with the installed SymPy version).
"""
from collections import Counter
from math import comb
import sympy as S
X,Y,Z = S.symbols('X Y Z')
V=(X,Y,Z)
MON=(X**3,Y**3,Z**3,X**2*Y,X**2*Z,X*Y**2,Y**2*Z,X*Z**2,Y*Z**2,X*Y*Z)
POINTS=tuple(tuple((i>>j)&1 for j in range(3)) for i in range(1,8))

def polynomial(c):
    return S.expand(sum(t for i,t in enumerate(MON) if c>>i&1))

def smooth_chart(c):
    f=polynomial(c)
    grad=[S.diff(f,v) for v in V]
    for k,v in enumerate(V):
        others=tuple(V[j] for j in range(3) if k!=j)
        equations=[S.Poly(g.subs(v,1),*others,modulus=2).as_expr() for g in grad]
        basis=S.groebner(equations,*others,order='lex',modulus=2)
        if not(len(basis.polys)==1 and basis.polys[0].as_expr()==1):
            return False
    return True

def mask(c):
    f=polynomial(c)
    return sum(1<<i for i,p in enumerate(POINTS)
               if int(f.subs(dict(zip(V,p))))%2==0)

curves=[mask(c) for c in range(1,1024) if smooth_chart(c)]
assert len(curves)==336
multiplicity=Counter(curves)
# B_j = sum_{|T|=j} binom(number_of_smooth_cubics_through_T,2)
#     = sum_{k>=j} binom(k,j) P_k.
B={}
for j in range(8):
    total=0
    for T in range(128):
        if T.bit_count()!=j: continue
        n=sum(count for m,count in multiplicity.items() if m&T==T)
        total+=comb(n,2)
    B[j]=total
P={}
for j in reversed(range(8)):
    P[j]=B[j]-sum(comb(k,j)*P[k] for k in range(j+1,8))
assert [P[j] for j in range(8)]==[12740,22575,14448,5488,1008,21,0,0]
selected=((1,0,0),(0,1,0),(1,1,0),(1,0,1),(1,1,1))
through=[]
for c in range(1,1024):
    f=polynomial(c)
    if all(int(f.subs(dict(zip(V,p))))%2==0 for p in selected):
        through.append(c)
assert [c for c in through if smooth_chart(c)]==[60,172]
print('smooth_cubics',len(curves))
print('binomial_moments',B)
print('unordered_pair_distribution',dict(sorted((k,v) for k,v in P.items() if v)))
print('fixed_five_smooth',[60,172])
print('VERIFY_OK')
