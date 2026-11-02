"""Reproduce numerical checks for affine-resolvable incidence negative type.

Requires Python 3 and NumPy. The all-parameter proof is analytic; this checks
independently constructed finite affine geometries against its spectral formula.
"""
from itertools import product
from collections import deque
from math import log, sqrt
import numpy as np


def affine_design(q, dimension):
    points = list(product(range(q), repeat=dimension))
    normals = []
    for a in product(range(q), repeat=dimension):
        if not any(a):
            continue
        leading = next(x for x in a if x)
        canonical = tuple((x * pow(leading, -1, q)) % q for x in a)
        if canonical == a:
            normals.append(a)
    lines = [(a, z) for a in normals for z in range(q)]
    inc = np.array([[int(sum(x * a for x, a in zip(point, normal)) % q == z)
                     for normal, z in lines] for point in points], dtype=int)
    classes = np.repeat(np.arange(len(normals)), q)
    return inc, classes


def root_transverse(s):
    low, high = 0.0, 1.0
    def f(p):
        return s * (3.0 ** p - 1.0) ** 2 - 2.0 ** (3.0 * p)
    while f(high) <= 0:
        high *= 2
    for _ in range(90):
        mid = (low + high) / 2
        if f(mid) > 0:
            high = mid
        else:
            low = mid
    return (high + low) / 2


def assemble(q, dimension, p):
    inc, cl = affine_design(q, dimension)
    v, b = inc.shape
    s = q ** (dimension - 1)
    r = b // q
    a = 2.0 ** p
    c = 3.0 ** p
    D = np.full((v+b, v+b), a, dtype=float)
    np.fill_diagonal(D, 0.0)
    D[v:, v:] = np.where(cl[:, None] == cl[None, :], a*a, a)
    np.fill_diagonal(D[v:, v:], 0.0)
    D[:v, v:] = np.where(inc == 1, 1.0, c)
    D[v:, :v] = D[:v, v:].T
    return D, inc, cl, (v, b, s, r, a, c)


def check_geometry(inc, classes):
    v, b = inc.shape
    q = np.bincount(classes)[0]
    assert np.all(inc.sum(axis=0) == v // q)
    r = (v-1)//(q-1)
    lam = (v//q-1)//(q-1)
    assert np.array_equal(inc @ inc.T, (r-lam)*np.eye(v,dtype=int) + lam*np.ones((v,v),dtype=int))
    # Every pair of points lies on the same number of hyperplanes.
    gram = inc @ inc.T
    assert len(set(gram[np.triu_indices(v, 1)].tolist())) == 1
    # Distinct hyperplanes within the same parallel class are disjoint.
    gh = inc.T @ inc
    for j in range(b):
        for k in range(j+1, b):
            if classes[j] == classes[k]:
                assert gh[j,k] == 0
            else:
                assert gh[j,k] == v//(q*q)



def check_shortest_paths(inc):
    v,b = inc.shape
    total = v+b
    neighbors = [[] for _ in range(total)]
    for x in range(v):
        for y in np.flatnonzero(inc[x]):
            neighbors[x].append(v+int(y))
            neighbors[v+int(y)].append(x)
    D,_,_,_=assemble_from_incidence(inc)
    for x in range(total):
        dist = [-1]*total
        dist[x]=0
        queue=deque([x])
        while queue:
            a=queue.popleft()
            for z in neighbors[a]:
                if dist[z] == -1:
                    dist[z]=dist[a]+1
                    queue.append(z)
        assert all(i >= 0 for i in dist)
        assert np.array_equal(np.asarray(dist,dtype=float),D[x])


def assemble_from_incidence(inc):
    v,b=inc.shape
    n=round(v/(int(inc.sum(axis=0)[0])))
    r=b//n
    # Hyperplanes are listed consecutively by parallel class.
    cl=np.repeat(np.arange(r),n)
    D=np.full((v+b,v+b),2.0)
    np.fill_diagonal(D,0.0)
    D[v:,v:]=np.where(cl[:,None]==cl[None,:],4.0,2.0)
    np.fill_diagonal(D[v:,v:],0.0)
    D[:v,v:]=np.where(inc==1,1.0,3.0)
    D[v:,:v]=D[:v,v:].T
    return D,None,None,None

def formula_eigenvalues(n, v, b, s, r, a, c):
    F = a*(v-1) + (v/b)*(a*(b-n)+a*a*(n-1)) - 2*s*(1+(n-1)*c)
    parallel = a*((n-1)*a - n)
    center = -(a+a*a)/2
    spread = sqrt(((a-a*a)/2)**2 + s*(c-1)**2)
    return np.array(sorted([0.0, F/(1+v/b)] +
                           [parallel]*(r-1) +
                           [center+spread]*(v-1) +
                           [center-spread]*(v-1)))


def run_case(q, dimension):
    sample_D, inc, classes, params = assemble(q,dimension,0.0)
    v,b,s,r,_,_ = params
    assert v == q**dimension and b == q*r
    assert r == (v-1)//(q-1)
    check_geometry(inc,classes)
    if dimension <= 3:
        check_shortest_paths(inc)
    p_par = log(q/(q-1),2)
    p_tr = root_transverse(s)
    crit = min(p_par,p_tr)
    candidates = [0.0, 0.27*crit, 0.67*crit, crit, crit+0.15]
    for p in candidates:
        D,_,_,(v,b,s,r,a,c)=assemble(q,dimension,p)
        ones = np.ones(v+b)/sqrt(v+b)
        Q = np.eye(v+b) - np.outer(ones,ones)
        e1 = np.linalg.eigvalsh(Q @ D @ Q)
        e2 = formula_eigenvalues(q,v,b,s,r,a,c)
        assert np.max(np.abs(e1-e2)) < 2e-9, (q,dimension,p, np.max(np.abs(e1-e2)))
        nontrivial = sorted(e1,key=lambda x: abs(x),reverse=True)[:v+b-1]
        # Ranks at endpoints certified by formula, numerical test checks the eigenvalues.
        if p < crit - 1e-8:
            assert max(nontrivial) < -1e-8
        elif p > crit + 1e-8:
            assert max(nontrivial) > 1e-8
    assert p_tr > p_par if dimension == 2 else p_tr < p_par
    endpoint_nullity = r-1 if p_par < p_tr else v-1
    print(f'AG({dimension},{q}): N={v+b} s={s} parallel={p_par:.9f} transversal={p_tr:.9f} endpoint-nullity={endpoint_nullity}')

if __name__ == '__main__':
    for q, dimension in [(3,2),(3,3),(3,4),(5,2),(5,3)]:
        run_case(q,dimension)
    print('AFFINE_RESOLVABLE_NEGATIVE_TYPE_SPECTRUM_OK')
