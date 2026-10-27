"""Numerical replay for the exact budgeted weighted-barbell spectral-gap formula.

The infinite-family proof is in RESULT.md; these finite checks are diagnostics.
"""
import math
import numpy as np


def formula(p, q, budget=1.0):
    assert p >= q >= 2 and budget > 0
    n = p + q
    r, s = p - 1, q - 1
    t0 = (2 * q - 1) / r
    tmin = math.sqrt(p / (2 * r))
    t = min(1.0, max(tmin, t0))
    mu = ((q + 1) * t + 2 * q - 1) / n
    D = p + 4 * q - 4 - r * r * (t - t0)**2 / n
    lam = budget / D
    a = lam * mu / t
    b = lam * (t + 2 - mu)
    h = lam * (p * mu - t)
    c = max(0.0, lam * (1 - mu / t) / r)
    return dict(t=t, mu=mu, D=D, lam=lam, a=a, b=b, h=h, c=c)


def test(p, q):
    f = formula(p, q)
    n, r, s = p + q, p - 1, q - 1
    L = np.zeros((n, n))
    def add(i, j, w):
        L[i, i] += w
        L[j, j] += w
        L[i, j] -= w
        L[j, i] -= w
    # Large side leaves 0 .. r-1, hub r; small hub p, small leaves p+1 .. n-1.
    for i in range(r): add(i, r, f['a'])
    for i in range(r):
        for j in range(i): add(i, j, f['c'])
    add(r, p, f['h'])
    for i in range(p + 1, n): add(i, p, f['b'])
    eigen = np.linalg.eigvalsh(L)
    total = np.trace(L)/2
    assert np.isclose(total, 1.0, atol=2e-12), (p,q,total)
    assert np.isclose(eigen[1], f['lam'], atol=1e-11, rtol=1e-10), (p,q,eigen[1],f)
    assert np.linalg.norm(L @ np.ones(n)) < 5e-13
    # Explicit Fiedler scalar coordinate in the four group levels.
    z = np.array([0.0] * r + [f['t'],f['t']+1] + [f['t']+2]*s)
    z -= z.mean()
    assert np.linalg.norm(L @ z - f['lam']*z) < 1e-10
    assert f['a'] > 0 and f['b'] > 0 and f['h'] > 0 and f['c'] >= 0
    t,mu,D = f['t'],f['mu'],f['D']
    actual_D = np.dot(z,z) + r*(1-t*t)
    assert np.isclose(actual_D,D,atol=1e-10), (p,q,actual_D,D)
    # Clique-edge length feasibility in the simplex part.
    if r>1:
        sq = 2*r*(1-t*t)/(r-1)
        assert sq<=1+1e-12, (p,q,sq)
        if f['c']>1e-12: assert abs(sq-1)<1e-10
    if f['c']>1e-12: assert p*(p-1)>2*(2*q-1)**2
    return f


def main():
    cases=0
    for p in range(2, 51):
        for q in range(2, p+1):
            test(p,q)
            cases+=1
    print('PASS:',cases,'weighted barbell graph sizes, budgets, algebraic connectivity and dual identities')
    for p,q in [(3,3),(5,2),(8,3),(9,3),(11,4),(30,10)]:
        f=test(p,q)
        print(f'p={p}, q={q}: t={f["t"]:.9g}, D={f["D"]:.9g}, gap={f["lam"]:.9g}, inner-large-weight={f["c"]:.9g}')

if __name__=='__main__':
    main()
