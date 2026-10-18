#!/usr/bin/env python3
"""Finite exact certificate for negative orientable cyclic words over Z/4Z of order 3.
Only Python standard library is required. All search loops are finite and exhausted.
"""
from collections import Counter
from itertools import product

Q = 4

def invol3(t):
    return tuple((-v) % Q for v in t[::-1])

def invol2(t):
    return tuple((-v) % Q for v in t[::-1])

def vertex_class(v):
    return min(v, invol2(v))

def text_triple(t):
    return ''.join(map(str, t))

triples = list(product(range(Q), repeat=3))
classes = sorted({tuple(sorted((t, invol3(t)))) for t in triples})
fixed = [a for a, b in classes if a == b]
nonfixed = [(a, b) for a, b in classes if a != b]
assert len(fixed) == 8 and len(nonfixed) == 28
vertices = sorted({vertex_class(v) for v in product(range(Q), repeat=2)})
assert len(vertices) == 10

def endpoints(t):
    return vertex_class(t[:2]), vertex_class(t[1:])

for a, b in nonfixed:
    assert endpoints(a) == endpoints(b)[::-1]

degree = Counter({v: 0 for v in vertices})
for a, _ in nonfixed:
    v, w = endpoints(a)
    degree[v] += 1
    degree[w] += 1
expected_degree = {
    (0, 0): 3, (0, 1): 7, (0, 2): 6, (0, 3): 7,
    (1, 1): 8, (1, 2): 7, (1, 3): 4,
    (2, 1): 7, (2, 2): 3, (3, 1): 4,
}
assert dict(degree) == expected_degree, (degree, expected_degree)
odd = {v for v in vertices if degree[v] % 2}
assert odd == {(0,0),(0,1),(0,3),(1,2),(2,1),(2,2)}

# Any 25-class selection must omit exactly three edges; their endpoints
# must constitute a perfect matching of the six odd-degree vertices.
odd_edges = [(text_triple(a), v, w) for a, _ in nonfixed
             for v, w in [endpoints(a)] if v in odd and w in odd and v != w]
matchings = []
for i, (a, va, wa) in enumerate(odd_edges):
    for j in range(i + 1, len(odd_edges)):
        b, vb, wb = odd_edges[j]
        for c, vc, wc in odd_edges[j + 1:]:
            if len({va, wa, vb, wb, vc, wc}) == 6:
                matchings.append(tuple(sorted([a,b,c])))
matchings.sort()
assert matchings == [('001','032','122'),('003','012','221')], matchings

def divergence(t, v):
    return int(t[:2] == v) - int(t[1:] == v)

def difference(t, v):
    return divergence(t, v) - divergence(t, invol2(v))

special = [((1,2), ('001','032','122'), -2),
           ((0,3), ('003','012','221'), +2)]
for v, omitted, expected in special:
    rep_values = {text_triple(a): difference(a, v) for a, b in nonfixed}
    assert all(difference(a, v) == difference(b, v) for a,b in nonfixed)
    remaining = sum(value for label, value in rep_values.items() if label not in omitted)
    assert remaining == expected, (v, remaining)
    total = sum(rep_values.values())
    omitted_vector = [rep_values[x] for x in omitted]
    print('excluded perfect matching',','.join(omitted),
          'invariant vertex', ''.join(map(str,v)),
          'total',total,'omitted',omitted_vector,'remaining',remaining)

word = '001201322330323133102111'
assert len(word) == 24
windows = [tuple(map(int, (word + word[:2])[i:i+3])) for i in range(len(word))]
assert len(windows) == len(set(windows)) == 24
for t in windows:
    assert t not in fixed
    assert invol3(t) not in windows
assert len(set(tuple(sorted((t, invol3(t)))) for t in windows)) == 24
print('fixed triples', len(fixed), 'nonfixed classes',len(nonfixed),
      'quotient vertices',len(vertices),'odd-degree vertices',len(odd))
print('quotient vertex degrees', [(str(v),degree[v]) for v in vertices])
print('perfect matchings of odd-degree vertices',matchings)
print('valid cyclic witness',word,'length',len(word))
print('all checks passed: exact maximum period is 24')
