from math import gcd, prod
from itertools import product
from collections import defaultdict

def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def phi(n): return sum(gcd(i,n)==1 for i in range(1,n+1))
def sigma(n): return sum(divisors(n))
def formula(n,d):
 s=0
 for e in divisors(n):
  g=gcd(d,e)
  if g>1:s+=e//g*phi(g)
 return s

def simplified(n,d):
 z=n
 for p in range(2,n+1):
  if d%p==0 and all(p%j for j in range(2,int(p**.5)+1)):
   while z%p==0:z//=p
 return (n//z-1)*sigma(z)

def cosets(n):
 return [frozenset((a+i*d)%n for i in range(n//d)) for d in divisors(n) for a in range(d)]

def qclosure(n,S):
 S=set(S)
 while 1:
  T=S|{(2*y-x)%n for x in S for y in S}
  if T==S:return frozenset(S)
  S=T

def independent(n):
 subs={frozenset():('empty',0)}
 for S in cosets(n): subs[S]=('coset',0)
 group=defaultdict(list)
 for d in divisors(n):
  for a in range(d):group[d].append(frozenset((a+i*d)%n for i in range(n//d)))
 for d in divisors(n):
  base=group[d][0]
  observed=defaultdict(int)
  for V in subs:
   if V and not(base&V) and qclosure(n,base|V)==frozenset(range(n)):
    observed[len(V)]+=1
  expected=defaultdict(int)
  for e in divisors(n):
   g=gcd(d,e)
   if g>1:expected[n//e]+=e//g*phi(g)
  if dict(observed)!=dict(expected):raise AssertionError((n,d,dict(observed),dict(expected)))
  if sum(observed.values())!=formula(n,d) or formula(n,d)!=simplified(n,d):raise AssertionError((n,d))
 if n<=11:
  alls={frozenset(i for i in range(n) if (mask>>i)&1) for mask in range(1,1<<n)}
  actual={S for S in alls if all((2*y-x)%n in S for x in S for y in S)}
  assert actual==set(cosets(n)),(n,len(actual),len(cosets(n)))
 return [(d, formula(n,d)) for d in divisors(n)]

for n in [3,5,7,9,11,15,21,27,35,45]:
 print('cyclic',n,independent(n))

# Independently compare arbitrary abelian-group coset complementation counts with cyclic quotient criterion.
def add(x,y,mods):return tuple((a+b)%m for a,b,m in zip(x,y,mods))
def neg(x,mods):return tuple((-a)%m for a,m in zip(x,mods))
def grp(mods):return list(product(*[range(m) for m in mods]))
def generated(mods, seeds):
 z=tuple(0 for m in mods);out={z}; todo=[z]; seeds=list(seeds)
 while todo:
  a=todo.pop()
  for b in seeds:
   c=add(a,b,mods)
   if c not in out:out.add(c);todo.append(c)
 return frozenset(out)
def subgroups(mods):
 elements=grp(mods); zero=tuple(0 for m in mods); seen={frozenset((zero,))}; todo=list(seen)
 while todo:
  H=todo.pop()
  for x in elements:
   if x in H:continue
   J=generated(mods,list(H)+[x])
   if J not in seen:seen.add(J);todo.append(J)
 return sorted(seen,key=lambda h:(len(h),sorted(h)))
def all_cosets(mods,groups):
 elements=grp(mods);seen={}
 for H in groups:
  for t in elements:
   V=frozenset(add(t,h,mods) for h in H)
   seen[V]=(t,H)
 return seen

def test_abelian(mods):
 E=grp(mods);G=subgroups(mods);cs=all_cosets(mods,G);A=frozenset(E)
 zero=tuple(0 for m in mods)
 print('abelian',mods,'subgroups',len(G),'cosets',len(cs))
 for H in G:
  U=H
  observed=defaultdict(int)
  for V in cs:
   if U & V:continue
   Vg=cs[V][1]; reps=[x for x in V]
   k=generated(mods,list(H)+list(Vg)+[reps[0]])
   if k==A:observed[len(V)]+=1
  expected=defaultdict(int)
  for K in G:
   M=generated(mods,list(H)+list(K))
   s=len(E)//len(M)
   if s==1:continue
   # count elements of quotient that generate it, direct and independent of cyclicity
   generators=sum(generated(mods,list(M)+[t])==A for t in E)
   expected[len(K)]+=generators//len(K)
  assert dict(observed)=={k:v for k,v in expected.items() if v},(mods,H,observed,expected)
 print('abelian OK',mods,'singleton',sum(1 for V in cs if not ({zero}&V) and generated(mods,list(cs[V][1])+[next(iter(V))])==A))
for mods in [(3,3),(3,5),(3,9)]:test_abelian(mods)
print('CHECKER_OK')
