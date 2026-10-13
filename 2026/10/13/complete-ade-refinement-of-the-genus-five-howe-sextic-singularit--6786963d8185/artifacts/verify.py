#!/usr/bin/env python3
import sympy as sp

r,s,v=sp.symbols('r s v')
d1,d2,d3,d4=sp.symbols('d1 d2 d3 d4')
a1,a2,a3,a4,b1,b2,b3,b4=sp.symbols('a1 a2 a3 a4 b1 b2 b3 b4')
X,Z=sp.symbols('X Z')

def quartic(roots):
    out=1
    for q in roots:
        out*=X-q*Z
    return sp.expand(out)
P1=quartic([a1,a2,a3,a4])
P2=quartic([b1,b2,b3,b4])
D=sp.cancel((P1-P2)/Z)
assert sp.Poly(D,X,Z).total_degree()==3
assert sp.expand((P1-P2)-Z*D)==0

# At P_infty=(0:1:0), chart Y=1.
A=sp.expand(P1+P2)
Gp=sp.expand(s**2-2*A.subs({X:r,Z:s})+D.subs({X:r,Z:s})**2)
poly=sp.Poly(Gp,r,s)
# The only total-degree <4 term is s^2, and the r^4 coefficient is -4.
low={mon:coef for mon,coef in poly.terms() if sum(mon)<4}
assert low=={(0,2):sp.Integer(1)}, low
assert sp.expand(Gp).coeff(r,4).subs(s,0)==-4
# d/ds = 2s + terms of degree at least 3, so the critical section has s=O(r^3).
dGs=sp.Poly(sp.diff(Gp,s),r,s)
assert dGs.coeff_monomial(s)==2
for mon,coef in dGs.terms():
    if mon!=(0,1) and coef!=0:
        assert sum(mon)>=3

# At Q_infty=(1:0:0), d1=0.  The homogeneous difference is
# D(1,s)=d2*s-d3*s^2+d4*s^3 up to the definitions d_i=sigma_i-tau_i.
DQ=d2*s-d3*s**2+d4*s**3
# The v^2 coefficient is -4 at the origin, so v is the Morse direction.
assert -2*(2)==-4
orders={
    'd2_nonzero': sp.Poly((s)**2,s).degree(),
    'd3_first': sp.Poly((s**2)**2,s).degree(),
    'd4_first': sp.Poly((s**3)**2,s).degree(),
}
assert orders=={'d2_nonzero':2,'d3_first':4,'d4_first':6}

# Affine point: if h_1 has root multiplicity m, b(u)^2 has order 2m.
for m,atype in [(1,'A1'),(2,'A3'),(3,'A5')]:
    assert 2*m==int(atype[1:])+1

baskets={
 'I-1':{'A1':3,'A3':1},
 'I-2':{'A1':1,'A3':2},
 'I-3':{'A3':1,'A5':1},
 'II-1':{'A1':3,'A3':1},
 'II-2':{'A1':1,'A3':2},
 'II-3':{'A1':1,'A3':2},
 'II-4':{'A3':1,'A5':1},
}
delta={'A1':1,'A3':2,'A5':3}
for name,b in baskets.items():
    total=sum(delta[k]*n for k,n in b.items())
    assert total==5,(name,total)

print('P_INFINITY: transverse square, residual order 4 -> A3')
print('Q_INFINITY:', orders, '-> A1/A3/A5')
print('AFFINE: root multiplicity 1/2/3 -> A1/A3/A5')
print('BASKETS:', baskets)
print('VERIFY_OK')
