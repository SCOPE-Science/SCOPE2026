#!/usr/bin/env python3
import itertools
import sympy as sp

s3 = sp.sqrt(3)
a = sp.sqrt((3+s3)/6)
b = sp.sqrt((3-s3)/12)
c = sp.sqrt((3-s3)/6)
d = sp.sqrt((3+s3)/12)

vectors = []
labels = {}
for typ, (large, small) in enumerate(((a,b),(c,d))):
    for distinguished in range(3):
        base = [small, small, small]
        base[distinguished] = large
        for signs in itertools.product((1,-1), repeat=3):
            v = tuple(sp.simplify(signs[i]*base[i]) for i in range(3))
            vectors.append(v)
            labels[v] = (typ, distinguished, signs)

assert len(vectors) == 48
assert len(set(vectors)) == 48
vectors = list(dict.fromkeys(vectors))

def dot(v,w):
    return sp.simplify(sum(v[i]*w[i] for i in range(3)))

def cross(v,w):
    return (
        sp.simplify(v[1]*w[2]-v[2]*w[1]),
        sp.simplify(v[2]*w[0]-v[0]*w[2]),
        sp.simplify(v[0]*w[1]-v[1]*w[0]),
    )

edges = []
adj = {i:set() for i in range(len(vectors))}
for i in range(len(vectors)):
    assert sp.simplify(dot(vectors[i], vectors[i]) - 1) == 0
    for j in range(i+1, len(vectors)):
        if dot(vectors[i], vectors[j]) == 0:
            edges.append((i,j))
            adj[i].add(j)
            adj[j].add(i)

assert len(edges) == 48
assert all(len(adj[i]) == 2 for i in adj)

for i,j in edges:
    vi, vj = vectors[i], vectors[j]
    ti, pi, _ = labels[vi]
    tj, pj, _ = labels[vj]
    assert {ti,tj} == {0,1}
    assert pi == pj
    z = cross(vi,vj)
    squares = [sp.simplify(x*x) for x in z]
    assert sum(1 for x in squares if sp.simplify(x) == 0) == 1
    assert sum(1 for x in squares if sp.simplify(x-sp.Rational(1,2)) == 0) == 2

triangles = []
for i,j in edges:
    for k in adj[i].intersection(adj[j]):
        triangles.append(tuple(sorted((i,j,k))))
assert len(set(triangles)) == 0

# Scalar identities used in the human proof.
assert sp.simplify(a*c - 1/sp.sqrt(6)) == 0
assert sp.simplify(b*d - 1/(2*sp.sqrt(6))) == 0
assert sp.simplify(a*a - 2*b*b) > 0
assert sp.simplify(a*d - b*c - b*d) > 0

print("VERIFY_OK")
print("equality_vectors=48")
print("orthogonal_pairs=48")
print("orthogonal_graph_degree=2")
print("orthogonal_triangles=0")
print("cross_product_pattern={0,1/2,1/2}")
