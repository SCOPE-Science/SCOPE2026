"""Independent algebraic classification, without exhaustive 16 choose 4 enumeration."""
from itertools import product,permutations,combinations
from collections import defaultdict,deque,Counter
V=list(product(range(4),repeat=2))
S={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
plus=lambda a,b:((a[0]+b[0])%4,(a[1]+b[1])%4)
neg=lambda a:((-a[0])%4,(-a[1])%4)
K={(0,0),(2,0),(0,2),(2,2)}
cyclic=lambda g:{(k*g[0]%4,k*g[1]%4) for k in range(4)}
H=[K,cyclic((1,2)),cyclic((2,1)),cyclic((1,3))]
assert all(len(h)==4 and not any(plus(a,neg(b)) in S for a,b in combinations(h,2)) for h in H)
assert all(len(h&k)==2 for h,k in combinations(H[:1]+H[1:2],2))
assert all(len(H[0]&h)==2 for h in H[1:])
assert all(len(a&b)==1 for a,b in combinations(H[1:],2))
cosets=[]; owners=[]
for i,h in enumerate(H):
    seen=set()
    for v in V:
        c=frozenset(plus(v,x) for x in h)
        if c not in seen:cosets.append(c); owners.append(i);seen.add(c)
    assert len(seen)==4
assert len(set(cosets))==16
edges=set(); neighbors=defaultdict(set)
for i,j in combinations(range(16),2):
    if len(cosets[i]&cosets[j])==2:
        edges.add((i,j));neighbors[i].add(j);neighbors[j].add(i)
assert len(edges)==24
assert {len(neighbors[i]) for i in range(16) if owners[i]==0}=={6}
assert {len(neighbors[i]) for i in range(16) if owners[i]!=0}=={2}
assert all(owners[a]==0 or owners[b]==0 for a,b in edges)
hubs=[i for i,x in enumerate(owners) if x==0]
assert len(hubs)==4
pairs=Counter()
for v in range(16):
    if owners[v]!=0:
        a,b=sorted(neighbors[v]);pairs[(a,b)]+=1
assert len(pairs)==6 and all(pairs[z]==2 for z in combinations(sorted(hubs),2))
print('COSET_STRUCTURE_PASS four hubs six pairs each doubled 12 intermediate states')
P=list(permutations(range(4)))
assert len(P)==24
E=set()
for i,j in combinations(range(24),2):
    a,b=P[i],P[j]
    overlap=sum(x==y for x,y in zip(a,b))
    assert overlap!=3
    if overlap==2: E.add((i,j));assert sum(x!=y for x,y in zip(a,b))==2
assert len(E)==72
assert all(sum(i in e for e in E)==6 for i in range(24))
# Every transposition changes sign; adjacent permutations differ by one transposition.
print('PERMUTATION_STRUCTURE_PASS order-24 transposition Cayley graph degree6 edges72')
print('ALGEBRA_PASS')
