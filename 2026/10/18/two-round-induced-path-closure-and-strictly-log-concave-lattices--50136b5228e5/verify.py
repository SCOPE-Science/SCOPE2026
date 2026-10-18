"""Direct finite checks for induced-P3 closure on triangular graphs.
Run with Python 3.10+ and no third-party modules.
"""
from itertools import combinations, permutations
from math import comb
from collections import Counter

def check_n(n):
    edges = list(combinations(range(n), 2))
    index = {e: i for i, e in enumerate(edges)}
    rules=[]
    for i,j in combinations(range(len(edges)),2):
        a,b=edges[i],edges[j]
        if len(set(a+b))==4:
            t=sum(1<<index[tuple(sorted((x,y)))] for x in a for y in b)
            rules.append(((1<<i)|(1<<j), t))
    def step(s):
        t=s
        for prem, targets in rules:
            if prem&s == prem:
                t |= targets
        return t
    all_count=1<<len(edges)
    closed=set()
    times=Counter()
    all_mob=[]
    for s in range(all_count):
        v=s
        active={x for k,e in enumerate(edges) if s>>k&1 for x in e}
        has_disjoint=any(s&prem==prem for prem,_ in rules)
        expected=sum(1<<i for i,(a,b) in enumerate(edges) if a in active and b in active) if has_disjoint else s
        steps=0
        while True:
            v1=step(v)
            if v1==v:break
            v=v1;steps+=1
            assert steps<=2,(n,s,'slow')
        assert v==expected,(n,s,v,expected)
        # A proper missing edge after the first step occurs iff its endpoints are sibling leaves.
        first=step(s)
        adj=[set() for _ in range(n)]
        for j,(a,b) in enumerate(edges):
            if s>>j&1:adj[a].add(b);adj[b].add(a)
        cherry=any(len(adj[a])==1 and len(adj[b])==1 and adj[a]==adj[b]
                   for a,b in combinations(active,2) if not (s>>index[tuple(sorted((a,b)))]&1))
        assert (steps==2)==(has_disjoint and cherry),(n,s,steps,cherry)
        if s==v:closed.add(s)
        times[steps]+=1
    theory=(n+2)*2**(n-1)-n*(n+1)
    assert len(closed)==theory,(n,len(closed),theory)
    rank_counts=Counter()
    # rank via longest chain in the actual closed-set order.
    rank={}
    for s in sorted(closed,key=int.bit_count):
        if s==0:rank[s]=0
        else:
            rank[s]=1+max(rank[t] for t in rank if t!=s and t&s==t)
        rank_counts[rank[s]]+=1
    expected_rank={0:1,1:comb(n,2),2:3*comb(n,3)}
    for k in range(3,n+1):expected_rank[k]=(n-k+1)*comb(n,k)
    assert rank_counts==expected_rank,(n,rank_counts,expected_rank)
    # Bottom-to-top Möbius recurrence on actual closed-set lattice.
    if n<=5:
        mu={}
        for s in sorted(closed,key=int.bit_count):
            mu[s]=1 if s==0 else -sum(v for t,v in mu.items() if t&s==t)
        full=(1<<len(edges))-1
        assert mu[full]==(-1)**n,(n,mu[full])
    print('EXHAUSTIVE',n,'subsets',all_count,'closed',len(closed),'ranks',[rank_counts[i] for i in range(n+1)],'time_counts',dict(sorted(times.items())),'PASS')

for n in (4,5,6):check_n(n)
for n in range(4,101):
    c=[1,comb(n,2),3*comb(n,3)]+[(n-k+1)*comb(n,k) for k in range(3,n+1)]
    assert all(c[j]*c[j]>c[j-1]*c[j+1] for j in range(1,n))
# Every permutation of the six atoms of T(4) can be tested for adjacency preservation.
e=list(combinations(range(4),2))
def adjacent(i,j):return bool(set(e[i])&set(e[j]))
aut=sum(all(adjacent(i,j)==adjacent(p[i],p[j]) for i,j in combinations(range(6),2)) for p in permutations(range(6)))
assert aut==48
print('AUTOMORPHISM_T4',aut,'PASS')
print('VERIFY_OK exact_closure=PASS two_round_cherry=PASS graded_rank=PASS mobius=PASS strict_logconcavity=PASS exceptional_symmetry=PASS')
