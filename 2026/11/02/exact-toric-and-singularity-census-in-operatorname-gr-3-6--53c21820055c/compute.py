from itertools import permutations,combinations,product
from collections import Counter,defaultdict
from math import comb

def necklaces(n,k):
  out={}
  for p in permutations(range(n)):
    fixed=[j for j in range(n) if p[j]==j]
    ip=[0]*n
    for i,j in enumerate(p):ip[j]=i
    base={j for j in range(n) if ip[j]>j}
    for tags in product((0,1),repeat=len(fixed)):
      I=base | {j for j,b in zip(fixed,tags) if b}
      if len(I)!=k:continue
      Is=[]; X=frozenset(I)
      for a in range(n):
        Is.append(X)
        if a in X:
          X=frozenset((X-{a})|{p[a]})
      assert X==Is[0],(p,Is)
      neck=tuple(Is)
      if neck in out:assert out[neck]==(p,tuple(tags))
      out[neck]=(p,tuple(tags))
  return out

def support(N,n,k):
  cc=list(combinations(range(n),k))
  out=[]
  for B in cc:
    good=True
    for a,I in enumerate(N):
      order=lambda t:(t-a)%n
      x=sorted(map(order,B)); y=sorted(map(order,I))
      if any(u<v for u,v in zip(x,y)):
        good=False;break
    if good:out.append(B)
  return tuple(out)

def binary(B,n,k):
  s=set(B); B0=B[0]
  indices={a:i for i,a in enumerate(B0)}
  A=[[0]*n for _ in range(k)]
  for i,a in enumerate(B0):A[i][a]=1
  for j in range(n):
    if j not in indices:
      for i,a in enumerate(B0):
        C=tuple(sorted((set(B0)-{a})|{j}))
        A[i][j]=int(C in s)
  def det2(C):
    # rank by elimination over F2
    rows=[sum(A[i][j]<<q for q,j in enumerate(C)) for i in range(k)]
    rank=0
    for q in range(k):
      for j in range(rank,k):
        if (rows[j]>>q)&1:
          rows[j],rows[rank]=rows[rank],rows[j];break
      else:continue
      for j in range(k):
        if j!=rank and ((rows[j]>>q)&1):rows[j]^=rows[rank]
      rank+=1
    return rank==k
  return all((C in s)==det2(C) for C in combinations(range(n),k))

def dimension(B,n):
  s=set(B)
  parent=list(range(n))
  def root(i):
    while parent[i]!=i:i=parent[i]
    return i
  def union(i,j):
    parent[root(i)]=root(j)
  for b in B:
    for a in b:
      for c in range(n):
        if c not in b and tuple(sorted((set(b)-{a})|{c})) in s:union(a,c)
  return n-len({root(i) for i in range(n)})


def main(n=6,k=3):
 N=necklaces(n,k)
 print('necklaces',len(N))
 c=Counter(); allc=Counter(); supports={}; duplicates=[]
 for neck,p in N.items():
   B=support(neck,n,k)
   if not B:print('EMPTY',neck);continue
   if B in supports:duplicates.append((neck,supports[B]))
   supports[B]=neck
   good=binary(B,n,k)
   dim=dimension(B,n)
   allc[dim]+=1
   if good:c[dim]+=1
 print('distinct',len(supports),'duplicate',len(duplicates))
 print('all dim',dict(sorted(allc.items())))
 print('toric dim',dict(sorted(c.items())))
 print('total',sum(c.values()), 'nonregular',len(N)-sum(c.values()))
 return N,supports

if __name__=='__main__':main()

def is_smooth_toric(B,n):
  dim=dimension(B,n)
  s=set(B)
  degs=[]
  for b in B:
    deg=sum(tuple(sorted((set(b)-{a})|{c})) in s for a in b for c in range(n) if c not in b)
    degs.append(deg)
  return all(q==dim for q in degs), Counter(degs)


def smooth_run(n=6,k=3):
 N=necklaces(n,k)
 ret=Counter(); witnesses={}
 for neck in N:
   B=support(neck,n,k)
   if binary(B,n,k):
     dim=dimension(B,n)
     sm,degs=is_smooth_toric(B,n)
     ret[(dim,sm)]+=1
     if not sm and dim not in witnesses:witnesses[dim]=(neck,B,degs)
 print('smooth/singular dim',dict(sorted(ret.items())))
 print('smooth total',sum(v for (d,s),v in ret.items() if s))
 print('singular total',sum(v for (d,s),v in ret.items() if not s))
 for d,(_,B,c) in witnesses.items(): print('singular witness dim',d,'bases',B,'vertex degrees',c)
 return ret
if __name__=='__main__':smooth_run()

def forbidden_U24(B,n,k):
 s=set(B)
 if k!=3:return None
 for c in range(n):
   for S in combinations([t for t in range(n) if t!=c],4):
     if all(tuple(sorted((c,a,b))) in s for a,b in combinations(S,2)):
       return True,(c,S)
 return False,None

def independent_checks():
 for n,k in [(5,2),(5,3),(6,2),(6,3)]:
   nn=necklaces(n,k)
   if k==3:
     discrep=[]
     for nt in nn:
       bb=support(nt,n,k)
       if (not binary(bb,n,k))!=forbidden_U24(bb,n,k)[0]:discrep.append(nt)
     print(n,k,'independent U24 check matches',len(nn),'discrepancies',len(discrep))
 for n in (4,5,6):
   tot=sum(len(necklaces(n,k)) for k in range(n+1))
   print('decorated permutations total',n,tot)
if __name__=='__main__':independent_checks()
