"""Exact zero-forcing and exchange-metric census on KG(6,2); Python stdlib only."""
from itertools import combinations
from collections import Counter, deque

pairs=list(combinations(range(6),2))
n=len(pairs)
assert n==15
adj=[]
for a in pairs:
    adj.append(sum(1<<j for j,b in enumerate(pairs) if len(set(a).intersection(b))==0))
full=(1<<n)-1

def forces(seed):
    colored=seed
    while colored!=full:
        newly=0
        for i in range(n):
            if colored>>i&1:
                remaining=adj[i]&~colored
                if remaining and remaining&(remaining-1)==0:
                    newly|=remaining
        if not newly:
            return False
        colored|=newly
    return True

# Monotonicity makes proving absence of 9-seed sets sufficient for Z>=10.
assert sum(forces(sum(1<<i for i in c)) for c in combinations(range(n),9))==0
seeds=sorted(sum(1<<i for i in c) for c in combinations(range(n),10) if forces(sum(1<<i for i in c)))
assert len(seeds)==1662
where={m:i for i,m in enumerate(seeds)}
neighbor=[]
for m in seeds:
    linked=[]
    for i in range(n):
        if m>>i&1:
            for j in range(n):
                if not (m>>j&1):
                    nxt=(m^(1<<i))|(1<<j)
                    if nxt in where:
                        linked.append(where[nxt])
    neighbor.append(sorted(linked))
assert all(i in neighbor[j] for j,ns in enumerate(neighbor) for i in ns)
deg=Counter(map(len,neighbor));assert deg==Counter({26:450,30:432,32:420,29:360}),deg
assert sum(map(len,neighbor))//2==24270

hist=Counter(); ecc=Counter()
for start in range(len(seeds)):
    dist=[-1]*len(seeds);dist[start]=0
    queue=deque([start])
    while queue:
        x=queue.popleft()
        for y in neighbor[x]:
            if dist[y]==-1:
                dist[y]=dist[x]+1;queue.append(y)
    assert min(dist)==0 and -1 not in dist
    ecc[max(dist)]+=1
    if start==0:
        pass
    for d in dist:
        if d>0:hist[d]+=1
assert ecc==Counter({5:1662}),ecc
hist={str(k):v//2 for k,v in sorted(hist.items())}
assert sum(hist.values())==1662*1661//2
print('DIRECT_PASS',{'zero_forcing_number':10,'minimum_sets':len(seeds),'edges':24270,'degrees':dict(sorted(deg.items())),'eccentricities':dict(ecc),'distance_histogram':hist})
