from fractions import Fraction
from math import comb
from collections import defaultdict
from itertools import product, combinations
from functools import lru_cache

def tau(s): return 1 if s==1 else s**(s-2)
def rooted(n,k,s):
    if k==1:return Fraction(int(s==n))
    if k==n:return Fraction(int(s==1))
    if not 1<=s<=n-k+1:return Fraction()
    return Fraction(comb(n-k,s-1)*tau(s)*(k-1),k*n**(n-k-1))*Fraction(n-s)**(n-s-k)

checks=0
for n in range(2,51):
  for k in range(1,n+1):
    ps=[rooted(n,k,s) for s in range(1,n+1)]
    assert sum(ps)==1
    assert sum((s*p for s,p in enumerate(ps,1)),Fraction())==Fraction(n,k)
    checks+=2
  for k in range(1,n):
    pk=[rooted(n,k,s) for s in range(1,n+1)]
    pq=[rooted(n,k+1,s) for s in range(1,n+1)]
    for a in range(n):
      for b in range(a+1,n):
        assert pk[a]*pq[b] <= pk[b]*pq[a]
        checks+=1
    for t in range(2,n+1):
      assert sum(pk[t-1:])>=sum(pq[t-1:]); checks+=1
    # For a uniformly chosen vertex of an unconditioned rooted forest,
    # the tagged-component law is the size bias of a uniformly chosen root component.
    vk=[Fraction(k*s,n)*pk[s-1] for s in range(1,n+1)]
    vq=[Fraction((k+1)*s,n)*pq[s-1] for s in range(1,n+1)]
    assert sum(vk)==sum(vq)==1; checks+=1
    for a in range(n):
      for b in range(a+1,n):
        assert vk[a]*vq[b]<=vk[b]*vq[a]; checks+=1
    assert sum((sum(pk[t-1:])-sum(pq[t-1:]) for t in range(2,n+1)),Fraction())==Fraction(n,k)-Fraction(n,k+1)
    checks+=1
    d=sum(abs(pk[s]-pq[s]) for s in range(n))/2
    assert d<=1; checks+=1

def direct_rooted(n,k):
   roots=set(range(k)); nons=list(range(k,n)); counts=defaultdict(int)
   for pars in product(range(n), repeat=n-k):
     nxt=dict(zip(nons,pars))
     comp={r:0 for r in roots}; valid=True
     for v in range(n):
       x=v; seen=set()
       while x not in roots:
          if x in seen:valid=False; break
          seen.add(x);x=nxt[x]
       if not valid:break
       comp[x]+=1
     if valid:counts[comp[0]]+=1
   return counts
for n in range(2,8):
  for k in range(1,n+1):
   cnt=direct_rooted(n,k); den=sum(cnt.values())
   assert den==(k*n**(n-k-1) if k<n else 1)
   for s in range(1,n+1):assert Fraction(cnt[s],den)==rooted(n,k,s)
   checks+=n+1

def forest_counts(n,k):
  # unrooted forests using canonical Bell decomposition by component containing vertex 0
  @lru_cache(None)
  def f(m,h):
   if m==0:return int(h==0)
   if h<1:return 0
   return sum(comb(m-1,s-1)*tau(s)*f(m-s,h-1) for s in range(1,m+1))
  den=f(n,k)
  return [Fraction(comb(n-1,s-1)*tau(s)*f(n-s,k-1),den) for s in range(1,n+1)]
first=[]
for n in range(3,12):
 for k in range(1,n):
  a=forest_counts(n,k); b=forest_counts(n,k+1)
  bad=[(i+1,j+1) for i in range(n) for j in range(i+1,n) if a[i]*b[j]>a[j]*b[i]]
  if bad: first.append((n,k,bad[0],a,b))
  checks+=n*(n-1)//2
# Independent direct enumeration of all edge subsets forming forests.
def direct_unrooted(n,k):
    pairs=list(combinations(range(n),2))
    counts=defaultdict(int)
    for es in combinations(pairs,n-k):
        parent=list(range(n))
        def root(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        ok=True
        for u,v in es:
            a,b=root(u),root(v)
            if a==b: ok=False;break
            parent[a]=b
        if not ok: continue
        r=root(0)
        counts[sum(root(i)==r for i in range(n))]+=1
    return counts
for n in range(2,7):
    for k in range(1,n+1):
        cnt=direct_unrooted(n,k)
        den=sum(cnt.values())
        assert den>0
        for s in range(1,n+1):
            assert Fraction(cnt[s],den)==forest_counts(n,k)[s-1]
            checks+=1
print('checks=',checks,'first unrooted LR violations=',[(n,k,bad) for n,k,bad,*_ in first[:10]])
assert first[0][:3]==(5,2,(1,2)),first[0]
print('n5,k2=',forest_counts(5,2),'n5,k3=',forest_counts(5,3))
print('all verified')

# Independently compare the two-component forest closed form to the
# component-decomposition recurrence, and verify the exact obstruction ratio.
for n in range(4,55):
    # The count of two-component forests is recovered by summing its masses'
    # unnormalized component decomposition terms.
    f_two=sum(comb(n-1,s-1)*tau(s)*tau(n-s) for s in range(1,n))
    closed=Fraction((n-1)*(n+6),2)*n**(n-4)
    assert f_two==closed;checks+=1
for n in range(5,31):
    a=forest_counts(n,2)
    b=forest_counts(n,3)
    computed=(a[0]/b[0])/(a[1]/b[1])
    claimed=1+Fraction((n-4)*(5*n-7),(n-2)**3*(n+5))
    assert computed==claimed and computed>1
    checks+=1
print('Additional closed-form and all-order obstruction checks passed; total counted exact checks:',checks)
