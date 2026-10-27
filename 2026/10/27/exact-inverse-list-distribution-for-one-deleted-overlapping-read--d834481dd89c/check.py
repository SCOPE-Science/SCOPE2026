"""Verification of single sliding-window deletion inverse-list laws."""
from itertools import product
from collections import defaultdict,Counter

def runstat(z,s):
    if all(x==z[0] for x in z):return -1
    runs=[];k=0
    for a in z:
        if not runs or a!=runs[-1][0]:runs.append([a,1])
        else:runs[-1][1]+=1
    return sum(v>=s for _,v in runs[1:-1])

def claimed(y,q,ell):
    if any(y[i][1:]!=y[i+1][:-1] for i in range(len(y)-1)):
        return 1 if sum(y[i][1:]!=y[i+1][:-1] for i in range(len(y)-1))==1 and compatible_gap(y,ell) else 0
    z=y[0]+tuple(a[-1] for a in y[1:]);v=runstat(z,ell-1)
    return 2*q-1 if v==-1 else 2*q+v

def compatible_gap(y,ell):
    j=next(i for i in range(len(y)-1) if y[i][1:]!=y[i+1][:-1])
    a,b=y[j],y[j+1]
    return a[2:]==b[:-2]

def inverse(q,ell,n):
    inv=defaultdict(set)
    for x in product(range(q), repeat=n):
        ws=tuple(x[i:i+ell] for i in range(n-ell+1))
        for k in range(len(ws)):
            inv[ws[:k]+ws[k+1:]].add(x)
    return inv

def polynomial(q,s,N):
    # [u^N] q(q-1)u^2/((1-u)(1-qu-(q-1)(t-1)u^s))
    # polynomial truncated power series with integer coeffs represented as arrays.
    poly=[[0]*(N+1) for _ in range(N+1)]
    poly[0][0]=1
    for m in range(1,N+1):
        for k in range(N+1):
            poly[m][k]=poly[m-1][k] * q
            if m>=s:
                poly[m][k]-=(q-1)*poly[m-s][k]
                if k>=1:poly[m][k]+=(q-1)*poly[m-s][k-1]
    # multiply by 1/(1-u) and q(q-1)u^2
    return [q*(q-1)*sum(poly[j][k] for j in range(max(0,N-1))) for k in range(N+1)]

cases=0;parents=0
for q in (2,3):
 for ell in (2,3,4,5):
  for n in range(ell+1,min(10 if q==2 else 8,ell+7)):
   inv=inverse(q,ell,n)
   assert inv
   for y,ps in inv.items():
    c=claimed(y,q,ell)
    assert len(ps)==c,(q,ell,n,y,len(ps),c)
    cases+=1;parents+=len(ps)
   assert max(map(len,inv.values()))==2*q+(n-3)//(ell-1),(q,ell,n)
   obs=Counter()
   for y,ps in inv.items():
    if all(y[i][1:]==y[i+1][:-1] for i in range(len(y)-1)):
     z=y[0]+tuple(a[-1] for a in y[1:]);v=runstat(z,ell-1)
     if v>=0:obs[v]+=1
   expected=polynomial(q,ell-1,n-1)
   assert all(obs.get(k,0)==expected[k] for k in range(len(expected))),(q,ell,n,obs,expected)
   print('PASS',q,ell,n,'observed_max',max(map(len,inv.values())),'received',len(inv),'z_distribution',dict(sorted(obs.items())))
print('VERIFY_OK',cases,'nonempty received configurations;',parents,'total distinct parent incidences')

def expected_inconsistent_singletons(q,ell,n):
    # every input yields one output per maximal run of equal l-mers;
    # consistent output incidence sum is 2 q^n-q plus run-stat sum.
    h=n-ell-2
    S=q*(q-1)**2*sum((j+1)*q**j for j in range(h+1))
    return q**n*(n-ell-1) -(n-ell)*q**(n-ell)+q-S

for q in (2,3):
 for ell in (2,3,4,5):
  for n in range(ell+1,min(10 if q==2 else 8,ell+7)):
   inv=inverse(q,ell,n)
   inc=sum(1 for y,v in inv.items() if any(y[i][1:]!=y[i+1][:-1] for i in range(len(y)-1)))
   e=expected_inconsistent_singletons(q,ell,n)
   assert inc==e,(q,ell,n,inc,e)
print('INCONSISTENT_SINGLETON_COUNTS_OK')
