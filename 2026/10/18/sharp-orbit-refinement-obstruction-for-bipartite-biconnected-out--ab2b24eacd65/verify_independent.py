"""Second certificate: combination enumeration and NetworkX exact isomorphisms.
Not dependent on the first verifier's canonicalization or orbit computations.
"""
from itertools import combinations
from collections import Counter,defaultdict
import networkx as nx

def possible(n):
    return [(a,b) for a in range(n) for b in range(a+2,n)
            if (b-a)%2 and not (a==0 and b==n-1)]

def legal(es):
    for (a,b),(c,d) in combinations(es,2):
        if len({a,b,c,d})<4:continue
        if (a<c<b) != (a<d<b):return False
    return True

def make_graph(n,es):
    g=nx.cycle_graph(n)
    g.add_edges_from(es)
    return g

def equitable(g):
    cols={v:0 for v in g}
    while True:
        sig={v:(cols[v],tuple(sorted(Counter(cols[w] for w in g[v]).items()))) for v in g}
        key={s:i for i,s in enumerate(sorted(set(sig.values())))}
        new={v:key[sig[v]] for v in g}
        if len(set(new.values()))==len(set(cols.values())):return new
        cols=new

def independent_orbits(g):
    gm=nx.algorithms.isomorphism.GraphMatcher(g,g)
    components={u:{u} for u in g}
    for iso in gm.isomorphisms_iter():
        for u,v in iso.items():
            z=components[u]|components[v]
            for w in z:components[w]=z
    return {u:min(components[u]) for u in g}

def main():
    expectations={4:(1,1,0),6:(4,2,0),8:(21,4,0),10:(126,13,0),12:(818,48,1)}
    for n,(label_expected,class_expected,bad_expected) in expectations.items():
        rep=[]; labeled=0;bad=[]
        E=possible(n)
        for count in range(n//2-1):  # 0..n/2-2 chords
            for es in combinations(E,count):
                if not legal(es):continue
                labeled+=1
                g=make_graph(n,es)
                if any(nx.is_isomorphic(g,h) for h in rep):continue
                rep.append(g)
                col=equitable(g);orb=independent_orbits(g)
                if any(col[u]==col[v] and orb[u]!=orb[v]
                       for u in g for v in g):
                    bad.append(tuple(sorted(tuple(sorted(e)) for e in es)))
        print(f'n={n}: combination_labeled={labeled} isomorphism_classes={len(rep)} failures={len(bad)}')
        if bad:print('exception_edge_chords=',bad)
        assert (labeled,len(rep),len(bad))==(label_expected,class_expected,bad_expected)
    print('INDEPENDENT_EXHAUSTIVE_PASS')

if __name__=='__main__':main()
