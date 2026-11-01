"""Recompute exact algebraic identities supporting the Poisson three-atom resolution theorem.

Run: python CHECK.py. Standard library only. This is a check of finite algebraic identities,
not a replacement for the analytic root-count and asymptotic arguments.
"""
from fractions import Fraction as F
from math import sqrt

# Sparse exact bivariate polynomials in x and s.
def const(a):
    a=F(a)
    return {(0,0):a} if a else {}
def var(i):
    return {(1,0):F(1)} if i=='x' else {(0,1):F(1)}
def add(*polys):
    r={}
    for p in polys:
        for k,c in p.items(): r[k]=r.get(k,F(0))+c
    return {k:c for k,c in r.items() if c}
def mul(*polys):
    r=const(1)
    for p in polys:
        tmp={}
        for (i,j),a in r.items():
            for (u,v),b in p.items():
                k=(i+u,j+v);tmp[k]=tmp.get(k,F(0))+a*b
        r={k:c for k,c in tmp.items() if c}
    return r
def scale(p,c):return {k:a*F(c) for k,a in p.items() if a*F(c)}
def power(p,n):
    r=const(1)
    for _ in range(n):r=mul(r,p)
    return r
def derivative(p,v):
    z=0 if v=='x' else 1
    out={}
    for exp,a in p.items():
        if exp[z]:
            nxt=(exp[0]-1,exp[1]) if z==0 else (exp[0],exp[1]-1)
            out[nxt]=a*exp[z]
    return out

X=var('x'); S=var('s'); I=const(1); X2=power(X,2)
A=add(X2,S)
B=add(X2,S,scale(X,-2),I)
C=add(X2,S,scale(X,2),I)
y=X2
Q=add(scale(power(add(y,S),4),3),mul(add(scale(S,4),I),add(I,scale(y,-4))))
# Derivative of the three reciprocal kernels multiplied by their common denominator.
num=scale(add(mul(X,power(B,2),power(C,2)),
              mul(add(X,scale(I,-1)),power(A,2),power(C,2)),
              mul(add(X,I),power(A,2),power(B,2))),-2)
assert add(num,scale(mul(X,Q),2))=={}, 'Derivative numerator identity failed'

# At the threshold s=1/2 verify the double critical root exactly.

def eval_poly(p,x,s):
    return sum(a*F(x)**i*F(s)**j for (i,j),a in p.items())
# Direct threshold factor: 3(2y-1)^2(4y^2+12y+17)/16, substitute y=x^2.
Qc=scale(mul(power(add(scale(y,2),scale(I,-1)),2),
             add(scale(power(y,2),4),scale(y,12),scale(I,17))),F(3,16))
# Equality specialized to s=1/2 (as a polynomial in x).
def specialize_s(p,v):
    out={}
    for (i,j),c in p.items():out[(i,0)]=out.get((i,0),F(0))+c*F(v)**j
    return {k:c for k,c in out.items() if c}
assert specialize_s(Q,F(1,2))==Qc,'Threshold factorization failed'
# Root-bracketing examples (checks, not proof for all s).
for s in [F(1,100),F(1,4),F(49,100)]:
    # Q(0)>0; unique min y0 from derivative; Q(y0)<0 numerically.
    r=((4*float(s)+1)/3)**(1/3)
    y0=r-float(s)
    Q0=float(eval_poly(Q,F(0),s))
    qmin=9*r**4*(r*r-1)
    assert y0>0 and Q0>0 and qmin<0
for s in [F(51,100),F(1),F(3)]:
    r=((4*float(s)+1)/3)**(1/3)
    assert r>1

print('CHECK_OK: exact two-variable derivative identity, exact critical factorization, strict-minimum root controls')
