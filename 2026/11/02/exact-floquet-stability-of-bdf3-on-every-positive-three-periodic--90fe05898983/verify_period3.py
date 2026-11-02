#!/usr/bin/env python3
"""Reproduce the exact polynomial certificates for three-periodic variable-step BDF3.

Requires Python 3, sympy, numpy. No numerical sampling is used as proof.
"""
import random
import sympy as sp
import numpy as np

x, y, z = sp.symbols('x y z', positive=True)

def lagrange_coefficients(u,v,w):
    t=sp.symbols('t')
    nodes=[sp.Integer(0),-u,-u-v,-u-v-w]
    L=[sp.prod((t-nodes[j])/(nodes[i]-nodes[j])
               for j in range(4) if j != i) for i in range(4)]
    return [sp.factor(sp.diff(li,t).subs(t,0)) for li in L]

def polydata(u,v,w):
    H=3*u**2+4*u*v+2*u*w+v**2+v*w
    K=u**2+4*u*v+2*u*w+3*v**2+3*v*w+w**2
    # M(u,v,w) maps (d_{n-1},d_{n-2}) to (d_n,d_{n-1}).
    # a=A/D; b=-C/D, with A,C,D all strictly positive.
    D=v*w*(v+w)*H
    A=w*u**2*K
    C=v*u**2*(u+v)**2
    return A,C,D

# The Lagrange derivative produces exactly the advertised recurrence.
u,v,w = sp.symbols('u v w', positive=True)
weights=lagrange_coefficients(u,v,w)
AA,CC,DD=polydata(u,v,w)
assert sp.cancel((weights[2]+weights[3])/weights[0]-AA/DD)==0
assert sp.cancel(weights[3]/weights[0]+CC/DD)==0
assert sp.factor(sum(weights))==0

# Three consecutive step lengths, in increasing n order: x, y, z.
A1,C1,D1=polydata(x,z,y)
A2,C2,D2=polydata(y,x,z)
A3,C3,D3=polydata(z,y,x)
P=sp.expand(D1*D2*D3)
U=sp.expand(A1*A2*A3 - A3*C2*D1 - A1*C3*D2 - A2*C1*D3)
V=sp.expand(C1*C2*C3)
# trace=U/P, determinant=V/P of the product M(z,y,x) M(y,x,z) M(x,z,y).
X=x**2*y**2*z**2*(x+y)*(x+z)*(y+z)
s=x+y+z
q2=x*y+x*z+y*z
Jm=sp.expand(P-U+V)
Jp=sp.expand(P+U+V)
Jd=sp.expand(P-V)
assert sp.expand(Jm - 6*X*s**4*q2)==0
assert sp.expand(Jd - X*s**2*sp.cancel(Jd/(X*s**2)))==0

def strict_positive_coefficients(q):
    poly=sp.Poly(sp.expand(q),x,y,z)
    assert poly.total_degree()>=0
    assert len(poly.terms())>0
    assert all(coef>0 for coef in poly.coeffs())
    return len(poly.terms())

# Exact, exhaustive algebraic certificates. All common factors X are positive.
H_minus=sp.cancel(Jm/X)
H_plus=sp.cancel(Jp/X)
H_det=sp.cancel(Jd/X)
print('Positive coefficients in three Schur factors:',
      strict_positive_coefficients(H_minus),
      strict_positive_coefficients(H_plus),
      strict_positive_coefficients(H_det))
assert sp.factor(H_minus)==6*s**4*q2
assert sp.Poly(H_plus,x,y,z).total_degree()==6
assert sp.Poly(H_det,x,y,z).total_degree()==6

def cyclic(a,b,c):
    return x**a*y**b*z**c+y**a*z**b*x**c+z**a*x**b*y**c
claimed_plus=(6*cyclic(5,0,1)+10*cyclic(4,2,0)+40*cyclic(4,1,1)
              +22*cyclic(4,0,2)+26*cyclic(3,3,0)+114*cyclic(3,2,1)
              +120*cyclic(3,1,2)+206*x**2*y**2*z**2)
claimed_det=(3*cyclic(5,1,0)+6*cyclic(5,0,1)+17*cyclic(4,2,0)
             +47*cyclic(4,1,1)+23*cyclic(4,0,2)+31*cyclic(3,3,0)
             +121*cyclic(3,2,1)+124*cyclic(3,1,2)
             +207*x**2*y**2*z**2)
assert sp.expand(H_plus-claimed_plus)==0
assert sp.expand(H_det-claimed_det)==0

# Determinant and trace limits along h=(t,1,t^{-1}).
t=sp.symbols('t',positive=True)
sub={x:t,y:sp.Integer(1),z:1/t}
tr=sp.cancel(U.subs(sub)/P.subs(sub))
det=sp.cancel(V.subs(sub)/P.subs(sub))
assert sp.limit(tr,t,sp.oo)==-1
assert sp.limit(det,t,sp.oo)==0
assert sp.limit(t*(tr+1),t,sp.oo)==sp.Rational(16,3)
assert sp.limit(t*det,t,sp.oo)==0
assert sp.limit(t**3*det,t,sp.oo)==sp.Rational(1,3)
print('Degeneration: trace -> -1, determinant -> 0, t*(trace+1) -> 16/3')

# Independent numerical construction from the full Lagrange formulas.
def direct_matrix(a,b,c):
    xx=np.array([0.,-a,-a-b,-a-b-c])
    ww=[]
    for i in range(4):
        if i==0:
            ww.append(sum(1/(xx[0]-xx[j]) for j in range(1,4)))
        else:
            ww.append(np.prod([xx[0]-xx[j] for j in range(1,4) if j!=i])/
                      np.prod([xx[i]-xx[j] for j in range(4) if j!=i]))
    # For i>0: w_i=L_i'(0), obtained by differentiating its numerator.
    return np.array([[(ww[2]+ww[3])/ww[0],ww[3]/ww[0]],[1.,0.]])

def float_poly_matrix(a,b,c):
    H=3*a*a+4*a*b+2*a*c+b*b+b*c
    K=a*a+4*a*b+2*a*c+3*b*b+3*b*c+c*c
    return np.array([[a*a*K/(b*(b+c)*H),-a*a*(a+b)**2/(c*(b+c)*H)],[1.,0.]])

rng=random.Random(271828)
count=0
for i in range(1200):
    steps=[10**rng.uniform(-3,3) for _ in range(3)]
    ma=direct_matrix(steps[0],steps[2],steps[1]);
    mb=direct_matrix(steps[1],steps[0],steps[2]);
    mc=direct_matrix(steps[2],steps[1],steps[0]);
    fa=float_poly_matrix(steps[0],steps[2],steps[1]);
    fb=float_poly_matrix(steps[1],steps[0],steps[2]);
    fc=float_poly_matrix(steps[2],steps[1],steps[0]);
    assert np.allclose(ma,fa,rtol=2e-7,atol=5e-10)
    assert np.allclose(mb,fb,rtol=2e-7,atol=5e-10)
    assert np.allclose(mc,fc,rtol=2e-7,atol=5e-10)
    mon=mc@mb@ma
    assert np.max(abs(np.linalg.eigvals(mon)))<1+1e-8
    count+=1
print('Independent sampled Lagrange matrices / monodromy comparisons:',count)
print('ALL EXACT AND NUMERICAL CHECKS PASSED')
