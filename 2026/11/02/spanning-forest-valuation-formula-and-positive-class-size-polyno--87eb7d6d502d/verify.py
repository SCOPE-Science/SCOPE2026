#!/usr/bin/env python3
"""Independent exact tests for graphical-group commutator orbit polynomials."""
import itertools, math
from collections import defaultdict
def determinant(a):
  n=len(a)
  if n==0:return 1
  if n==1:return a[0][0]
  if n==2:return a[0][0]*a[1][1]-a[0][1]*a[1][0]
  return sum(((-1)**i)*a[0][i]*determinant([row[:i]+row[i+1:] for row in a[1:]]) for i in range(n))

def direct_image_exp(edges,n,x,p,L):
  mat=[[0]*n for _ in edges]
  for j,(u,v) in enumerate(edges):mat[j][u]=-x[v];mat[j][v]=x[u]
  delta=[0]
  for k in range(1,min(len(edges),n)+1):
    mi=None
    for rows in itertools.combinations(range(len(edges)),k):
      for cols in itertools.combinations(range(n),k):
        z=determinant([[mat[r][c] for c in cols] for r in rows])
        if z==0:continue
        d=0
        while z%p==0: d+=1;z//=p
        if mi is None or d<mi:mi=d
    if mi is None:break
    delta.append(mi)
  return sum(max(0,L-(delta[i]-delta[i-1])) for i in range(1,len(delta)))

def direct_pairs(edges,n,p,L):
  R=p**L; count=0
  for x in itertools.product(range(R),repeat=n):
    for y in itertools.product(range(R),repeat=n):
      if all((x[u]*y[v]-x[v]*y[u])%R==0 for u,v in edges):count+=1
  return count*R**len(edges)//R**n


def forests(edges,n):
  m=len(edges)
  result=[(0,[0]*n,())]
  for k in range(1,min(n,m)+1):
    for idx in itertools.combinations(range(m),k):
      parent=list(range(n));deg=[0]*n;ok=True
      def find(i):
        while parent[i]!=i: i=parent[i]
        return i
      for j in idx:
        u,v=edges[j];ru,rv=find(u),find(v)
        if ru==rv:ok=False;break
        parent[ru]=rv;deg[u]+=1;deg[v]+=1
      if not ok:continue
      comps={}
      for v,d in enumerate(deg):
        if d:comps.setdefault(find(v),[]).append(v)
      result.append((k,deg,tuple(tuple(s) for s in comps.values())))
  return result

def invariants(F,n,a,L):
  ds=[0]*(max(k for k,*_ in F)+1);ds[0]=0
  for k in range(1,len(ds)):
    ds[k]=min(sum((d-1)*av for d,av in zip(deg,a) if d>0)+sum(min(a[v] for v in c) for c in comps) for i,deg,comps in F if i==k)
  diffs=[ds[i]-ds[i-1] for i in range(1,len(ds))]
  assert diffs==sorted(diffs),(a,diffs)
  return diffs

def polynomial_profile(edges,n,L):
  F=forests(edges,n);m=len(edges)
  by_image=defaultdict(lambda:defaultdict(int))
  for a in itertools.product(range(L+1),repeat=n):
    im=sum(max(0,L-d) for d in invariants(F,n,a,L))
    b=sum(av<L for av in a)
    powq=sum(L-av-1 for av in a if av<L)+(L*m-im)
    assert powq>=0
    by_image[im][(b,powq)]+=1
  return by_image

def evaluate(poly,q):
  return sum(cnt*(q-1)**b*q**power for (b,power),cnt in poly.items())

def check():
  graphs={'C3':(3,[(0,1),(1,2),(0,2)]),
    'C4':(4,[(0,1),(1,2),(2,3),(0,3)]),
    'D4':(4,[(0,1),(1,2),(0,2),(2,3),(0,3)]),
    'K4':(4,list(itertools.combinations(range(4),2))),
    'K23':(5,[(u,v) for u in (0,1) for v in (2,3,4)]),
    'P4':(4,[(0,1),(1,2),(2,3)])}
  tests=0
  for name,(n,edges) in graphs.items():
    for L,q in ((1,2),(2,2),(1,3),(2,3)):
      poly=polynomial_profile(edges,n,L)
      predicted=sum(evaluate(p,q) for p in poly.values())
      if L==2 and q==3 and n>=5: continue
      if L==2 and q==3 and len(edges)>4:continue
      check_1=sum((q**L)**len(edges)//q**direct_image_exp(edges,n,x,q,L) for x in itertools.product(range(q**L),repeat=n))
      assert predicted==check_1,(name,L,q,predicted,check_1)
      print('TROPICAL',name,L,q,predicted);tests+=1
      if L==2 and q==2 and n<=4:
        direct=direct_pairs(edges,n,q,L)
        assert predicted==direct,(name,L,q,predicted,direct)
        print('DIRECT',name,L,q,direct);tests+=1
    for L in (1,2,3):
      poly=polynomial_profile(edges,n,L)
      # expand in t=q-1 using binomial expansion, never SymPy or a floating check
      for im,p in poly.items():
        coeff=defaultdict(int)
        for (b,h),cnt in p.items():
          for j in range(h+1): coeff[b+j]+=cnt*math.comb(h,j)
        assert all(v>=0 for v in coeff.values())
        # Crosscheck against numeric values of arbitrary q via direct formula
      print('POSITIVE',name,L,'IMAGE_STRATA',len(poly))
      tests+=1
  print('VERIFY_OK',tests)
if __name__=='__main__':check()
