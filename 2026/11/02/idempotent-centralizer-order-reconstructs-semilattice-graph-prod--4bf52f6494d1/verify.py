"""Finite checks for centralizers of idempotents in graph products of two-point semilattices.
Run with Python 3 (standard library only). This is a finite test, not a proof of general statements.
"""
from functools import lru_cache
from itertools import combinations, product

@lru_cache(maxsize=None)
def normal(word, n, edges):
    """Shuffle-independent Foata layers after deleting commuting-separated repetitions."""
    w = list(word)
    while True:
        hit = False
        for i in range(len(w)):
            for j in range(i+1, len(w)):
                if w[i] == w[j] and all((min(w[i], t), max(w[i], t)) in edges for t in w[i+1:j]):
                    del w[j]
                    hit = True
                    break
            if hit: break
        if not hit: break
    rem = list(range(len(w)))
    layers = []
    while rem:
        minima = [i for i in rem if all(i <= j or (min(w[i],w[j]),max(w[i],w[j])) in edges for j in rem)]
        assert minima
        layers.append(tuple(sorted(w[i] for i in minima)))
        rem = [i for i in rem if i not in minima]
    return tuple(layers)

def flatten(x):
    return tuple(a for layer in x for a in layer)

def mult(x,y,n,edges):
    return normal(flatten(x)+flatten(y),n,edges)

def supp(x):
    return frozenset(flatten(x))

def clique(S,edges):
    return all((min(a,b),max(a,b)) in edges for a,b in combinations(S,2))

def verify_graph(n, edges, max_length):
    vertices = tuple(range(n))
    es = frozenset(edges)
    cliques = [frozenset(v for v in vertices if mask & (1<<v)) for mask in range(1<<n)]
    cliques = [s for s in cliques if clique(s, es)]
    e = {s:normal(tuple(sorted(s)),n,es) for s in cliques}
    elements = {normal(w,n,es) for l in range(max_length+1) for w in product(vertices,repeat=l)}
    univ = frozenset(v for v in vertices if all(v==u or (min(u,v),max(u,v)) in es for u in vertices))
    for w in elements:
        A = supp(w)
        assert (mult(w,w,n,es)==w) == clique(A,es), ('idempotence',n,es,w)
        assert all(mult(w,e[frozenset((v,))],n,es)==mult(e[frozenset((v,))],w,n,es) for v in vertices) == (A<=univ), ('center',n,es,w)
        for S in cliques:
            x=e[S]
            cm=mult(w,x,n,es)==mult(x,w,n,es)
            inter=all(mult(w,e[frozenset((s,))],n,es)==mult(e[frozenset((s,))],w,n,es) for s in S)
            T=A&S
            wt=all(all((min(v,s),max(v,s)) in es for s in S-T) for v in A-S) \
                and mult(w,e[T],n,es)==w and mult(e[T],w,n,es)==w
            assert cm == inter == wt, ('centralizer',n,es,S,w,cm,inter,wt)
    # Test the exact witness for every asserted noninclusion of centralizers.
    for S in cliques:
        for T in cliques:
            predicted = (T-S)<=univ
            if not predicted:
                t=next(t for t in T-S if t not in univ)
                b=next(b for b in vertices if b!=t and (min(b,t),max(b,t)) not in es)
                witness=mult(mult(e[S],e[frozenset((b,))],n,es),e[S],n,es)
                assert mult(witness,e[S],n,es)==mult(e[S],witness,n,es)
                assert mult(witness,e[T],n,es)!=mult(e[T],witness,n,es)
            else:
                # Generator tests together with the proved intersection mechanism
                # establish sufficiency; finite sampling below probes it directly.
                assert all((mult(w,e[S],n,es)!=mult(e[S],w,n,es)) or \
                           mult(w,e[T],n,es)==mult(e[T],w,n,es) for w in elements)
    return len(elements),len(cliques)

def main():
    tested=0; elems=0
    for n in (1,2,3,4):
        pairs=list(combinations(range(n),2))
        length={1:6,2:6,3:6,4:5}[n]
        for m in range(1<<len(pairs)):
            edges=frozenset(p for i,p in enumerate(pairs) if m&(1<<i))
            num,ns=verify_graph(n,edges,length)
            tested+=1; elems+=num
            if n==4 and m%16==15: print('CHECKPOINT',n,m+1,'graphs tested')
    print('VERIFY_OK: %d graphs; %d normal forms inspected' % (tested,elems))

if __name__=='__main__': main()
