#!/usr/bin/env python3
"""Exact finite checks for endpoint-backbite generators and sorting macros."""
from itertools import permutations
from random import Random

def W(st,odd):
 a,b=st
 if odd:return tuple(v for i in range(len(a)) for v in ((1,b[i]),(0,a[i])))+((1,b[-1]),)
 return tuple(v for i in range(len(a)) for v in ((0,a[i]),(1,b[i])))

def conv(w):return (tuple(v for c,v in w if c==0),tuple(v for c,v in w if c==1))

def direct(st,odd):
 w=W(st,odd);o=set()
 for i in range(2,len(w)):
  if w[i][0]!=w[0][0]:o.add(conv(tuple(reversed(w[:i]))+w[i:]))
 for i in range(len(w)-3,-1,-1):
  if w[i][0]!=w[-1][0]:o.add(conv(w[:i+1]+tuple(reversed(w[i+1:]))))
 return o

def move(st,typ,j,odd):
 a,b=st;n=len(a);m=len(b)
 if typ=='P':
  return ((tuple(reversed(a[:j-1]))+a[j-1:],tuple(reversed(b[:j]))+b[j:]) if odd else
    (tuple(reversed(a[:j]))+a[j:],tuple(reversed(b[:j-1]))+b[j-1:]))
 return a[:n-j+1]+tuple(reversed(a[n-j+1:])),b[:m-j]+tuple(reversed(b[m-j:]))

def predicted(st,odd):
 n=len(st[0]);return {move(st,k,j,odd) for k in ('P','S') for j in range(2,n+1)}

def apply(st,seq,odd):
 for t,j in seq:st=move(st,t,j,odd)
 return st

def yswap(n,i,odd):
 if not odd:
  j=n-i+1;return [('S',j),('S',2),('S',j)]
 if i==n:return [('S',2)]
 j=i+1;return [('P',j),('P',2),('P',j)]

def xbase(n):return [('P',3)]+yswap(n,1,True)+yswap(n,2,True)+yswap(n,1,True)

def xswap(n,i,odd):
 if not odd:
  j=i+1;return [('P',j),('P',2),('P',j)]
 if i==1:return xbase(n)
 if i<n-1:
  j=i+2;return [('P',j)]+xbase(n)+[('P',j)]
 return [('S',3)]+yswap(n,n-1,True)+yswap(n,n,True)+yswap(n,n-1,True)

# Enumerate actual vertex-word backbites and compare all predicted moves.
checks=0
for odd in (False,True):
 for n in (2,3,4):
  for a in permutations(range(n)):
   for b in permutations(range(n+int(odd))):
    st=(a,b)
    assert direct(st,odd)==predicted(st,odd),('wrong backbite',n,odd,st)
    checks+=1
print('Exact oriented transition comparisons:',checks)

# Test pure adjacent transpositions for all indices and non-small orders.
checks=0
for odd in (False,True):
 for n in range(3,11):
  ref=(tuple(range(n)),tuple(range(n+int(odd))))
  for i in range(1,n):
   a=list(ref[0]);a[i-1],a[i]=a[i],a[i-1]
   assert apply(ref,xswap(n,i,odd),odd)==(tuple(a),ref[1])
   checks+=1
  for i in range(1,len(ref[1])):
   b=list(ref[1]);b[i-1],b[i]=b[i],b[i-1]
   assert apply(ref,yswap(n,i,odd),odd)==(ref[0],tuple(b))
   checks+=1
print('Pure adjacent swap identity tests:',checks)

# Constructively sort both components, inspecting each step and its cost.
rng=Random(20261004);samples=0
for odd in (False,True):
 for n in range(3,9):
  for rep in range(120):
   a=list(range(n));b=list(range(n+int(odd)))
   rng.shuffle(a);rng.shuffle(b);st=(tuple(a),tuple(b));cost=0
   for side in (0,1):
    for value in range(len(st[side])):
     pos=st[side].index(value)
     while pos>value:
      ops=xswap(n,pos,odd) if side==0 else yswap(n,pos,odd)
      st=apply(st,ops,odd);cost+=len(ops);pos-=1
   assert st==(tuple(range(n)),tuple(range(n+int(odd))))
   assert cost<= (3*n*(n-1) if not odd else (15*n*n-9*n)//2)
   samples+=1
print('Constructive sorting instances:',samples)
print('PASS')
