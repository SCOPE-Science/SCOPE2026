#!/usr/bin/env python3
"""Independent finite-table tests for morphisms/idempotents of Gödel-chain EARS powers.
Stdlib only; all mathematical definitions are included here.
"""
from itertools import product,combinations
from math import comb, factorial

assertions=0
scalar_trials=0
product_trials=0

def check(b,info=None):
 global assertions
 assertions+=1
 if not b: raise AssertionError((assertions,info))

def equ(a,b,n): return n-1 if a==b else min(a,b)
def reg(a,b,n): return n-1 if a>0 and b>0 else 0

def scalars(m,n):
 out=[tuple([n-1]*m)]
 for k in range(min(m-2,n-2)+1):
  for target in combinations(range(1,n-1),k):
   out.append((0,*target,*([n-1]*(m-1-k))))
 check(len(out)==len(set(out)))
 return out

def hom_scalar(f,m,n):
 return all(f[equ(a,b,m)]==equ(f[a],f[b],n) and f[reg(a,b,m)]==reg(f[a],f[b],n) for a,b in product(range(m),repeat=2))

for m,n in product(range(2,7),repeat=2):
 true=set()
 for rest in product(range(n),repeat=m-1):
  f=(*rest,n-1)
  scalar_trials+=1
  if hom_scalar(f,m,n):true.add(f)
 claim=set(scalars(m,n))
 check(true==claim,(m,n,'scalar classification'))
 check(len(true)==1+sum(comb(n-2,k) for k in range(min(m-2,n-2)+1)))

def powhom_choices(ms,n):
 # Each entry is the total map as a precomputed table of values on all source tuples.
 dom=list(product(*(range(m) for m in ms)))
 candidates=[tuple([n-1]*len(dom))]
 for i,m in enumerate(ms):
  for f in scalars(m,n):
   if f[0]==n-1:continue
   candidates.append(tuple(f[x[i]] for x in dom))
 check(len(set(candidates))==len(candidates))
 return dom,candidates

def product_morph_test(ms,n,exhaust=False):
 global product_trials
 dom,candidates=powhom_choices(ms,n)
 idx={x:k for k,x in enumerate(dom)}
 q=len(dom)
 equivtable=[[idx[tuple(equ(x[i],y[i],ms[i]) for i in range(len(ms)))] for y in dom] for x in dom]
 regtable=[[idx[tuple(reg(x[i],y[i],ms[i]) for i in range(len(ms)))] for y in dom] for x in dom]
 def ishom(f):
  for i in range(q):
   for j in range(q):
    if f[equivtable[i][j]] !=equ(f[i],f[j],n) or f[regtable[i][j]] != reg(f[i],f[j],n):return False
  return True
 for f in candidates:
  check(ishom(f),(ms,n,'predicted map failed'))
 if exhaust:
  real=set()
  top=idx[tuple(m-1 for m in ms)]
  for partial in product(range(n),repeat=q-1):
   t=(*partial,n-1)
   # input tuple product order puts top last.
   product_trials+=1
   if ishom(t):real.add(t)
  check(real==set(candidates),(ms,n,'full exhaustive'))
 return q,len(candidates)

for ms,n in [((2,2),2),((2,3),2),((2,3),3),((3,3),3),((3,3),4)]:
 q,c=product_morph_test(ms,n,exhaust=True)
 print(f'EXHAUSTIVE source={ms}, target={n}, |source|={q}, homs={c}')

# Operation-level validation of all nontrivial small algebra maps, including 3->3 powers.
for ms,n in [((3,3,3),3),((4,4),4),((3,4),5),((2,3,4),4)]:
 q,c=product_morph_test(ms,n)
 print(f'CONSTRUCTED source={ms}, target={n}, |source|={q}, homs={c}')

# All endomorphism tuples and exact idempotent counts and automorphisms.
for m in range(2,7):
 p=m-2
 options=[None]+[(i,f) for i in range(3) for f in ()] # overwritten per rank
 for r in range(1,5):
  if r>=4 and m>3:continue
  hs=[f for f in scalars(m,m) if f[0]==0]
  opts=[None]+[(src,f) for src in range(r) for f in hs]
  observed=0
  invertible=0
  for outs in product(opts,repeat=r):
   # symbolic composition f_j(f_source(x))
   idem=True
   for j,o in enumerate(outs):
    if o is None: continue
    i,f=o
    if outs[i] is None:idem=False;break
    t,g=outs[i]
    if t!=i or tuple(f[g[x]] for x in range(m)) != f:idem=False;break
   if idem:observed+=1
   if all(o is not None for o in outs):
    srcs=[o[0] for o in outs]
    if len(set(srcs))==r and all(o[1]==tuple(range(m)) for o in outs):invertible+=1
  weighted=[sum(comb(p,k) for k in range(a+1)) for a in range(p+1)]
  predicted=sum(comb(r,t)*sum((1+sum(vals))**(r-t) for vals in product(weighted,repeat=t)) for t in range(r+1))
  check(observed==predicted,(m,r,observed,predicted))
  check(invertible==factorial(r),(m,r,invertible))
  check(len(opts)**r == (1+r*2**p)**r)
  print(f'IDEMPOTENTS m={m},rank={r}: {observed}/{len(opts)**r}, automorphisms={invertible}, weights={weighted}')

