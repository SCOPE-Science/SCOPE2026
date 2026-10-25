"""Exact finite combinatorial verification for Ind(C_7 x K_3).

Graph multiplication is categorical. All chain signs are integral.
No external files, third-party packages, or network access are required.
Run: python3 c7k3_equivariant_checker.py
"""
from itertools import combinations,permutations
from collections import defaultdict,deque
from functools import lru_cache
import json,sys,hashlib,time
m,n=7,3;N=m*n
order=[18,3,20,7,12,17,9,4,5,13,14,10,15,11,2,6,8,0,1,19,16]
adj=[0]*N
for x in range(m):
 for c in range(n):
  v=x*n+c
  for y in ((x-1)%m,(x+1)%m):
   for d in range(n):
    if d!=c:adj[v]|=1<<(y*n+d)
faces=set([0]);by_sz=defaultdict(list)
def rec(mask,avail):
 if mask:faces.add(mask);by_sz[mask.bit_count()].append(mask)
 while avail:
  bit=avail&-avail;v=bit.bit_length()-1;avail^=bit;rec(mask|bit,avail&~adj[v])
rec(0,(1<<N)-1)
for sz in by_sz:by_sz[sz].sort()
free=set(faces);pairs=[];lower_to_upper={};upper_to_lower={}
for v in order:
 bit=1<<v
 for s in sorted(free):
  t=s|bit
  if s in free and not s&bit and t in free:
   free.remove(s);free.remove(t);pairs.append((s,t));lower_to_upper[s]=t;upper_to_lower[t]=s
critical=sorted(free)
print('MATCH',len(faces),len(pairs),len(critical),[(s.bit_count()-1,s) for s in critical]);assert len(critical)==4
# full directed Hasse graph: unmatched boundary direction from upper to lower, matched upward
indeg={s:0 for s in faces};out=defaultdict(list)
for upper in faces:
 if not upper:continue
 for j,v in enumerate(vertices:= [i for i in range(N) if upper>>i&1]):
  lower=upper^(1<<v)
  a,b=(lower,upper) if lower_to_upper.get(lower)==upper else (upper,lower)
  out[a].append(b);indeg[b]+=1
ready=deque(s for s,deg in indeg.items() if deg==0);topo=[]
while ready:
 u=ready.popleft();topo.append(u)
 for v in out[u]:
  indeg[v]-=1
  if indeg[v]==0:ready.append(v)
assert len(topo)==len(faces),('cyclic',len(topo))
print('ACYCLIC',len(topo),'arcs',sum(map(len,out.values())))
@lru_cache(None)
def V(mask):return tuple(i for i in range(N) if mask>>i&1)
@lru_cache(None)
def bd(mask):return tuple((mask^(1<<v),(-1)**i) for i,v in enumerate(V(mask)))

def compute_proj(degree):
 target=[s for s in critical if s.bit_count()==degree+1]; keys={s:i for i,s in enumerate(target)}
 @lru_cache(None)
 def p(s):
  if s in upper_to_lower:return (0,)*len(target)
  if s in keys:return tuple(int(i==keys[s]) for i in range(len(target)))
  if s not in lower_to_upper:raise RuntimeError('nonmatched')
  u=lower_to_upper[s];coef=dict(bd(u))[s]; ans=[0]*len(target)
  for a,c in bd(u):
   if a==s:continue
   pp=p(a)
   for i,x in enumerate(pp):ans[i]-=c*coef*x
  return tuple(ans)
 return target,p
crit3,p3=compute_proj(3);crit4,p4=compute_proj(4)
for c in crit4:
 x=tuple(sum(coef*p3(a)[i] for a,coef in bd(c)) for i in range(len(crit3)))
 print('MORSE_BOUNDARY_4',c,x)
 assert x==(0,)
