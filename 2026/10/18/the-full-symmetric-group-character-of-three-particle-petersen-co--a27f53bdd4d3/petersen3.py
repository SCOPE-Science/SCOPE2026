#!/usr/bin/env python3
from itertools import combinations,combinations_with_replacement, permutations
from collections import defaultdict,Counter
from functools import lru_cache
import sys,time,math,json
V=list(combinations(range(5),2));VI={v:i for i,v in enumerate(V)}
E=list(combinations(range(10),2));E=[e for e in E if not(set(V[e[0]])&set(V[e[1]]))];EI={e:i for i,e in enumerate(E)}
assert len(V)==10 and len(E)==15
inc=[[j for j,(a,b) in enumerate(E) if i in (a,b)] for i in range(10)]
assert all(len(t)==3 for t in inc)
GEN=[(v,e) for v in range(10) for e in inc[v][1:]]
BASE=[a[0] for a in inc]
ch={}
for k in range(4):
 gen_lists=[]
 for s in combinations(GEN,k):
  if len({v for v,e in s})==k:gen_lists.append(s)
 mons=list(combinations_with_replacement(range(15),3-k))
 bases=[(s,m) for s in gen_lists for m in mons]
 ch[k]=bases
print('CHAIN_DIMS',{k:len(v) for k,v in ch.items()},flush=True)
indexes={k:{c:i for i,c in enumerate(bases)} for k,bases in ch.items()}

def boundary(k,c):
 if k==0:return []
 gs,mon=c; out={}
 for j,(v,e) in enumerate(gs):
  for edge,coeff in ((e,1),(BASE[v],-1)):
   key=(gs[:j]+gs[j+1:],tuple(sorted(mon+(edge,))))
   ix=indexes[k-1][key];out[ix]=out.get(ix,0)+(-1)**j*coeff
 return [(i,a) for i,a in out.items() if a]

def rank_sparse(k,p):
 bas={}; maxlen=0
 for t,c in enumerate(ch[k]):
  column={i:a%p for i,a in boundary(k,c)}
  while column:
   pivot=max(column)
   if pivot not in bas:
    inv=pow(column[pivot],-1,p)
    bas[pivot]={i:(a*inv)%p for i,a in column.items()}
    maxlen=max(maxlen,len(column));break
   row=bas[pivot]
   factor=column[pivot]
   for i,a in row.items():
    nxt=(column.get(i,0)-factor*a)%p
    if nxt:column[i]=nxt
    elif i in column:del column[i]
  if t%500==0:print('progress',k,p,t,'rank',len(bas),'maxlen',maxlen,flush=True)
 return len(bas)

def permutation_on_edges(pi):
 pV=[VI[tuple(sorted((pi[a],pi[b])))] for a,b in V]
 pE=[EI[tuple(sorted((pV[a],pV[b])))] for a,b in E]
 return pV,pE

def cycles(perm):
 seen=set(); cs=[]
 for i in range(len(perm)):
  if i not in seen:
   v=i;cy=[]
   while v not in seen:seen.add(v);cy.append(v);v=perm[v]
   cs.append(cy)
 return cs

def signed_h1_trace(pv,pe):
 vtrace=sum(a==i for i,a in enumerate(pv))
 etrace=0
 for j,(a,b) in enumerate(E):
  if pe[j]==j:etrace+=1 if (pv[a],pv[b])==(a,b) else -1
 return etrace-vtrace+1

def hom2_trace(pi):
 pV,pE=permutation_on_edges(pi)
 # edge Sym algebra multiset trace = count fixed edge monomials
 edg_cycl=cycles(pE);v_cycl=cycles(pV)
 poly=[1,0,0,0]
 for cy in edg_cycl:
  l=len(cy)
  for deg in range(l,4):poly[deg]+=poly[deg-l]
 for cy in v_cycl:
  l=len(cy)
  if l>3:continue
  v=cy[0]; gl=pi # not used
  # g^l fixes v; count incident graph edges fixed under pE^l.
  count=0
  for e in inc[v]:
   e1=e
   for _ in cy:e1=pE[e1]
   if e1==e:count+=1
  tr=count-1
  for deg in range(3,l-1,-1):poly[deg]-=tr*poly[deg-l]
 h1=signed_h1_trace(pV,pE)
 return poly[3]-1+h1,h1,poly[3]

def part(n,maxpart=None):
 if n==0:yield ();return
 if maxpart is None:maxpart=n
 for a in range(min(n,maxpart),0,-1):
  for t in part(n-a,a):yield (a,)+t

def cells(lam):return {(i,j) for i,r in enumerate(lam) for j in range(r)}
@lru_cache(None)
def char(lam,mu):
 if not mu:return int(not lam)
 l=mu[0]; out=0; C=cells(lam)
 for nu in part(sum(lam)-l):
  N=cells(nu)
  if not N<=C:continue
  R=C-N
  # connected and no 2x2
  if not R:continue
  seen={next(iter(R))};stack=list(seen)
  while stack:
   i,j=stack.pop()
   for a,b in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
    if (a,b) in R and (a,b) not in seen:seen.add((a,b));stack.append((a,b))
  if seen!=R:continue
  if any({(i,j),(i+1,j),(i,j+1),(i+1,j+1)}<=R for i,j in R):continue
  out+=(-1)**(len({i for i,j in R})-1)*char(nu,mu[1:])
 return out

def conjugacy_rep(mu):
 pi=[];offset=0
 for l in mu:
  pi+=list(range(offset+1,offset+l))+[offset];offset+=l
 return pi

def centralizer(mu):
 c=Counter(mu);return math.prod(l**r*math.factorial(r) for l,r in c.items())

def test_char():
 mus=list(part(5));lams=list(part(5))
 traces=[]
 for mu in mus:
  pi=conjugacy_rep(mu);h2,h1,chain=hom2_trace(pi);traces.append(h2)
  print('CLASS',mu,'H2',h2,'H1',h1,'LEF',chain,flush=True)
 print('IRREPS')
 for lam in lams:
  mult=sum(traces[i]*char(lam,mu)/centralizer(mu) for i,mu in enumerate(mus))
  print(lam,'mult',round(mult,7),'char',[char(lam,mu) for mu in mus],flush=True)
 assert all(abs(sum(traces[i]*char(lam,mu)/centralizer(mu) for i,mu in enumerate(mus))-round(sum(traces[i]*char(lam,mu)/centralizer(mu) for i,mu in enumerate(mus))))<1e-7 for lam in lams)

if __name__=='__main__':
 test_char()
 if '--ranks' in sys.argv:
  for k in (1,2,3):
   for p in (3,):
    t=time.time();r=rank_sparse(k,p);print('RANK',k,p,r,'elapsed',round(time.time()-t,3),flush=True)
