"""Independent face and mod-two boundary-matrix check for short square sequences.

Run: python square4_homology.py
Requires networkx (no dependency on companion checker).
"""
import itertools
from collections import defaultdict,Counter
import networkx as nx


def next_graphs(g):
    N=len(g)
    for x,y in g.edges:
        h=nx.Graph(g)
        h.add_edges_from([(x,N),(N,N+1),(N+1,y)])
        yield h
    for center in g:
        for x,y in itertools.combinations(list(g[center]),2):
            h=nx.Graph(g)
            h.add_edges_from([(x,N),(N,y)])
            yield h


def mod2rank(cols):
    pivots={}
    for col in cols:
        v=col
        while v:
            p=v.bit_length()-1
            if p not in pivots:
                pivots[p]=v
                break
            v^=pivots[p]
    return len(pivots)


def betti(g):
    N=len(g)
    nonadj=[[not g.has_edge(i,j) for j in range(N)] for i in range(N)]
    dfaces=defaultdict(list)
    for mask in range(1,1<<N):
        chosen=[i for i in range(N) if mask>>i&1]
        valid=True
        for comb in itertools.combinations(chosen,4):
            if all(nonadj[x][y] for x,y in itertools.combinations(comb,2)):
                valid=False
                break
        if valid:dfaces[len(chosen)-1].append(mask)
    ranks={}
    for d in range(1,max(dfaces)+1):
        row_index={f:j for j,f in enumerate(dfaces[d-1])}
        cols=[]
        for mask in dfaces[d]:
            parity=0
            for i in range(N):
                if mask>>i&1:
                    parity^=1<<row_index[mask^(1<<i)]
            cols.append(parity)
        ranks[d]=mod2rank(cols)
    answer={}
    for d,ls in dfaces.items():
        dimension=len(ls)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)
        if dimension:answer[d]=dimension
    return answer


def main():
    graphs=[nx.cycle_graph(4)]
    counts=[]
    for n in range(1,5):
        if n>1:
            candidates=[h for g in graphs for h in next_graphs(g)]
            classes=[]
            for h in candidates:
                if not any(nx.is_isomorphic(h,k) for k in classes):classes.append(h)
            graphs=classes
        summary=Counter()
        for graph in graphs:
            b=betti(graph)
            assert set(b).issubset({5}), (n,b)
            summary[(len(graph),b.get(5,0))]+=1
        counts.append(dict(summary))
        print('squares',n,'classes',len(graphs),'mod2_by_(vertices,beta5)',sorted((v,r,k) for (v,r),k in summary.items()),flush=True)
    assert [sum(x.values()) for x in counts]==[1,2,7,29]
    assert counts[3]=={(7,0):3,(8,0):4,(8,1):4,(9,2):7,(9,3):2,(9,4):1,(10,4):8}
    print('PASS independent construction and full mod-two homology in all degrees for 39 graph types')

if __name__=='__main__':main()
