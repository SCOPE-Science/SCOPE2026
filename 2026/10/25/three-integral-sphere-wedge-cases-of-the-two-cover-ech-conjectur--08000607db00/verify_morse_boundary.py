from itertools import combinations
from collections import Counter
from functools import lru_cache
from time import perf_counter
import sys,hashlib
m=int(sys.argv[1]);t=perf_counter(); E=list(combinations(range(m),2))
faces=set()
for i,j in E:
 bs=[1<<k for k,e in enumerate(E) if i in e or j in e];a=[0]
 for b in bs:a+=[v|b for v in a]
 faces.update(a)
faces.discard(0);U=set(faces); low_to_up={};up_to_low={}
for i in range(len(E)):
 b=1<<i
 lo=[x for x in U if not x&b and (x|b) in U]
 for x in lo:
  up=x|b;low_to_up[x]=up;up_to_low[up]=x;U.remove(x);U.remove(up)
critical3=sorted(x for x in U if x.bit_count()==4);critical4=sorted(x for x in U if x.bit_count()==5)
idx={x:i for i,x in enumerate(critical3)}
@lru_cache(None)
def red(x):
 if x in idx:return {idx[x]:1}
 u=low_to_up.get(x)
 if u is None:return {}
 b=u^x
 pos=(u&(b-1)).bit_count(); ep=(-1)**pos
 ans={}
 tmp=u
 while tmp:
  b2=tmp&-tmp;tmp-=b2;y=u^b2
  if y==x:continue
  yp=(u&(b2-1)).bit_count()
  fac=-((-1)**yp)*ep
  for j,val in red(y).items():ans[j]=ans.get(j,0)+fac*val
 return {k:v for k,v in ans.items() if v}
rows=[]
for upper in critical4:
 coeff={};tmp=upper
 while tmp:
  b=tmp&-tmp;tmp-=b; y=upper^b
  ep=(-1)**((upper&(b-1)).bit_count())
  for j,v in red(y).items(): coeff[j]=coeff.get(j,0)+ep*v
 rows.append({k:v for k,v in coeff.items() if v})
print('m',m,'critical',len(critical3),len(critical4),'nonzero cols',sum(bool(x) for x in rows),'nonzero entries',sum(map(len,rows)),'largest coefficient',max((abs(v) for x in rows for v in x.values()),default=0),'memo',red.cache_info(),'seconds',round(perf_counter()-t,3),flush=True)
for i,rr in enumerate(rows):
 if rr:print(i,rr)
