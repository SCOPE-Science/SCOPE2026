#!/usr/bin/env python3
"""Exact and numerical checks of two-component sampling comparison.
Run with Python 3 and SymPy 1.14 or newer.
"""
from fractions import Fraction
import math
import random
import sympy as sp

k, t = sp.symbols('k t', real=True)
A = 1-k*(1+t)/2
D = 1-k*(1-t)/2
h2 = k**2*(1-t**2)/4
p = sp.expand(A**2-h2)
r = sp.expand(D**2-h2)
q2 = sp.expand(h2*(D-A)**2)
r_plus=sp.factor(p**2+q2)
r_minus=sp.factor(r**2+q2)
h4=1-(1-k)**4
w_plus=sp.factor((r_plus+1-h4*(1+t)/2)/2)
w_minus=sp.factor((r_minus+1-h4*(1-t)/2)/2)
P=3*k**2*t**3+k**2*t**2+k**2*t-k**2-2*k*t**2-8*k*t+2*k+8*t
Q=19*k**6-116*k**5+356*k**4-848*k**3+1344*k**2-1104*k+368
assert sp.simplify(w_plus-w_minus-k*t*(k-2)*(k**2*t**2+(k-2)**2)/2)==0
assert sp.simplify(r_minus-w_minus+k**2*(2-k)*(1-t**2)*(2-k+k*t)/4)==0
assert sp.simplify(r_plus-w_minus-k*(k-2)*P/4)==0
assert sp.factor(sp.resultant(P, sp.diff(P,t), t))==48*k**4*Q
S=sp.sturm(Q,k)
signs=lambda pt:[int(sp.sign(s.subs(k,pt))) for s in S]
assert signs(sp.Rational(3,2)) == [1,-1,-1,1,1,-1,1]
assert signs(sp.Integer(2)) == [-1,-1,1,-1,-1,-1,1]
roots=sp.nroots(Q,maxsteps=150)
kr=[float(sp.re(z)) for z in roots if abs(float(sp.im(z)))<1e-10 and 1.5 < float(sp.re(z))<2]
assert len(kr)==1
kv=kr[0]
tstar=float(sp.nsolve(sp.diff(P,t).subs(k,kv), .34))
assert abs(float(P.subs({k:kv,t:tstar}))) < 1e-10
assert 1.64548<kv<1.64550 and .34232<tstar<.34233

kv=sp.Rational(5,3);tv=sp.Rational(1,3)
assert sp.factor(P.subs({k:kv,t:tv})) == -sp.Rational(4,81)
assert sp.factor(r_plus.subs({k:kv,t:tv})) == sp.Rational(1217,2187)
assert sp.factor(r_minus.subs({k:kv,t:tv})) == sp.Rational(802,2187)
assert sp.factor(w_plus.subs({k:kv,t:tv})) == sp.Rational(1117,2187)
assert sp.factor(w_minus.subs({k:kv,t:tv})) == sp.Rational(1202,2187)
assert sp.factor((r_plus-w_minus).subs({k:kv,t:tv})) == sp.Rational(5,729)

# Compare exact closed forms against direct products of two 2x2 matrices.
def matmul(X,Y):
    return [[sum(X[i][a]*Y[a][j] for a in range(2)) for j in range(2)] for i in range(2)]
def transpose(X):
    return [[X[j][i] for j in range(2)] for i in range(2)]
def matsum(X,Y):
    return [[X[i][j]+Y[i][j] for j in range(2)] for i in range(2)]
def squareform(X):
    return matmul(transpose(X),X)
def matscale(s,X):
    return [[s*x for x in row] for row in X]

r_eval=[sp.lambdify((k,t),expr,"math") for expr in [r_plus,r_minus,w_plus,w_minus,P]]
r_e0,r_e1,r_e2,r_e3,p_eval=r_eval
rng=random.Random(20261015)
count=0
for i in range(1000):
    K=rng.uniform(.00001,1.99999)
    T=rng.uniform(.00001,.99999)
    a=math.sqrt((1+T)/2);b=math.sqrt((1-T)/2)
    u=[a,b];v=[a,-b]
    B=lambda z:[[float(ii==jj)-K*z[ii]*z[jj] for jj in range(2)] for ii in range(2)]
    B1=B(u); B2=B(v)
    C12=matmul(B2,B1); C21=matmul(B1,B2)
    RR=matscale(.5,matsum(squareform(C12),squareform(C21)))
    WW=matscale(.25,matsum(matsum(squareform(matmul(B1,B1)),squareform(matmul(B2,B2))),matsum(squareform(C12),squareform(C21))))
    vals=[float(expr(K,T)) for expr in r_eval]
    for m,vec in [(RR,vals[:2]),(WW,vals[2:4])]:
        assert max(abs(m[0][1]),abs(m[1][0])) < 2e-12
        assert abs(m[0][0]-vec[0]) < 2e-12
        assert abs(m[1][1]-vec[1]) < 2e-12
        count+=3
    # Strictly mean-square contractive in the nondegenerate range.
    assert max(vals[:2])<1+1e-12
    assert max(vals[2:4])<1+1e-12
    count+=2
    # Full worst-direction criterion, including cases where R+ is not max.
    observed=max(vals[:2])-max(vals[2:4])
    if abs(vals[4])>1e-8 and K < 1.9999:
        assert (observed>0)==(vals[4]<0)
        count+=1

# Dense grid around threshold also validates sign classification.
for Ki in range(1,200):
    K=Ki/100
    for Ti in range(1,100):
        T=Ti/100
        pval=float(p_eval(K,T))
        rr=max(float(r_e0(K,T)),float(r_e1(K,T)))
        ww=float(r_e3(K,T))
        if abs(pval)>1e-9:
            assert (rr>ww)==(pval<0)
        count+=1
print('PASS',count,'direct/parametric assertions; sextic_kstar=%.12f tstar=%.12f'%(kv if isinstance(kv,float) else kr[0],tstar))
