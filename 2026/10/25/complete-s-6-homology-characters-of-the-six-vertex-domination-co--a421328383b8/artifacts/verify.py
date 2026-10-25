#!/usr/bin/env python3
"""Exact integer verification of rational permutation modules on a finite graph-property complex.

Run with Python 3.10+ and no third-party dependencies.
"""
import itertools, collections
n=6
edges=list(itertools.combinations(range(n),2))
full=(1<<n)-1
F=collections.defaultdict(list)
for mask in range(1<<len(edges)):
 adj=[1<<i for i in range(n)]
 for i,(u,v) in enumerate(edges):
  if mask>>i&1:
   adj[u]|=1<<v; adj[v]|=1<<u
 # If exists a dominating 2-set then not in D6,3
 if any((adj[u]|adj[v])==full for u,v in edges): continue
 if mask:F[mask.bit_count()-1].append(mask)
assert set(F)==set(range(7))

# Exact rank/character certificate for an S_6-simplicial complex.

import math,collections,itertools,json


def exact_kernel(k):
    if k==0:return {'rank':0,'kernel':[],'free':[],'max_coeff':0,'pivots':[]}
    lower={f:i for i,f in enumerate(F[k-1])}
    piv={};orig={};ker=[];free=[];allp=[];maxcoeff=0
    for j,s in enumerate(F[k]):
        v={lower[s^(1<<i)]:(1 if r%2==0 else -1) for r,i in enumerate(x for x in range(15) if s>>x&1)}
        coeff={j:1}
        while v:
            a=min(v);c=v[a]
            if a not in piv:
                if abs(c)!=1: raise ArithmeticError(f'Nonunit pivot at k={k}, j={j}, row={a}, coefficient={c}')
                piv[a]={q:z*c for q,z in v.items()}
                orig[a]={q:z*c for q,z in coeff.items()}
                allp.append(c)
                break
            for q,z in piv[a].items():
                zz=v.get(q,0)-c*z
                if zz:v[q]=zz
                else:v.pop(q,None)
            for q,z in orig[a].items():
                zz=coeff.get(q,0)-c*z
                if zz:coeff[q]=zz
                else:coeff.pop(q,None)
            if v: maxcoeff=max(maxcoeff,max(map(abs,v.values())))
        else:
            ker.append(coeff);free.append(j)
    return {'rank':len(piv),'kernel':ker,'free':free,'max_coeff':maxcoeff,'pivots':collections.Counter(allp)}

ranks={}
for k in range(1,7):
 res=exact_kernel(k)
 ranks[k]=res
 print('exact B',k,'rank',res['rank'],'nullity',len(res['kernel']),'max',res['max_coeff'],'pivots',res['pivots'],flush=True)

# C_0 augmented boundary (one row of 1's) gives rank 1, no H0.
assert ranks[1]['rank']==14
for k in range(1,4):
 assert ranks[k]['rank']+ranks[k+1]['rank']==len(F[k]),(k,ranks[k]['rank'],ranks[k+1]['rank'],len(F[k]))
assert ranks[6]['rank']==len(F[6]);assert len(F[4])-ranks[4]['rank']-ranks[5]['rank']==115
assert len(F[5])-ranks[5]['rank']-ranks[6]['rank']==24
print('exact betti 115 H4, 24 H5; lower zero')

def parts(n,m=None):
 if n==0:yield ()
 else:
  for x in range(min(n,m or n),0,-1):
   for y in parts(n-x,x):yield (x,)+y

def perm(mu):
  g=list(range(6));a=0
  for k in mu:
   for i in range(a,a+k):g[i]=a+(i-a+1)%k
   a+=k
  return g

def action(g,k):
  eg=[edges.index(tuple(sorted((g[i],g[j])))) for i,j in edges]
  inv={f:i for i,f in enumerate(F[k])}
  aa=[]
  for s in F[k]:
   a=[eg[i] for i in range(15) if s>>i&1]
   t=sum(1<<q for q in a)
   inversion=sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
   aa.append((inv[t],(-1)**(inversion%2)))
  return aa

# Verify chain identities and the signed action on two generators.
face_index={k:{face:j for j,face in enumerate(faces)} for k,faces in F.items()}
def signed_boundary(k,s):
    if k==0:return {-1:1}
    return {face_index[k-1][s^(1<<bit)]:(1 if place%2==0 else -1)
            for place,bit in enumerate(x for x in range(15) if s>>x&1)}
