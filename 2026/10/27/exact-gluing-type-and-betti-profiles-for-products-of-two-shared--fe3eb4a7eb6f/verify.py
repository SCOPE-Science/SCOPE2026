"""Independent finite checks of product semigroup invariants and the gluing formulas.
Run: python3 verify.py (Python standard library only).
"""
from math import gcd
from heapq import heappop, heappush

def invariants(gens):
    gens=sorted(set(gens)); mod=min(gens)
    ds=[10**80]*mod; ds[0]=0; queue=[(0,0)]
    while queue:
        value,r=heappop(queue)
        if value!=ds[r]: continue
        for gen in gens:
            s=(r+gen)%mod
            if value+gen<ds[s]:
                ds[s]=value+gen;heappush(queue,(ds[s],s))
    assert max(ds)<10**80
    def member(v): return v>=0 and v>=ds[v%mod]
    pf=sorted(w-mod for w in ds if w>=mod and all(member(w-mod+gen) for gen in gens))
    genus=(sum(ds)//mod)-(mod-1)//2 if mod%2 else (2*sum(ds)//mod-(mod-1))//2
    assert 2*sum(ds)%mod==0
    genus=(2*sum(ds)//mod-(mod-1))//2
    return max(ds)-mod,genus,pf,ds

def representable(n,x,y):
    return any(n-i*x>=0 and (n-i*x)%y==0 for i in range(n//x+1))

count=0;two=0;one=0
for m in range(3,24):
 for a in range(1,m):
  if gcd(m,a)!=1: continue
  for b in range(a+1,m):
   if gcd(m,b)!=1:continue
   h=[m,m+a,m+b]; d=(m+a)*(m+b)
   c=[m*m,m*(m+a),m*(m+b),d]
   fh,gh,pfh,_=invariants(h)
   fc,gc,pfc,_=invariants(c)
   assert pfc==[m*v+(m-1)*d for v in pfh]
   assert fc==m*fh+(m-1)*d
   assert 2*gc==2*m*gh+(m-1)*(d-1)
   t=len(pfh); assert t in (1,2)
   dg=gcd(m+a,m+b)
   sym=dg>1 and representable(m,(m+a)//dg,(m+b)//dg)
   assert sym==(t==1)
   defect=2*gc-fc-t
   assert defect==m*(2*gh-fh-t)+(m-1)*(t-1)
   if t==1: assert defect==0;one+=1
   else:assert defect>=m-1;two+=1
   count+=1
endpoint=0
for m in range(3,100):
 h=[m,m+1,2*m-1];f,g,pf,ap=invariants(h)
 q=(2*m-1)//3
 predicted=[min(r*(m+1),(m-r)*(2*m-1)) for r in range(m)]
 assert ap==predicted
 assert (len(pf)==1)==(m%3==2)
 endpoint+=1
print('VERIFY_OK common_generator_products=',count,'symmetric=',one,'nonsymmetric=',two,'endpoint=',endpoint)
