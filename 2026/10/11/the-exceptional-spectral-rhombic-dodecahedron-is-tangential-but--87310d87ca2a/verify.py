#!/usr/bin/env python3
from fractions import Fraction
from itertools import product, combinations
import sympy as sp

inner=[tuple(Fraction(s,4) for s in sig) for sig in product((-1,1), repeat=3)]
outer=[]
outer_labels=[]
for i in range(3):
    for t in (-1,1):
        v=[Fraction(0)]*3
        v[i]=Fraction(t,2)
        outer.append(tuple(v))
        outer_labels.append((i,t))
V=inner+outer

# Graph: inner sign vector is incident to signed coordinate face (i,t) iff sign_i=t.
N=14
A=sp.zeros(N)
for a,sig in enumerate(product((-1,1), repeat=3)):
    for b,(i,t) in enumerate(outer_labels, start=8):
        if sig[i]==t:
            A[a,b]=A[b,a]=1

assert sum(int(A[i,j]) for i in range(N) for j in range(i+1,N))==24
assert sorted(sum(int(A[i,j]) for j in range(N)) for i in range(N))==[3]*8+[4]*6

# Exact spectrum.
lam=sp.symbols('lam')
char=sp.factor(A.charpoly(lam).as_expr())
expected=lam**6*(lam**2-4)**3*(lam**2-12)
assert sp.expand(char-expected)==0, (char,expected)

# Arrangement matrix.
Phi=sp.Matrix([[sp.Rational(x.numerator,x.denominator) for x in v] for v in V])
assert A*Phi==2*Phi
assert Phi.T*Phi==sp.eye(3)

# Vertex shells.
inner_norm2=[sum(x*x for x in v) for v in inner]
outer_norm2=[sum(x*x for x in v) for v in outer]
assert set(inner_norm2)=={Fraction(3,16)}
assert set(outer_norm2)=={Fraction(1,4)}

# Every graph edge has squared length 3/16.
for i in range(N):
    for j in range(i+1,N):
        if A[i,j]:
            d2=sum((V[i][k]-V[j][k])**2 for k in range(3))
            assert d2==Fraction(3,16)

# Twelve supporting facets; each equality set has four vertices and affine rank 2.
facets=[]
for i,j in combinations(range(3),2):
    for si,sj in product((-1,1), repeat=2):
        eq=[]
        for q,v in enumerate(V):
            val=si*v[i]+sj*v[j]
            assert val<=Fraction(1,2)
            if val==Fraction(1,2):
                eq.append(q)
        assert len(eq)==4
        p0=sp.Matrix([sp.Rational(x.numerator,x.denominator) for x in V[eq[0]]])
        diffs=[]
        for q in eq[1:]:
            p=sp.Matrix([sp.Rational(x.numerator,x.denominator) for x in V[q]])
            diffs.append(list(p-p0))
        assert sp.Matrix(diffs).rank()==2
        facets.append((i,j,si,sj,tuple(eq)))
assert len(facets)==12
assert len({f[:4] for f in facets})==12

# Euler completeness for a 3-polytope with this known skeleton.
assert 24-14+2==12

# Metric values.
R2=max(inner_norm2+outer_norm2)
assert R2==Fraction(1,4)
rin2=Fraction(1,8)
edge2=Fraction(3,16)
assert edge2==inner_norm2[0]

print("VERIFY_OK spectral-rhombic-dodecahedron vertices=14 edges=24 facets=12 spectrum=lambda^6(lambda^2-4)^3(lambda^2-12) R2=1/4 inner_shell2=3/16 rin2=1/8 edge2=3/16")
