from fractions import Fraction as Q
from functools import lru_cache
from math import comb

def harmonic(s):return sum((Q(1,i) for i in range(1,s+1)),Q())
def beta(z,m):
    out=Q(1,z)
    for i in range(1,m+1):out*=Q(i,z+i)
    return out

def closed(u,v,a,b,m):
    n=u+v+m
    x=harmonic(u)-a*(Q(1,u+b)-beta(u+b,m))
    y=harmonic(v)-b*(Q(1,v+a)-beta(v+a,m))
    return n*x,n*y

def independent(u,v,a,b,m,which):
    k=u+v;n=k+m
    flag=(1<<u)-1 if which==1 else ((1<<v)-1)<<u
    support=((1<<a)-1) | (((1<<b)-1)<<u)
    parmask=((1<<m)-1)<<k
    @lru_cache(None)
    def E(S):
        missing=flag&~S
        if not missing:return Q()
        if missing.bit_count()==1 and (missing&support) and (S&parmask):
            other=support&~flag
            if other & ~S==0:return Q()
        unseen=[i for i in range(n) if not (S>>i)&1]
        return (Q(n)+sum((E(S|(1<<i)) for i in unseen),Q()))/len(unseen)
    return E(0)

N=0
for u in range(1,5):
 for v in range(1,5):
  if u+v<3:continue
  for a in range(1,u+1):
   for b in range(1,v+1):
    for m in range(1,4):
     x,y=closed(u,v,a,b,m)
     assert x==independent(u,v,a,b,m,1),(u,v,a,b,m,x,independent(u,v,a,b,m,1))
     assert y==independent(u,v,a,b,m,2)
     assert Q(u,1)/x+Q(v,1)/y<1
     N+=1
print('PASS: exact rational closed form equals independent first-hit subset dynamic programming; strict inequality in',N,'parameter cases')
for u in range(1,12):
 for v in range(1,12):
  if u+v<3:continue
  for a in range(1,u+1):
   for b in range(1,v+1):
    for m in [1,2,3,5,9,20,50]:
     x,y=closed(u,v,a,b,m)
     assert Q(u,1)/x+Q(v,1)/y<1
print('PASS: independent extended exact-rational parameter sweep, all dimensions 1..11 and mixed-column counts 1,2,3,5,9,20,50')
