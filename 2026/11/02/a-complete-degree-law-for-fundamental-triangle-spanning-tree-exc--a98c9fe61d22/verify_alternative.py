#!/usr/bin/env python3
"""Independent formal-coefficient recurrence for cyclic-gap mobility polynomial."""
from collections import defaultdict

def polynomials(n):
 # Weighted cyclic compositions: n/m * sum over m ordered positive gaps.
 layers=[{(0,0):1}]
 for m in range(1,n+1):
  last=layers[-1]; this=defaultdict(int)
  for (length,activity),count in last.items():
   for gap in range(1,n-length+1):
    this[(length+gap,activity+1)]+=count*(1 if gap==1 else 2)
    if gap>=3:this[(length+gap,activity+2)]+=count*(gap-2)
  layers.append(this)
 result=defaultdict(int)
 for m in range(1,n+1):
  for (length,activity),count in layers[m].items():
   if length==n:
    assert count*n%m==0
    result[activity]+=count*n//m
 return dict(result)

def fib(n):
 p,q=0,1
 for _ in range(n):p,q=q,p+q
 return p

def lucas(n):
 p,q=2,1
 for _ in range(n):p,q=q,p+q
 return p
for r in range(3,13):
 a=polynomials(r)
 assert sum(a.values())==lucas(2*r)-2,(r,a)
 assert sum(k*v for k,v in a.items())==3*r*fib(2*r-2)
 assert a.get(1)==2*r and a.get(r)==1
 print('WHEEL_ALTERNATIVE_OK',r,len(a),sum(a.values()))
print('WHEEL_ALTERNATIVE_COMPLETE')
