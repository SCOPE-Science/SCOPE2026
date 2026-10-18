"""Independent graph-isomorphism and colour-refinement verification.

Needs networkx >=3. This program does NOT rely on a graph catalogue.
The companion C++ enumerator supplies completeness for the ten-vertex case.
"""
import itertools
import sys
from collections import Counter, defaultdict
from pathlib import Path
import networkx as nx


def graph_from_rows(a,b,rows):
    g=nx.Graph()
    g.add_nodes_from(range(a+b))
    for i,mask in enumerate(rows):
        for j in range(b):
            if mask & (1<<j):
                g.add_edge(i,a+j)
    return g


def refinement(g):
    nodes=list(g)
    c={v:0 for v in nodes}
    for _ in range(len(nodes)):
        signatures={v:(c[v],tuple(sorted(Counter(c[w] for w in g[v]).items()))) for v in nodes}
        palette={signature:k for k,signature in enumerate(sorted(set(signatures.values())))}
        new={v:palette[signatures[v]] for v in nodes}
        if len(set(new.values()))==len(set(c.values())):
            return new
        c=new
    raise AssertionError('Refinement failed to stabilize')


def orbit_classes(g):
    # Complete automorphism enumeration: no color-refinement heuristic involved.
    p=list(g)
    def find(x):
        while p[x]!=x:x=p[x]
        return x
    for permutation in nx.algorithms.isomorphism.GraphMatcher(g,g).isomorphisms_iter():
        for u,v in permutation.items():
            p[find(u)]=find(v)
    groups=defaultdict(set)
    for v in g:groups[find(v)].add(v)
    return sorted((frozenset(s) for s in groups.values()),key=lambda x:min(x))


def is_bad(g):
    colors=refinement(g)
    partition=defaultdict(set)
    for v,c in colors.items():partition[c].add(v)
    # Each equal open-neighbourhood class is a full symmetric automorphism orbit.
    if all(len({frozenset(g[v]) for v in cell})==1 for cell in partition.values()):
        return False
    return set(map(frozenset,partition.values()))!=set(orbit_classes(g))


def reconstruct(a,b,code):
    columns=[(code>>(j*a))&((1<<a)-1) for j in range(b)]
    rows=[sum(1<<j for j in range(b) if columns[j]&(1<<i)) for i in range(a)]
    return rows


def main():
    here=Path(__file__).resolve().parent
    expected=[[25,38,7,56],[28,7,11,19,28]]
    for n in (9,10):
        candidates=[]
        for line in (here/f'candidates{n}.txt').read_text().splitlines():
            a,b,code=map(int,line.split())
            assert a+b==n and a<=b
            g=graph_from_rows(a,b,reconstruct(a,b,code))
            assert nx.is_connected(g) and nx.is_bipartite(g)
            if is_bad(g) and not any(nx.is_isomorphic(g,h) for h in candidates):
                candidates.append(g)
        print('canonical-candidates',n,'checked',len((here/f'candidates{n}.txt').read_text().splitlines()),'bad-isomorphism-types',len(candidates))
        assert len(candidates)==(0 if n==9 else 2)
        if n==10:
            for a,b,rows in [(4,6,expected[0]),(5,5,expected[1])]:
                g=graph_from_rows(a,b,rows)
                assert any(nx.is_isomorphic(g,h) for h in candidates)
                print('witness',a,b,rows,'edges',g.number_of_edges(), 'colour-sizes',sorted(Counter(refinement(g).values()).values()),'orbit-sizes',sorted(map(len,orbit_classes(g))))
    # Independently generate every simple connected bipartite graph representation
    # of orders 1..9 (row permutations suppressed but NOT graph isomorphisms).
    for n in range(1,10):
        evaluated=1 if n==1 else 0
        for a in range(1,n//2+1):
            b=n-a
            for rows in itertools.combinations_with_replacement(range(1,1<<b),a):
                mask=0
                for r in rows:mask |= r
                if mask != (1<<b)-1:continue
                g=graph_from_rows(a,b,rows)
                if not nx.is_connected(g):continue
                evaluated+=1
                assert not is_bad(g),(n,a,b,rows)
        print('independent-full-enumeration',n,evaluated,'bad',0,flush=True)
    print('PASS')


if __name__=='__main__':main()
