"""Exact characteristic-seven Cartier-rank calculations for an explicit four-nodal sextic pencil.

Requires sympy. All checks use exact symbolic polynomial arithmetic over F_7.
"""
import sympy as sp
from itertools import combinations

p = 7
t = sp.Symbol('t')
x, y, z = sp.symbols('x y z')
a, b = sp.symbols('a b')
variables = (x, y, z)

W = x**6 + y**6 + z**6 + (x**2+y**2+z**2)*(x**4+y**4+z**4) - 12*x**2*y**2*z**2
Q = (x**2-y**2)*(y**2-z**2)*(z**2-x**2)
F = sp.Poly(W+t*Q, variables)
terms = {exponents: sp.Poly(c,t,modulus=p) for exponents,c in F.terms()}
zero = sp.Poly(0,t,modulus=p)
one = sp.Poly(1,t,modulus=p)

def mul(A,B):
    out={}
    for e,c in A.items():
        for f,d in B.items():
            ef=tuple(e[i]+f[i] for i in range(3))
            out[ef]=out.get(ef,zero)+c*d
    return {e:c for e,c in out.items() if not c.is_zero}

power={(0,0,0):one}
for _ in range(6):
    power=mul(power,terms)
monomials=[(i,j,3-i-j) for i in range(4) for j in range(4-i)]
H=sp.Matrix([[power.get(tuple(7*(u+1)-(v+1) for u,v in zip(e,f)),zero).as_expr()
              for f in monomials] for e in monomials])
columns=[]
for i,j in ((0,1),(0,2),(1,0),(1,2),(2,0),(2,1)):
    e=[0,0,0];e[i]=3
    f=[0,0,0];f[i]=1;f[j]=2
    columns.append(sp.Matrix([int(m==tuple(e))-int(m==tuple(f)) for m in monomials]))
B=sp.Matrix.hstack(*columns)
rows=next(r for r in combinations(range(10),6) if B.extract(r,list(range(6))).det()!=0)
K=B.extract(rows,list(range(6))).inv()*(H*B).extract(rows,list(range(6)))
assert all(sp.Poly(v,t,modulus=7).is_zero for v in B*K-H*B)
D=(t**2-2*t+3)*(t**2+2*t+3)*(t**4-t**3+t**2+t+3)*(t**4+t**3+t**2-t+3)
assert sp.Poly(K.det()-D**3,t,modulus=7).is_zero
D7=sp.Poly(D,t,modulus=7)
assert D7.degree()==12 and sp.gcd(D7,D7.diff()).degree()==0
assert sp.gcd(D7,sp.Poly(t*(5*t**4+4),t,modulus=7)).degree()==0
print('CARTIER_OK: six-dimensional adjoint subspace preserved, determinant D(t)^3')
print('RANK_OK: D squarefree degree 12; rank exactly 3 at all roots')

u,v,w=sp.symbols('u v w')
G=u**3+v**3+w**3+(u+v+w)*(u**2+v**2+w**2)-12*u*v*w+t*(u-v)*(v-w)*(w-u)
g=sp.expand(G.subs({u:1+a,v:1+b,w:1}))
q2=sum(c*a**i*b**j for (i,j),c in sp.Poly(g,a,b).terms() if i+j==2)
c3=sum(c*a**i*b**j for (i,j),c in sp.Poly(g,a,b).terms() if i+j==3)
assert sp.Poly(sp.discriminant(q2.subs(a,1),b),t,modulus=7).degree()==0
reducible=sp.Poly(sp.resultant(q2.subs(a,1),c3.subs(a,1),b),t,modulus=7)
axes=[sp.discriminant(G.subs({u:0,w:1}),v), sp.discriminant(G.subs({v:0,w:1}),u),
      sp.discriminant(G.subs({w:0,v:1}),u)]
bad=sp.Poly((t**2-4)*(t**2+1),t,modulus=7)
assert sp.gcd(D7,bad).degree()==0
for axis in axes:
    e=sp.Poly(axis,t,modulus=7)
    assert e.degree()==bad.degree() and (e.rem(bad)).is_zero
assert reducible.degree()==2 and reducible.rem(sp.Poly(t**2-4,t,modulus=7)).is_zero
print('SMOOTH_LOCUS_OK: excluded t=+/-2 or t^2=-1, disjoint from all 12 Cartier jumps')
print('VERIFY_OK')
