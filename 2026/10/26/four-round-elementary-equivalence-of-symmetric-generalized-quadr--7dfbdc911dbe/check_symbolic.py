"""Exact distance-intersection certificate using symbolic polynomial arithmetic (requires sympy)."""
import sympy as sp
from itertools import product
q=sp.symbols('q',integer=True,positive=True)
I=sp.eye(5);L=sp.zeros(5)
for i,j,c in ((1,0,1),(0,1,q+1),(2,1,1),(1,2,q),
              (3,2,1),(2,3,q),(4,3,q+1),(3,4,q)):
    L[i,j]=c
D=[I,L,L**2-(q+1)*I,L**3-(2*q+1)*L,
   (L**4-(3*q+1)*L**2+q*(q+1)*I)/(q+1)]
assert all(sp.simplify(D[k][i,0])==int(i==k) for k,i in product(range(5),repeat=2))
assert all(sp.simplify((L*D[k]-((q+1 if k==1 else q) if k>0 else 0)*D[k-1]-(1 if k==1 or k==2 else (q+1 if k==3 else 0))*D[k+1])[i,j])==0
           for k in (1,2,3) for i,j in product(range(5),repeat=2))
for d in range(5):
    pairs=[]
    for a,b in product(range(5),repeat=2):
        p=sp.factor(D[a][d,b])
        if p==0: continue
        # Positivity for every integer q >= 2 follows from a strictly positive constant
        # and nonnegative coefficients in the auxiliary variable h=q-2.
        h=sp.symbols('h')
        poly=sp.Poly(sp.expand(p.subs(q,h+2)),h)
        assert poly.TC()>0 and all(c>=0 for c in poly.all_coeffs()),(d,a,b,p)
        pairs.append((a,b,str(p)))
    print('distance',d,'factorized intersections',pairs)
print('SYMBOLIC POSITIVITY AND RECURRENCES VERIFIED FOR ALL q >= 2')
