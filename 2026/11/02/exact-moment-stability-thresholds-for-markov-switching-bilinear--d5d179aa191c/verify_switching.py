"""Standalone finite checks for an exact stochastic switching law.

Run: python verify_switching.py
Dependencies: Python 3, numpy, sympy (used only for symbolic checks).
Analytical infinite-time conclusions are proved in RESULT.md, not by these finite tests.
"""
from fractions import Fraction
from itertools import product
import math
import random
import numpy as np
import sympy as sp

COUNT = 0

def close(a, b, tol=2e-11):
    global COUNT
    assert abs(float(a)-float(b)) <= tol*(1+abs(float(a))+abs(float(b))), (a,b)
    COUNT += 1

u,v,p=sp.symbols('u v p',real=True)
a=1+2*u+v
b=1-2*u+v
f=sp.expand(a*b)
assert sp.simplify(f-((1+v)**2-4*u**2))==0
COUNT+=1
T=sp.Matrix([[(1-p)*a,p*b],[p*a,(1-p)*b]])
assert sp.simplify(T.trace()-2*(1-p)*(1+v))==0
assert sp.simplify(T.det()-(1-2*p)*f)==0
COUNT+=2
pc=(4*u*u-v*v)/(2*(4*u*u-v-v*v))
assert sp.simplify((sp.eye(2)-T).det().subs(p,pc))==0
COUNT+=1

x=sp.symbols('x',positive=True)
beta,d=sp.symbols('beta d',real=True)
expr=sp.expand((f-1).subs({u:x*beta,v:x*x*(beta*beta+d*d)}))
assert sp.simplify(expr-x*x*(x*x*(beta*beta+d*d)**2-2*(beta*beta-d*d)))==0
COUNT+=1

rng=np.random.default_rng(84691)
J=np.array([[0.,1.],[-1.,0.]])
I=np.eye(2)
for i in range(100):
    xx=float(rng.uniform(.02,.75)); be=float(rng.uniform(-3.,3.)); dd=float(rng.uniform(.01,2.))
    zz=rng.normal(size=2)
    for sign in (-1,1):
        K=(1+sign*xx*be)*I+sign*xx*dd*J
        mag=(1+sign*xx*be)**2+(xx*dd)**2
        close(np.linalg.norm(K@zz)**2,mag*np.linalg.norm(zz)**2)
        close(np.linalg.det(K),mag)

# Exact exhaustive path enumeration vs matrix-transfer formulas.
xx=.2;be=-2.;dd=1.
A=(1+xx*be)**2+(xx*dd)**2
B=(1-xx*be)**2+(xx*dd)**2
close(A,2/5);close(B,2.)
for pp in [0.12,0.5,0.73,0.75,0.8,0.93,1.]:
    P=np.array([[1-pp,pp],[pp,1-pp]])
    for power in [0.5,1.,2.,4.]:
        aa=A**(power/2); bb=B**(power/2)
        DD=np.diag([aa,bb]);TT=P@DD
        initial=np.array([.5,.5]);ones=np.ones(2)
        for n in range(1,9):
            formula=initial@DD@np.linalg.matrix_power(TT,n-1)@ones
            enumerated=0.
            for path in product([0,1],repeat=n):
                prob=.5
                weight=1.
                for t,sgn in enumerate(path):
                    weight *= (aa if sgn==0 else bb)
                    if t:prob*= P[path[t-1],sgn]
                enumerated+=prob*weight
            close(formula,enumerated)

# Critical moment formula and sharp comparison to the Perron root.
for q in [0.2,0.5,1.,2.,3.,4.,6.]:
    aa=A**(q/2);bb=B**(q/2)
    threshold=(1-aa)*(bb-1)/(aa+bb-2*aa*bb)
    assert 0<threshold<1
    COUNT+=1
    for pp in [0.03,.2,.49,.5,.6,.75,.85,.92,.98,1.]:
        TT=np.array([[(1-pp)*aa,pp*bb],[pp*aa,(1-pp)*bb]])
        r=max(abs(np.linalg.eigvals(TT)))
        assert ((r<1) if pp>threshold+1e-9 else (r>1) if pp<threshold-1e-9 else abs(r-1)<1e-8)
        COUNT+=1

# Check the exact rational example and sign of second/fourth moment stability.
assert Fraction(2,5)*Fraction(2,1)==Fraction(4,5)
assert (Fraction(1,1)-Fraction(2,5))*(Fraction(2,1)-1)/(Fraction(2,5)+2-2*Fraction(4,5)) == Fraction(3,4)
assert (Fraction(1,1)-Fraction(4,25))*(Fraction(4,1)-1)/(Fraction(4,25)+4-2*Fraction(16,25)) == Fraction(7,8)
COUNT+=3
for pp in [0.5,0.75,0.8,0.875,1.]:
    for q in [2.,4.]:
        aa=A**(q/2);bb=B**(q/2)
        P=np.array([[1-pp,pp],[pp,1-pp]])
        TT=P@np.diag([aa,bb])
        r=max(abs(np.linalg.eigvals(TT)))
        print(f'flip={pp:.3f} order={q:g} moment_Perron={r:.12g}')
print('PASS',COUNT,'finite/symbolic checks')
