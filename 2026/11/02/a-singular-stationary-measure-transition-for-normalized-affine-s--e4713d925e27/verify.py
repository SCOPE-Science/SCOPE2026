"""Exact algebra and independent numerical checks of an axisymmetric sphere map."""
from sympy import symbols, factor, simplify, sqrt, Rational
from math import sqrt as fsqrt
import random
random.seed(211)

A,R,h=symbols('A R h', positive=True, real=True)
Delta=(A-h)**2+R**2*(1-h**2)
c=(1-R**2)
identity=factor(Delta-(1-c*h/A)**2)
assert simplify(identity-((A-(1+R)*h)*(A-(1-R)*h)*(A*A+R*R-1)/A**2))==0
assert simplify(Delta.subs(h,A/(1+R))-R**2)==0
assert simplify((1-c*h/A).subs(h,A/(1-R))+R)==0
assert factor(Delta.subs(R**2,1-A**2))==(A*h-1)**2
f=(A-h)/(1-A*h)
assert simplify(f.subs(h,f)-h)==0
assert simplify(1-f**2-((1-A**2)*(1-h**2)/(1-A*h)**2))==0
assert simplify(f.diff(h)+(1-A**2)/(1-A*h)**2)==0
Lq=((1-A**2/(1+R))/R)**2
Lp=R**2/(1-A*A)
assert factor((Lq-1))==factor((1-A*A/(1+R)-R)*(1-A*A/(1+R)+R)/R**2)
assert simplify(Lq.subs(A**2,1-R**2)-1)==0
assert simplify(Lp.subs(A**2,1-R**2)-1)==0
for alpha,r in [(0.2,0.6),(0.7,0.6),(0.8,0.6),(0.95,0.6),(0.5,0.3)]:
    def step(x):
        y=[alpha-x[0]]+[-r*t for t in x[1:]]
        norm=fsqrt(sum(t*t for t in y))
        return [t/norm for t in y]
    pole=[1.,0.,0.,0.]
    assert max(abs(z-w) for z,w in zip(step(step(pole)),pole))<1e-13
    hs=alpha/(1+r)
    q=[hs,fsqrt(1-hs*hs),0,0]
    assert max(abs(z-w) for z,w in zip(step(step(q)),q))<1e-13
    for k in range(80):
        ts=[random.gauss(0,1) for _ in range(4)]
        nn=fsqrt(sum(z*z for z in ts)); x=[z/nn for z in ts]
        if abs(alpha*alpha+r*r-1)<1e-14:
            assert max(abs(z-w) for z,w in zip(step(step(x)),x))<1e-12
        else:
            old=x[0]
            for j in range(4000):x=step(x)
            target=(1 if old>hs else -1) if alpha*alpha+r*r<1 else hs
            assert abs(x[0]-target)<1e-8,(alpha,r,old,x[0],target)
    print('checked',alpha,r,'side',round(alpha*alpha+r*r-1,5))
print('PASS: exact symbolic identities, sphere orbit tests, and stability-side trajectories')
