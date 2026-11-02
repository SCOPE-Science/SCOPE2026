"""Independent finite checks of wheel rainbow-diamond edge colorings."""
from itertools import combinations, product
from math import factorial

def conflicts(n):
    vertices=list(range(n+1)); hub=n
    edges=[tuple(sorted((i,hub))) for i in range(n)]+[tuple(sorted((i,(i+1)%n))) for i in range(n)]
    edges=[tuple(sorted(e)) for e in edges]
    ec={e:i for i,e in enumerate(edges)}
    bad=set()
    for i,j in combinations(range(2*n),2):
        if set(edges[i]) & set(edges[j]):bad.add((i,j))
    for vs in combinations(vertices,4):
        es=[ec[e] for e in combinations(vs,2) if e in ec]
        if len(es)>=5:
            for a,b in combinations(sorted(es),2):bad.add((a,b))
    return bad

def allowed(n):
    pairs={(i,j) for i,j in combinations(range(n),2)}
    pairs|={(n+i,n+(i+1)%n) if n+i<n+(i+1)%n else (n+(i+1)%n,n+i) for i in range(n)}
    for i in range(n):
        for j in [(i-1)%n,i,(i+1)%n,(i+2)%n]:
            a,b=sorted((j,n+i));pairs.add((a,b))
    return pairs

def count(n):
    ls=[set(range(n))-{(i-1)%n,i,(i+1)%n,(i+2)%n} for i in range(n)]
    ans=0
    for first in ls[0]:
        d={first:1}
        for j in range(1,n):
            d={c:sum(v for p,v in d.items() if p!=c) for c in ls[j]}
        ans+=sum(v for c,v in d.items() if c!=first)
    return ans

for n in range(5,35):
    assert conflicts(n)==allowed(n),(n,conflicts(n)^allowed(n))
print('CONFLICTS_OK 30')
for n in (5,6,7):
    ls=[set(range(n))-{(i-1)%n,i,(i+1)%n,(i+2)%n} for i in range(n)]
    b=sum(all(seq[i]!=seq[(i+1)%n] for i in range(n)) for seq in product(*[sorted(x) for x in ls]))
    assert count(n)==b,(n,b,count(n))
print('EXHAUSTIVE_OK 3')
assert [count(n) for n in (5,6,7,8,9,10)]==[1,2,367,11966,400376,13440226]
print('COUNTS_OK 6')
for n in (5,6,7,8,9,10,12,16,24,40):
    a=count(n)
    print('n',n,'normalized',a,'named',a*factorial(n),'ratio',f'{a/(n-4)**n:.9f}')
print('VERIFY_OK')
