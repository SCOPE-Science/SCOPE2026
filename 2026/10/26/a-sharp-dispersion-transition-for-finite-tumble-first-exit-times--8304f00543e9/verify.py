#!/usr/bin/env python3
"""Algebraic and stochastic spot checks for a finite-tumble exit-time formula."""
import math, random
import sympy as sp
import mpmath as mp

x,p,z=sp.symbols('x p z', positive=True)
K2=z*(z+1)*(z+p+1)/(z+p)
# Entire hyperbolic expressions in K2, avoiding arbitrary branch at zero.
Den=1+(K2*x*x)/2+(K2*x*x)**2/24 +(z*(z+p+1)/(z+p))*x*(1+K2*x*x/6)  # terms to order z^2
Flap=sp.series(p/(p+z)/Den,z,0,3).removeO().expand()
mean=((p+1)*(x*x+2*x)+2)/(2*p)
variance=((p+1)**2*(x**4+4*x**3)+(12+6*p)*x*x+12*x+6)/(6*p*p)
assert sp.simplify(Flap.coeff(z,1)+mean)==0
assert sp.simplify(2*Flap.coeff(z,2)-mean**2-variance)==0
M=(p+1)*x*x+2*(p+1)*x+2
N=(p+1)**2*(x**4+4*x**3)+(12+6*p)*x*x+12*x+6
Q=2*N/(3*M*M)
B=(2*p*p+3*p-2)*x*x+(4*p-2)*x-1
assert sp.simplify(Q-sp.Rational(2,3)+4*B/(3*M*M))==0
C=(2*p**3+5*p*p+p-2)*x**3+(6*p*p+3*p-3)*x*x-6*p*x-6*p
assert sp.simplify(sp.diff(Q,x)-8*C/(3*M**3))==0
assert sp.simplify(Q-variance/mean**2)==0
print('Exact symbolic identities passed (five).')
mp.mp.dps=60
for pp in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('0.75'),mp.mpf('1'),mp.mpf('3')]:
  for xx in [mp.mpf('0.1'),mp.mpf('0.3'),mp.mpf('1'),mp.mpf('2'),mp.mpf('5'),mp.mpf('10')]:
    def f(zz):
      kk=mp.sqrt(zz*(zz+1)*(zz+pp+1)/(zz+pp))
      return pp/(pp+zz)/(mp.cosh(xx*kk)+kk/(1+zz)*mp.sinh(xx*kk))
    # Use true symmetric real derivatives; analytic continuation within neighborhood of origin.
    dm=-mp.diff(f,0); dv=mp.diff(f,0,2)-dm**2
    m=float(((pp+1)*(xx*xx+2*xx)+2)/(2*pp))
    v=float(((pp+1)**2*(xx**4+4*xx**3)+(12+6*pp)*xx**2+12*xx+6)/(6*pp**2))
    assert abs(float(mp.re(dm))/m-1)<1e-25
    assert abs(float(mp.re(dv))/v-1)<1e-25
print('60 high-precision moment checks passed.')

def sample_T(xx,pp,rng):
  t=0.0; loc=0.0; state=0
  for _ in range(1000000):
    if state==0:
      tau=rng.expovariate(pp)
      t+=tau;state=1 if rng.random()<0.5 else -1
    else:
      tau=rng.expovariate(1.0)
      delta=(xx-loc) if state>0 else (xx+loc)
      if delta<=tau:
        return t+delta
      loc+=state*tau;t+=tau;state=0
  raise RuntimeError('excess steps')

rng=random.Random(417225)
for pp,xx in [(0.25,1.),(0.5,1.),(1.,1.),(2.,2.),(5.,0.7)]:
  arr=[sample_T(xx,pp,rng) for _ in range(30000)]
  vm=sum(arr)/len(arr); vv=sum((v-vm)**2 for v in arr)/len(arr)
  em=float(mean.subs({x:xx,p:pp})); ev=float(variance.subs({x:xx,p:pp}))
  assert abs(vm/em-1)<0.03,(pp,xx,vm,em)
  assert abs(vv/ev-1)<0.08,(pp,xx,vv,ev)
  print(f'event-simulation p={pp}, x={xx}: mean {vm:.6f}/{em:.6f}, variance {vv:.6f}/{ev:.6f}')
print('All finite tests passed.')
