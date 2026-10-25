#!/usr/bin/env python3
"""Exact integral discrete-Morse certificate for the neighborhood complex of T_7.
Usage: python verify.py [matching_certificate.json.gz]
Python standard library only. No external input beyond the matching certificate.
"""
import collections
import gzip
import itertools
import json
import pathlib
import sys
from functools import lru_cache

HERE = pathlib.Path(__file__).resolve().parent
certificate = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'matching_certificate.json.gz'
data = json.loads(gzip.decompress(certificate.read_bytes()))
vertices = list(itertools.combinations(range(7),2))
assert [list(e) for e in vertices] == data['vertex_edges']
# T_7 = L(K_7): two vertices adjacent iff their edges intersect.
faces=set()
for edge in vertices:
    nb=sum(1 << j for j,f in enumerate(vertices) if edge != f and (edge[0] in f or edge[1] in f))
    assert nb.bit_count()==10
    s=nb
    while s:
        faces.add(s)
        s=(s-1)&nb
assert len(faces)==18494
fvec=collections.Counter(x.bit_count()-1 for x in faces)
assert [fvec[i] for i in range(10)] == [21,210,1190,3780,5187,4410,2520,945,210,21]
print('ORIGINAL_FACE_VECTOR',*[fvec[i] for i in range(10)])

pairs = [tuple(p) for p in data['pairs']]
critical=set(data['critical'])
assert len(pairs)==9120 and len(critical)==254
seen=set()
lowup={}
upperlower={}
for a,b in pairs:
    assert a in faces and b in faces and a not in seen and b not in seen
    assert (a&b)==a and (b^a).bit_count()==1
    seen.add(a);seen.add(b)
    lowup[a]=b;upperlower[b]=a
assert set(faces)-seen==critical
cvec=collections.Counter(x.bit_count()-1 for x in critical)
assert [cvec[i] for i in range(10)] == [1,0,0,246,7,0,0,0,0,0]
print('MATCHING_PAIRS',len(pairs),'CRITICAL_VECTOR',*[cvec[i] for i in range(5)])

# Acyclicity on the FULL directed Hasse diagram. Reversing all matched
# edges and directing all other cover relations from coface to facet
# must produce a directed acyclic graph.
adj={x:[] for x in faces};indeg={x:0 for x in faces}
for upper in faces:
    if upper.bit_count()==1: continue
    bits=upper
    while bits:
        bit=bits&-bits;bits-=bit
        lower=upper^bit
        if lowup.get(lower)==upper:
            src,dst=lower,upper
        else:
            src,dst=upper,lower
        adj[src].append(dst)
        indeg[dst]+=1
queue=collections.deque(x for x in faces if indeg[x]==0)
visit=0
while queue:
    a=queue.popleft();visit+=1
    for b in adj[a]:
        indeg[b]-=1
        if indeg[b]==0: queue.append(b)
assert visit==len(faces),f'Directed matching cycle: only {visit} visited'
print('DIRECTED_HASSE_ACYCLIC',visit)

# Integral signed Morse boundary in degree 4 -> 3. A lower 3-face
# paired upward to a 4-face propagates along all other facets of that
# upper simplex, with the exact incidence quotient (always +/-1).
# Upper faces paired downward to dimension two do not terminate
# 4-to-3 gradient paths; critical three-faces do.
critical3={x for x in critical if x.bit_count()==4}
critical4=sorted(x for x in critical if x.bit_count()==5)
def facets_with_sign(mask):
    out=[];idx=0;bits=mask
    while bits:
        bit=bits&-bits;bits-=bit
        out.append((mask^bit, 1 if idx%2==0 else -1))
        idx+=1
    return out

@lru_cache(None)
def project(f):
    if f in critical3:return ((f,1),)
    if f not in lowup: # upper face of a (dimension-two, dimension-three) pair
        assert f in upperlower and f.bit_count()==4
        return ()
    upper=lowup[f]
    assert upper.bit_count()==5 and f.bit_count()==4
    boundary=facets_with_sign(upper)
    inv=next(coeff for g,coeff in boundary if g==f)
    result=collections.defaultdict(int)
    for g,sign in boundary:
        if g==f:continue
        for h,coeff in project(g):result[h]-=inv*sign*coeff
    return tuple(sorted((h,c) for h,c in result.items() if c))

zero=0
for f in critical4:
    result=collections.defaultdict(int)
    for g,s in facets_with_sign(f):
        for h,c in project(g):result[h]+=s*c
    surviving={h:c for h,c in result.items() if c}
    assert not surviving,('NONZERO_BOUNDARY',f,surviving)
    zero+=1
print('SIGNED_MORSE_BOUNDARIES_ZERO',zero)
print('INTEGRAL_HOMOLOGY_H3_Z246_H4_Z7')
print('HOMOTOPY_WEDGE_246_S3_7_S4')
print('VERIFY_OK_TRIANGULAR_T7_NEIGHBORHOOD_INTEGRAL_WEDGE')