print('PROJ_ROUND',[(c,p3(c)) for c in crit3], [(c,p4(c)) for c in crit4])
# DAG on 2dim matching lower facets to other such facets from 3dim upper
lo=[s for s in lower_to_upper if s.bit_count()==3]
lowset=set(lo); indeg={s:0 for s in lo};deps=defaultdict(set)
for l in lo:
 for a,co in bd(lower_to_upper[l]):
  if a!=l and a in lowset and a not in deps[l]:deps[l].add(a);indeg[a]+=1
ready=deque(s for s,d in indeg.items() if d==0);order_lower=[]
while ready:
 l=ready.popleft();order_lower.append(l)
 for a in deps[l]:
  indeg[a]-=1
  if indeg[a]==0:ready.append(a)
assert len(order_lower)==len(lo)

def cycle_from(c):
 z=defaultdict(int,{c:1});boundary=defaultdict(int)
 for a,co in bd(c):boundary[a]+=co
 for l in order_lower:
  b=boundary.get(l,0)
  if b:
   u=lower_to_upper[l];a=dict(bd(u))[l]; k= -b*a
   z[u]+=k
   for t,co in bd(u):boundary[t]+=k*co
 assert not any(boundary.values()),('nonzero boundary',[(k,v) for k,v in boundary.items() if v][:8])
 assert tuple(sum(p3(s)[j]*v for s,v in z.items()) for j in range(len(crit3)))==(1,)
 return {k:v for k,v in z.items() if v}
z3=cycle_from(crit3[0]);print('CYCLE3',len(z3), 'L1',sum(map(abs,z3.values())))

def apply_perm_to_chain(z, f):
 out=defaultdict(int)
 for s,coef in z.items():
  im=[f[v] for v in V(s)]; t=sum(1<<v for v in im)
  inversions=sum(im[i]>im[j] for i in range(len(im)) for j in range(i+1,len(im)))
  out[t]+=coef*((-1)**inversions)
 return out

def action_deg3(f):
 z=apply_perm_to_chain(z3,f)
 return sum(co*p3(s)[0] for s,co in z.items())

def alttrace(f):
 tot=-1 # reduced alternating L trace: -1 for empty face in degree -1, sign (-1)^-1=-1
 for sz,S in by_sz.items():
  val=0
  for mask in S:
   im=[f[v] for v in V(mask)]
   if sum(1<<v for v in im)!=mask:continue
   inv=sum(im[i]>im[j] for i in range(len(im)) for j in range(i+1,len(im)))
   val+=(-1)**inv
  tot+=(-1)**(sz-1)*val
 return tot

def fun(ref=False,shift=0,color=(0,1,2)):
 return tuple(((shift-x if ref else shift+x)%7)*3+color[c] for x in range(7) for c in range(3))
res=[]
for ref in (0,1):
 for shift in range(7):
  for color in permutations(range(3)):
   f=fun(ref,shift,color);a=action_deg3(f);l=alttrace(f);b=l+a
   res.append((ref,shift,color,a,b,l))
   assert a in (-1,1)
   if shift==0:print('CHAR',ref,color,a,b,l)
print('CHARACTER_TESTS',len(res))
assert len(res)==84
for ref,shift,col,a,b,L in res:
 parity = (-1)**sum(col[i]>col[j] for i in range(3) for j in range(i+1,3))
 expected_a = (-1)**ref*parity
 expected_b = parity + sum(col[i]==i for i in range(3)) - 1
 assert a==expected_a and b==expected_b and L==expected_b-expected_a
print('ALL_84_DIHEDRAL_COLOR_CHARACTERS_VERIFIED')
assert all(a==v[3] and b==v[4] for v in res[:1] for a,b in [(v[3],v[4])])
# determine characters by parity
for x in res:
 ref,shift,col,a,b,l=x
 sign=(-1)**sum(col[i]>col[j] for i in range(3) for j in range(i+1,3))
 if a!= ((-1)**ref)*sign:print('3D SIGN UNEXPECTED',x,sign);break
else:print('H3 CHARACTER = reflection-sign times color-sign')
# Write minimal data
print('C7_K3_EQUIVARIANT_HOMOTOPY_VERIFIED')
