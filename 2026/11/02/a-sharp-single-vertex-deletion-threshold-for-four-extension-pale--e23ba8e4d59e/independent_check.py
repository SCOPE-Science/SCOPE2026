#!/usr/bin/env python3
"""Independent direct-histogram spot verification of critical finite fields.

Uses quadratic-character powering, not square-set membership or bitset intersections.
The main full census is in verify_paley.py.
"""
import json

POLYS={81:(2,1,0,0,1),121:(1,0,1),125:(1,1,0,1),169:(2,0,1)}
PRIMES={81:3,121:11,125:5,169:13}
TESTS={81:0,89:2,97:2,121:2,125:1,137:3,169:4,181:2,233:6}

def field(q):
 p=PRIMES.get(q,q)
 if p==q:
  return lambda a,b:(a-b)%p, lambda a,b:(a*b)%p
 f=POLYS[q];e=len(f)-1
 def d(a):
  z=[]
  for _ in range(e):z.append(a%p);a//=p
  return z
 def enc(v):
  w=0
  for c in reversed(v):w=w*p+c%p
  return w
 def sub(a,b):
  a,b=d(a),d(b)
  return enc([(a[i]-b[i])%p for i in range(e)])
 def mul(a,b):
  a,b=d(a),d(b)
  z=[0]*(2*e-1)
  for i in range(e):
   for j in range(e):z[i+j]+=a[i]*b[j]
  for i in range(len(z)-1,e-1,-1):
   t=z[i]%p
   for j in range(e):z[i-e+j]-=t*f[j]
  return enc(z[:e])
 return sub,mul

def char_by_power(q,mul):
 def exp(a,r):
  ans=1
  while r:
   if r&1:ans=mul(ans,a)
   a=mul(a,a);r>>=1
  return ans
 neg1= q-1 if q not in POLYS else PRIMES[q]-1
 assert exp(2,q-1)==1
 chars=[0]*q
 for t in range(1,q):
  s=exp(t,(q-1)//2)
  assert s in (1,neg1),(q,t,s)
  chars[t]= 1 if s==1 else -1
 assert chars.count(1)==chars.count(-1)==(q-1)//2
 return chars

def minimum(q):
 sub,mul=field(q)
 chi=char_by_power(q,mul)
 relation=[[int(chi[sub(x,y)]==1) for y in range(q)] for x in range(q)]
 minimum=q;witness=None
 for a in range(2,q):
  for b in range(a+1,q):
   S={0,1,a,b};counts=[0]*16
   for x in range(q):
    if x in S:continue
    r=relation[x]
    code=r[0]+2*r[1]+4*r[a]+8*r[b]
    counts[code]+=1
   val=min(counts)
   if val<minimum:
    minimum=val;witness=(0,1,a,b,counts.index(val))
 return minimum,witness

def main():
 for q,expected in TESTS.items():
  observed,witness=minimum(q)
  assert observed==expected,(q,observed,expected)
  print(json.dumps({'q':q,'direct_min':observed,'minimizer':witness},sort_keys=True))
 print('INDEPENDENT_CHECK_OK')
if __name__=='__main__':main()
