"""Diagnostic numerical checks of finite Cesaro singular bulk law.

Python 3 standard library only. Results are finite diagnostics, not the proof.
"""
from math import asin, cos, log, pi, sin, sqrt


def cdf(t):
    if t <= 0:
        return 0.0
    if t >= 2:
        return 1.0
    return (2/pi)*asin(t/2)+(t/pi)*log((2+sqrt(4-t*t))/t)


def sturm(eig, d, e):
    """Count negative eigenvalues of a symmetric tridiagonal minus eig I."""
    q = d[0]-eig
    tiny = 1e-25
    if abs(q) < tiny:
        q = -tiny
    neg = int(q < 0)
    for i in range(1, len(d)):
        q = d[i]-eig-e[i-1]*e[i-1]/q
        if abs(q) < tiny:
            q = -tiny
        neg += (q < 0)
    return neg


def singulars_bidiagonal(diag, subdiag):
    n = len(diag)
    # B.T B: d_i=b_i^2+c_{i+1}^2, offdiag_i=b_{i+1}c_{i+1}.
    d = [diag[i]**2 + (subdiag[i]**2 if i < n-1 else 0.0) for i in range(n)]
    e = [diag[i+1]*subdiag[i] for i in range(n-1)]
    # Gershgorin upper bound, nonnegative lower bound.
    upper = max(d[i]+(abs(e[i-1]) if i else 0)+(abs(e[i]) if i<n-1 else 0)
                for i in range(n))+1
    out = []
    for rank in range(1,n+1):
        lo, hi = 0.0, upper
        for _ in range(70):
            mid = (lo+hi)*0.5
            if sturm(mid,d,e) >= rank:
                hi = mid
            else:
                lo = mid
        out.append(sqrt(max(0.0,(lo+hi)*0.5)))
    return out


def w1_grid(vals, steps=10000):
    # Integrate absolute difference in CDFs over common support [0,2]
    vals = sorted(vals)
    p = 0
    total = 0.0
    for k in range(steps):
        t = 2*(k+.5)/steps
        while p<len(vals) and vals[p]<=t:
            p+=1
        total += abs(p/len(vals)-cdf(t))*(2/steps)
    return total


def run():
    for ell in range(1,23):
        vals=singulars_bidiagonal([1.0]*ell,[-1.0]*(ell-1))
        exact=[2*sin((2*k-1)*pi/(4*ell+2)) for k in range(1,ell+1)]
        assert max(abs(a-b) for a,b in zip(vals,exact)) < 3e-7, ell
    for n in (1,2,3,4,8,16,24,40,64):
        diag=[i/n for i in range(1,n+1)]
        subdiag=[-i/n for i in range(1,n)]
        vals=singulars_bidiagonal(diag,subdiag)
        assert all(0<=v<=2+1e-8 for v in vals)
        distance=w1_grid(vals)
        # numerical quadrature error O(steps^-1), dwarfed by bound.
        assert distance <= 12/sqrt(n)+2e-4,(n,distance)
        print(f"n={n:3d} W1_numeric={distance:.7f} bound={12/sqrt(n):.7f}")
    print("FINITE_DIAGNOSTICS_OK")

if __name__=='__main__':
    run()
