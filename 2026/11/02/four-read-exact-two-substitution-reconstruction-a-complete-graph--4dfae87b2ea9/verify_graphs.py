"""Independent graph criterion and motif-count verification, standard library."""
from itertools import combinations
from math import comb

def predicted(n):
    return 10*comb(n,5)+180*comb(n,6)+315*comb(n,7)+105*comb(n,8)+(5 if n==5 else 0)

def signature(n,edges):
    vertices=set().union(*[set(edge) for edge in edges]); counts=[sum(v in edge for edge in edges) for v in vertices]
    return tuple(sorted(counts,reverse=True)),len(vertices)

def unique_from_graph(n,edges):
    vertices=set().union(*[set(e) for e in edges])
    if len(vertices)<=4: return False
    for D in combinations(range(n),2):
        if all(len(set(D).intersection(e))==1 for e in edges):return False
    return True

for n in range(5,10):
    edges=list(combinations(range(n),2)); total=0
    by_union={};by_signature={}
    for rows in combinations(edges,4):
        if unique_from_graph(n,rows):
            total+=1
            sig,v=signature(n,rows)
            by_union[v]=by_union.get(v,0)+1
            by_signature[(v,sig)]=by_signature.get((v,sig),0)+1
    print(f'n={n}; graph_uniques={total}; expected={predicted(n)}; by_union={dict(sorted(by_union.items()))}')
    assert total==predicted(n)
    expected_union={5:10*comb(n,5)+(5 if n==5 else 0),6:180*comb(n,6),7:315*comb(n,7),8:105*comb(n,8)}
    assert all(by_union.get(k,0)==v for k,v in expected_union.items())
print('VERIFY_GRAPH_MOTIFS_OK')
