"""Independent domination of the once-subdivided graph, reproducible finite checks.

All tests compare independently implemented definitions against formulas.
Python 3.10+; optional networkx for nonisomorphic forest tests.
"""
from itertools import combinations
from collections import Counter
import random

def edges_of(n, graphmask):
    pairs = list(combinations(range(n), 2))
    return [e for j,e in enumerate(pairs) if (graphmask >> j) & 1]

def formula_poly(n, edges):
    out = Counter()
    for w in range(1 << n):
        ecount = sum(bool((w >> u) & 1 and (w >> v) & 1) for u, v in edges)
        if any((w >> v)&1 and not any((w >> a)&1 for a,b in edges if b==v) and not any((w >> b)&1 for a,b in edges if a==v) for v in range(n)):
            continue
        out[n-w.bit_count()+ecount] += 1
    return +out

def direct_poly(n, edges):
    m = len(edges)
    neighborhoods = [0]*(n+m)
    for j,(u,v) in enumerate(edges):
        p = n+j
        neighborhoods[u] |= 1 << p
        neighborhoods[v] |= 1 << p
        neighborhoods[p] |= (1 << u) | (1 << v)
    full = (1 << (n+m)) - 1
    out = Counter()
    for s in range(1 << (n+m)):
        rem = s
        independent = True
        dom = s
        while rem:
            low = rem & -rem
            v = low.bit_length()-1
            if neighborhoods[v] & s:
                independent = False
                break
            dom |= neighborhoods[v]
            rem -= low
        if independent and dom == full:
            out[s.bit_count()] += 1
    return +out, 1 << (n+m)

def induced_matching_number(n, edges):
    ans=0
    m = len(edges)
    for s in range(1<<m):
        k=s.bit_count()
        if k<=ans: continue
        vertices=0
        disjoint=True
        for j,(u,v) in enumerate(edges):
            if (s>>j)&1:
                uv=(1<<u)|(1<<v)
                if uv & vertices:
                    disjoint=False
                    break
                vertices |= uv
        if disjoint and sum(((vertices>>u)&1) and ((vertices>>v)&1) for u,v in edges)==k:
            ans=k
    return ans

def multiply(a,b):
    out=Counter()
    for e,c in a.items():
        for f,d in b.items():out[e+f]+=c*d
    return +out

def add(a,b):
    out=Counter(a)
    for e,c in b.items():out[e]+=c
    return +out

def sub(a,b):
    out=Counter(a)
    for e,c in b.items():out[e]-=c
    return +out

def forest_dp(n, edges):
    nbr=[[] for _ in range(n)]
    for u,v in edges:nbr[u].append(v); nbr[v].append(u)
    seen=set()
    def dfs(v,p):
        seen.add(v)
        a={0:1}; prod_all={0:1}; prod_none={0:1}
        for u in nbr[v]:
            if u==p:continue
            assert u not in seen, 'Not a forest'
            au,bu,cu=dfs(u,v)
            a=multiply(a,add(au,bu))
            prod_none=multiply(prod_none,au)
            joined={e+1:k for e,k in add(bu,cu).items()}
            prod_all=multiply(prod_all,add(au,joined))
        b={e-1:k for e,k in sub(prod_all,prod_none).items() if k}
        c={e-1:k for e,k in prod_none.items()}
        return +Counter(a),+Counter(b),+Counter(c)
    res={0:1}
    for r in range(n):
        if r not in seen:
            a,b,c=dfs(r,-1)
            res=multiply(res,add(a,b))
    return +Counter({e+n:k for e,k in res.items()})

def run():
    count=0; subsets=0
    for n in range(0,6):
        for mask in range(1 << (n*(n-1)//2)):
            edges=edges_of(n,mask)
            predicted=formula_poly(n,edges)
            direct,ns=direct_poly(n,edges)
            assert predicted==direct,(n,edges,predicted,direct)
            im=induced_matching_number(n,edges)
            assert min(predicted)==n-im,(n,edges,predicted,im)
            count+=1;subsets+=ns
    print('All labeled simple graphs n=0,...,5: ',count,'base graphs,',subsets,'direct vertex subsets checked',flush=True)
    rng=random.Random(271828)
    count6=0;subsets6=0
    for n in (6,7):
        for trial in range(90 if n==6 else 30):
            p=rng.choice([.15,.24,.33,.40])
            edges=[uv for uv in combinations(range(n),2) if rng.random()<p]
            if n+len(edges)>19:continue
            predicted=formula_poly(n,edges)
            direct,ns=direct_poly(n,edges)
            assert predicted==direct,(n,edges)
            im=induced_matching_number(n,edges)
            assert min(predicted)==n-im,(n,edges,predicted,im)
            count6+=1;subsets6+=ns
    print('Random graphs n=6,7: ',count6,'base graphs,',subsets6,'direct vertex subsets checked',flush=True)
    try:
        import networkx as nx
        f_count=0; f_subsets=0
        for n in range(1,11):
            trees=[nx.empty_graph(1)] if n==1 else list(nx.nonisomorphic_trees(n))
            for T in trees:
                edges=list(T.edges())
                poly=formula_poly(n,edges)
                dpoly=forest_dp(n,edges)
                assert poly==dpoly,(n,edges,poly,dpoly)
                f_count+=1;f_subsets+=1<<n
        print('Nonisomorphic trees n=1,...,10: ',f_count,'trees,',f_subsets,'base vertex subsets checked; recurrence agrees',flush=True)
        f_count=0
        for n in range(1,9):
            for trial in range(80):
                # random forest by deleting edges in a random labeled tree
                T=nx.random_labeled_tree(n,seed=rng.randrange(10**9)) if n>=2 else nx.empty_graph(1)
                edges=[e for e in T.edges() if rng.random()<.7]
                assert formula_poly(n,edges)==forest_dp(n,edges)
                f_count+=1
        print('Random forests n=1,...,8: ',f_count,'recurrence checks',flush=True)
    except ImportError:
        print('Optional networkx absent; tree tests skipped',flush=True)
    # The ladder example is relevant to an explicit published comparison.
    rungs=3
    edges=[(i,i+1) for i in range(rungs-1)]+[(rungs+i,rungs+i+1) for i in range(rungs-1)]+[(i,rungs+i) for i in range(rungs)]
    lp,steps=direct_poly(2*rungs,edges)
    assert lp==formula_poly(2*rungs,edges)
    assert min(lp)==4 and lp[4]==1
    print('Ladder L_3: independent domination polynomial of full subdivision=',sorted(lp.items()),'direct subsets=',steps,flush=True)
    for n,edges in [(3,[(0,1),(1,2)]),(4,[(0,1),(1,2),(2,3),(3,0)]),(4,[(0,1),(0,2),(0,3)]),(5,list(combinations(range(5),2)))]:
        print('sample n=',n,'m=',len(edges),'polynomial coefficients=',sorted(formula_poly(n,edges).items()),'induced matching=',induced_matching_number(n,edges))
    print('ALL TESTS PASSED')

if __name__=='__main__':run()
