#!/usr/bin/env python3
"""Exact finite checks for Paley(13) open-neighborhood topology."""
from itertools import combinations
from collections import Counter, defaultdict

q=13
squares={i*i%q for i in range(1,q)}
assert squares=={1,3,4,9,10,12}
neighbor=[frozenset((v+d)%q for d in squares) for v in range(q)]
assert all(len(n)==6 for n in neighbor)
faces={frozenset()}
for N in neighbor:
    for k in range(1,7):
        faces.update(frozenset(t) for t in combinations(sorted(N),k))
assert len(faces)==599
f=Counter(len(s)-1 for s in faces)
assert [f[j] for j in range(-1,6)]==[1,13,78,221,195,78,13]

# Contract each omitted triangular loop across three actual 2-simplices.
absent=0
for a,b,c in combinations(range(q),3):
    T=frozenset((a,b,c))
    if T in faces: continue
    absent+=1
    assert any(all(frozenset((v,u,w)) in faces for u,w in [(a,b),(b,c),(c,a)]) for v in range(q) if v not in T)
assert absent==65

# Enumerate elementary collapses, checking uniqueness of each containing facet.
working=set(faces)
matched=[]
while True:
    maxima=[]
    for t in working:
        if not any(t < x for x in working):
            maxima.append(t)
    found=None
    for f in sorted(maxima,key=lambda s:(-len(s), tuple(sorted(s)))):
        for x in sorted(f):
            g=f-{x}
            if g and g in working and not any(g<=h for h in maxima if h!=f):
                found=(g,f)
                break
        if found:break
    if found is None:break
    g,f=found
    assert all((not g<=h or h==f) for h in maxima)
    matched.append(found)
    working.remove(g);working.remove(f)
assert len(matched)==218
assert max(map(len,working))==3
assert len(working)==163
assert Counter(len(s)-1 for s in working)==Counter({2:81,1:68,0:13,-1:1})

# Affine group character of the unique nonzero reduced homology.
def lefschetz(a,b):
    z=-1 # empty augmented simplex
    for f in faces:
        if not f: continue
        xs=sorted(f)
        ys=[(a*x+b)%q for x in xs]
        if set(ys)!=set(xs):continue
        inversions=sum(ys[i]>ys[j] for i in range(len(xs)) for j in range(i+1,len(xs)))
        z+=(-1)**(len(xs)-1+inversions)
    return z
for a in squares:
    for b in range(q):
        expected=(25 if b==0 else -1) if a==1 else 1
        assert lefschetz(a,b)==expected,(a,b)
print('PASS: 599 faces, 65 missing triangle fillings, 218 elementary collapses, 25 two-spheres, all 78 group characters')
