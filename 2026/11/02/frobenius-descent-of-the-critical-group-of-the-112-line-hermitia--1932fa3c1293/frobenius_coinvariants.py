#!/usr/bin/env python3
"""Exact Galois coinvariants of graph chip-firing for 112 Fermat-quartic lines in characteristic three."""
import collections,json
from hermitian_lines import enumerator,adjacency,canonical,mul

def frob(a):return mul(a,mul(a,a))
def frpoint(p):return canonical(tuple(frob(c) for c in p))

def local_snf(M,p,E):
 n=len(M);mod=p**E
 B=[[x%mod for x in row] for row in M]
 vals=[]
 def valuation(x):
  if x==0:return E
  z=0
  while x%p==0:x//=p;z+=1
  return z
 for k in range(n-1):
  best=E;spot=None
  for i in range(k,n):
   for j in range(k,n):
    v=valuation(B[i][j])
    if v<best:best=v;spot=(i,j)
    if best==0:break
   if best==0:break
  if spot is None:raise RuntimeError((p,E,k,vals))
  i,j=spot;B[i],B[k]=B[k],B[i]
  for row in B:row[k],row[j]=row[j],row[k]
  a=B[k][k];power=p**best; inv=pow((a//power)%(mod//power),-1,mod//power)
  for i in range(k+1,n):
   if not B[i][k]:continue
   assert B[i][k]%power==0
   factor=(B[i][k]//power*inv)%(mod//power)
   for j in range(k,n):B[i][j]=(B[i][j]-factor*B[k][j])%mod
   assert B[i][k]==0
  for j in range(k+1,n):
   if not B[k][j]:continue
   assert B[k][j]%power==0
   factor=(B[k][j]//power*inv)%(mod//power)
   for i in range(k,n):B[i][j]=(B[i][j]-factor*B[i][k])%mod
   assert B[k][j]==0
  vals.append(best)
 assert all(B[n-1][j]==0 for j in range(n))
 return collections.Counter(vals)

if __name__=='__main__':
 lines=enumerator();A=adjacency(lines);l2i={frozenset(x):i for i,x in enumerate(lines)}
 sigma=[l2i[frozenset(frpoint(p) for p in l)] for l in lines]
 assert all(sigma[sigma[i]]==i for i in range(112))
 orbits=[];seen=set()
 for i in range(112):
  if i in seen:continue
  o=sorted({i,sigma[i]});seen.update(o);orbits.append(o)
 assert len(orbits)==60 and collections.Counter(len(o) for o in orbits)=={1:8,2:52}
 fixed=[o[0] for o in orbits if len(o)==1]
 assert len(fixed)==8 and all(sum(A[i][j] for j in fixed)==4 for i in fixed)
 assert sum(A[i][j] for i in fixed for j in fixed)//2==16
 half1={j for j in fixed if A[fixed[0]][j]}
 half0=set(fixed)-half1
 assert len(half0)==len(half1)==4
 assert all(A[i][j]==(1 if ((i in half0) != (j in half0)) else 0) for i in fixed for j in fixed)
 m=len(orbits)
 B=[[sum((30 if k==orbit[0] else 0)-A[k][orbit[0]] for k in other) for orbit in orbits] for other in orbits]
 assert all(sum(B[i][j] for i in range(m))==0 for j in range(m))
 assert all(sum(B[i][j]*len(orbits[j]) for j in range(m))==0 for i in range(m))
 traceAP=sum(A[i][sigma[i]] for i in range(112))
 trr=(traceAP-30+70)//12
 trs=7-trr
 assert 2*trr-10*trs==traceAP-30
 nr=(90+trr)//2;ns=(21+trs)//2
 assert nr+ns==59
 print('FROBENIUS_LINE_ORBITS 8 fixed, 52 conjugate pairs',flush=True)
 print('FROBENIUS_ADJACENCY_CORRELATION',traceAP,'INVARIANT_EIGEN_MULT',nr,ns,flush=True)
 data={}
 for p,E in [(2,16),(5,8),(7,8)]:
  c=local_snf(B,p,E)
  data[str(p)]={str(i):j for i,j in sorted(c.items())}
  power_expected={2:2*nr+3*ns-4,5:ns,7:nr-1}[p]
  assert sum(i*j for i,j in c.items())==power_expected,(p,c,power_expected)
  print('PADIC_FROB_COINV',p,dict(sorted(c.items())),'v=',power_expected,flush=True)
 n=59;factors=[1]*n
 for pp,c in data.items():
  vals=[]
  for v,cnt in sorted((int(k),v) for k,v in c.items()):vals += [v]*cnt
  assert len(vals)==n
  factors=[a*int(pp)**v for a,v in zip(factors,vals)]
 assert all(factors[i+1]%factors[i]==0 for i in range(n-1))
 fc=sorted(collections.Counter(factors).items())
 print('FROB_COINV_INVARIANT_FACTORS',fc)
 from pathlib import Path
 with (Path(__file__).resolve().parent/'frobenius_certificate.json').open('w') as f:json.dump({'frob_orbits':{'fixed_lines':8,'pairs':52},'trace_AP':traceAP,'invariant_eig':{'28':nr,'40':ns},'local_smith':data,'invariant_factors':fc},f,indent=2)
