"""Q_L-correct string extraction: classes mod 2Q_L = 2Z a1 + 6Z a2.
A_n(w) = c_[w](n - |w|^2/4). Check consistency per class; extract vacuum c^0_0."""
from fractions import Fraction as Q
from collections import defaultdict
import json
G = [[Q(2), Q(-1)], [Q(-1), Q(2, 3)]]
def dot(u, v):
    return G[0][0]*u[0]*v[0] + G[0][1]*u[0]*v[1] + G[1][0]*u[1]*v[0] + G[1][1]*u[1]*v[1]
def add(u, v): return (u[0]+v[0], u[1]+v[1])
def mul(s, u): return (s*u[0], s*u[1])
def E36(w):
    x, y = w; return 18*x*x - 18*x*y + 6*y*y
def modL(w): return (w[0] % 2, w[1] % 6)
POS = [(1,0),(1,3),(2,3),(0,1),(1,1),(1,2)]
ALLR = POS + [(-a,-b) for (a,b) in POS]
RHO = (3,5); KPL = 6; K = 2
N = 8; B = 18
Lam = (0,0)
keys = []
for n in range(N+1):
    for a in range(-B, B+1):
        for b in range(-B, B+1):
            keys.append((n, (a,b)))
keys.sort(key=lambda k: (k[0], (Lam[0]-k[1][0])+(Lam[1]-k[1][1])))
m = {(0, Lam): Q(1)}
base = dot(add(Lam, RHO), add(Lam, RHO))
def dot3(u, v): return 6*u[0]*v[0]-3*u[0]*v[1]-3*u[1]*v[0]+2*u[1]*v[1]
base3 = dot3(RHO, RHO)
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
print('grade totals:', [sum(A[n].values()) for n in range(N+1)])
c = defaultdict(dict); conf = []
for n in range(N+1):
    for w, v in A[n].items():
        cl = modL(w); e = 36*n - E36(w)
        if e < 0: conf.append(('neg', n, w)); continue
        if e in c[cl]:
            if c[cl][e] != v: conf.append(('mm', cl, e, c[cl][e], v, (n, w)))
        else: c[cl][e] = v
print('nconf', len(conf), conf[:6])
print('nclasses', len(c))
for cl in sorted(c):
    es = sorted(c[cl])
    print('class', cl, [(e, c[cl][e]) for e in es if e <= 200][:12])
json.dump({str(cl): {str(e): c[cl][e] for e in sorted(c[cl])} for cl in c},
          open('output/artifacts/stringQL.json', 'w'))
