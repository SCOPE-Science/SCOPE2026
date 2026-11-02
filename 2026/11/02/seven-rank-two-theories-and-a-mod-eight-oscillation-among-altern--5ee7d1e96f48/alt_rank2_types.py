#!/usr/bin/env python3
"""Generate exact one-pebble extension spectra over A_n from cycle partitions."""
from collections import Counter
from math import lcm

def partitions(n,minv=1):
 if n==0:yield ()
 else:
  for v in range(minv,n+1):
   for tail in partitions(n-v,v):yield (v,)+tail

def has_even_root(ct):
 if any(c%2 for v,c in ct.items() if v%2==0):return False
 return sum(c//2 for v,c in ct.items() if v%2==0)%2==0 or any(c>=2 for v,c in ct.items() if v%2)

def category(partition):
 ct=Counter(partition)
 if sum(c for v,c in ct.items() if v%2==0)%2:return None
 o=lcm(*partition)
 if o==1:return 'E'
 if o==2:return 'I+' if has_even_root(ct) else 'I-'
 if o==3:
  t=ct.get(3,0);f=ct.get(1,0)
  return 'T+' if f>=4 or (t>=2 and f>=2) or t>=4 else 'T-'
 if o==4:return 'F+' if has_even_root(ct) else 'F-'
 return 'X+' if has_even_root(ct) else 'X-'

def cats(n):
 out={}
 for p in partitions(n):
  k=category(p)
  if k is not None:out.setdefault(k,p)
 return out
if __name__=='__main__':
 for n in range(3,41):
  d=cats(n)
  print(f'{n:2d}',','.join(sorted(d)))
