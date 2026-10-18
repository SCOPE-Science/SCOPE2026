#!/usr/bin/env python3
"""Exact sixth-moment expansion for the six vertices of the A2 root hexagon.
No external libraries; all identities use integer and rational Laurent polynomials.
"""
from collections import defaultdict, Counter
from itertools import combinations_with_replacement, product
from fractions import Fraction
from math import factorial

ROOTS=((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))
EXP=((0,0,0),(1,0,0),(0,0,0),(0,1,0),(0,0,0),(0,0,1))
ZERO=(0,0,0)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def trim(d): return {k:v for k,v in d.items() if v}
def plus(*args):
 d=defaultdict(Fraction)
 for a in args:
  for k,v in a.items():d[k]+=v
 return trim(d)
def scale(a,x): return trim({k:v*x for k,v in a.items()})
def times(a,b):
 d=defaultdict(Fraction)
 for k,v in a.items():
  for l,w in b.items():d[add(k,l)]+=v*w
 return trim(d)
def conj(a):return {neg(k):v for k,v in a.items()}
def mon(k,c=1):return {k:Fraction(c)}

# Expand coefficient of a frequency in P^m, then sum modulus squares.
def moment(m):
 cube=defaultdict(lambda:defaultdict(int))
 for indices in combinations_with_replacement(range(6),m):
  n=factorial(m)
  for k in Counter(indices).values():n//=factorial(k)
  xy=tuple(sum(ROOTS[i][j] for i in indices) for j in range(2))
  a=tuple(sum(EXP[i][j] for i in indices) for j in range(3))
  cube[xy][a]+=n
 res=defaultdict(int)
 for g in cube.values():
  for a,mult in g.items():
   for b,nmult in g.items():res[tuple(a[i]-b[i] for i in range(3))]+=mult*nmult
 return dict(res),cube

m6,_=moment(3)
# The following independent expected coefficients are conjugate pairs.
expected={(0,0,0):996}
positive={(-2,-1,2):9,(-2,0,1):9,(-1,-2,2):9,(-1,-1,1):36,
 (-1,0,0):9,(-1,0,1):144,(-1,1,0):144,(0,-2,1):9,(0,-1,0):9,(0,-1,1):144}
for k,v in positive.items(): expected[k]=v; expected[neg(k)]=v
assert m6==expected, 'Sixth-moment coefficient table mismatch'

m4,_=moment(2)
U=mon((1,0,0));V=mon((0,1,0));W=mon((0,0,1))
S=plus(U,V,W)
formula4=plus(mon(ZERO,54),scale(times(S,conj(S)),4))
assert m4==formula4, 'Fourth-moment identity mismatch'

# Check the trigonometric normal form EXACTLY after replacing
# a=A*B, b=A/B, c=A*F and t=(B+B^-1)/2, cos(phi)=(F+F^-1)/2.
def substitute(exps):
 out=defaultdict(Fraction)
 for (u,v,w),coef in exps.items():
  out[(u+v+w,u-v,w)]+=coef
 return trim(out)
a2=mon((1,0,0));b2=mon((0,1,0));f2=mon((0,0,1))
t=scale(plus(b2,conj(b2)),Fraction(1,2))
cosphi=scale(plus(f2,conj(f2)),Fraction(1,2))
cosphialpha=scale(plus(times(f2,conj(a2)),times(conj(f2),a2)),Fraction(1,2))
B=plus(mon(ZERO),scale(times(t,t),2),scale(times(t,cosphi),2))
normal=plus(mon(ZERO,708),scale(times(t,t),576),scale(times(t,cosphi),576),scale(times(B,cosphialpha),36))
assert substitute(m6)==normal, 'Real-variable normal form mismatch'

# Exact sixth-root values in Z[eta], eta=exp(pi*i/3), eta^2=eta-1.
ETA=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
def value(k):
 out=[0,0]
 for exp,co in m6.items():
  j=sum(e*kk for e,kk in zip(exp,k))%6
  out[0]+=co*ETA[j][0];out[1]+=co*ETA[j][1]
 return tuple(out)
answers={}
for k in product(range(6),repeat=3):
 val=value(k)
 assert val[1]==0, 'Moment not real for sixth-root test'
 answers[k]=val[0]
assert min(answers.values())==546
assert max(answers.values())==2040
assert {k for k,v in answers.items() if v==546}=={(1,5,3),(5,1,3)}
assert {k for k,v in answers.items() if v==2040}=={(0,0,0)}

# Every lattice triple sum falls in [-3,3]^2: no alias on grids >=7.
assert all(-3<=a<=3 and -3<=b<=3 for a,b in moment(3)[1])
for n in (7,8,11):
 keys=list(moment(3)[1].keys())
 assert len({(x%n,y%n) for x,y in keys})==len(keys)

print('PASS: exact fourth and sixth coefficient identities, real normal form,')
print('      full mu6 phase census (216 triples), two minimizers, one maximizer,')
print('      finite-grid nonaliasing at orders 7, 8, 11.')
