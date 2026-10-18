#!/usr/bin/env python3
"""Exact face-lattice and primitive-normal checks for capped-crown order polytopes.

No optional dependencies. Exhauts all nonempty polytope faces for n=3,4;
checks specified minimal singular cones and all fixed points for n=3,4,5.
"""
from collections import Counter
from itertools import combinations
from math import comb


def data(n):
    d = 2*n+2
    covers = [(0,1+i) for i in range(n)]
    covers += [(1+i,1+n+j) for i in range(n) for j in range(n) if i != j]
    covers += [(1+n+j,d-1) for j in range(n)]
    facets = [(0,d), (d-1,d+1)] + covers
    vertices = [w for w in range(1 << d)
                if all((w>>a&1) <= (w>>b&1) for a,b in covers)]
    masks = [sum((1 << i) for i,w in enumerate(vertices)
                 if (w>>a&1) == (0 if j==d else (1 if j==d+1 else (w>>j&1))))
             for a,j in facets]
    return d, facets, vertices, masks


def active_of_face(face, masks):
    return sum(1 << j for j, f in enumerate(masks) if face & f == face)


def cone_rank(fmask, facets, d):
    parent = list(range(d+2))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i, (a,b) in enumerate(facets):
        if fmask >> i & 1:
            ra,rb = root(a),root(b)
            parent[ra] = rb
    return (d+2) - len({root(i) for i in range(d+2)})


def expected_blocks(n):
    top = 2*n+1
    # Labels of lower/upper elements and boundary elements.
    aa = lambda i:1+i
    bb = lambda i:1+n+i
    x=[]
    for j in range(n):
        x.append(("lower",j,tuple(sorted([0,bb(j)]+[aa(i) for i in range(n) if i!=j]))))
        x.append(("upper",j,tuple(sorted([top,aa(j)]+[bb(i) for i in range(n) if i!=j]))))
    for A in combinations(range(n),2):
        for B in combinations([j for j in range(n) if j not in A],2):
            x.append(("middle4",(A,B),tuple(sorted([aa(i) for i in A]+[bb(j) for j in B]))))
    for T in combinations(range(n),3):
        x.append(("middle6",T,tuple(sorted([aa(i) for i in T]+[bb(j) for j in T]))))
    return x


def classify(n, exhaustive=False):
    d,facets,vertices,masks=data(n)
    full=(1<<len(vertices))-1
    expected={}
    for typ,label,block in expected_blocks(n):
        intended=sum(1<<j for j,(a,b) in enumerate(facets)
                     if a in block and b in block)
        face=full
        for j,f in enumerate(masks):
            if intended>>j&1:
                face &= f
        assert face and active_of_face(face,masks)==intended,(n,typ,label)
        dim=d-cone_rank(intended,facets,d)
        correct=(n+2 if typ in ('lower','upper') else
                 2*n-1 if typ=='middle4' else 2*n-3)
        assert dim==correct,(typ,label,dim)
        expected[face]=(typ,label,dim)
    formula=2*n+comb(n,2)*comb(n-2,2)+comb(n,3)
    assert len(expected)==formula,(n,len(expected),formula)
    fixed_smooth=sum(cone_rank(active_of_face(1<<v,masks),facets,d)==active_of_face(1<<v,masks).bit_count()
                     for v in range(len(vertices)))
    assert fixed_smooth==1,(n,fixed_smooth)
    if exhaustive:
        faces={full}
        for f in masks:
            for x in tuple(faces):
                y=x&f
                if y:faces.add(y)
        status={}
        for face in faces:
            mask=active_of_face(face,masks)
            status[face] = cone_rank(mask,facets,d)<mask.bit_count()
        bad=[face for face in faces if status[face]]
        maximal=[face for face in bad
                 if not any(face!=other and face & other == face for other in bad)]
        assert set(maximal)==set(expected),(n,len(maximal),len(expected))
        f_count=Counter()
        for f in faces:
            f_count[d-cone_rank(active_of_face(f,masks),facets,d)]+=1
        print('n=%d vertices=%d faces=%d singular_components=%d by_dimension=%s' %
              (n,len(vertices),len(faces),len(maximal),
               dict(sorted(Counter(expected[z][2] for z in expected).items()))))
    else:
        print('n=%d vertices=%d predicted_components=%d all_candidate_cones_exact' %
              (n,len(vertices),len(expected)))

for n in (3,4,5):
    classify(n,n<=4)
print('VERIFY_OK')
