"""Independent finite checks for the three-survivor multiset packing theorem."""
from itertools import combinations
from math import comb

def profiles(q,n):
    if q==1:
        yield (n,);return
    for k in range(n+1):
        for tail in profiles(q-1,n-k):yield(k,)+tail

def intersect(a,b):return sum(min(x,y) for x,y in zip(a,b))
def valid(C):return all(intersect(x,y)<=2 for x,y in combinations(C,2))
def pure(q,n):return [tuple(n if i==j else 0 for i in range(q)) for j in range(q)]
def light(q,n):return tuple(2 if i<n-q else 1 for i in range(q))
def codes(q,n):return pure(q,n)+[light(q,n)] if n<=2*q else pure(q,n)

tested=0
for q in range(2,7):
    for n in range(q+2,2*q+2):
        P=list(profiles(q,n)); L=[x for x in P if max(x)<=2]
        assert all(intersect(x,y)>=3 for x,y in combinations(L,2))
        C=codes(q,n); assert valid(C)
        assert len(C)==(q+1 if n<=2*q else q)
        # Every heavy must have >=3 in some coordinate; two heavies sharing
        # such a coordinate have intersection >=3.
        for x in P:
            if x not in L:assert max(x)>=3
        tested+=len(P)
        print(f'q={q}, n={n}, profiles={len(P)}, light={len(L)}, constructed={len(C)}')

# Independent exhaustive classification of maximum codebooks for ternary q=3.
for n,want in [(5,9),(6,1)]:
    q=3;P=list(profiles(q,n));good=[]
    for inds in combinations(range(len(P)),4):
        C=tuple(P[i] for i in inds)
        if valid(C):good.append(frozenset(C))
    patterns=set()
    if n==6:patterns.add(frozenset(pure(q,n)+[(2,2,2)]))
    else:
        for s in range(q):
            a=tuple(1 if j==s else 2 for j in range(q))
            for j in range(q):
                heavy=list(pure(q,n))
                if j!=s:
                    z=[0]*q;z[s]=n-1;z[j]=1;heavy[s]=tuple(z)
                patterns.add(frozenset(heavy+[a]))
    assert len(good)==want and set(good)==patterns,(n,len(good),want)
    print(f'q=3, n={n}, exhaustive optimal codebooks={len(good)}')

# Check all structural boundary codebooks against all arbitrary admissible
# heavy vectors for q=2..6 without enumerating every codebook.
for q in range(2,7):
  for n in [2*q-1,2*q]:
    if n<q+2:continue
    P=list(profiles(q,n))
    for l in [x for x in P if max(x)<=2]:
      for i in range(q):
        candidates=[x for x in P if x[i]>=3 and intersect(l,x)<=2]
        allowed=[]
        if n==2*q:allowed=[pure(q,n)[i]]
        else:
            s=l.index(1)
            if i!=s:allowed=[pure(q,n)[i]]
            else:
                allowed=[pure(q,n)[i]]
                for j in range(q):
                    if j==i:continue
                    z=[0]*q;z[i]=n-1;z[j]=1;allowed.append(tuple(z))
        assert set(candidates)==set(allowed),(q,n,l,i,len(candidates),len(allowed))
    print(f'q={q}, n={n}, rigidity candidate classification passed')

# n=q+1 two-light construction verifying the preceding strict gap.
for q in range(2,16):
  n=q+1
  if q%2==0:
    m=q//2
    a=tuple([2]*m+[1]+[0]*(m-1))
    b=tuple([1]+[0]*(m-1)+[2]*m)
  else:
    m=q//2
    a=tuple([2]*(m+1)+[0]*m)
    b=tuple([0]*m+[2]*(m+1))
  C=pure(q,n)+[a,b]
  assert all(sum(x)==n for x in C) and len(set(C))==q+2 and valid(C),(q,a,b,intersect(a,b))
print(f'All finite checks pass; profiles analyzed={tested}')
