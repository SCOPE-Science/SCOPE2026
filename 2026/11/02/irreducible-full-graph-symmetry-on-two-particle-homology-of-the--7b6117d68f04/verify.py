#!/usr/bin/env python3
"""Exact cellular and character verification for the unordered two-point space of K4,4."""
import itertools
from collections import Counter

N=4
V=range(2*N)
E=[(i,N+j) for i in range(N) for j in range(N)]
C0=list(itertools.combinations(V,2)); I0={x:i for i,x in enumerate(C0)}
C1=[(v,e) for v in V for e in E if v not in e]; I1={x:i for i,x in enumerate(C1)}
C2=[(e,f) for i,e in enumerate(E) for f in E[i+1:] if set(e).isdisjoint(f)]; I2={x:i for i,x in enumerate(C2)}
assert (len(C0),len(C1),len(C2))==(28,96,72)
B1=[{} for _ in C1]
for j,(v,(a,b)) in enumerate(C1):
 B1[j]={I0[tuple(sorted((v,b)))]:1,I0[tuple(sorted((v,a)))]:-1}
B2=[{} for _ in C2]
for j,(e,f) in enumerate(C2):
 a,b=e;c,d=f
 for key,coeff in [((b,f),1),((a,f),-1),((d,e),-1),((c,e),1)]:
  i=I1[key];B2[j][i]=B2[j].get(i,0)+coeff
 z={}
 for i,b in B2[j].items():
  for k,v in B1[i].items():z[k]=z.get(k,0)+b*v
 assert not any(z.values())

def rank_mod(columns,prime):
 piv={}
 for col in columns:
  v={k:a%prime for k,a in col.items() if a%prime}
  while v:
   i=min(v)
   if i not in piv:
    t=pow(v[i],-1,prime);piv[i]={j:(a*t)%prime for j,a in v.items() if (a*t)%prime};break
   a=v[i];row=piv[i]
   for j,t in row.items():
    vv=(v.get(j,0)-a*t)%prime
    if vv:v[j]=vv
    else:v.pop(j,None)
 return len(piv)

# Explicit integral top cycles: disjoint four-cycles on complementary 2+2 vertex sets.
def square(As,Bs):
 a,b=sorted(As);c,d=sorted(Bs)
 return {(a,N+c):1,(b,N+c):-1,(b,N+d):1,(a,N+d):-1}
SQUARE=[]
for AA in itertools.combinations(range(4),2):
 for BB in itertools.combinations(range(4),2):SQUARE.append((set(AA),set(BB),square(AA,BB)))
T=[]
for i,(A,B,x) in enumerate(SQUARE):
 for j,(C,D,y) in enumerate(SQUARE):
  if i>=j or A&C or B&D:continue
  vec={}
  for e,u in x.items():
   for f,v in y.items():
    if (e,f) in I2:key=(e,f);s=1
    else:key=(f,e);s=-1
    ix=I2[key];vec[ix]=vec.get(ix,0)+s*u*v
  assert len(vec)==16
  z={}
  for jj,v in vec.items():
   for ii,c in B2[jj].items():z[ii]=z.get(ii,0)+v*c
  assert all(c==0 for c in z.values())
  T.append(vec)
assert len(T)==18,(len(T))
assert rank_mod(B1,1009)==27
assert rank_mod(B2,1009)==60
assert rank_mod(T,1009)==12
# The 12 independent integral 2-cycles provide a 12-dimensional rational kernel,
# and the mod-1009 rank 60 provides an opposite bound on the rational kernel dimension.
# Hence rank(B2)=60 over Q; exact unimodularity/torsion beyond H2 is not asserted.

P=list(itertools.permutations(range(4)))
def ctype(p):
 seen=set();out=[]
 for i in range(4):
  if i in seen:continue
  j=i;k=0
  while j not in seen:seen.add(j);k+=1;j=p[j]
  out.append(k)
 return tuple(sorted(out))
# irreducible S4 characters indexed by partitions
chi211={(1,1,1,1):3,(1,1,2):-1,(1,3):0,(2,2):-1,(4,):1}
chi22={(1,1,1,1):2,(1,1,2):0,(1,3):-1,(2,2):2,(4,):0}
chi31={(1,1,1,1):3,(1,1,2):1,(1,3):0,(2,2):-1,(4,):-1}
counts=Counter();counts_swap=Counter(); diag=Counter()
def gtrace(vmap):
 sg=1 if vmap[0]<4 else -1
 vm=lambda v:vmap[v]
 em=lambda e:tuple(sorted((vm(e[0]),vm(e[1]))))
 c0=sum({vm(a),vm(b)}=={a,b} for a,b in C0)
 c1=sg*sum(vm(v)==v and em(e)==e for v,e in C1)
 c2=0
 for e,f in C2:
  ee,ff=em(e),em(f)
  if ee==e and ff==f:c2+=1
  elif ee==f and ff==e:c2-=1
 ce=sg*sum(em(e)==e for e in E)
 cv=sum(vm(v)==v for v in V)
 return c0-c1+c2+ce-cv
for swap in (0,1):
 for p in P:
  for q in P:
   vmap=tuple(p[i] if not swap else 4+q[i] for i in range(4))+tuple(4+q[i] if not swap else p[i] for i in range(4))
   observed=gtrace(vmap)
   expected=0 if swap else chi211[ctype(p)]*chi22[ctype(q)]+chi22[ctype(p)]*chi211[ctype(q)]
   assert observed==expected,(swap,p,q,observed,expected)
   counts[observed]+=1
   if swap:counts_swap[observed]+=1
   if not swap and p==q:diag[ctype(p)]=observed
assert sum(counts.values())==1152
assert counts_swap=={0:576}
assert sum(k*v for k,v in counts.items())==0
assert diag=={t:2*chi211[t]+2*chi31[t] for t in diag}
# Orthogonality over S4xS4: only two distinct irreducibles occur.
print('K44_UNORDERED_TWO_POINT_12_IRRED_WREATH_CERTIFIED', 'C', (28,96,72), 'rank',(27,60),'torus_cycles',len(T),'independent',12,'group',sum(counts.values()),'traces',sorted(counts.items()))
