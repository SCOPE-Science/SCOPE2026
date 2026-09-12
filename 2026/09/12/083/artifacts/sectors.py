"""Affine distributions for nonvacuum L(L) + sector top-space extraction.
For class cl mod 2Q_L: coset lowest weight config minimizes F(n,w) = 36n - E36(w)
over (n,w) with w in cl, A_n(w) > 0. h(M) = Delta_L + Fmin/36. Top dim = A at minimizer
(if unique; sum if several)."""
from fractions import Fraction as Q
from collections import defaultdict
import json

def dot3(u, v): return 6*u[0]*v[0]-3*u[0]*v[1]-3*u[1]*v[0]+2*u[1]*v[1]
def add(u, v): return (u[0]+v[0], u[1]+v[1])
def mul(s, u): return (s*u[0], s*u[1])
def E36(w):
    x, y = w; return 18*x*x - 18*x*y + 6*y*y
def modL(w): return (w[0] % 2, w[1] % 6)

POS = [(1,0),(1,3),(2,3),(0,1),(1,1),(1,2)]
ALLR = POS + [(-a,-b) for (a,b) in POS]
RHO = (3,5); KPL = 6; K = 2
LAMBDAS = {'0': (0,0), 'w1': (2,3), 'w2': (1,2), '2w2': (2,4)}
N = 5; B = 14

OUT = {}
for name, Lam in LAMBDAS.items():
    keys = []
    for n in range(N+1):
        for a in range(-B, B+1):
            for b in range(-B, B+1):
                keys.append((n, (a,b)))
    keys.sort(key=lambda k: (k[0], (Lam[0]-k[1][0])+(Lam[1]-k[1][1])))
    m = {(0, Lam): Q(1)}
    base3 = dot3(add(Lam, RHO), add(Lam, RHO))
    for key in keys:
        if key == (0, Lam): continue
        n, w = key
        wr = add(w, RHO)
        dd3 = base3 - (dot3(wr, wr) - 36*n)
        if dd3 == 0: m[key] = Q(0); continue
        S3 = 0
        for (a, b) in POS:
            j = 1
            while True:
                kk = (n, (w[0]+j*a, w[1]+j*b))
                if abs(kk[1][0]) > B or abs(kk[1][1]) > B: break
                c = m.get(kk)
                if c: S3 += dot3(add(w, mul(j, (a,b))), (a,b)) * c
                j += 1
        for np in range(1, n+1):
            for (a, b) in ALLR:
                j = 1
                while j*np <= n:
                    kk = (n-j*np, (w[0]+j*a, w[1]+j*b))
                    if abs(kk[1][0]) <= B and abs(kk[1][1]) <= B:
                        c = m.get(kk)
                        if c: S3 += (dot3(add(w, mul(j, (a,b))), (a,b)) + 3*K*np) * c
                    j += 1
            j = 1
            while j*np <= n:
                kk = (n-j*np, w)
                c = m.get(kk)
                if c: S3 += (3*K*np)*2*c
                j += 1
        m[key] = (2*S3)/dd3 if dd3 != 0 else Q(0)
    A = defaultdict(dict)
    for (n, w), v in m.items():
        if v != 0: A[n][w] = int(v)
    print(name, 'totals', [sum(A[n].values()) for n in range(N+1)])
    # sector minima of F = 36n - E36(w)
    best = {}
    for n in range(N+1):
        for w, v in A[n].items():
            cl = modL(w); F = 36*n - E36(w)
            if cl not in best or F < best[cl][0]:
                best[cl] = (F, [((n, w), v)])
            elif F == best[cl][0]:
                best[cl][1].append(((n, w), v))
    OUT[name] = {str(cl): {'F': F, 'states': [[list(nw), v] for (nw, v) in st]} for cl, (F, st) in best.items()}
    print(name, 'nsectors', len(best))
json.dump(OUT, open('output/artifacts/sectors.json', 'w'))
