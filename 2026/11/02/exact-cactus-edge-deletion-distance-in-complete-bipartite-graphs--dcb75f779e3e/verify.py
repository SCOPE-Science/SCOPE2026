#!/usr/bin/env python3
"""Direct finite checks for maximum spanning cacti of complete bipartite graphs.

Uses only the Python standard library. Run: python3 verify.py
"""


def max_cycle_formula(p, q):
    return min(p-1, q-1, (p+q-1)//3)


def constructive_cactus(p, q):
    """Return a spanning connected cactus with the proposed maximum edges."""
    k = max_cycle_formula(p, q)
    if k == 0:
        return [(0, p+j) for j in range(q)] if p == 1 else [(i, p) for i in range(p)]
    x = max(0, 2*k-p)
    assert 0 <= x <= min(k-1, q-k-1)
    y = k-1-x
    a_next, b_next = 2, 2
    edges = []

    def edge(a, b):
        assert 0 <= a < p and 0 <= b < q
        edges.append((a, p+b))

    edge(0,0); edge(1,0); edge(1,1); edge(0,1)
    for _ in range(x):
        a = a_next; a_next += 1
        u,v = b_next,b_next+1; b_next+=2
        edge(0,u); edge(a,u); edge(a,v); edge(0,v)
    for _ in range(y):
        a,b = a_next,a_next+1; a_next+=2
        v = b_next; b_next+=1
        edge(a,0); edge(a,v); edge(b,v); edge(b,0)
    for i in range(a_next,p):
        edge(i,0)
    for j in range(b_next,q):
        edge(0,j)
    assert len(edges)==len(set(edges))
    return edges


def is_connected_cactus(n, edges):
    if n == 1:
        return not edges
    g = [[] for _ in range(n)]
    for eid,(u,v) in enumerate(edges):
        assert u != v
        g[u].append((v,eid))
        g[v].append((u,eid))
    discovery = [-1]*n
    low = [0]*n
    estack = []
    blocks=[]
    timer=0

    def dfs(u, parent_edge=-1):
        nonlocal timer
        discovery[u]=low[u]=timer
        timer+=1
        for v,eid in g[u]:
            if eid == parent_edge:
                continue
            if discovery[v]<0:
                estack.append(eid)
                dfs(v,eid)
                low[u]=min(low[u],low[v])
                if low[v] >= discovery[u]:
                    block=[]
                    while True:
                        e=estack.pop()
                        block.append(e)
                        if e==eid:break
                    blocks.append(block)
            elif discovery[v] < discovery[u]:
                low[u]=min(low[u],discovery[v])
                estack.append(eid)
    dfs(0)
    if any(t<0 for t in discovery):
        return False
    for block in blocks:
        if len(block)==1:
            continue
        deg={}
        for eid in block:
            u,v=edges[eid]
            deg[u]=deg.get(u,0)+1
            deg[v]=deg.get(v,0)+1
        if len(block)!=len(deg) or any(d!=2 for d in deg.values()):
            return False
    return True


def brute_optimum(p, q):
    all_edges=[(i,p+j) for i in range(p) for j in range(q)]
    M=len(all_edges)
    optimum=-1
    maximizers=0
    for mask in range(1<<M):
        count=mask.bit_count()
        if count<optimum:
            continue
        edges=[all_edges[i] for i in range(M) if mask&(1<<i)]
        if is_connected_cactus(p+q,edges):
            if count>optimum:
                optimum=count
                maximizers=0
            maximizers+=1
    return optimum,maximizers


def main():
    table=[(p,q) for p in range(1,5) for q in range(1,5)]
    table += [(2,5),(2,6),(3,5),(2,7)]
    total=0
    for p,q in table:
        result,count=brute_optimum(p,q)
        prediction=p+q-1+max_cycle_formula(p,q)
        assert result==prediction,(p,q,result,prediction)
        total+=1<< (p*q)
        print('BRUTE_ALL_EDGE_SUBSETS_OK',p,q,result,count,1<<(p*q))
    for p in range(1,31):
        for q in range(1,31):
            witness=constructive_cactus(p,q)
            assert len(witness)==p+q-1+max_cycle_formula(p,q)
            assert is_connected_cactus(p+q,witness), (p,q)
    print('CONSTRUCTIVE_CACTI_OK',30*30,'PARAMETER_PAIRS')
    print('DIRECT_EXHAUSTIVE_CHECKS_OK',len(table),'PARAMETER_PAIRS',total,'EDGE_SUBSETS')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
