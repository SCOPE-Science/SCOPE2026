"""Second implementation: exact online decision-tree recursion on vertex candidates.
Only Python standard library is required; no graph packages.
"""
from functools import lru_cache
from itertools import product
from random import Random

def adjacency(n,edges):
    N=[{i} for i in range(n)]
    for a,b in edges:
        assert 0<=a<n and 0<=b<n and a!=b
        N[a].add(b); N[b].add(a)
    return tuple(frozenset(v) for v in N)

def exact(N):
    n=len(N)
    # Center sets, not count-based local predictions.
    @lru_cache(None)
    def score(C):
        C=set(C)
        if len({N[v] for v in C})<=1:return 0
        mx=0
        for q in range(n):
            yes=frozenset(v for v in C if q in N[v]);no=frozenset(C-yes)
            if yes and no:mx=max(mx,1+min(score(yes),score(no)))
        return mx
    return score(frozenset(range(n)))

def predicted(N):
    n=len(N)
    if n==1 or n==2:return 0
    if n==3:return 1
    if n==4:return 2
    for x in range(n):
        other=set(range(n))-N[x]
        if len(N[x])<4:continue
        for y in range(n):
            a=len(other & N[y])
            if 2<=a<=len(other)-2:return 3
    return 2

def prufer_tree(code):
    n=len(code)+2
    deg=[1]*n
    for v in code:deg[v]+=1
    E=[]
    for v in code:
        leaf=min(i for i,d in enumerate(deg) if d==1)
        E.append((leaf,v));deg[leaf]-=1;deg[v]-=1
    a,b=[i for i,d in enumerate(deg) if d==1]
    E.append((a,b))
    return E

if __name__=='__main__':
    k=0
    for n in range(3,7):
        for code in product(range(n),repeat=n-2):
            N=adjacency(n,prufer_tree(code))
            assert exact(N)==predicted(N),(n,code)
            k+=1
    print('INDEPENDENT_ALL_LABELED_TREES_PASS',k,flush=True)
    rng=Random(27019)
    for n in range(7,17):
        for _ in range(35):
            code=tuple(rng.randrange(n) for _ in range(n-2))
            N=adjacency(n,prufer_tree(code))
            assert exact(N)==predicted(N)
    print('INDEPENDENT_RANDOM_TREES_PASS',350,flush=True)
    tests=[]
    # At least one cycle. Subdivided or augmented with pendant edges, preserving girth >= 5.
    for n in range(5,16):
        E=[(i,(i+1)%n) for i in range(n)]
        tests.append((n,E))
        for leafcount in range(1,5):
            edges=E+[(n+i,rng.randrange(n)) for i in range(leafcount)]
            tests.append((n+leafcount,edges))
    for n,E in tests:
        N=adjacency(n,E)
        assert exact(N)==predicted(N),(n,E)
    print('INDEPENDENT_UNICYCLIC_PASS',len(tests),flush=True)
    E=[(1,0),(1,2),(1,3),(1,4),(0,5),(5,6),(5,7)]
    N=adjacency(8,E)
    assert exact(N)==3 and predicted(N)==3
    # Complete two-round branches: x=5, + branch (centers 0,5,6,7) and - branch (1,2,3,4).
    assert set(N[5])=={0,5,6,7}
    assert set(range(8))-N[5]=={1,2,3,4}
    assert len(N[0]&N[5])==2 and len(N[2]&({1,2,3,4}))==2
    print('INDEPENDENT_EIGHT_VERTEX_WITNESS_PASS')
    print('ALL_INDEPENDENT_CHECKS_PASS')
