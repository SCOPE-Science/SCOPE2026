#!/usr/bin/env python3
"""Independent finite verification of the parity and nerve classification of
perfect-matching complexes of multi-theta graphs.

No outside packages required.  Does not substitute for the universal proof.
"""
from itertools import product,combinations
from collections import Counter
import sys


def build(lengths):
    assert len(lengths)>=2 and all(L>=2 for L in lengths)
    adj={0:set(),1:set()}
    paths=[]; nextid=2
    for L in lengths:
        vertices=[0]+list(range(nextid,nextid+L-1))+[1]
        nextid+=L-1
        paths.append(vertices)
        for v in vertices:
            adj.setdefault(v,set())
        for u,v in zip(vertices,vertices[1:]):
            adj[u].add(v); adj[v].add(u)
    return adj,paths

def enumerate_perfect_matchings(adj):
    n=len(adj)
    if n%2: return []
    def rec(uncovered,edges):
        if not uncovered:
            yield frozenset(edges)
            return
        v=min(uncovered)
        for w in sorted(adj[v]&uncovered):
            yield from rec(uncovered-{v,w},edges+[(min(v,w),max(v,w))])
    return list(rec(set(adj),[]))

def faces_of_facets(facets):
    faces={frozenset()}
    for f in facets:
        vals=list(f)
        for mask in range(1,1<<len(vals)):
            faces.add(frozenset(vals[i] for i in range(len(vals)) if mask>>i&1))
    return faces

def rank_mod2(rows):
    piv={}
    for z in rows:
        while z:
            c=z.bit_length()-1
            if c not in piv:
                piv[c]=z;break
            z^=piv[c]
    return len(piv)

def betti_reduced(faces):
    by_dim={}
    for s in faces:
        if s:by_dim.setdefault(len(s)-1,[]).append(s)
    if not by_dim:return {}
    maxd=max(by_dim)
    ranks={}
    for d in range(1,maxd+1):
        faceidx={s:i for i,s in enumerate(by_dim[d-1])}
        rows=[]
        for s in by_dim[d]:
            bits=0
            for x in s:
                bits ^= 1<<faceidx[s-{x}]
            rows.append(bits)
        ranks[d]=rank_mod2(rows)
    ranks[0]=1
    return {d:len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)
            for d in range(maxd+1) if len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)}

def expected(lengths):
    r=len(lengths); q=sum(L%2==0 for L in lengths)
    if q==0:return 'sphere',r-2,r
    if q==2:
        if r==2:return 'sphere',0,2
        return 'contractible',None,2
    return 'void',None,0

def check(lengths,homology=False):
    adj,paths=build(lengths)
    matches=enumerate_perfect_matchings(adj)
    typ,dim,nmatch=expected(lengths)
    assert len(matches)==nmatch,(lengths,'matching number',len(matches),nmatch)
    if typ=='void':return
    r=len(lengths)
    # Every individual intersection is contractible (a simplex). The pattern
    # of empty intersections is predicted exactly from the arm parity.
    for size in range(1,len(matches)+1):
        for js in combinations(range(len(matches)),size):
            ints=set.intersection(*(set(matches[j]) for j in js))
            predicted=(size<len(matches)) if typ=='sphere' else bool(len(matches)>1 and r>2)
            # Single facet may be nonempty; for sphere all proper intersections nonempty.
            if typ=='contractible':predicted=True
            assert bool(ints)==predicted,(lengths,js,ints,predicted)
    if homology:
        faces=faces_of_facets(matches)
        betti=betti_reduced(faces)
        b={dim:1} if typ=='sphere' else {}
        assert betti==b,(lengths,betti,b)
    return True

# independent exact tests of all parity patterns and varying arm lengths
count=0; full=0
for r in range(2,7):
    samples=product((2,3,4,5),repeat=r)
    for L in samples:
        if r==6 and max(L)>3:continue
        run_full=(r<=4 and sum(L)<=13)
        check(L,homology=run_full)
        count+=1;full+=run_full
print('OK',count,'multitheta graphs; exact F2 homology for',full,'cases.')
print('Representative [3,3,3,3] => S^2; [2,2,3] => contractible; [2,2,2,2] => no perfect matching.')

# Signed simplicial Lefschetz checks for the all-odd equal-arm subfamily.
# An invariant nonempty simplex contributes sign(permutation of its vertices)
# times (-1)^(simplex dimension).  The reduced Lefschetz number subtracts 1.
def sign_of_perm_image(original,image):
    target=sorted(original)
    imap=[target.index(v) for v in image]
    inversions=sum(imap[i]>imap[j] for i in range(len(imap)) for j in range(i+1,len(imap)))
    return -1 if inversions%2 else 1

def lefschetz_under_automorphism(faces,vmap):
    def image_edge(e):return tuple(sorted((vmap[e[0]],vmap[e[1]])))
    total=-1 # reduced chain degree -1
    for face in faces:
        if not face:continue
        sortface=sorted(face)
        ims=[image_edge(e) for e in sortface]
        if set(ims)==set(sortface):
            total+=(-1)**(len(sortface)-1)*sign_of_perm_image(sortface,ims)
    return total

lchecks=0
for r in range(4,7):
    ls=[3]*r
    adj,paths=build(ls)
    facets=enumerate_perfect_matchings(adj)
    faces=faces_of_facets(facets)
    # Adjacent transpositions generate arm permutations; full path reversal.
    for i in range(r-1):
        vmap={v:v for v in adj}
        for a,b in zip(paths[i][1:-1],paths[i+1][1:-1]):
            vmap[a]=b;vmap[b]=a
        assert lefschetz_under_automorphism(faces,vmap)==(-1)**(r-2)*(-1)
        lchecks+=1
    vmap={0:1,1:0}
    for p in paths:
        for a,b in zip(p[1:-1],reversed(p[1:-1])):vmap[a]=b
    assert lefschetz_under_automorphism(faces,vmap)==(-1)**(r-2)
    lchecks+=1
print('OK',lchecks,'exact reduced Lefschetz action checks.')
