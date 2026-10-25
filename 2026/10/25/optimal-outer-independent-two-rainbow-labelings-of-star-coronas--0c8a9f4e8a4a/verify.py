"""Independent verification of optimal outer-independent 2-rainbow labelings.

Labels use bit masks: 0=empty, 1={1}, 2={2}, 3={1,2}.
Only the Python standard library is required.
"""
from itertools import combinations, product
from collections import Counter


def adjacency_of_base(n, edges, leaves=2):
    N = (1+leaves)*n
    adj = [0]*N
    def edge(a,b):
        adj[a] |= 1<<b
        adj[b] |= 1<<a
    for a,b in edges: edge(a,b)
    for v in range(n):
        for j in range(leaves):
            edge(v,n+leaves*v+j)
    return adj


def valid(labels, adj):
    empty = sum(1<<v for v,c in enumerate(labels) if c==0)
    for i,c in enumerate(labels):
        if c: continue
        if adj[i] & empty: return False
        union = 0
        m = adj[i]
        while m:
            b = m & -m
            union |= labels[b.bit_length()-1]
            m -= b
        if union != 3: return False
    return True


def independence_profile(n, edges):
    profile = Counter()
    for bits in range(1<<n):
        if all(not ((bits>>u)&1 and (bits>>v)&1) for u,v in edges):
            profile[bits.bit_count()]+=1
    return profile


def predicted_profile(n, edges):
    deg=[0]*n
    for a,b in edges:
        deg[a]+=1;deg[b]+=1
    iso={i for i,d in enumerate(deg) if d==0}
    profile = Counter()
    for bits in range(1<<n):
        if any((bits>>a)&1 and (bits>>b)&1 for a,b in edges):
            continue
        mul=1
        for v in range(n):
            if (bits>>v)&1:
                mul *= (2 if v in iso else 4)
        profile[bits.bit_count()] += mul
    return profile


def brute_optimal_profile(n, edges, weighted_only=False, leaves=2):
    adj=adjacency_of_base(n,edges,leaves)
    N=(1+leaves)*n
    counts=Counter()
    if not weighted_only:
        minweight=10**9
        for lab in product(range(4),repeat=N):
            if not valid(lab,adj): continue
            weight=sum(x.bit_count() for x in lab)
            if weight<minweight:
                minweight=weight;counts.clear()
            if weight==minweight:
                counts[sum(x==0 for x in lab[:n])]+=1
        assert minweight==2*n, (n,edges,minweight)
        return counts
    for on in combinations(range(2*N),2*n):
        mask=sum(1<<b for b in on)
        lab=tuple((mask>>(2*i))&3 for i in range(N))
        if valid(lab,adj):
            counts[sum(x==0 for x in lab[:n])]+=1
    return counts


def blowup(n,edges,r):
    return n*r, [(a*r+i,b*r+j) for a,b in edges for i in range(r) for j in range(r)]


def independence_eval(n,edges,z):
    c=independence_profile(n,edges)
    return sum(v*z**k for k,v in c.items())


def run():
    scenarios=0
    for n in range(1,4):
        pairs=list(combinations(range(n),2))
        for emask in range(1<<len(pairs)):
            edges=[pair for i,pair in enumerate(pairs) if (emask>>i)&1]
            brute=brute_optimal_profile(n,edges)
            pred=predicted_profile(n,edges)
            assert brute==pred, (n,edges,brute,pred)
            scenarios+=1
    # Larger cases enumerate ALL candidate weight-2n functions,
    # using no structural assumptions about their zero positions.
    n=4
    cases={
        'empty':[],
        'path':[(0,1),(1,2),(2,3)],
        'cycle':[(0,1),(1,2),(2,3),(3,0)],
        'star':[(0,1),(0,2),(0,3)],
        'complete':list(combinations(range(n),2)),
    }
    for name,edges in cases.items():
        brute=brute_optimal_profile(n,edges,weighted_only=True)
        pred=predicted_profile(n,edges)
        assert brute==pred, (name,brute,pred)
        scenarios+=1
    # For at least three private leaves, the unique optimum is the
    # all-double-labeling of base vertices with all leaves empty.
    for leaves, n in [(3,1),(3,2),(3,3),(4,1),(4,2)]:
        pairs=list(combinations(range(n),2))
        for emask in range(1<<len(pairs)):
            edges=[pair for i,pair in enumerate(pairs) if (emask>>i)&1]
            brute=brute_optimal_profile(n,edges,weighted_only=True,leaves=leaves)
            assert brute==Counter({0:1}), (leaves,n,edges,brute)
            scenarios+=1
    for r in range(1,4):
        n2,e2=blowup(3,[(0,1),(1,2)],r)
        assert independence_eval(n2,e2,4)==independence_eval(3,[(0,1),(1,2)],5**r-1)
    print('VERIFICATION_OK', 'graphs=',scenarios,'plus_three_blowup_identities')
    for n,edges in [(1,[]),(2,[(0,1)]),(3,[(0,1),(1,2)]),(3,[(0,1),(1,2),(2,0)]),(4,cases['cycle'])]:
        p=predicted_profile(n,edges)
        print('profile',n,edges,dict(sorted(p.items())),'total',sum(p.values()))

if __name__=='__main__':run()
