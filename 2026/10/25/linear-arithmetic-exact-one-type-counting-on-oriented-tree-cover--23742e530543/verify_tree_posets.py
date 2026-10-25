"""Independent exhaustive enumeration for one-point extensions of tree-cover posets.

Run: python verify_tree_posets.py
All inputs are finite directed covers with an undirected tree as their support.
"""
from itertools import product
from random import Random


def theorem_count(n, arcs):
    lower=[[] for _ in range(n)]
    upper=[[] for _ in range(n)]
    neighbors=[[] for _ in range(n)]
    for u,v in arcs:
        upper[u].append(v)
        lower[v].append(u)
        neighbors[u].append(v)
        neighbors[v].append(u)
    memo_d={}
    memo_u={}
    def down(v):
        if v not in memo_d:
            p=1
            for w in lower[v]: p*=down(w)
            memo_d[v]=1+p
        return memo_d[v]
    def up(v):
        if v not in memo_u:
            p=1
            for w in upper[v]: p*=up(w)
            memo_u[v]=1+p
        return memo_u[v]
    d=[down(v) for v in range(n)]
    u=[up(v) for v in range(n)]
    # Ideal count J(P) by two-state tree DP.
    adj=[[] for _ in range(n)]
    for lo,hi in arcs:
        adj[lo].append((hi,True))
        adj[hi].append((lo,False))
    def visit(v,parent):
        ans=[1,1]
        for w,v_is_lower in adj[v]:
            if w==parent: continue
            child=visit(w,v)
            if v_is_lower:
                # v < w; w included forces v included.
                ans[0]*=child[0]
                ans[1]*=child[0]+child[1]
            else:
                # w < v; v included forces w included.
                ans[0]*=child[0]+child[1]
                ans[1]*=child[1]
        return ans
    states=visit(0,-1)
    ideals=sum(states)
    singleton=sum(z-2 for z in d)
    branching=0
    for v in range(n):
        branch=u[v]-2-sum(u[w]-1 for w in upper[v])
        assert branch >=0,(n,arcs,v,branch)
        branching+=(d[v]-1)*branch
    return 2*ideals-1+singleton+branching, (ideals,singleton,branching)


def direct_count(n, arcs):
    # All directed reachability, recomputed independently from the theorem DP.
    upper=[[] for _ in range(n)]
    for a,b in arcs: upper[a].append(b)
    reach=[[False]*n for _ in range(n)]
    for a in range(n):
        stack=upper[a][:]
        while stack:
            b=stack.pop()
            if not reach[a][b]:
                reach[a][b]=True
                stack.extend(upper[b])
    total=0
    for tags in product(range(3),repeat=n):
        # 0 means old vertex below new; 1 incomparable; 2 above new.
        if any(tags[a]>tags[b] for a,b in arcs):
            continue
        lows=[a for a in range(n) if tags[a]==0]
        highs=[b for b in range(n) if tags[b]==2]
        if all(reach[a][b] for a in lows for b in highs):
            total+=1
    return total


def tree_from_prufer(sequence,n):
    deg=[1]*n
    for v in sequence: deg[v]+=1
    edges=[]
    for v in sequence:
        leaf=next(i for i in range(n) if deg[i]==1)
        edges.append((leaf,v))
        deg[leaf]-=1; deg[v]-=1
    a,b=[i for i in range(n) if deg[i]==1]
    return edges+[(a,b)]


def run():
    examples=[
        ('singleton',1,[]),
        ('chain4',4,[(0,1),(1,2),(2,3)]),
        ('antichain1',1,[]),
        ('N-poset',4,[(0,1),(2,1),(2,3)]),
        ('fork-up-down',5,[(0,2),(1,2),(2,3),(2,4)]),
        ('zigzag6',6,[(0,1),(2,1),(2,3),(4,3),(4,5)])
    ]
    for name,n,arcs in examples:
        fast,components=theorem_count(n,arcs)
        direct=direct_count(n,arcs)
        assert fast==direct,(name,fast,direct)
        print('EXAMPLE',name,n,'count',fast,'terms',components)
    random=Random(613251)
    checked=0
    for n in range(2,7):
        alltrees=product(range(n),repeat=n-2)
        limit={2:5,3:100,4:1000,5:5000,6:500000}[n]
        for pi,prufer in enumerate(alltrees):
            edges=tree_from_prufer(prufer,n)
            for bits in product(range(2),repeat=n-1):
                arcs=[(a,b) if t==0 else (b,a) for (a,b),t in zip(edges,bits)]
                exact,_=theorem_count(n,arcs)
                brute=direct_count(n,arcs)
                assert exact==brute,(n,arcs,exact,brute)
                checked+=1
                if checked>=limit and n==6: break
            if checked>=limit and n==6: break
        print('CHECKED_THROUGH_N',n,checked)
    sampled=0
    for n in range(7,11):
        for _ in range(120):
            prufer=[random.randrange(n) for _ in range(n-2)]
            edges=tree_from_prufer(prufer,n)
            arcs=[(a,b) if random.randrange(2)==0 else (b,a) for a,b in edges]
            exact,_=theorem_count(n,arcs)
            brute=direct_count(n,arcs)
            assert exact==brute,(n,arcs,exact,brute)
            sampled+=1
    print('RANDOM_EXTENDED_CASES',sampled)
    print('ALL_TESTS_PASS')

if __name__=='__main__': run()
