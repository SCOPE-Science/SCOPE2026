#!/usr/bin/env python3
"""Standalone exact and high-precision checks for a two-cycle theorem.
Requires SymPy and mpmath; finite tests supplement, not replace, its proof.
"""
import sympy as sp
from mpmath import mp

z, mu, w, c = sp.symbols('z mu w c', real=True)
poly = z**5-mu*z**4+mu*z-1
quartic = z**4+(1-mu)*(z**3+z**2+z)+1
assert sp.expand(poly-(z-1)*quartic)==0
assert sp.expand(quartic/z**2-(w**2+(1-mu)*w-(1+mu))).subs(w,z+1/z).simplify()==0
roots = [(mu-1+sp.sqrt(mu**2+2*mu+5))/2,
         (mu-1-sp.sqrt(mu**2+2*mu+5))/2]
for root in roots:
    assert sp.simplify(root**2+(1-mu)*root-(1+mu))==0
p = (1-mu**2)/(1-2*mu*c+mu**2)
B=sp.Matrix([[1+p,1],[p,1]])
assert sp.simplify(B.det())==1
assert sp.simplify(sp.trace(B)-(2+p))==0
for sign in [1,-1]:
    rr=sp.sqrt(mu**2+2*mu+5)
    q=2*(1-mu**2)/(2+mu+mu**2-sign*mu*rr)
    w0=(mu-1+sign*rr)/2
    assert sp.simplify(q-(1-mu**2)/(1-mu*w0+mu**2))==0
    assert sp.simplify(sp.limit(q/(1-mu),mu,1)-(2+sign*sp.sqrt(2)))==0
mp.dps=70

def f(u,s):
    a=2*mp.pi*s
    return mp.atan(u*mp.sin(a)/(1-u*mp.cos(a)))/mp.pi

def T(u,s,t):
    return ((2*s+t+f(u,s))%1, (s+t+f(u,s))%1)

def distance(a,b):
    return min(abs(a-b),abs(a-b+1),abs(a-b-1))

def chi(u,s):
    a=2*mp.pi*s
    q=(1-u*u)/(1-2*u*mp.cos(a)+u*u)
    return mp.acosh(1+q/2)

for u in map(mp.mpf,['0.00001','0.07','0.4','0.8','0.99999']):
    r=mp.sqrt(u*u+2*u+5)
    exps=[]
    for sign in [1,-1]:
        ss=mp.acos((u-1+sign*r)/4)/(2*mp.pi)
        tt=(2*ss)%1
        a,b=T(u,ss,tt)
        assert max(distance(a,(-ss)%1),distance(b,(-2*ss)%1))<mp.mpf('1e-60')
        aa,bb=T(u,a,b)
        assert max(distance(aa,ss),distance(bb,tt))<mp.mpf('1e-60')
        exact=mp.acosh(1+(1-u*u)/(2+u+u*u-sign*u*r))
        assert abs(chi(u,ss)-exact)<mp.mpf('1e-60')
        exps.append(exact)
    assert exps[0]>exps[1]>0
    if u<mp.mpf('0.001'):
        assert abs((exps[0]-exps[1])/u-1)<mp.mpf('0.0001')
    if u>mp.mpf('0.99'):
        eps=1-u
        for sign,cc in [(1,exps[0]),(-1,exps[1])]:
            assert abs(cc/mp.sqrt(eps)-mp.sqrt(2+sign*mp.sqrt(2)))<mp.mpf('0.0001')
        assert abs(exps[0]/exps[1]-(1+mp.sqrt(2)))<mp.mpf('0.0001')
print('PASS: exact polynomial, Jacobian, radical identities, endpoints, and 20 high-precision return/spectrum checks')
