"""Finite rational and independent low-dimensional convex-hull tests.
Analytical arguments in RESULT.md establish the infinite-dimensional claims.
Requires Python >=3.10; hull tests require numpy and scipy.
"""
from fractions import Fraction
from math import comb, factorial, sqrt, prod


def rational_certificates():
    odd_checks = even_checks = 0
    for m in range(1, 11):
        b = Fraction(comb(2*m, m), 4**m)
        q = (2*m+1)*b*b
        p = 2*m*b*b
        ao = (1-Fraction(1, 4*m+2))**(2*m)
        ae = (1-Fraction(1, 4*m-2))**(2*m-1)
        assert q > ao  # m=1..4 needed explicitly; extra cases cross-check.
        assert (p == ae if m == 1 else (p < ae if m in (2, 3) else p > ae))
        assert q == prod((1-Fraction(1, 4*j*j) for j in range(1, m+1)), start=Fraction(1))
        odd_checks += 1
        even_checks += 1
    assert Fraction(1)+Fraction(5,11)+Fraction(5,11)**2/2+Fraction(5,11)**3/6 > Fraction(11,7)
    assert Fraction(1)+Fraction(1,2)+Fraction(1,8)+Fraction(1,48) > Fraction(23,14)
    assert Fraction(22,23)*Fraction(7,11) == Fraction(14,23)
    return odd_checks, even_checks


def independent_hulls():
    import numpy as np
    from scipy.spatial import ConvexHull
    tested=0
    for n in range(3, 9):
        # Compute an orthonormal basis of the zero-sum hyperplane.
        a = np.eye(n)[:, :n-1]-np.eye(n)[:, -1, None]
        basis,_ = np.linalg.qr(a)
        basis = basis[:, :n-1]
        e = np.eye(n)-np.ones((n,n))/n
        verts = np.concatenate((e @ basis, -e @ basis),axis=0)
        hull=ConvexHull(verts, qhull_options='Qx')
        d=n-1
        volume=second=0.0
        mean=np.zeros(d)
        for inds in hull.simplices:
            v=verts[inds,:]
            simplex_volume=abs(np.linalg.det(v))/factorial(d)
            s=v.sum(axis=0)
            norm2=(np.sum(v*v)+s@s)/((d+1)*(d+2))
            volume+=simplex_volume
            second+=simplex_volume*norm2
            mean+=simplex_volume*s/(d+1)
        exact_volume=sqrt(n)*comb(d,d//2)/factorial(d)
        exact_second=(d*(2*n-1)/(n*n*(n+1))) if n%2 else ((2*n-3)/(n*(n+1)))
        assert abs(volume-exact_volume)<1e-10
        assert abs(second/volume-exact_second)<1e-10
        assert np.linalg.norm(mean/volume)<1e-10
        tested+=1
    return tested


if __name__ == '__main__':
    oc,ec=rational_certificates()
    hc=independent_hulls()
    print(f'CHECK_OK odd_exact={oc} even_exact={ec} independent_hulls={hc} (+ analytical infinite proof)')
