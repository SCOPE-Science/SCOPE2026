from itertools import product
from collections import Counter,defaultdict
import sympy as S
from functools import lru_cache
E=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
lookup={a:i for i,a in enumerate(E)}
# polynomial restriction / transforms (all over F2)
def pol_mul(A,B):
 C={}
 for e,c in A.items():
  for f,d in B.items():
   g=tuple(x+y for x,y in zip(e,f));C[g]=C.get(g,0)^(c&d)
 return {e:c for e,c in C.items() if c}
def substit(e,linear):
 out={(0,0,0):1}
 for j,n in enumerate(e):
  for _ in range(n):out=pol_mul(out,{tuple(1 if k==i else 0 for k in range(3)):1 for i in linear[j]})
 return sum(1<<lookup[g] for g,c in out.items() if c)
TR=[]
for linear in [[[1],[0],[2]],[[0],[2],[1]],[[0,1],[1],[2]]]:
 TR.append([substit(e,linear) for e in E])
def act(m,T):
 o=0
 while m:
  t=m&-m;o^=T[t.bit_length()-1];m^=t
 return o
seen=bytearray(1<<15);reps=[]
for k in range(1,1<<15):
 if seen[k]:continue
 Q=[k]; seen[k]=1
 for v in Q:
  for t in TR:
   u=act(v,t)
   if not seen[u]:seen[u]=1;Q.append(u)
 reps.append((k,len(Q)))
print('orbits',len(reps),'sum',sum(c for _,c in reps))
# restriction to 7 lines via 2 independent kernel vectors
def dot(a,b):return ((a&b).bit_count()&1)
lines=[]
for a in range(1,8):
 B=[b for b in range(1,8) if not dot(a,b)]; x=B[0];y=next(v for v in B if v!=x)
 lines.append((a,x,y))
# Evaluate monomial on u*x+v*y with GF2 coeff, return odd coefficients for u^3v and uv^3
L=[]
for a,x,y in lines:
 linear=[]
 for j in range(3):
  linear.append([i for i,w in enumerate((x,y)) if w>>j&1])
 odd=[]
 for e in E:
  v={(0,0):1}
  for j,n in enumerate(e):
   for _ in range(n):
    W={}
    for ex,co in v.items():
     for t in linear[j]:
      g=(ex[0]+(t==0),ex[1]+(t==1));W[g]=W.get(g,0)^co
    v={p:q for p,q in W.items() if q}
  odd.append((v.get((3,1),0),v.get((1,3),0)))
 L.append(tuple(sum((1<<i) for i,v in enumerate(odd) if v[j]) for j in range(2)))
def bc(m):return sum(((m&u).bit_count()%2==0 and (m&v).bit_count()%2==0) for u,v in L)
# smoothness: on affine charts no common solution to F=F_x=F_y=F_z=0 algebraic closure
x,y,z=S.symbols('x y z'); V=[x,y,z];
@lru_cache(None)
def smooth(m):
 P=sum(S.prod(V[j]**n for j,n in enumerate(e)) for i,e in enumerate(E) if m>>i&1)
 D=[S.diff(P,w) for w in V]
 for j,w in enumerate(V):
  W=[v for k,v in enumerate(V) if k!=j]
  ps=[S.Poly(p.subs(w,1),*W,modulus=2).as_expr() for p in [P]+D]
  gb=S.groebner(ps,*W,order='lex',modulus=2)
  if not gb.is_zero_dimensional and not gb.contains(S.Integer(1)):
   return False
  if not gb.contains(S.Integer(1)):return False
 return True
# rational point count
points=[(i&1,(i>>1)&1,(i>>2)&1) for i in range(1,8)]
def np(m):
 return sum(sum((m>>i&1)*S.prod(p[j] if e[j] else 1 for j in range(3)) for i,e in enumerate(E))%2==0 for p in points)
from time import time
t=time(); smoothreps=[]
for k,sz in reps:
 if smooth(k):smoothreps.append((k,sz,bc(k),np(k)))
print('secs',time()-t, 'smooth orbits',len(smoothreps),'forms',sum(sz for _,sz,_,_ in smoothreps))
by=Counter();by_np=Counter()
for k,sz,b,n in smoothreps:by[b]+=sz;by_np[(b,n)]+=sz
print('bitangent dist',sorted(by.items()));print('joint',sorted(by_np.items()))
import csv
with open('all_orbits.csv','w') as f:
 wr=csv.writer(f);wr.writerow(['mask','orbit_size','smooth','bitangents','rational_points'])
 wr.writerows((k,sz,int(smooth(k)),bc(k),np(k)) for k,sz in reps)
with open('smooth_orbits.csv','w') as f:
 wr=csv.writer(f);wr.writerow(['mask','orbit_size','rational_bitangents','rational_points']);wr.writerows(smoothreps)