print(f'VERIFY_OK {assertions} exact assertions; {scalar_trials} exhaustively tested scalar maps; {product_trials} exhaustively tested product-to-chain maps; weighted star-root idempotent census checked for 2<=m<=6, 1<=r<=4 in feasible ranges')

# Exhaust every set map on the four-element Boolean square, not merely coordinate maps.
ms=(2,2); n=2
D=list(product(*(range(t) for t in ms)))
N=len(D)
A=list(product(range(2),repeat=2))
idx={a:i for i,a in enumerate(D)}
found=[]
for trial in product(range(N),repeat=N):
 if trial[-1] != N-1: continue
 ok=True
 for x,y in product(range(N),repeat=2):
  u=D[x];v=D[y];h=D[trial[x]]; k=D[trial[y]]
  e=idx[tuple(equ(u[j],v[j],2) for j in range(2))]
  rr=idx[tuple(reg(u[j],v[j],2) for j in range(2))]
  if D[trial[e]]!=tuple(equ(h[j],k[j],2) for j in range(2)) or D[trial[rr]]!=tuple(reg(h[j],k[j],2) for j in range(2)):
   ok=False;break
 if ok:found.append(trial)
check(len(found)==9)
check(sum(all(t[t[x]]==t[x] for x in range(N)) for t in found)==6)
check(sum(len(set(t))==N for t in found)==2)

from fractions import Fraction
for m in range(2,7):
 weights=[sum(comb(m-2,k) for k in range(a+1)) for a in range(m-1)]
 maxr=6
 coef=[Fraction(0)]*(maxr+1)
 coef[1]=1+len(weights)
 for k in range(2,maxr+1):
  coef[k]=sum((Fraction(w**(k-1),factorial(k-1)) for w in weights),Fraction(0))
 b=[Fraction(0)]*(maxr+1);b[0]=1
 for r in range(1,maxr+1):
  b[r]=sum((k*coef[k]*b[r-k] for k in range(1,r+1)),Fraction(0))/r
  predicted=sum(comb(r,t)*sum((1+sum(vals))**(r-t) for vals in product(weights,repeat=t)) for t in range(r+1))
  check(factorial(r)*b[r]==predicted,(m,r,b[r],predicted))

print(f'VERIFY_OK_FINAL {assertions} exact assertions; {scalar_trials} scalar and {product_trials} product-to-chain mappings exhaustively screened; 4^4 maps on Boolean square; exact EGF through r=6 for m<=6')

# Independent operation-table checks for every constructed product endomorphism.
verified_tables=0
verified_binary_pairs=0
for m,r in [(2,2),(2,3),(3,2),(3,3),(4,2),(5,2)]:
 domain=list(product(range(m),repeat=r))
 coord_opts=[None]+[(i,f) for i in range(r) for f in scalars(m,m) if f[0]==0]
 for outs in product(coord_opts,repeat=r):
  table={x:tuple(m-1 if o is None else o[1][x[o[0]]] for o in outs) for x in domain}
  for x in domain:
   check(table[table[x]] in domain)
   for y in domain:
    u=tuple(equ(x[i],y[i],m) for i in range(r))
    v=tuple(reg(x[i],y[i],m) for i in range(r))
    a=table[x];b=table[y]
    check(table[u]==tuple(equ(a[i],b[i],m) for i in range(r)))
    check(table[v]==tuple(reg(a[i],b[i],m) for i in range(r)))
    verified_binary_pairs+=1
  direct=all(table[table[x]]==table[x] for x in domain)
  symbol=True
  for o in outs:
   if o is None:continue
   i,f=o
   if outs[i] is None or outs[i][0]!=i:
    symbol=False;break
   g=outs[i][1]
   if tuple(f[g[x]] for x in range(m))!=f:
    symbol=False;break
  check(direct==symbol)
  verified_tables+=1
print(f'VERIFY_OK_CERTIFIED {assertions} exact assertions; {scalar_trials} scalar maps screened; {product_trials} product-to-chain maps screened; {verified_tables} product endomorphism tables checked on {verified_binary_pairs} ordered pairs, each with both operations; EGF checked m<=6, r<=6')
