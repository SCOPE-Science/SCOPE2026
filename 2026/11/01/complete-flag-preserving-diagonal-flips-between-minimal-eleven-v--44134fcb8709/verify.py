#!/usr/bin/env python3
"""Finite verification of flag-preserving diagonal flips on two eleven-vertex flag surfaces.
Requires only the Python standard library. Run beside flag_flip_certificate.json.
"""
import itertools, json
from collections import defaultdict
from pathlib import Path

N=11

def graph6_edges(s):
    nums=[ord(c)-63 for c in s]
    assert nums[0]==N and len(nums)==1+(N*(N-1)//2+5)//6
    bits=[(v>>i)&1 for v in nums[1:] for i in (5,4,3,2,1,0)]
    return {frozenset((a,b)) for (a,b),bit in zip(((i,j) for j in range(1,N) for i in range(j)),bits) if bit}

def triangles(E):
    return {frozenset(x) for x in itertools.combinations(range(N),3) if all(frozenset(y) in E for y in itertools.combinations(x,2))}

def k4(E):
    return [v for v in itertools.combinations(range(N),4) if all(frozenset(y) in E for y in itertools.combinations(v,2))]

def neighbors(E,u):
    return {v for v in range(N) if v!=u and frozenset((u,v)) in E}

def has_cycle_link(E,v):
    A=neighbors(E,v)
    # Link graph is connected and each of its vertices has precisely 2 neighbors.
    L={frozenset((a,b)) for a,b in itertools.combinations(A,2) if frozenset((a,b)) in E}
    if len(A)<3 or len(L)!=len(A) or any(sum(a in f for f in L)!=2 for a in A):return False
    frontier={min(A)}; reached=set(frontier)
    while frontier:
        newer={b for a in frontier for b in A if frozenset((a,b)) in L and b not in reached}
        reached|=newer;frontier=newer
    return reached==A

def iso(E,F,p):
    return sorted(p)==list(range(N)) and {frozenset(p[v] for v in edge) for edge in E}==F

def list_isomorphisms(E,F):
    # Backtracking all graph isomorphisms, matching degrees and adjacencies at every step.
    deg=lambda e,i:len(neighbors(e,i))
    ranks=sorted(range(N),key=lambda v:(-deg(E,v),v))
    groups=defaultdict(list)
    for v in range(N):groups[deg(F,v)].append(v)
    solutions=[]; mapping={};used=set()
    def go(i):
        if i==N:
            solutions.append(tuple(mapping[k] for k in range(N)));return
        u=ranks[i]
        for v in groups[deg(E,u)]:
            if v in used:continue
            if any((frozenset((u,w)) in E)!=(frozenset((v,mapping[w])) in F) for w in mapping):continue
            mapping[u]=v;used.add(v);go(i+1);used.remove(v);del mapping[u]
    go(0)
    return solutions

def main():
    C=json.loads(Path(__file__).with_name('flag_flip_certificate.json').read_text())
    graphsets={name:{frozenset((a,b)) for a,b in itertools.combinations(range(N),2)}-graph6_edges(s) for name,s in C['graph6_complements'].items()}
    assert set(graphsets)=={'G1','G2'}
    counts={};orbits={}
    for name,E in graphsets.items():
        fs=triangles(E)
        assert [N,len(E),len(fs)]==C['f_vectors'][name]==[11,30,20]
        assert not k4(E) and all(has_cycle_link(E,v) for v in range(N))
        assert N-len(E)+len(fs)==1
        observed=[]
        for e in itertools.combinations(range(N),2):
            ab=frozenset(e)
            if ab not in E:continue
            opposite=[v for v in range(N) if ab|{v} in fs]
            assert len(opposite)==2
            c,d=opposite
            assert frozenset((c,d)) not in E
            # Necessary and sufficient for the two-triangle flip to remain flag.
            if neighbors(E,c)&neighbors(E,d)!={*e}:continue
            newE=(E-{ab})|{frozenset((c,d))}
            prescribed=(fs-{ab|{c},ab|{d}})|{frozenset((c,d,e[0])),frozenset((c,d,e[1]))}
            assert triangles(newE)==prescribed and not k4(newE)
            observed.append((tuple(sorted(e)),tuple(sorted((c,d))),newE))
        entries=C['flips'][name]
        assert len(observed)==len(entries)
        assert {(o[0],o[1]) for o in observed}=={(tuple(x['removed']),tuple(x['added'])) for x in entries}
        other='G1' if name=='G2' else 'G2'
        for entry in entries:
            result=next(E_ for r,a,E_ in observed if r==tuple(entry['removed']) and a==tuple(entry['added']))
            assert entry['other_type']==other and iso(result,graphsets[other],entry['isomorphism'])
            assert not iso(result,E,entry['isomorphism'])
        # independently count all automorphisms, compare supplied complete list
        aut=list_isomorphisms(E,E)
        assert len(aut)==len(C['automorphisms'][name])
        assert set(aut)=={tuple(p) for p in C['automorphisms'][name]}
        flipped={frozenset(x['removed']) for x in entries}
        images={frozenset(p[v] for v in next(iter(flipped))) for p in aut}
        assert images==flipped
        counts[name]=(len(entries),len(aut));orbits[name]=len(images)
    assert counts=={'G1':(5,10),'G2':(4,8)}
    print('VERIFY_OK',counts,'single_flip_orbit_sizes',orbits)

if __name__=='__main__':main()
