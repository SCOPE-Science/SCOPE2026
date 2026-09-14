"""Build Groetzsch graph M4 (Mycielski of C5), enumerate maximal independent
sets / minimal vertex covers, solve fractional Waldschmidt LP with symmetry
reduction (exact rational arithmetic)."""
import itertools
from fractions import Fraction

# Vertices: v0..v4 -> 0..4 ; u0..u4 -> 5..9 ; w -> 10
n = 11
edges = set()
for i in range(5):
    a, b = i, (i + 1) % 5
    edges.add((min(a, b), max(a, b)))
for j in range(5):
    u = 5 + j
    for vv in ((j - 1) % 5, (j + 1) % 5):
        edges.add((min(u, vv), max(u, vv)))
for i in range(5):
    edges.add((5 + i, 10))
edges = sorted(edges)
print("num edges:", len(edges))
assert len(edges) == 20

adj = {v: set() for v in range(n)}
for a, b in edges:
    adj[a].add(b)
    adj[b].add(a)
print("degrees:", sorted((len(adj[v]), v) for v in range(n)))

# triangle check
tris = 0
for a, b in edges:
    if adj[a] & adj[b]:
        tris += 1
print("triangles:", tris)

# maximal independent sets via brute force
maximal_ind = []
for mask in range(1 << n):
    S = [v for v in range(n) if mask & (1 << v)]
    Sset = set(S)
    ok = True
    for a, b in edges:
        if a in Sset and b in Sset:
            ok = False
            break
    if not ok:
        continue
    # maximal?
    maximal = True
    for v in range(n):
        if v not in Sset and not (adj[v] & Sset):
            maximal = False
            break
    if maximal:
        maximal_ind.append(Sset)
print("num maximal independent sets:", len(maximal_ind))
print("indep sizes:", sorted(len(S) for S in maximal_ind))
print("alpha(G) =", max(len(S) for S in maximal_ind))

mincovers = [set(range(n)) - S for S in maximal_ind]
print("num minimal covers:", len(mincovers))
print("cover sizes:", sorted(len(C) for C in mincovers))

# orbit types of minimal covers: (# in V, # in U, w in/out)
from collections import Counter
types = Counter()
for C in mincovers:
    nv = len([v for v in C if v < 5])
    nu = len([v for v in C if 5 <= v < 10])
    nw = 1 if 10 in C else 0
    types[(nv, nu, nw)] += 1
print("cover orbit-type counts:")
for t in sorted(types):
    print("  ", t, types[t])

# Symmetry-reduced primal LP: min 5p+5q+s s.t. nv*p+nu*q+nw*s>=1 per type, p,q,s>=0
Ts = sorted(types)
planes = []  # each (A,B,C,D) meaning A p+B q+C s >= D
for (nv, nu, nw) in Ts:
    planes.append((Fraction(nv), Fraction(nu), Fraction(nw), Fraction(1)))
planes.append((Fraction(1), Fraction(0), Fraction(0), Fraction(0)))
planes.append((Fraction(0), Fraction(1), Fraction(0), Fraction(0)))
planes.append((Fraction(0), Fraction(0), Fraction(1), Fraction(0)))

def det3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

def solve3(M, rhs):
    D = det3(M)
    if D == 0:
        return None
    outs = []
    for col in range(3):
        Mm = [list(r) for r in M]
        for r in range(3):
            Mm[r][col] = rhs[r]
        outs.append(det3(Mm) / D)
    return outs

best = None
bestpt = None
P = len(planes)
for combo in itertools.combinations(range(P), 3):
    M = [[planes[k][j] for j in range(3)] for k in combo]
    rhs = [planes[k][3] for k in combo]
    sol = solve3(M, rhs)
    if sol is None:
        continue
    p, q, s = sol
    if all(planes[k][0] * p + planes[k][1] * q + planes[k][2] * s >= planes[k][3] for k in range(P)):
        val = 5 * p + 5 * q + s
        if best is None or val < best:
            best = val
            bestpt = (p, q, s)
print("exact LP optimum (Waldschmidt upper bound):", best, "=", float(best))
print("at (p,q,s) =", bestpt)

tight = [k for k in range(P) if planes[k][0] * bestpt[0] + planes[k][1] * bestpt[1] + planes[k][2] * bestpt[2] == planes[k][3]]
print("tight plane indices:", tight, [planes[k] for k in tight])
