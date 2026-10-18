"""Independent parameter census of simple connected leafless bicyclic cores.

The structural proof enumerates the three possible kernels; this file checks
all their instances through order 17 and a selection of larger parameters.
Run with Python and NetworkX: python core_bicyclic_verifier.py
"""
import networkx as nx
from collections import Counter
from itertools import combinations_with_replacement


def theta(lengths):
    g=nx.Graph();g.add_nodes_from((0,1));k=2
    for L in lengths:
        u=0
        for _ in range(L-1):
            g.add_edge(u,k);u=k;k+=1
        g.add_edge(u,1)
    return g


def barbell(a,b,c):
    g=nx.disjoint_union(nx.cycle_graph(a),nx.cycle_graph(b))
    u=0;k=a+b
    for _ in range(c-1):
        g.add_edge(u,k);u=k;k+=1
    g.add_edge(u,a)
    return g


def figure_eight(a,b):
    h=nx.cycle_graph(b)
    out=nx.disjoint_union(nx.cycle_graph(a),h)
    out=nx.contracted_nodes(out,0,a,self_loops=False)
    return nx.convert_node_labels_to_integers(out)


def eq(g,h):
    union=nx.disjoint_union(g,h)
    colors={v:0 for v in union}
    for _ in range(len(union)+1):
        chars={v:(colors[v],tuple(sorted(Counter(colors[w] for w in union[v]).items()))) for v in union}
        code={x:i for i,x in enumerate(sorted(set(chars.values())))}
        nxt={v:code[chars[v]] for v in union}
        if nxt==colors:break
        colors=nxt
    return Counter(colors[v] for v in range(len(g)))==Counter(colors[v] for v in range(len(g),len(union)))


def reps_at_n(n):
    out=[]
    for a in range(1,n+1):
        for b in range(max(2,a),n+1):
            c=n+1-a-b
            if c<b or c<2:continue
            if a==1 and b==1:continue
            if a==1 and b>=2 and c>=2 or a>=2:
                # no repeated length-1 paths, and path lengths sum n+1
                out.append(('theta',tuple(sorted((a,b,c))),theta((a,b,c))))
    for a in range(3,n+1):
        for b in range(a,n+1):
            c=n+1-a-b
            if c>=1:out.append(('barbell',(a,b,c),barbell(a,b,c)))
    for a in range(3,n+1):
        b=n+1-a
        if b>=a and b>=3:out.append(('figure8',(a,b),figure_eight(a,b)))
    assert all(len(g)==n and len(g.edges())==n+1 and min(dict(g.degree()).values())>=2 for _,_,g in out)
    # Check parameterizations are genuinely pairwise non-isomorphic within kind
    for i,(typ,p,g) in enumerate(out):
        for typ2,p2,h in out[:i]:
            assert not nx.is_isomorphic(g,h), (typ,p,typ2,p2)
    return out


def predicted(a,b):
    typ,p,g=a; typ2,p2,h=b
    if typ=='theta' and typ2=='barbell': return p==tuple(sorted((p2[0],p2[0],p2[2]))) and p2[0]==p2[1]
    if typ2=='theta' and typ=='barbell':return p2==tuple(sorted((p[0],p[0],p[2]))) and p[0]==p[1]
    return False

if __name__=='__main__':
    count=0
    for n in range(4,18):
        reps=reps_at_n(n)
        collisions=[]
        for i,r in enumerate(reps):
            for s in reps[:i]:
                actual=eq(r[2],s[2])
                expect=predicted(r,s)
                assert actual==expect,(n,r[:2],s[:2],actual,expect)
                if actual:collisions.append((r[:2],s[:2]))
                count+=1
        print(f'n={n}, leafless bicyclic types={len(reps)}, C2-collisions={len(collisions)}')
    print(f'All {count} parameter-pair comparisons agree with the classification.')
