#!/usr/bin/env python3
"""Standalone finite checks for a Hamming-Rips coordinate-swap fixed complex.

Uses Python's standard library only. The theorem for all alphabets is established
by the accompanying argument, not by these finite tests.
"""
from itertools import combinations
from math import comb


def orbit_vertices(q):
    return ([('A', a, c) for a in range(q) for c in range(q)] +
            [('B', a, b, c) for c in range(q) for a in range(q)
             for b in range(a+1, q)])


def orbit(v):
    if v[0] == 'A':
        _, a, c = v
        return ((a, a, c),)
    _, a, b, c = v
    return ((a, b, c), (b, a, c))


def pair_ok(x, y):
    return all(sum(i != j for i, j in zip(a, b)) <= 2
               for a in orbit(x) for b in orbit(y))


def direct_graph(q):
    verts = orbit_vertices(q)
    links = [set() for _ in verts]
    for i, j in combinations(range(len(verts)), 2):
        if pair_ok(verts[i], verts[j]):
            links[i].add(j)
            links[j].add(i)
    return verts, links


def maximal_cliques(links):
    output=[]
    def bk(R,P,X):
        if not P and not X:
            output.append(frozenset(R)); return
        pivot=max(P|X,key=lambda u:len(P&links[u])) if P|X else None
        for v in list(P-(links[pivot] if pivot is not None else set())):
            bk(R|{v}, P&links[v], X&links[v]);P.remove(v);X.add(v)
    bk(set(),set(range(len(links))),set())
    return set(output)


def predicted_facets(q, verts):
    idx={v:i for i,v in enumerate(verts)}
    faces=[]
    # All orbit vertices supported on the third coordinate c, plus its fixed row.
    for c in range(q):
        faces.append([('A',a,c) for a in range(q)] +
                     [('B',a,b,c) for a in range(q) for b in range(a+1,q)])
    # The fixed column with all two-point orbits incident to symbol a.
    for a in range(q):
        for c in range(q):
            faces.append([('A',a,d) for d in range(q)] +
                         [('B',min(a,b),max(a,b),c)
                          for b in range(q) if b!=a])
    # The genuinely new attaching triangles.
    for c in range(q):
        for d in range(q):
            if c==d:continue
            for a,b in combinations(range(q),2):
                faces.append([('B',a,b,c),('A',a,d),('A',b,d)])
    return {frozenset(idx[v] for v in face) for face in faces}


def betti_mod_two(maxcliques):
    dim=max(map(len,maxcliques))
    faces=[set() for _ in range(dim)]
    for F in maxcliques:
        for k in range(1,len(F)+1):
            faces[k-1].update(combinations(sorted(F),k))
    indices=[{f:i for i,f in enumerate(sorted(F))} for F in faces]
    ranks=[]
    for k in range(1,len(faces)):
        lower=indices[k-1]
        pivots={}
        for face in faces[k]:
            mask=0
            for sub in combinations(face,len(face)-1):
                mask ^= 1<<lower[sub]
            while mask:
                bit=mask.bit_length()-1
                if bit in pivots:mask^=pivots[bit]
                else:pivots[bit]=mask;break
        ranks.append(len(pivots))
    return [len(faces[k]) - (ranks[k-1] if k else 0) -
            (ranks[k] if k<len(ranks) else 0) - (1 if k==0 else 0)
            for k in range(len(faces))]



def run():
    for q in range(2,6):
        vs,adj=direct_graph(q)
        actual=maximal_cliques(adj)
        expected=predicted_facets(q,vs)
        assert actual==expected,(q,len(actual-expected),len(expected-actual))
        n=q*(q-1)*comb(q,2)
        beta2=n-(q-1)**2
        assert len(actual)==q+q*q+n,(q,len(actual))
        if q<=4:
            bet=betti_mod_two(actual)
            assert bet[0]==0 and bet[1]==0 and bet[2]==beta2 and all(x==0 for x in bet[3:]),(q,bet)
            print('q=%d vertices=%d facets=%d mod2_betti2=%d other_reduced_betti=0 PASS' %
                  (q,len(vs),len(actual),beta2))
        else:
            print('q=%d vertices=%d facets=%d exact_facet_check=PASS predicted_betti2=%d (not calculated)' %
                  (q,len(vs),len(actual),beta2))
    print('All checks passed. Finite cases do not prove the all-q statement.')

if __name__=='__main__':
    run()
