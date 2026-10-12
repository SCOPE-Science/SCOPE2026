"""Exact and independent checks for quantum average mixing on subdivided cliques.

Run: python3 verify.py   (requires SymPy and NumPy)
"""
from itertools import combinations
from math import comb
import numpy as np
import sympy as sp


def incidence(n):
    es = list(combinations(range(n), 2))
    b = sp.zeros(n, len(es))
    for col, (u, v) in enumerate(es):
        b[u, col] = b[v, col] = 1
    return b, es


def exact_projectors(n):
    b, es = incidence(n)
    m = len(es)
    p0 = sp.ones(n, n) / n
    p1 = sp.eye(n) - p0
    q = b.T * p1 * b / (n - 2)
    w = sp.eye(m) - sp.ones(m, m) / m - q
    def image_projector(p, sigma, sign):
        return (p.row_join(sign * p * b / sigma)).col_join(
            (sign * b.T * p / sigma).row_join(b.T * p * b / (sigma * sigma))) / 2
    # Form the sum of squares of paired +/- projectors without radicals.
    vv = (p0.multiply_elementwise(p0) + p1.multiply_elementwise(p1)) / 2
    ve = ((p0 * b).multiply_elementwise(p0 * b) / (2 * (2 * (n - 1)))
          + (p1 * b).multiply_elementwise(p1 * b) / (2 * (n - 2)))
    ee = ((sp.ones(m, m) / m).multiply_elementwise(sp.ones(m, m) / m)
          + q.multiply_elementwise(q)) / 2 + w.multiply_elementwise(w)
    out = vv.row_join(ve).col_join(ve.T.row_join(ee))
    # Projectors partition the identity; pairwise products vanish.
    assert p0 * p1 == sp.zeros(n, n)
    assert q * w == sp.zeros(m, m)
    assert w * w == w
    return out, b


def orbit_formula(n, b):
    m = n * (n - 1) // 2
    p = sp.Rational(n - 2, 2 * n)
    h = sp.Rational(n - 4, 2 * n * (n - 2))
    t = sp.Rational(1, n * n * (n - 1)) + sp.Rational(2, n * n * (n - 2))
    c0 = (sp.Rational(2, n*n*(n-1)**2) + sp.Rational(2, n*n)
          + sp.Rational((n-3)**2, (n-1)**2))
    c1 = (sp.Rational(2, n*n*(n-1)**2)
          + sp.Rational((n-4)**2, 2*n*n*(n-2)**2)
          + sp.Rational((n-3)**2, (n-2)**2*(n-1)**2))
    c2 = (sp.Rational(2, n*n*(n-1)**2)
          + sp.Rational(8, n*n*(n-2)**2)
          + sp.Rational(4, (n-2)**2*(n-1)**2))
    a = b.T*b - 2*sp.eye(m)
    ee = c0*sp.eye(m) + c1*a + c2*(sp.ones(m,m)-sp.eye(m)-a)
    vv = p*sp.eye(n) + sp.ones(n,n)/n**2
    ve = h*b + t*sp.ones(n,m)
    return vv.row_join(ve).col_join(ve.T.row_join(ee))


def spectral_formula(n):
    p = sp.Rational(n-2,2*n)
    r = sp.Rational((n-4)*(2*n*n-5*n-4),2*n*(n-2)**2)
    delta = sp.Rational((n-4)*(n-3),2*n*(n-2))
    eta = sp.Rational((n-3)**3+4,(n-2)**2*(n-1))
    v = [sp.Integer(1), sp.Rational(n-3,2*(n-1))]
    # Standard 2x2 block eigenvalues; exact numeric comparison for all n.
    roots = [sp.N((p+r-sp.sqrt((p+r)**2-4*delta))/2,45),
             sp.N((p+r+sp.sqrt((p+r)**2-4*delta))/2,45)]
    expected = [float(v[0]), float(v[1])] + [float(roots[0])]*(n-1) + [float(roots[1])]*(n-1)
    expected += [float(eta)]*(n*(n-3)//2)
    return sorted(expected), delta, eta


def verify_symbolic():
    x=sp.symbols('x', integer=True, positive=True)
    c0=sp.Rational(2,1)/(x*x*(x-1)**2)+sp.Rational(2,1)/(x*x)+(x-3)**2/(x-1)**2
    c1=sp.Rational(2,1)/(x*x*(x-1)**2)+(x-4)**2/(2*x*x*(x-2)**2)+(x-3)**2/((x-2)**2*(x-1)**2)
    c2=sp.Rational(2,1)/(x*x*(x-1)**2)+sp.Rational(8,1)/(x*x*(x-2)**2)+sp.Rational(4,1)/((x-2)**2*(x-1)**2)
    r=c0+(x-4)*c1-(x-3)*c2
    eta=c0-2*c1+c2
    rt= c0+2*(x-2)*c1+(x-2)*(x-3)*c2/2
    h=(x-4)/(2*x*(x-2))
    p=(x-2)/(2*x)
    assert sp.cancel(rt-(x-2)/(x-1)) == 0
    assert sp.cancel(r-(x-4)*(2*x*x-5*x-4)/(2*x*(x-2)**2)) == 0
    assert sp.cancel(eta-((x-3)**3+4)/((x-2)**2*(x-1))) == 0
    assert sp.cancel(p*r-(x-2)*h*h - (x-4)*(x-3)/(2*x*(x-2))) == 0
    print('SYMBOLIC_OK sector_identities=4')


def verify_matrices():
    matrices=0
    exact_entries=0
    for n in range(3,9):
        direct, b=exact_projectors(n)
        orbit=orbit_formula(n,b)
        assert direct == orbit, ('exact orbit failure',n)
        expected, delta, eta=spectral_formula(n)
        aa=np.zeros((n+b.cols,n+b.cols),float)
        aa[:n,n:]=np.array(b).astype(float)
        aa[n:,:n]=aa[:n,n:].T
        eig, uu=np.linalg.eigh(aa)
        independent=np.zeros_like(aa)
        for value in np.unique(np.round(eig,10)):
            cols=uu[:,np.isclose(eig,value,atol=1e-8)]
            proj=cols@cols.T
            independent+=proj*proj
        err=np.max(np.abs(independent-np.array(direct).astype(float)))
        assert err<1e-11, ('independent adjacency spectral construction',n,err)
        obs=sorted(np.linalg.eigvalsh(np.array(direct).astype(float)))
        assert len(expected)==len(obs)
        assert max(abs(u-v) for u,v in zip(expected,obs)) < 3e-12, n
        rank=np.sum(np.array(obs)>1e-9)
        assert rank==({3:3,4:7}.get(n, n+comb(n,2)))
        matrices+=1
        exact_entries+=(n+comb(n,2))**2
    print('VERIFY_OK exact_graph_orders=3..8 exact_entries=%d independent_adjacency_spectra=%d' % (exact_entries,matrices))

if __name__ == '__main__':
    verify_symbolic()
    verify_matrices()
