#!/usr/bin/env python3
"""Independently checks finite non-overlap code certificates using only Python stdlib.
Run: python verify.py [certificates.json]."""
import json,itertools,sys

def rc(w):
    return ''.join('1' if c=='0' else '0' for c in reversed(w))

def conflict(a,b):
    n=len(a)
    return any(a[:j]==b[n-j:] or b[:j]==a[n-j:] for j in range(1,n))

def oriented_words(n):
    return ['0'+''.join(mid)+'1' for mid in itertools.product('01',repeat=n-2)]

def candidates(n):
    # Each candidate is one reverse-complement orbit, whether fixed or paired.
    return sorted({tuple(sorted({w,rc(w)})) for w in oriented_words(n)
                  if not conflict(w,w) and not conflict(w,rc(w))})

def prefix_suffix_check(words):
    if not words:return True
    n=len(words[0]);
    return all(not ({w[:j] for w in words} & {w[-j:] for w in words})
               for j in range(1,n))

def verify(entry):
    n=entry['n'];orbits=candidates(n);m=len(orbits)
    assert m==entry['candidate_orbits']
    edges=set()
    for i in range(m):
        for j in range(i+1,m):
            if any(conflict(a,b) for a in orbits[i] for b in orbits[j]):
                edges.add((i,j))
    assert len(edges)==entry['conflict_edges']
    inds=entry['selected_orbit_indices'];assert inds==sorted(set(inds))
    assert all(type(i) is int and 0<=i<m for i in inds)
    code=[w for i in inds for w in orbits[i]]
    assert all(rc(w) in code for w in code)
    assert prefix_suffix_check(code)
    assert sum(len(orbits[i]) for i in inds)==entry['maximum_codewords']
    # Dual certificate: every conflict clique can contribute at most one orbit
    # to an admissible code. A multicover by cliques that pays each vertex's
    # codeword weight bounds EVERY code by total clique multiplicity.
    cover=[0]*m;cost=0
    for clique,mult in entry['clique_multicover']:
        assert isinstance(mult,int) and mult>=1 and clique==sorted(set(clique))
        assert all(type(i) is int and 0<=i<m for i in clique)
        assert all((min(i,j),max(i,j)) in edges for i,j in itertools.combinations(clique,2))
        for i in clique:cover[i]+=mult
        cost+=mult
    assert all(cover[i]>=len(orbit) for i,orbit in enumerate(orbits))
    assert cost==len(code)==entry['maximum_codewords']
    return code,m,len(edges),cost

def check_all_order():
    # Computational checks supplement, but do not replace, the general proof.
    for k in range(4,60):
        w='0'*k+'110'+'1'*(k-2)
        v=rc(w)
        assert len(w)==2*k+1 and w!=v
        assert prefix_suffix_check((w,v))
    for k in range(1,60):
        w='0'*k+'1'*k
        assert rc(w)==w and not conflict(w,w)

if __name__=='__main__':
    with open(sys.argv[1] if len(sys.argv)>1 else 'certificates.json',encoding='utf8') as fh: data=json.load(fh)
    assert data['schema_version']==1
    assert [e['n'] for e in data['entries']]==list(range(2,17))
    totals=[]
    for e in data['entries']:
        code,m,edges,cost=verify(e)
        totals.append((e['n'],m,edges,cost))
    check_all_order()
    assert [x[3] for x in totals]==[1,0,1,0,2,0,5,2,14,10,42,44,132,170,430]
    print('VERIFY_OK lengths=2..16 candidates_and_edges_rebuilt=yes primal_nonoverlap_and_RC=yes integral_clique_multicovers=yes sharp_maxima='+','.join(f'{n}:{v}' for n,_,_,v in totals)+' odd_length_existence_construction_k=4..59 even_length_fixed_words_k=1..59')
