#!/usr/bin/env python3
"""Exact rational finite-state verification of weak-selection game thresholds.
Public-goods game details and source: https://arxiv.org/abs/2604.07228
Uses only Python standard library. No simulation or external data required.
"""
from fractions import Fraction as Q
from itertools import combinations

N=6
PAIRS=tuple(tuple(sorted((i,(i+1)%N))) for i in range(N))
REP={
 'adjacent': ((0,1,2),(3,4,5)),
 'interlaced': ((0,1,3),(2,4,5)),
 'alternating': ((0,2,4),(1,3,5)),
}
EXPECTED={
 'adjacent': ('-5/4','226939309381/975051893376','4181/31104','10860709/376177428','2514358699/121881486672'),
 'interlaced': ('-5/4','1928892220173728284145/7878141219193012523808','16961/133344','20517216197359753/708975991648039284','3862525997180182316/246191913099781641369'),
 'alternating': ('-5/4','23209/92016','89/720','643/23004','1481/115020'),
}

def normalize_partition(p):
 return tuple(sorted(tuple(sorted(e)) for e in p))

def dihedral():
 return [tuple((d*i+a)%N for i in range(N)) for a in range(N) for d in (1,-1)]

def maps_preserving(triples):
 base=normalize_partition(triples)
 return [g for g in dihedral() if normalize_partition(tuple(tuple(g[i] for i in e) for e in triples))==base]

def image(s,g):
 t=0
 for i in range(N):
  if s&(1<<i):t|=1<<g[i]
 return t

def orbits(triples):
 maps=maps_preserving(triples)
 states=set(range(1, (1<<N)-1))
 blocks=[]
 while states:
  s=min(states)
  block=set(image(s,g) for g in maps)
  assert block <= states
  states-=block
  blocks.append(sorted(block))
 return blocks

def gaussian(A,b):
 n=len(b); a=[row[:]+[b[i]] for i,row in enumerate(A)]
 for col in range(n):
  pivot=next((i for i in range(col,n) if a[i][col]!=0),None)
  assert pivot is not None,'singular transient matrix'
  a[col],a[pivot]=a[pivot],a[col]
  v=a[col][col]
  for j in range(col,n+1):a[col][j]/=v
  for i in range(col+1,n):
   z=a[i][col]
   if z:
    for j in range(col+1,n+1):a[i][j]-=z*a[col][j]
    a[i][col]=Q(0)
 x=[Q(0) for i in range(n)]
 for i in range(n-1,-1,-1):
  x[i]=a[i][n]-sum((a[i][j]*x[j] for j in range(i+1,n)),Q(0))
 return x

def compute(triples):
 triples=normalize_partition(triples)
 groups=PAIRS+triples
 W=[[Q(0) for m in range(N)] for f in range(N)]
 for e in groups:
  for f in e:
   for m in e:
    if f!=m:W[f][m]+=Q(1,3*(len(e)-1))
 assert all(sum(w)==1 for w in W)
 assert all(W[f][m]==W[m][f] for f in range(N) for m in range(N))
 blocks=orbits(triples); reps=[b[0] for b in blocks]; idx={s:j for j,b in enumerate(blocks) for s in b}
 q=len(blocks)
 A=[[Q(0) for j in range(q)] for i in range(q)]
 B=[[Q(0) for t in range(5)] for i in range(q)]
 for i,s in enumerate(reps):
  pay=[[Q(0) for t in range(5)] for f in range(N)]
  # Coefficients are [cost, b, b*d2, b*d3, b*d3^2], with cost c.
  for e in groups:
   n=sum(bool(s & (1<<f)) for f in e)
   benefit=[Q(0)]*5
   if n>=1:benefit[1]=Q(1,len(e))
   if n>=2:benefit[2 if len(e)==2 else 3]=Q(1,len(e))
   if n>=3:benefit[4]=Q(1,len(e))
   for f in e:
    if s & (1<<f):pay[f][0]-=1
    for t in range(1,5):pay[f][t]+=benefit[t]
  for f in range(N):
   for m in range(N):
    if ((s>>f)&1)==((s>>m)&1):continue
    base=W[f][m]
    if not base:continue
    news=s^(1<<f)
    A[i][i]+=base/(2*N)
    if 0<news<(1<<N)-1:A[i][idx[news]]-=base/(2*N)
    direction=((s>>m)&1)-((s>>f)&1)
    for t in range(5):
     B[i][t]+=base*direction*(pay[m][t]-pay[f][t])/(4*N*N)
 v=[Q(sum((s & (s-1))==0 for s in block),N) for block in blocks]
 # left Green potential: y^T = v^T A^{-1}
 y=gaussian([[A[j][i] for j in range(q)] for i in range(q)],v)
 coef=[sum((y[i]*B[i][t] for i in range(q)),Q(0)) for t in range(5)]
 # Independently check adjoint residual exactly.
 assert [sum((A[j][i]*y[j] for j in range(q)),Q(0)) for i in range(q)]==v
 return coef,q

def main():
 allparts={normalize_partition((x,tuple(sorted(set(range(N))-set(x))))) for x in combinations(range(N),3)}
 assert len(allparts)==10
 classes={normalize_partition((tuple(g[i] for i in e) for e in p)):name
    for name,p in REP.items() for g in dihedral()}
 assert len(classes)==10 and set(classes)==allparts
 for name,p in REP.items():
  coef,q=compute(p)
  assert tuple(map(str,coef))==EXPECTED[name],(name,coef)
  B=coef[1]+coef[2]*Q(1,2)+coef[3]*3+coef[4]*9
  derivative=Q(23,10)*B+coef[0]
  assert (derivative>0)==(name=='adjacent')
  print(name,'orbits',q,'threshold',Q(5,4)/B,'derivative',derivative)
 print('PASS: 10 partitions, 3 dihedral classes, 62-state exact weak-selection equations, coefficients, sign reversal')
if __name__=='__main__':main()
