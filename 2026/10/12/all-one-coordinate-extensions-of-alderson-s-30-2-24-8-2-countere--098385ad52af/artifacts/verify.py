from collections import Counter
from itertools import combinations

N=64
MASK=(1<<N)-1

def wt(x): return x.bit_count()
F={x for x in range(1,N) if wt(x) in (3,4)}
G=set(range(1,N))-F
assert len(F)==35 and len(G)==28

e=[1<<i for i in range(6)]
one=N-1
T={0,*e,one}
assert len(T)==8
# Difference set of T: every nonzero pair difference is unique and is exactly G.
pairs={}
for a,b in combinations(sorted(T),2):
    d=a^b
    assert d not in pairs
    pairs[d]=(a,b)
assert set(pairs)==G

# Graph Gamma: minimum-distance graph of the base code.
adj=[0]*N
for a in range(N):
    m=0
    for d in F: m |= 1<<(a^d)
    adj[a]=m
assert all((adj[a]>>a)&1==0 for a in range(N))
assert all(adj[a].bit_count()==35 for a in range(N))

# Character spectrum of the Cayley graph.
spec=Counter()
for u in range(N):
    lam=sum(1 if ((u&d).bit_count()%2)==0 else -1 for d in F)
    spec[lam]+=1
assert spec==Counter({35:1,3:35,-5:28})

# Exact strongly-regular common-neighbor counts.
for a in range(N):
    for b in range(a+1,N):
        c=(adj[a]&adj[b]).bit_count()
        assert c==(18 if ((adj[a]>>b)&1) else 20)

# Standard-library Bron-Kerbosch over bit masks; enumerate maximal cliques.
def maximal_cliques(adjacency):
    out=[]
    def bk(R,P,X):
        if P==0 and X==0:
            out.append(R); return
        ux=P|X
        if ux:
            # pivot maximizing neighbors in P
            best=None; bestc=-1; z=ux
            while z:
                lb=z & -z; u=lb.bit_length()-1; z-=lb
                c=(P & adjacency[u]).bit_count()
                if c>bestc: best,bestc=u,c
            cand=P & ~adjacency[best] & MASK
        else:
            cand=P
        while cand:
            lb=cand & -cand; v=lb.bit_length()-1; cand-=lb
            bk(R|lb, P & adjacency[v], X & adjacency[v])
            P &= ~lb; X |= lb
    bk(0,MASK,0)
    return out

# Maximum cocliques are maximal cliques of complement.
comp=[(MASK ^ (1<<a) ^ adj[a]) for a in range(N)]
mc_comp=maximal_cliques(comp)
max_coc=[r for r in mc_comp if r.bit_count()==8]
assert max(r.bit_count() for r in mc_comp)==8
assert len(max_coc)==64
translates={sum(1<<(t^a) for t in T) for a in range(N)}
assert len(translates)==64 and set(max_coc)==translates

# Maximum cliques of Gamma: exactly 240 affine cosets of the 30 special 3-spaces.
mc=maximal_cliques(adj)
max_cli=[r for r in mc if r.bit_count()==8]
assert max(r.bit_count() for r in mc)==8
assert len(max_cli)==240

def span3(a,b,c):
    return {0,a,b,c,a^b,a^c,b^c,a^b^c}
Ws=set()
for a,b,c in combinations(range(1,N),3):
    # independent iff c not in span(a,b)
    if c in {a,b,a^b}: continue
    W=frozenset(span3(a,b,c))
    if all((x==0 or x in F) for x in W): Ws.add(W)
assert len(Ws)==30
cosets=set()
for W in Ws:
    for a in range(N):
        A=frozenset(a^w for w in W)
        cosets.add(A)
assert len(cosets)==240
clique_sets={frozenset(i for i in range(N) if (r>>i)&1) for r in max_cli}
assert clique_sets==cosets

# Each affine 3-flat A indexes a partition {T+a:a in A}; all 240 are distinct.
partitions=set()
for A in cosets:
    classes=tuple(sorted(tuple(sorted(t^a for t in T)) for a in A))
    flat=[x for C in classes for x in C]
    assert len(flat)==64 and len(set(flat))==64
    partitions.add(classes)
assert len(partitions)==240

# Any such extension is distance-invariant with local distribution 25^35,30^7,31^21.
# Base distance is 24 on F-differences, 30 on G-differences.
def base_dist(a,b): return 24 if (a^b) in F else 30
for classes in partitions:
    color={x:i for i,C in enumerate(classes) for x in C}
    profiles=[]
    for a in range(N):
        p=Counter()
        for b in range(N):
            if a==b: continue
            d=base_dist(a,b)+(color[a]!=color[b])
            p[d]+=1
        profiles.append(p)
    assert all(p==Counter({25:35,30:7,31:21}) for p in profiles)

assert len(partitions)*40320==9676800
print('F_SIZE',len(F),'G_SIZE',len(G))
print('SPECTRUM',dict(sorted(spec.items())))
print('MAX_COCLIQUES',len(max_coc))
print('SPECIAL_3SPACES',len(Ws))
print('MAX_CLIQUES',len(max_cli))
print('UNLABELED_EXTENSION_PARTITIONS',len(partitions))
print('LABELED_EXTENSION_COORDINATES',len(partitions)*40320)
print('LOCAL_DISTANCE_DISTRIBUTION',{25:35,30:7,31:21})
print('VERIFY_OK')
