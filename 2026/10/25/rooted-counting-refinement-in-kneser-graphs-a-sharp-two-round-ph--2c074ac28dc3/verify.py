"""Independent finite tests of anchored Kneser graph counting refinement.
Standard library only. Counts are exact integers. Not a substitute for the proof.
"""
from itertools import combinations
from math import comb


def c(n,r):
    return comb(n,r) if 0 <= r <= n else 0


def quotient(n,k):
    m=n-2*k
    return [[c(k-t,u)*c(m+t,k-u) for u in range(k+1)] for t in range(k+1)]


def refine_quotient(n,k):
    B=quotient(n,k)
    col=[0]*k+[1]
    stages=[tuple(col)]
    for step in range(k+4):
        palette=sorted(set(col))
        keys=[(col[t], tuple(sum(B[t][u] for u in range(k+1) if col[u]==z) for z in palette)) for t in range(k+1)]
        dictionary={key:i for i,key in enumerate(sorted(set(keys)))}
        nxt=[dictionary[key] for key in keys]
        if len(set(nxt))==len(set(col)):
            break
        col=nxt
        stages.append(tuple(col))
    return stages


def full_refine(n,k):
    nodes=[frozenset(t) for t in combinations(range(n),k)]
    index={v:i for i,v in enumerate(nodes)}
    nbrs=[[j for j,w in enumerate(nodes) if not v & w] for v in nodes]
    anchor=frozenset(range(k))
    colors=[1 if v==anchor else 0 for v in nodes]
    rounds=0
    while True:
        values=[(colors[i],tuple(sorted(colors[j] for j in nbrs[i]))) for i in range(len(nodes))]
        lookup={v:i for i,v in enumerate(sorted(set(values)))}
        updated=[lookup[v] for v in values]
        if len(set(updated))==len(set(colors)):
            return rounds,nodes,colors
        colors=updated
        rounds+=1


def grouped(values):
    return {tuple(i for i,v in enumerate(values) if v==c) for c in set(values)}


def run():
    quot=0
    for k in range(1,16):
        for n in range(2*k+1, 4*k+4):
            stages=refine_quotient(n,k)
            depth=len(stages)-1
            assert len(set(stages[-1]))==k+1,(n,k,'not separated')
            assert depth<=k,(n,k,'upper bound')
            if n==2*k+1:
                assert depth==k-1,(n,k,'odd depth',depth)
            if k>=3:
                assert (depth==2)==(n>=3*k-2),(n,k,'two-round threshold',depth)
            if k==2:
                assert depth==1
            if k==1:
                assert depth==0
            quot+=1
    boundary=0
    for k in range(2,13):
        stages=refine_quotient(2*k,k)
        assert len(set(stages[-1]))==(3 if k>=2 else 2)
        boundary+=1
    exhaustive=0
    sizes=[]
    for k,n in [(1,4),(2,5),(2,8),(3,7),(3,8),(3,10),(4,9),(4,10),(4,12),(5,11)]:
        d,nodes,colors=full_refine(n,k)
        dq=len(refine_quotient(n,k))-1
        assert d==dq,(n,k,d,dq)
        root=frozenset(range(k))
        groups_by_t={t:tuple(i for i,v in enumerate(nodes) if len(v & root)==t) for t in range(k+1)}
        assert grouped(colors)==set(groups_by_t.values()),(n,k,'orbit classes')
        for t in range(k+1):
            assert len(groups_by_t[t])==c(k,t)*c(n-k,k-t)
        exhaustive+=1
        sizes.append([n,k,len(nodes),d])
    print('QUOTIENT_CHECKS',quot)
    print('BOUNDARY_MATCHING_CHECKS',boundary)
    print('FULL_GRAPH_CHECKS',exhaustive)
    print('FULL_GRAPH_CASES n,k,vertices,rounds:',sizes)
    print('ALL_TESTS_PASS')
if __name__=='__main__':
    run()