for k in range(2,7):
    for simplex in F[k]:
        accumulator=collections.Counter()
        for face_no,c in signed_boundary(k,simplex).items():
            for lower,c2 in signed_boundary(k-1,F[k-1][face_no]).items():
                accumulator[lower]+=c*c2
        assert all(z==0 for z in accumulator.values())
for g in ([1,0,2,3,4,5],[1,2,3,4,5,0]):
    acts={k:action(g,k) for k in F}
    for k in range(1,7):
        for i,simplex in enumerate(F[k]):
            image_index,image_sign=acts[k][i]
            lhs={j:image_sign*c for j,c in signed_boundary(k,F[k][image_index]).items()}
            rhs={}
            for face_no,c in signed_boundary(k,simplex).items():
                j,sgn=acts[k-1][face_no]
                rhs[j]=c*sgn
            assert lhs==rhs

def trace_ker(k,aa):
  res=ranks[k]
  tr=0
  for fr,vec in zip(res['free'],res['kernel']):
   for i,c in vec.items():
    j,sgn=aa[i]
    if j==fr:tr+=sgn*c
  return tr

characters=[]
for mu in parts(6):
    g=perm(mu)
    acts={k:action(g,k) for k in F}
    chie=sum((-1)**k*sum(s for i,(j,s) in enumerate(acts[k]) if i==j) for k in F)-1
    c5=trace_ker(5,acts[5])-sum(s for i,(j,s) in enumerate(acts[6]) if i==j)
    c4=chie+c5
    characters.append({'cycle_type':mu,'H4':c4,'H5':c5,'red_lef':chie})
    print('class',mu,'H4',c4,'H5',c5,'redlef',chie)

# Murnaghan–Nakayama character of symmetric group
from functools import lru_cache
@lru_cache(None)
def mn(lam,mu):
 if not mu:return 1 if not lam else 0
 k=mu[0];n=sum(lam)-k
 if n<0:return 0
 ans=0
 for nu in parts(n):
  if any((nu[i] if i<len(nu) else 0)>lam[i] for i in range(len(lam))):continue
  cells={(i,j) for i,li in enumerate(lam) for j in range(li)}-{(i,j) for i,li in enumerate(nu) for j in range(li)}
  if len(cells)!=k:continue
  if any({(i,j),(i+1,j),(i,j+1),(i+1,j+1)}<=cells for i,j in cells):continue
  seen={next(iter(cells))};stack=list(seen)
  while stack:
   i,j=stack.pop()
   for p in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
    if p in cells and p not in seen:seen.add(p);stack.append(p)
  if len(seen)!=len(cells):continue
  ans+=(-1)**(len({i for i,j in cells})-1)*mn(nu,mu[1:])
 return ans

def class_count(mu):
 c=collections.Counter(mu);z=math.prod(k**v*math.factorial(v) for k,v in c.items())
 return math.factorial(6)//z

allpart=list(parts(6))
for a in allpart:
    for b in allpart:
        inner=sum(class_count(mu)*mn(a,mu)*mn(b,mu) for mu in allpart)
        assert inner==(720 if a==b else 0)

specht={}
for la in parts(6):
 for deg in ['H4','H5']:
  numer=sum(class_count(tuple(z['cycle_type']))*z[deg]*mn(la,tuple(z['cycle_type'])) for z in characters)
  assert numer%720==0,(la,deg,numer)
  mult=numer//720
  assert mult>=0,(la,deg,mult)
  if mult:specht.setdefault(str(la),{})[deg]=mult
print('specht',json.dumps(specht,sort_keys=True))
for deg in ['H4','H5']:
 assert sum(d.get(deg,0)*mn(eval(la),(1,)*6) for la,d in specht.items())==({'H4':115,'H5':24}[deg])

out={'faces':{str(k):len(v) for k,v in F.items()},'rank_exact':{str(k):v['rank'] for k,v in ranks.items()},'max_intermediate_coefficients':{str(k):v['max_coeff'] for k,v in ranks.items()},'characters':characters,'specht_multiplicities':specht,}
print(json.dumps(out,sort_keys=True))
print('D63_S6_CHARACTER_VERIFY_OK')
