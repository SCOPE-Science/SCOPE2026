#!/usr/bin/env python3
"""Exact exhaustive certificate on the 729 saturated occupancy profiles."""
from itertools import product
from collections import Counter
from math import comb, factorial

C=tuple(product(range(3),repeat=6))
CAP=lambda z:min(z,2)
ZERO={(a,0,0,b,0,0) for a,b in product(range(3),repeat=2)}
THREE={(2,2,2,2,2,2)}
FOUR={(2,0,2,2,2,0),(2,2,0,2,0,2)}
R=ZERO|THREE|FOUR

def f(c):
 a,b=c[:3],c[3:]
 def go(x,opp):
  return (x[2],x[0],x[1]) if opp[1]==2 else (CAP(x[0]+x[2]),0,x[1])
 return go(a,b)+go(b,a)

assert len(C)==729 and len(R)==12
assert all(f(x)==x for x in ZERO|THREE)
assert f(tuple(sorted(FOUR)[0]))==tuple(sorted(FOUR)[1])
assert f(tuple(sorted(FOUR)[1]))==tuple(sorted(FOUR)[0])

def classify(v):
 for t in range(6):
  if v in ZERO:return t,1
  if v in THREE:return t,3
  if v in FOUR:return t,4
  v=f(v)
 raise AssertionError(('not recurrent within 5',v))

classes={v:classify(v) for v in C}
census=Counter(classes.values())
assert sum(census.values())==729
expected={(0,1):9,(0,3):1,(0,4):2,
          (1,1):72,(1,4):10,(2,1):360,(2,4):30,
          (3,1):160,(3,4):8,(4,1):51,(4,4):2,(5,1):24}
assert census==expected,(census,expected)

def feasible(v,s):
 minimum=sum(v)
 return minimum<=s if 2 in v else minimum==s

def sharp(m,n):
 return max(classes[a+b][0] for a in product(range(3),repeat=3) if feasible(a,m)
                            for b in product(range(3),repeat=3) if feasible(b,n))
for m in range(1,11):
 for n in range(1,11):
  if min(m,n)==1:want=2 if m==n==1 else 3
  elif min(m,n)==2:want=3 if m==n==2 else 4
  elif m==n==3:want=4
  else:want=5
  assert sharp(m,n)==want,(m,n,sharp(m,n),want)

def Rcount(s):return sum(comb(s,j) for j in range(2,s-1))
def Ecount(s):return sum(factorial(s)//(factorial(a)*factorial(b)*factorial(s-a-b))
 for a in range(2,s-3) for b in range(2,s-a-1) if s-a-b>=2)
assert Rcount(4)==6 and Ecount(6)==90

# For every realizable capped profile, the precise terminal period follows
# solely from membership of the first recurrent capped profile in ZERO/THREE/FOUR.
for v in C:
 x=v
 for t in range(classes[v][0]):x=f(x)
 assert x in R
 assert (1 if x in ZERO else 3 if x in THREE else 4)==classes[v][1]
print('SYMBOLIC_OK states=729 recurrent=12 bound=5 classes='+str(sorted(census.items())))
print('SHARP_OK matrix_mn_1_to_6='+str([[sharp(m,n) for n in range(1,7)] for m in range(1,7)]))
print('PERIODIC_EXAMPLES m=n=6 fixed=1 period3='+str(Ecount(6)**2)+' period4='+str(2*Rcount(6)**2))
