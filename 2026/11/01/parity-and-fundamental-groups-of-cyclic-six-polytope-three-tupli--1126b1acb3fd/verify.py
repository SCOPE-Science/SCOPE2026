#!/usr/bin/env python3
"""Reproducible finite checks for the three-tupling of cyclic six-polytope boundaries.
The unbounded parameter range in the accompanying theorem uses the written induction.
No packages beyond the Python standard library are needed.
"""
from itertools import combinations
from math import comb

def facets_matchings(n, is_cycle=True):
    edges=[(i,(i+1)%n) for i in range(n if is_cycle else n-1)]
    out=set()
    for triple in combinations(edges,3):
        six=frozenset(v for edge in triple for v in edge)
        if len(six)==6:
            out.add(tuple(sorted(six)))
    return out

def facets_gale(n):
    """Independently apply the original linear-order Gale evenness criterion."""
    ans=set()
    for six in combinations(range(n),6):
        v=set(six)
        omitted=[j for j in range(n) if j not in v]
        if all(sum(a < s < b for s in six)%2==0
               for a,b in combinations(omitted,2)):
            ans.add(six)
    return ans

def graph(n,cycle=True):
    verts=list(combinations(range(n),3))
    inds={x:i for i,x in enumerate(verts)}
    adj=[set() for x in verts]
    facets=facets_matchings(n,cycle)
    for f in facets:
        for x in combinations(f,3):
            y=tuple(t for t in f if t not in x)
            i,j=inds[x],inds[y]
            adj[i].add(j);adj[j].add(i)
    return verts,adj,facets

def bfs(adj,seed):
    seen={seed};stack=[seed]
    while stack:
        u=stack.pop()
        for w in adj[u]:
            if w not in seen:
                seen.add(w);stack.append(w)
    return seen

def component_profile(verts,adj):
    left=set(range(len(verts))); comps=[]
    while left:
        seen=bfs(adj,min(left))
        assert seen <= left
        left-=seen
        evens={sum(v%2==0 for v in verts[u]) for u in seen}
        comps.append((len(seen),sum(len(adj[u]) for u in seen)//2,tuple(sorted(evens))))
    return sorted(comps)

def main():
    # The two path-base components are checked from their independent parity seeds.
    V, adj, F=graph(8,False)
    assert len(V)==56 and len(F)==10
    assert sum(len(s) for s in adj)//2==100
    A=V.index((0,2,4));B=V.index((0,1,2))
    ca,cb=bfs(adj,A),bfs(adj,B)
    assert ca.isdisjoint(cb) and len(ca)==8 and len(cb)==48
    assert ca|cb==set(range(56))
    assert {sum(V[u][i]%2==0 for i in range(3)) for u in ca}=={0,3}
    assert {sum(V[u][i]%2==0 for i in range(3)) for u in cb}=={1,2}
    print('PATH_BASE_OK n=8 V=56 F=10 E=100 components=(8,48)')
    # The n=7 exceptional cyclic start is checked directly.
    V,adj,F=graph(7,True)
    assert component_profile(V,adj)==[(35,70,(0,1,2,3))]
    assert len(bfs(adj,0))==35 and len(F)==7
    print('CYCLE_BASE_OK n=7 connected V=35 F=7 E=70')
    # Independent facet-level comparison with Gale's criterion, not just counts.
    for n in range(7,17):
        F=facets_matchings(n,True)
        assert F==facets_gale(n),(n,len(F),len(facets_gale(n)))
        assert len(F)==n*(n-4)*(n-5)//6
    print('GALE_OK n=7..16 exact matching-facet equivalence')
    # Finite confirmations of the uniform graph count and parity components.
    for n in range(7,23):
        V,adj,F=graph(n,True)
        f=n*(n-4)*(n-5)//6
        assert len(V)==comb(n,3) and len(F)==f
        assert sum(map(len,adj))==20*f
        p=component_profile(V,adj)
        if n%2:
            assert len(p)==1 and p[0][0]==comb(n,3) and p[0][1]==10*f
            assert 10*f-comb(n,3)+1>=0
        else:
            m=n//2
            ex=[(2*comb(m,3),f,(0,3)),(2*m*comb(m,2),9*f,(1,2))]
            assert p==sorted(ex),(n,p,ex)
            assert f-2*comb(m,3)+1>=0
            assert 9*f-2*m*comb(m,2)+1>=0
    print('CYCLE_FORMULAS_OK n=7..22 exact vertices/edges/component ranks')
    # New-vertex covering lemma for the path extension n -> n+1.
    for n in range(8,29):
        f=facets_matchings(n+1,False)
        covered={tuple(sorted(x)) for face in f for x in combinations(face,3) if n in x}
        expected={x for x in combinations(range(n+1),3) if n in x}
        assert covered==expected
    print('PATH_EXTENSION_OK n=8..28 every new triple lies in a matching facet')
    print('ALL_VERIFY_OK')
if __name__=='__main__':main()
