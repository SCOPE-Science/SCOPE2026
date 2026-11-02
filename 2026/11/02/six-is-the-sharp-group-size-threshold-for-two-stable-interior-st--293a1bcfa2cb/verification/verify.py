#!/usr/bin/env python3
"""Exact checks for the two-stage public-goods threshold theorem.
Requires sympy >= 1.13. Does not use numerical fitting or simulation.
"""
from itertools import product
from math import comb
import sympy as sp

x, y, t, a, b, c = sp.symbols('x y t a b c', real=True)
count = 0

def check(statement):
    global count
    assert statement
    count += 1

def eq(expr, expected=0):
    check(sp.simplify(sp.expand(expr - expected)) == 0)

def pivotal(N, rewards):
    return sp.expand(sum(reward * comb(N-1, m-1) * x**(m-1) * (1-x)**(N-m)
                         for m, reward in rewards.items()))

# Focal-person pivotality formula, independently enumerated by all coplayer configurations.
for N in (4,5,6):
    th = {2: sp.Rational(7, 5), N-1: sp.Rational(9, 8)} if N>4 else {2:sp.Rational(7,5),3:sp.Rational(9,8)}
    if N==4: th={2:sp.Rational(7,5),3:sp.Rational(9,8)}
    P = pivotal(N, th)
    for den in (7, 11, 17):
        for num in range(1, den):
            q = sp.Rational(num,den)
            direct = sp.Rational(0)
            for bits in product((0,1),repeat=N-1):
                k=sum(bits)
                prob=q**k*(1-q)**(N-1-k)
                gain=sum(reward*int(k+1>=m>k) for m,reward in th.items())
                direct += prob*gain
            eq(direct,P.subs(x,q))

# Exact six-person symmetric two-good formula, its critical points and critical levels.
F = pivotal(6,{2:b,5:b})
eq(F,5*b*x*(1-x)*((1-x)**3+x**3))
eq(F.subs(x,sp.Rational(1,2)+y),b*(sp.Rational(5,16)+sp.Rational(5,2)*y**2-15*y**4))
eq(sp.diff(F,x).subs(x,sp.Rational(1,2)+y),5*b*y*(1-12*y**2))
for z in (sp.Rational(1,2), sp.Rational(1,2)-1/(2*sp.sqrt(3)),sp.Rational(1,2)+1/(2*sp.sqrt(3))):
    eq(sp.diff(F,x).subs(x,z))
eq(F.subs(x,sp.Rational(1,2)),5*b/16)
for z in (sp.Rational(1,2)-1/(2*sp.sqrt(3)),sp.Rational(1,2)+1/(2*sp.sqrt(3))):
    eq(F.subs(x,z),5*b/12)
eq(F.subs(x,0))
eq(F.subs(x,1))

# The cost c=b/3 yields four distinct interior roots, with exactly two stable.
G = sp.factor((F-b/3).subs(b,1))
eq(G,-15*(x-sp.Rational(1,2))**4+sp.Rational(5,2)*(x-sp.Rational(1,2))**2-sp.Rational(1,48))
check(sp.Poly(G,x).count_roots(0,1)==4)
roots=sorted([sp.Rational(1,2)+eps*sp.sqrt((5+sigma*2*sp.sqrt(5))/60)
              for sigma in (-1,1) for eps in (-1,1)],key=lambda z:float(z))
for i,z in enumerate(roots):
    eq(G.subs(x,z))
    check(0<float(z)<1)
    derivative=float(sp.diff(G,x).subs(x,z))
    check(derivative < 0 if i in (1,3) else derivative >0)
for j in range(5):
    lo = sp.Integer(0) if j==0 else roots[j-1]
    hi = sp.Integer(1) if j==4 else roots[j]
    sign=float(G.subs(x,(lo+hi)/2))
    check(sign > 0 if j in (1,3) else sign<0)

# For N=5, only thresholds (2,4) could have four variations. Their gain before cost
# is (A t+B t**3)/(1+t)**4, where t=x/(1-x), A=4*b_2, B=4*b_4.
A,B=sp.symbols('A B',positive=True)
Q=A-3*A*t+3*B*t**2-B*t**3
eq(sp.diff((A*t+B*t**3)/(1+t)**4,t)*(1+t)**5,Q)
eq(sp.discriminant(Q,t),-108*A*B*(A-B)**2)
eq(Q.subs(B,A), A*(1-t)**3)

# Exact Descartes sign-variation combinatorics for all pairs of strictly interior
# project thresholds in all N up to 5, over representative strict coefficient signs.
for N in range(2,6):
    choices=range(2,N)
    for m1 in choices:
      for m2 in choices:
        if m1>=m2: continue
        for h1,h2 in product((sp.Rational(1,2),sp.Integer(2)),repeat=2):
          d=[(h1 if j==m1-1 else 0)+(h2 if j==m2-1 else 0)-1
             for j in range(N)]
          signs=[sp.sign(v) for v in d if v]
          variations=sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))
          if N==5 and (m1,m2)==(2,4):
            check(variations<=4)
          else:
            check(variations<=2)
print(f'PASS: {count} exact rational/symbolic assertions')
