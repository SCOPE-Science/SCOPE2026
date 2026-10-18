from collections import defaultdict
from itertools import product
from math import comb

def space_ok(n,R):
 rows=[{j for j in range(n) if R[i*n+j]} for i in range(n)]
 cols=[{i for i in range(n) if R[i*n+j]} for j in range(n)]
 if any(s and s!=set(range(min(s),max(s)+1)) for s in rows):return False
 for t in range(n+1):
  U=set(range(t,n))
  sets=[{i for i in range(n) if rows[i]-(U)},
   {i for i in range(n) if not rows[i]&U},
   {j for j in range(n) if cols[j]-(U)},
   {j for j in range(n) if not cols[j]&U}]
  if any(s!=set(range(min(s),n)) for s in sets if s):return False
 return True

def form_ok(n,R):
 if not any(R):return True
 rows=[{j for j in range(n) if R[i*n+j]} for i in range(n)]
 if any(not row for row in rows):return False
 l=[];u=[]
 for row in rows:
  ll=min(row);uu=max(row)
  if row!=set(range(ll,uu+1)):return False
  l.append(ll);u.append(uu)
 if any(l[i]<l[i+1] or u[i]<u[i+1] for i in range(n-1)):return False
 if u[0]!=n-1 or l[-1]!=0:return False
 if any(l[i]>u[i+1]+1 for i in range(n-1)):return False
 return True

def count(n):
 states=[(l,u) for l in range(n) for u in range(l,n)]
 dp={s:1 for s in states if s[1]==n-1}
 for i in range(1,n):
  nd=defaultdict(int)
  for (l,u),q in dp.items():
   for ln,un in states:
    if ln<=l and un<=u and l<=un+1:
     nd[(ln,un)]+=q
  dp=nd
 return 1+sum(v for (l,u),v in dp.items() if l==0)


from collections import defaultdict

def go(n):
 rs=[(l,u) for l in range(n) for u in range(l,n)]
 ans=0;hist=defaultdict(int); bydiagonal=defaultdict(int)
 def rec(rows):
  nonlocal ans
  i=len(rows)
  if i==n:
   if rows[-1][0]>0:return
   for a,(l,u) in enumerate(rows):
    for b in range(n):
     if (l<=b<=u)!=(rows[b][0]<=a<=rows[b][1]):return
   ans+=1
   bydiagonal[sum(l<=a<=u for a,(l,u) in enumerate(rows))]+=1
   hist[sum(u-l+1 for l,u in rows)]+=1
   return
  prev=rows[-1] if i else None
  for l,u in rs:
   if i==0 and u<n-1:continue
   if prev and (l>prev[0] or u>prev[1] or prev[0]>u+1):continue
   good=True
   for j,(lj,uj) in enumerate(rows):
    if (l<=j<=u)!=(lj<=i<=uj):good=False;break
   if good:rec(rows+[(l,u)])
 rec([])
 return ans

from itertools import product

def antitone(q):
 for a in product(range(q),repeat=q):
  if all(a[i]>=a[i+1] for i in range(q-1)):yield a

def ok(g,f):
 q=len(g)
 if g[-1]!=0 or f[0]!=q-1:return False
 for x in range(q):
  if g[g[x]]>x or f[f[x]]<x:return False
  for y in range(q):
   if min(g[x],f[y])>g[max(x,y)]:return False
   if f[min(x,y)]>max(f[x],g[y]):return False
 return True


# Separate exhaustive relation and operator implementations for small chains.
expected_all = [2,5,30,267,2763,31005,367286,4526471]
expected_sym = [2,5,14,47,167,611,2270,8519]
for n in range(1,9):
    assert count(n) == expected_all[n-1], (n,'all')
    assert go(n)+1 == expected_sym[n-1], (n,'symmetric')
for n in range(1,5):
    for bits in product([0,1], repeat=n*n):
        assert space_ok(n,bits) == form_ok(n,bits), (n,bits)
for n in range(1,6):
    q=n+1
    gs=[g for g in antitone(q) if g[-1]==0]
    fs=[f for f in antitone(q) if f[0]==q-1]
    direct=sum(ok(g,f) for g in gs for f in fs)
    assert direct==expected_sym[n-1], (n,direct)
print('VERIFY_OK; all n<=8, symmetric n<=8, complete relations n<=4, direct unary axioms n<=5')
