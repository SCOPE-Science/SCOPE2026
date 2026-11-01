import itertools, collections, time, sys
import numpy as np
V=range(6); E=[(i,j) for i in V for j in range(i+1,6) if i//2!=j//2]
eidx={e:k for k,e in enumerate(E)}
incident={v:[eidx[e] for e in E if v in e] for v in V}
mons={n:list(itertools.combinations_with_replacement(range(len(E)),n)) for n in range(4)}
bases={k:[(tuple(vv),tuple(m)) for vv in itertools.combinations([(v,h) for v in V for h in incident[v][1:]],k) if len({v for v,h in vv})==k for m in mons[3-k]] for k in range(4)}
# canonical sort by vertex, choices; explicit combos inherently lexicographic
idx={k:{c:i for i,c in enumerate(bases[k])} for k in range(4)}
print('E',E,'sizes',{k:len(a) for k,a in bases.items()},flush=True)
def col_boundary(k):
 out=[]
 for (vv,mm) in bases[k]:
  cc=collections.defaultdict(int)
  for i,(v,h) in enumerate(vv):
   for ed,s in [(h,1),(incident[v][0],-1)]:
    x=idx[k-1][(vv[:i]+vv[i+1:], tuple(sorted(mm+(ed,))))]
    cc[x]+=(-1)**i*s
  out.append({a:b for a,b in cc.items() if b})
 return out
BC={k:col_boundary(k) for k in (1,2,3)}
print('nonzeros',{k:sum(len(c) for c in b) for k,b in BC.items()},flush=True)
for k in (2,3):
 for col in BC[k]:
  d=collections.defaultdict(int)
  for j,c in col.items():
   for i,cc in BC[k-1][j].items():d[i]+=c*cc
  assert not any(d.values())
print('d2=0',flush=True)

def rank_gf(cols,p=32003):
 piv={}; ops=0
 for t,col in enumerate(cols):
  d={i:c%p for i,c in col.items() if c%p}
  while d:
   i=min(d)
   if i not in piv:
    inv=pow(d[i],-1,p)
    piv[i]={a:(c*inv)%p for a,c in d.items() if c%p};break
   coeff=d[i]
   for a,c in piv[i].items():
    v=(d.get(a,0)-coeff*c)%p
    if v:d[a]=v
    elif a in d:del d[a]
   ops+=1
  if t%500==499:print('GF',len(cols),t+1,'rank',len(piv),'ops',ops,'time',round(time.monotonic()-START,2),flush=True)
 return len(piv),piv
START=time.monotonic()
for k in (1,2,3):
 print('rank',k,rank_gf(BC[k])[0],flush=True)
print('sec',time.monotonic()-START)
