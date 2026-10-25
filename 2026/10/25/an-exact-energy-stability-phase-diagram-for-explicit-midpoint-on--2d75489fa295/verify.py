"""Exact rational-polynomial checks of the explicit-midpoint energy identities.

No external packages are required. This verifies algebraic identities, not
independent novelty or every analytic quantifier in the written proof.
"""
from fractions import Fraction as F

# Bivariate polynomials in (h,b), sparse integer exponent tuples.
def const(v):
    return {} if v == 0 else {(0, 0): F(v)}
def var(which):
    return {(1, 0) if which == 'h' else (0, 1): F(1)}
def add(p, q):
    z = p.copy()
    for k, v in q.items():
        z[k] = z.get(k, F(0)) + v
        if z[k] == 0:
            del z[k]
    return z
def neg(p):
    return {k:-v for k,v in p.items()}
def sub(p, q):
    return add(p, neg(q))
def mul(p, q):
    z={}
    for (a,b),u in p.items():
        for (c,d),v in q.items():
            k=(a+c,b+d)
            z[k]=z.get(k,F(0))+u*v
            if z[k]==0: del z[k]
    return z
def scale(p, q):
    return mul(p,const(q))
def powp(p,n):
    z=const(1)
    for _ in range(n):z=mul(z,p)
    return z
def mm(a,b):
    return [[add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j]))
             for j in range(2)] for i in range(2)]
def mt(a):
    return [[a[j][i] for j in range(2)] for i in range(2)]
def madd(a,b):
    return [[add(a[i][j],b[i][j]) for j in range(2)] for i in range(2)]
I=[[const(int(i==j)) for j in range(2)] for i in range(2)]
h=var('h'); b=var('b'); t=powp(b,2)
L=[[const(-1),neg(b)],[b,const(0)]]
R=madd(madd(I,[[mul(h,L[i][j]) for j in range(2)] for i in range(2)]),
       [[scale(mul(powp(h,2),v),F(1,2)) for v in row] for row in mm(L,L)])
Q=[[sub(I[i][j],mm(mt(R),R)[i][j]) for j in range(2)] for i in range(2)]
g=sub(add(mul(powp(t,2),powp(h,3)),scale(h,4)),add(scale(mul(t,powp(h,2)),2),const(8)))
expected_22=scale(mul(mul(t,powp(h,3)),sub(const(4),mul(add(const(1),t),h))),F(1,4))
expected_12=scale(mul(mul(b,powp(h,2)),powp(sub(h,const(2)),2)),F(-1,4))
det=sub(mul(Q[0][0],Q[1][1]),mul(Q[0][1],Q[1][0]))
expected_det=scale(mul(mul(mul(t,powp(h,4)),sub(const(2),mul(t,h))),g),F(-1,16))
assert Q[1][1] == expected_22
assert Q[0][1] == expected_12
assert det == expected_det

def gv(t,x):
    return t*t*x**3-2*t*x*x+4*x-8
assert gv(F(3,8),F(8,3))==0
assert gv(F(1),F(2))==0
assert gv(F(4),F(1,2))<0
assert gv(F(4),F(1))>0
# At the critical balanced point, midpoint is precisely -I.
def ev(poly,hh,bb):
    return sum(v*hh**i*bb**j for (i,j),v in poly.items())
assert [[ev(R[i][j],F(2),F(1)) for j in range(2)] for i in range(2)] == [[-1,0],[0,-1]]
# Direct rational checking of the maximum and explicit spectral gap.
assert gv(F(3,8),F(8,3)+F(1,100))>0
assert gv(F(3,8),F(8,3)-F(1,100))<0
def phi(t,x):
    return t*t*x**3-2*t*x*x+2*x-4
assert phi(F(2), F(1)) < 0
assert phi(F(100), F(1,20)) < 0 and F(1,20)>F(2,100)
print('VERIFY_OK')
