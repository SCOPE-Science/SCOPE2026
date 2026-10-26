#!/usr/bin/env python3
"""Reproduce point-marker 1-WL thresholds in small projective planes."""
from collections import Counter
from itertools import product

FIELD_POLYS={4:(2,(1,1,1)),8:(2,(1,1,0,1)),9:(3,(1,0,1)),16:(2,(1,1,0,0,1)),25:(5,(2,0,1)),27:(3,(1,2,0,1))}

class Field:
 def __init__(self,q):
  self.q=q
  if q in FIELD_POLYS:
   self.p,self.poly=FIELD_POLYS[q];self.deg=len(self.poly)-1
  else:
   assert q>=2 and all(q%i for i in range(2,int(q**.5)+1))
   self.p=q;self.deg=1;self.poly=(0,1)
  self.a=[self.digits(i) for i in range(q)]
  self.add=[[self.encode([(self.a[i][t]+self.a[j][t])%self.p for t in range(self.deg)]) for j in range(q)] for i in range(q)]
  self.mul=[[self.mult(i,j) for j in range(q)] for i in range(q)]
  self.inv=[None]+[self.power(i,q-2) for i in range(1,q)]
  assert all(self.mul[i][self.inv[i]]==1 for i in range(1,q))
 def digits(self,n):
  z=[]
  for _ in range(self.deg):z.append(n%self.p);n//=self.p
  return z
 def encode(self,a):return sum(x*self.p**i for i,x in enumerate(a))
 def mult(self,i,j):
  if self.deg==1:return i*j%self.p
  d=self.deg; v=[0]*(2*d-1)
  for x in range(d):
   for y in range(d):v[x+y]=(v[x+y]+self.a[i][x]*self.a[j][y])%self.p
  for h in range(2*d-2,d-1,-1):
   v0=v[h]
   for k in range(d):v[h-d+k]=(v[h-d+k]-v0*self.poly[k])%self.p
  return self.encode(v[:d])
 def power(self,x,n):
  ans=1
  while n:
   if n&1:ans=self.mul[ans][x]
   x=self.mul[x][x];n//=2
  return ans
 def norm(self,v):
  if not any(v):return None
  h=next(a for a in v if a!=0);t=self.inv[h]
  return tuple(self.mul[a][t] for a in v)
 def dot(self,p,l):
  z=0
  for a,b in zip(p,l):z=self.add[z][self.mul[a][b]]
  return z

def plane(q):
 F=Field(q)
 # directly canonical list: (1,a,b), (0,1,a), (0,0,1)
 points=[(1,a,b) for a in range(q) for b in range(q)]+[(0,1,b) for b in range(q)]+[(0,0,1)]
 n=len(points);lines=points[:]
 adj=[[] for _ in range(2*n)]
 for i,p in enumerate(points):
  for j,l in enumerate(lines):
   if F.dot(p,l)==0:
    adj[i].append(n+j);adj[n+j].append(i)
 assert all(len(x)==q+1 for x in adj)
 return F,points,adj

def refine(adj,marks):
 n=len(adj)//2; marker_ids={x:i+2 for i,x in enumerate(marks)}
 arr=tuple(marker_ids.get(i,0) if i<n else 1 for i in range(2*n))
 for rounds in range(2*n+1):
  sig=[(arr[i],tuple(sorted(Counter(arr[j] for j in nbr).items()))) for i,nbr in enumerate(adj)]
  code={v:k for k,v in enumerate(sorted(set(sig)))}
  nxt=tuple(code[x] for x in sig)
  if nxt==arr:break
  # old partition always refines so count cannot shrink
  assert len(set(nxt))>=len(set(arr))
  arr=nxt
 else:raise AssertionError('nonconvergence')
 return len(set(arr)), rounds, arr

def main():
 for q in [2,3,4,5,7,8,9,11,13,16,25,27]:
  F,pts,adj=plane(q);n=len(pts)
  std=[pts.index(t) for t in [(1,0,0),(0,1,0),(0,0,1),(1,1,1)]]
  c3,r3,_=refine(adj,std[:3]);c4,r4,_=refine(adj,std)
  if F.deg==1:
   c5=None;r5=None
   assert c4==2*n and (q==2 and c3==2*n or q>2 and c3<2*n)
  else:
   generator=F.p # element represented by x
   fifth=pts.index(F.norm((generator,0,1)))
   c5,r5,_=refine(adj,std+[fifth]);assert c4<2*n and c5==2*n
  print(f'q={q} n={n} marked3={c3}/{2*n} marked4={c4}/{2*n} marked5={c5} rounds=({r3},{r4},{r5})')
 print('VERIFY_OK')
if __name__=='__main__':main()
