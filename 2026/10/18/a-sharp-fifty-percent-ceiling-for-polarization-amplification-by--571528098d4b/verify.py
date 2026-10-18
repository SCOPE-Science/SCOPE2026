"""Exact rational checks for a sharp FJ polarization-edge amplification theorem.
Run with Python 3 and SymPy: python verify_single_edge_polarization.py
"""
from fractions import Fraction
from random import Random
import sympy as sp

checks = 0

def chk(statement, desc):
    global checks
    if not statement:
        raise AssertionError(desc)
    checks += 1


def laplacian(n, edges):
    L = sp.zeros(n)
    for i, j, weight in edges:
        w = sp.Rational(weight)
        L[i, i] += w
        L[j, j] += w
        L[i, j] -= w
        L[j, i] -= w
    return L


def polarization(v):
    mean = sum(v) / len(v)
    return sp.factor(sum((a - mean)**2 for a in v))

# Independent exact inverse of the unweighted path and its new chord.
L = laplacian(4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)])
b = sp.Matrix([1, 0, -1, 0])
z = sp.Matrix([0, -1, -1, 2])
s = (sp.eye(4) + L) * z
zp = (sp.eye(4) + L + b*b.T).inv() * s
chk(list(s) == [1, -2, -4, 5], 'path innate opinions')
chk(polarization(z) == 6, 'path original polarization')
chk(polarization(zp) == sp.Rational(4941, 800), 'path updated polarization')
chk(sp.factor(polarization(zp) / polarization(z)) == sp.Rational(1647, 1600), 'amplification witness')

# Identity underlying the universal upper bound, checked symbolically.
r, tau, lam = sp.symbols('r tau lam', real=True)
poly = lam**2 - 2*(1+r+tau)/(1+r)**2 * lam + 1/(1+r)**2
certificate = ((1-3*r)**2/sp.Integer(4) + 3*(r-tau))/(1+r)**2
chk(sp.factor(poly.subs(lam, sp.Rational(3,2)) - certificate) == 0, '3/2 characteristic certificate')

# Independent exact rational graphs, comparing the full matrix with the 2D reduction.
rng = Random(521031)
for n in range(3, 9):
    for trial in range(24):
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                if rng.randrange(3):
                    edges.append((i, j, sp.Rational(rng.randint(1, 5), rng.randint(1, 4))))
        used = {(i, j) for i, j, _ in edges}
        absent = [(i, j) for i in range(n) for j in range(i+1, n) if (i,j) not in used]
        if not absent:
            # An already present connection may also be strengthened by one unit.
            i, j = 0, 1
        else:
            i, j = absent[rng.randrange(len(absent))]
        L = laplacian(n, edges)
        b = sp.zeros(n, 1)
        b[i] = 1
        b[j] = -1
        A = (sp.eye(n) + L).inv()
        v = A*b
        rr = sp.factor((b.T*A*b)[0])
        tt = sp.factor((b.T*A*A*b)[0])
        T = sp.eye(n) - v*b.T/(1+rr)
        chk(rr > 0 and tt > 0 and tt <= rr, 'PSD resolvent moments')
        chk(T*sp.ones(n,1) == sp.ones(n,1), 'mean preservation')
        chk(sp.factor(T.det()) == 1/(1+rr), 'matrix determinant lemma')
        chk(sp.factor(sp.trace(T.T*T) - (n-2) - 2*(1+rr+tt)/(1+rr)**2) == 0, 'rank-two trace identity')
        chk(sp.factor(certificate.subs({r:rr,tau:tt})) >= 0, '3/2 bound certificate')
        orig = sp.Matrix([rng.randint(-5, 5) for k in range(n)])
        if polarization(orig) == 0:
            continue
        # Any centered pre-edge vector is attainable, since innate opinions can be rescaled.
        opin = T*orig
        chk(polarization(opin) * 2 <= polarization(orig) * 3, 'finite graph polarization bound')

# Exact spectral ingredients for two weighted K_6 communities.
w = sp.symbols('w', positive=True)
a = 1 / (1+6*w)
rs = (1+5*a)/3
ts = (1+5*a**2)/3
chk(sp.factor(sp.limit(rs, w, sp.oo) - sp.Rational(1,3)) == 0, 'clique r limit')
chk(sp.factor(sp.limit(ts, w, sp.oo) - sp.Rational(1,3)) == 0, 'clique tau limit')
lamplus = (1+rs+ts + sp.sqrt((1+rs+ts)**2-(1+rs)**2))/(1+rs)**2
chk(sp.simplify(sp.limit(lamplus, w, sp.oo)-sp.Rational(3,2)) == 0, 'sharpness limit')
# Direct graph inverse checks, without using the proposed closed-form r and tau.
for weight in [1, 2, 10, 30, 100]:
    edges = [(i, j, weight) for offset in [0, 6] for i in range(offset, offset+6) for j in range(i+1, offset+6)]
    L = laplacian(12, edges)
    b = sp.zeros(12, 1)
    b[0], b[6] = 1, -1
    # In each clique, (I+L)^-1=(I + weight*6*(I-J/6))^-1.
    A = (sp.eye(12)+L).inv()
    rr = sp.factor((b.T*A*b)[0])
    tt = sp.factor((b.T*A*A*b)[0])
    chk(rr == rs.subs(w, weight), 'direct clique r check')
    chk(tt == ts.subs(w, weight), 'direct clique tau check')

print(f'PASS: {checks} symbolic, exact rational, and finite-graph checks')
print('sharp limiting squared amplification = 3/2')
