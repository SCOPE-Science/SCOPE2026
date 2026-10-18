"""Independent small-order test of the matching-pair C2 fibre and its orbit stratification."""
from itertools import combinations
from collections import defaultdict,Counter
import networkx as nx

def matchings(vertices):
    if not vertices:
        yield ();return
    x,*others=vertices
    for y in others:
        rem=tuple(z for z in others if z!=y)
        for rest in matchings(rem):yield ((x,y),)+rest

def incidence_graph(E,F):
    # vertex side labels distinguish E and F, edge objects are ground-set points
    b=nx.Graph(); ep={j:i for i,p in enumerate(E) for j in p};fp={j:i for i,p in enumerate(F) for j in p}
    for i in range(len(E)):b.add_node(('E',i),side='E');b.add_node(('F',i),side='F')
    for x in range(2*len(E)):
        a=('E',ep[x]);c=('F',fp[x]);assert not b.has_edge(a,c)
        b.add_edge(a,c)
    return b

def class_color(E,F):
    n=2*len(E)
    a={z:i for i,p in enumerate(E) for z in p};b={z:i for i,p in enumerate(F) for z in p}
    # first-round C2 atomic edge counts, including equality
    return tuple(sorted(Counter((sum(a[x]==a[y] and b[x]==b[y] for y in range(n)),sum(a[x]==a[y] and b[x]!=b[y] for y in range(n)),sum(a[x]!=a[y] and b[x]==b[y] for y in range(n)),sum(a[x]!=a[y] and b[x]!=b[y] for y in range(n))) for x in range(n)).items()))

def parts(n):
    p=[0]*(n+1);p[0]=1
    for k in range(1,n+1):
        for i in range(k,n+1):p[i]+=p[i-k]
    return p[n]

def main():
    for n in (4,6,8):
        E=tuple((2*j,2*j+1) for j in range(n//2));eg={frozenset(p) for p in E};buckets=[];signatures=set();graphs=[]
        for F in matchings(tuple(range(n))):
            if any(frozenset(p) in eg for p in F):continue
            H=incidence_graph(E,F);d=Counter(len(c)//2 for c in nx.connected_components(H));signature=tuple(sorted(d.elements()));signatures.add(signature)
            if not any(nx.is_isomorphic(H,G,node_match=lambda a,b:a['side']==b['side']) for G in graphs):graphs.append(H)
            assert len(class_color(E,F))==1
        target=parts(n//2)-parts(n//2-1)
        assert len(graphs)==len(signatures)==target,(n,len(graphs),len(signatures),target)
        print(f'n={n}: isomorphism types={len(graphs)}, partition-types={len(signatures)}; all first-round C2 single-color',flush=True)
    for t in range(2,101):
        n=2*t
        best=int(((4*n+9)**0.5-3)/2)
        assert best*(best+3)//2<=t
        assert (best+1)*(best+4)//2>t
    print('PASS: independent side-preserving graph isomorphism through n=8 and arithmetic extremum through n=200')
if __name__=='__main__':main()
