#!/usr/bin/env python3
"""Exact small-parameter verification for rectangular-band GLSG spectra.
The adjacency is built directly from the multiplication-table coordinates.
All arithmetic is in the integers; there is no floating-point eigensolver.
"""
from collections import Counter, deque
from itertools import product


def tensor(vectors):
    out = [1]
    for v in vectors:
        out = [x * y for x in out for y in v]
    return out


def basis(r):
    const = [1] * r
    return [(r, const)] + [(0, [-1 if i == 0 else 1 if i == j else 0 for i in range(r)]) for j in range(1, r)]


def check(a, b):
    vertices = list(product(range(a), range(b), range(a), range(b)))
    n = len(vertices)
    nbr = [[] for _ in vertices]
    for h, (i,j,k,l) in enumerate(vertices):
        for t, (ii,jj,kk,ll) in enumerate(vertices):
            if h == t:
                continue
            matching = ((i,j)==(ii,jj)) + ((k,l)==(kk,ll)) + ((i,l)==(ii,ll))
            if matching == 1:
                nbr[h].append(t)
    d = 3*a*b - 2*a - 2*b + 1
    assert all(len(row) == d for row in nbr), (a,b,'degree')
    observed = Counter()
    tensor_bases = [basis(a), basis(b), basis(a), basis(b)]
    for sectors in product(*tensor_bases):
        (u,v,w,t) = (entry[0] for entry in sectors)
        eigen = 1 + u*v + v*w + w*t - 2*v - 2*w
        vector = tensor([entry[1] for entry in sectors])
        for h in range(n):
            assert sum(vector[k] for k in nbr[h]) == eigen * vector[h], (a,b,sectors,h)
        observed[eigen] += 1
    assert sum(observed.values()) == n
    assert sum(z*mul for z,mul in observed.items()) == 0
    assert sum(z*z*mul for z,mul in observed.items()) == n*d
    unseen = set(range(n))
    components = []
    while unseen:
        start = next(iter(unseen)); q = deque([start]); unseen.remove(start); size=0
        while q:
            z=q.popleft(); size+=1
            for t in nbr[z]:
                if t in unseen:
                    unseen.remove(t);q.append(t)
        components.append(size)
    if a>=2 and b>=2:
        assert components == [n], (a,b,components)
    else:
        assert sorted(components)==[a*b]*(a*b), (a,b,components)
    if (a,b)==(2,2):
        assert observed == Counter({5:1, 1:10, -3:5}), observed
        for h in range(n):
            for t in range(h+1,n):
                common=len(set(nbr[h]).intersection(nbr[t]))
                assert common == (0 if t in nbr[h] else 2), (h,t,common)
    # Spectral reconstruction of unordered semigroup factors.
    size = a*b
    summation = (3*size + 1 - d)//2
    assert (3*size+1-d)%2 == 0
    assert sorted((a,b)) == sorted((min(k for k in range(1,size+1) if k*(summation-k)==size), summation-min(k for k in range(1,size+1) if k*(summation-k)==size)))
    return n, d, sorted(observed.items())


if __name__=='__main__':
    for a,b in product(range(1,5), repeat=2):
        n,d,spectrum = check(a,b)
        print(f'a={a} b={b} vertices={n} degree={d} spectrum={spectrum}')
    print('VERIFY_OK 16 rectangular bands; complete exact tensor eigenbases, degree, connectivity, reconstruction and Clebsch test')
