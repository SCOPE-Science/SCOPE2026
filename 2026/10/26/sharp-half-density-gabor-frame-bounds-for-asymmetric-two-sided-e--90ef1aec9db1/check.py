"""Reproduce identities and numerical spot checks for asymmetric Laplace Gabor bounds.
Run: python check.py (Python 3, sympy, numpy).
"""
import cmath
import math
import random
import sympy as sp

def bounds(a,b):
    u,v=math.exp(-a),math.exp(-b)
    alpha=1/(1+u*u)
    beta=v*v/(1+v*v)
    gamma=v*(u+v)/((1+u*u)*(1+v*v))
    y=((b-a)*gamma+math.sqrt((b-a)**2*gamma**2+4*a*b*alpha*beta))/(2*b*beta)
    x=math.log(y)/(a+b)
    amin=2*(alpha*math.exp(-2*a*x)+beta*math.exp(2*b*x)-2*gamma*math.exp((b-a)*x))
    bmax=2*((1/(1-u*u)+v*v/(1-v*v))**2+(u/(1-u*u)+v/(1-v*v))**2)
    return amin,bmax,x

def symbol(a,b,x,w):
    u,v=math.exp(-a),math.exp(-b)
    A,B=math.exp(-a*x),math.exp(b*x)
    t=cmath.exp(2j*math.pi*w)
    Z=lambda t:A/(1-u/t)+B*v*t/(1-v*t)
    return abs(Z(t))**2+abs(Z(-t))**2

def ztruncated(a,b,x,w,n=300):
    return sum((math.exp(-a*(x+k)) if x+k>=0 else math.exp(b*(x+k)))*cmath.exp(-2j*math.pi*k*w) for k in range(-n,n+1))

u,v,A,B,q=sp.symbols('u v A B q', positive=True)
E=A*q/(q-u*u)+B*v*v*q/(1-v*v*q)
O=(A*u*(1-v*v*q)+B*v*(q-u*u))/((q-u*u)*(1-v*v*q))
Ce=A-B*u*u*v*v;De=v*v*(B-A)
Co=u*(A-B*u*v);Do=v*(B-A*u*v)
assert sp.simplify(E-q*(Ce+De*q)/((q-u*u)*(1-v*v*q)))==0
assert sp.simplify(O-(Co+Do*q)/((q-u*u)*(1-v*v*q)))==0
alpha=1/(1+u*u);beta=v*v/(1+v*v);gamma=v*(u+v)/((1+u*u)*(1+v*v))
Sminus=2*((A/(1+u*u)-B*v*v/(1+v*v))**2+(A*u/(1+u*u)-B*v/(1+v*v))**2)
assert sp.simplify(Sminus-2*(alpha*A*A+beta*B*B-2*gamma*A*B))==0
Q1=sp.factor((-sp.Symbol('a')*alpha+sp.Symbol('b')*beta-(sp.Symbol('b')-sp.Symbol('a'))*gamma)*((1+u*u)*(1+v*v)))
assert sp.simplify(Q1+(1-u*v)*(sp.Symbol('a')+sp.Symbol('b')*u*v))==0
print('symbolic parity, minimum energy, endpoint derivative identities: PASS')
rng=random.Random(20261021)
for j in range(72):
    a=math.exp(rng.uniform(-1.8,1.4));b=math.exp(rng.uniform(-1.8,1.4))
    amin,bmax,x=bounds(a,b)
    assert 0<x<1 and amin>0 and bmax>amin, (a,b,x,amin,bmax)
    for ii in range(12):
        xx=rng.random();w=rng.random()
        s=symbol(a,b,xx,w)
        assert amin-2e-10<=s<=bmax+2e-10,(a,b,x,s,amin,bmax)
        assert abs(s-(abs(ztruncated(a,b,xx,w))**2+abs(ztruncated(a,b,xx,w+.5))**2))<2e-8,(a,b,xx,w)
    assert abs(symbol(a,b,x,.25)-amin)<2e-10
    assert abs(symbol(a,b,0,0)-bmax)<2e-10
print('72 rate pairs, 864 independent truncated Zak comparisons, and extremal evaluations: PASS')
for a,b in [(1,1),(1,3),(3,1),(.2,3),(3,.2),(4,4)]:
    lo,hi,x=bounds(a,b)
    print(f'a={a:g}, b={b:g}: A_opt={lo:.12g}, B_opt={hi:.12g}, x_min={x:.12g}, kappa={hi/lo:.12g}')
