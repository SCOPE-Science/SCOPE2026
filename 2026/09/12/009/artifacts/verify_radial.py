"""R4-corrected: radial multi-component localization recovery test (lane-1099).

Ansatz: nu^{ij}(x) = f_ij(s), s = |x|^2 (6 functions of one variable).
Then d_l nu^{ij} = 2 x_l g_ij with g_ij = f'_ij(s).
Cocycle equations E_abc(x; f(s), g(s)) = 0 must hold for ALL x on each sphere.
At fixed s, (f,g) in R^12 is s-independent on that sphere: stack 4 eqs x P
sphere points -> matrix (4P x 12); its null space = admissible (f(s),g(s)).
Inside jump: f=(1,0,..,0),g=0 must lie in null space (R1 guarantees it).
Transition requires a null vector with g01 != 0 (f01 must drop 1 -> 0).
If null space = span{e_f01, e_f23} (g = 0 forced), radial transitions are
impossible at linear order -> recovery FAILS (target blocked).
"""
import itertools, random
import sympy as sp
import numpy as np

x0, x1, x2, x3 = sp.symbols('x0 x1 x2 x3')
X = [x0, x1, x2, x3]
C1 = x0*x1; C2 = x2*x3
d1 = [sp.diff(C1, x) for x in X]; d2 = [sp.diff(C2, x) for x in X]

def sgn(p):
    p = list(p); inv = 0
    for i in range(4):
        for j in range(i+1, 4):
            if p[i] > p[j]:
                inv += 1
    return 1 if inv % 2 == 0 else -1

Pi = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        e = 0
        for k in range(4):
            for l in range(4):
                if len({i, j, k, l}) < 4:
                    continue
                e += sgn((i, j, k, l))*d1[k]*d2[l]
        Pi[i, j] = sp.expand(e)

pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
fsym = sp.symbols('f01 f02 f03 f12 f13 f23')
gsym = sp.symbols('g01 g02 g03 g12 g13 g23')
fD = dict(zip(pairs, fsym)); gD = dict(zip(pairs, gsym))
def Fget(D,i,j):
    if i == j:
        return sp.Integer(0)
    if (i,j) in D:
        return D[(i,j)]
    return -D[(j,i)]

trips = list(itertools.combinations(range(4),3))
eqs = []
for (a,b,c) in trips:
    ex = 0
    for l in range(4):
        ex += Pi[l,a]*2*X[l]*Fget(gD,b,c) + Fget(fD,l,a)*sp.diff(Pi[b,c],X[l])
        ex += Pi[l,b]*2*X[l]*Fget(gD,c,a) + Fget(fD,l,b)*sp.diff(Pi[c,a],X[l])
        ex += Pi[l,c]*2*X[l]*Fget(gD,a,b) + Fget(fD,l,c)*sp.diff(Pi[a,b],X[l])
    eqs.append(sp.expand(ex))
unknowns = list(fsym)+list(gsym)
print("unknown order:", unknowns)

def sphere_matrix(s, P, seed):
    rng = random.Random(seed)
    rows = []
    pts = 0
    while pts < P:
        v = [rng.gauss(0,1) for _ in range(4)]
        n2 = sum(t*t for t in v)
        if n2 < 1e-6:
            continue
        sc = (s/n2)**0.5
        pt = {x0:v[0]*sc, x1:v[1]*sc, x2:v[2]*sc, x3:v[3]*sc}
        for e in eqs:
            ee = sp.expand(e)
            row = []
            for u in unknowns:
                c = ee.coeff(u)
                row.append(float(c.subs(pt)))
            const = float(ee.subs({u:0 for u in unknowns}).subs(pt))
            assert abs(const) < 1e-9, const
            rows.append(row)
        pts += 1
    return np.array(rows)

for s in (0.25, 1.0, 4.0):
    M = sphere_matrix(s, 40, 1000+int(s*10))
    U, S, Vt = np.linalg.svd(M)
    print(f"--- sphere s={s}: matrix {M.shape}, sing vals:", np.round(S,3))
    tol = 1e-8
    null = Vt.T[:, S < tol]
    print(f"    nullity(tol {tol}):", null.shape[1])
    print("    null basis rows: [f01 f02 f03 f12 f13 f23 | g01 g02 g03 g12 g13 g23]")
    print(np.round(null,3))
    # transition feasibility: any null vector with |g01|>1e-6?
    feas = np.max(np.abs(null[6,:])) if null.shape[1] else 0.0
    print(f"    max |g01| over null basis: {feas:.2e} ->",
          "TRANSITION POSSIBLE" if feas > 1e-6 else "TRANSITION BLOCKED (g01 forced 0)")
print("R4-CORRECTED DONE")
