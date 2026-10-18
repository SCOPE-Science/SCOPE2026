"""Exact exhaustive arithmetic certificate for the 15-line icosahedral model.

Run: python3 verify_icosahedral_reduction.py
Only Python's standard library is needed. All characteristic-zero arithmetic is
in Z[phi] with phi^2=phi+1; finite-field arithmetic is in F_2[phi].
"""
from collections import Counter, defaultdict
from itertools import combinations, product

ZERO = (0, 0)
ONE = (1, 0)
PHI = (0, 1)
PHIM1 = (-1, 1)

def add(a, b): return (a[0]+b[0], a[1]+b[1])
def minus(a): return (-a[0], -a[1])
def sub(a, b): return add(a, minus(b))
def mul(a, b):
    return (a[0]*b[0]+a[1]*b[1],
            a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
def norm(a): return a[0]*a[0]+a[0]*a[1]-a[1]*a[1]

def cross(u, v):
    return (sub(mul(u[1], v[2]), mul(u[2], v[1])),
            sub(mul(u[2], v[0]), mul(u[0], v[2])),
            sub(mul(u[0], v[1]), mul(u[1], v[0])))
def det(a, b, c):
    u = cross(a, b)
    return add(add(mul(u[0], c[0]), mul(u[1], c[1])), mul(u[2], c[2]))
def same_point(u, v): return all(z == ZERO for z in cross(u, v))

normals = [(ONE, ZERO, ZERO), (ZERO, ONE, ZERO), (ZERO, ZERO, ONE)]
for j in range(3):
    for sign1, sign2 in product((1,-1), repeat=2):
        base = (ONE, PHI, PHIM1)
        v = [base[(k-j)%3] for k in range(3)]
        normals.append((v[0], mul(v[1], (sign1,0)), mul(v[2], (sign2,0))))
assert len(normals) == len(set(normals)) == 15

norms = Counter()
for ii, jj, kk in combinations(range(15), 3):
    d = det(normals[ii], normals[jj], normals[kk])
    norms['zero' if d == ZERO else abs(norm(d))] += 1
assert norms == Counter({'zero':70,16:188,4:156,1:37,64:4}), norms

# Construct all characteristic-zero intersection points from all 105 pairs.
points = []
incidence = defaultdict(list)
for i,j in combinations(range(15),2):
    q = cross(normals[i], normals[j])
    assert q != (ZERO,ZERO,ZERO)
    found = next((k for k,p in enumerate(points) if same_point(q,p)), None)
    if found is None:
        found=len(points)
        points.append(q)
    incidence[found].append((i,j))
assert len(points) == 31
multiplicities = []
for k in range(31):
    incident_lines = {i for pair in incidence[k] for i in pair}
    m=len(incident_lines)
    assert len(incidence[k]) == m*(m-1)//2
    for i in incident_lines: assert det(normals[i], normals[incidence[k][0][0]], normals[incidence[k][0][1]]) == ZERO
    multiplicities.append(m)
assert Counter(multiplicities) == Counter({2:15,3:10,5:6})

# GF(4) represented by 0,1,phi,phi+1 = 0,1,2,3 respectively.
def f4(z): return (z[0]&1) | ((z[1]&1)<<1)
def m4(x,y): return f4(mul((x&1,x>>1),(y&1,y>>1)))
def inv4(x): return next(y for y in (1,2,3) if m4(x,y)==1)
def proj4(v):
    for k in v:
        if k:
            inv=inv4(k)
            return tuple(m4(inv,x) for x in v)
    raise AssertionError('zero vector')
def reduce_point(u):
    v=list(u)
    while all(all(z%2==0 for z in a) for a in v):
        v=[(a//2,b//2) for a,b in v]
    return proj4(tuple(f4(z) for z in v))

fibres = defaultdict(Counter)
for k,u in enumerate(points):
    destination=reduce_point(u)
    for i,j in incidence[k]:
        assert reduce_point(cross(normals[i], normals[j])) == destination
    fibres[destination][multiplicities[k]] += 1
assert len(fibres)==8
expected = {
    (0,0,1):{2:1}, (0,1,0):{2:1}, (1,0,0):{2:1},
    (0,1,3):{3:2,5:2}, (1,0,2):{3:2,5:2}, (1,3,0):{3:2,5:2},
    (1,1,1):{3:4}, (1,2,3):{2:12}
}
assert {k:dict(v) for k,v in fibres.items()} == expected, fibres

reduced = Counter(proj4(tuple(f4(a) for a in row)) for row in normals)
assert reduced == Counter({(1,0,0):1,(0,1,0):1,(0,0,1):1,(1,2,3):12})
print('NORM_CERT', sorted(norms.items(),key=str))
print('GENERIC_POINTS',dict(Counter(multiplicities)))
print('GF4_LINES',dict(reduced))
print('GF4_FIBRES',sorted((p,dict(d)) for p,d in fibres.items()))
print('VERIFY_OK')
