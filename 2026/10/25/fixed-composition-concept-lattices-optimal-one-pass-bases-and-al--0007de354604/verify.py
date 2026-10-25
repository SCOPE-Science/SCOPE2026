from itertools import product,combinations
from math import factorial,comb
from functools import lru_cache

# Independent finite tests for the stated fixed-composition closure formulas.

def calc(m):
 n=sum(m);q=len(m);E=(1<<(n*q))-1
 # actual models
 mods=[]
 for f in product(range(q),repeat=n):
  if all(f.count(a)==m[a] for a in range(q)):
   mods.append(sum(1<<(i*q+f[i]) for i in range(n)))
 assert len(mods)==factorial(n)//__import__('math').prod(factorial(x) for x in m)
 @lru_cache(None)
 def c(S):
  C=[w for w in mods if (w&S)==S]
  if not C: return E
  x=E
  for w in C:x&=w
  return x
 
 stems=[]
 for i in range(n):
  for a in range(q):
   for b in range(a+1,q):stems.append((1<<(i*q+a))|(1<<(i*q+b)))
 for a in range(q):
  for I in combinations(range(n),m[a]+1):stems.append(sum(1<<(i*q+a) for i in I))
 for a in range(q):
  pos=range(n)
  for f in product(range(q),repeat=n):
   if all(f.count(b)==m[b] for b in range(q)):
    stems.append(sum(1<<(i*q+f[i]) for i in pos if f[i]!=a))
 stems=set(stems)
 b=n*comb(q,2)+sum(comb(n, m[a]+1) for a in range(q))+q*len(mods)
 assert len(stems)==b,(m,len(stems),b)
 assert all(c(S)!=S and all(c(S^(1<<j))==S^(1<<j) for j in range(n*q) if S>>j&1) for S in stems)
 cl=[]; non=[]
 for S in range(E+1):
  full=c(S)
  minimal_bad = full != S and all(c(S^(1<<j))==S^(1<<j) for j in range(n*q) if S>>j&1)
  assert minimal_bad == (S in stems), (m,S,minimal_bad)
  if full==S:cl.append(S)
  else:non.append(S)
  v=S
  for s in stems:
   if s&S==s:v|=c(s)
  assert v==full,(m,S,full,v)
 
 T=len(mods)
 feasible=sum(factorial(n)//(factorial(n-sum(x))*__import__('math').prod(factorial(t) for t in x)) for x in product(*(range(v+1) for v in m)))
 total=1+feasible-T*sum(2**v-1 for v in m)
 assert len(cl)==total,(m,len(cl),total)
 # compute Möbius of all closed intervals using inverse bottom-to-top for each source
 cs=sorted(cl,key=lambda z:z.bit_count())
 def r_counts(S):
  return [m[a]-sum((S>>(i*q+a))&1 for i in range(n)) for a in range(q)]
 def F(r):
  mm=sum(r)
  return sum((-1)**sum(t)*factorial(mm)//(factorial(mm-sum(t))*__import__('math').prod(factorial(z) for z in t)) for t in product(*(range(x+1) for x in r)))
 intervals=0
 for source in cs:
  if source==E:continue
  sups=[v for v in cs if v&source==source]
  mus={source:1}
  for dest in sups[1:]:
   mus[dest]=-sum(x for v,x in mus.items() if v&dest==v)
   if dest==E:expected=-F(r_counts(source))
   elif dest in mods: expected=(-1)**(dest.bit_count()-source.bit_count())*(1-sum(z>0 for z in r_counts(source)))
   else:expected=(-1)**(dest.bit_count()-source.bit_count())
   assert mus[dest]==expected,(m,source,dest,mus[dest],expected)
   intervals+=1
 return (m,len(mods),len(stems),len(cl),intervals,F(m))

for m in [(1,1,1),(2,1,1),(1,1,1,1),(3,1,1),(2,2,1)]:
 print('EXHAUSTIVE_OK',calc(m),flush=True)
print('VERIFY_OK closure=PASS minimal_premises=PASS direct_basis=PASS interval_mobius=PASS')
