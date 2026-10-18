#!/usr/bin/env python3
"""Finite-field incidence-graph refinement and closure checker."""
from collections import Counter
from itertools import product

class Field:
 def __init__(self,p,e=1,poly=None):
  self.p=p; self.e=e; self.q=p**e; self.poly=poly
  assert e==1 or (poly and len(poly)==e+1 and poly[-1]==1)
  self.coeff=[tuple((i//(p**j))%p for j in range(e)) for i in range(self.q)]
  self.index={c:i for i,c in enumerate(self.coeff)}
  self.addtable=[[self.index[tuple((a+b)%p for a,b in zip(self.coeff[i],self.coeff[j]))] for j in range(self.q)] for i in range(self.q)]
  self.multable=[[self._mul(i,j) for j in range(self.q)] for i in range(self.q)]
  self.inv=[None]+[next(j for j in range(1,self.q) if self.multable[i][j]==1) for i in range(1,self.q)]
  assert all(self.multable[i][self.inv[i]]==1 for i in range(1,self.q))
 def _mul(self,i,j):
  if self.e==1: return i*j%self.p
  p=self.p; e=self.e
  c=[0]*(2*e-1)
  for k,a in enumerate(self.coeff[i]):
   for l,b in enumerate(self.coeff[j]): c[k+l]=(c[k+l]+a*b)%p
  for k in range(2*e-2,e-1,-1):
   lead=c[k]
   for l in range(e): c[k-e+l]=(c[k-e+l]-lead*self.poly[l])%p
  return self.index[tuple(c[:e])]
 def add(self,a,b):return self.addtable[a][b]
 def neg(self,a): return self.index[tuple((-v)%self.p for v in self.coeff[a])]
 def sub(self,a,b):return self.addtable[a][self.neg(b)]
 def mul(self,a,b):return self.multable[a][b]
 def div(self,a,b):return self.multable[a][self.inv[b]]
 def norm(self,v):
  h=next((z for z in v if z!=0),None)
  assert h is not None
  return tuple(self.div(z,h) for z in v)
 def cross(self,a,b):
  return self.norm((self.sub(self.mul(a[1],b[2]),self.mul(a[2],b[1])),self.sub(self.mul(a[2],b[0]),self.mul(a[0],b[2])),self.sub(self.mul(a[0],b[1]),self.mul(a[1],b[0]))))
 def dot(self,a,b):
  return self.add(self.add(self.mul(a[0],b[0]),self.mul(a[1],b[1])),self.mul(a[2],b[2]))
 def vectors(self):
  return sorted(set(self.norm(v) for v in product(range(self.q),repeat=3) if any(v)))

def plane(f):
 V=f.vectors(); n=len(V); I={x:i for i,x in enumerate(V)}
 adj=[[] for x in range(2*n)]
 for i,p in enumerate(V):
  for j,l in enumerate(V):
   if f.dot(p,l)==0:
    adj[i].append(n+j);adj[n+j].append(i)
 assert all(len(z)==f.q+1 for z in adj)
 return V,I,adj

def refine(adj,marked):
 n=len(adj)//2
 colors=[0]*n+[1]*n
 for k,i in enumerate(marked): colors[i]=k+2
 history=[]
 while True:
  ct=Counter(colors)
  history.append((len(ct),sum(v==1 for i,v in ct.items() if i not in (0,1)),sum(v==1 for v in ct.values()),len(set(colors[:n]))))
  sig=[(colors[i],tuple(sorted(Counter(colors[j] for j in adj[i]).items()))) for i in range(len(adj))]
  d={s:t for t,s in enumerate(sorted(set(sig)))}
  new=[d[s] for s in sig]
  if len(set(new))==len(set(colors)):
   break
  colors=new
 return colors,history

def closure(f,V,I,marks):
 n=len(V);pts=set(marks);lins=set()
 history=[]
 while True:
  pre=(len(pts),len(lins));history.append(pre)
  L={I[f.cross(V[a],V[b])] for a in pts for b in pts if a<b}
  lins |= L
  P={I[f.cross(V[a],V[b])] for a in lins for b in lins if a<b}
  pts |= P
  if (len(pts),len(lins))==pre:break
 return len(pts),len(lins),history

def cases():
 fields=[(2,1,None),(3,1,None),(5,1,None),(7,1,None),(11,1,None),(2,2,[1,1,1]),(2,3,[1,1,0,1]),(3,2,[1,0,1]),(2,4,[1,1,0,0,1])]
 for p,e,poly in fields:
  f=Field(p,e,poly); q=f.q
  V,I,adj=plane(f)
  O=I[(0,0,1)]; X=I[(1,0,0)];Y=I[(0,1,0)];U=I[(1,1,1)]
  frame=[O,X,Y,U]
  extra=I[f.norm((p,0,1))] if e>1 else None
  marks = [O,X,Y] if q==2 else (frame+[extra] if e>1 else frame)
  for label,M in [('target',marks),('frame',frame)] if e>1 else [('target',marks)]:
   c,h=refine(adj,M)
   cpts,crows,ch=closure(f,V,I,M)
   discreteness=(len(set(c))==len(adj))
   if e>1:
    assert discreteness == (label=='target')
    if label=='target': assert cpts==len(V) and crows==len(V)
   print('q',q,'field',p,e,'case',label,'marks',len(M),'vertices',len(adj),'WL_hist',h,'closure',cpts,crows,'discrete',discreteness,'closure_hist',ch)

if __name__=='__main__':cases()
