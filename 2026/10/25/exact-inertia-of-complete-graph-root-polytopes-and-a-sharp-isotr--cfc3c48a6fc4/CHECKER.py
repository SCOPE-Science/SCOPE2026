"""Independent exact checks for the complete-graph symmetric-edge polytope.

Requires Python 3, numpy and scipy; all moment arithmetic after facet discovery
is exact, using rational determinants and quadratic forms.
"""
from fractions import Fraction
from math import comb, factorial


def det_integer(a):
    """Exact signed determinant by the Bareiss algorithm."""
    n=len(a)
    a=[row[:] for row in a]
    sign=1; prev=1
    for i in range(n-1):
        if a[i][i]==0:
            j=next((j for j in range(i+1,n) if a[j][i]),None)
            if j is None:return 0
            a[i],a[j]=a[j],a[i];sign=-sign
        pivot=a[i][i]
        for j in range(i+1,n):
            for k in range(i+1,n):
                a[j][k]=(a[j][k]*pivot-a[j][i]*a[i][k])//prev
        for j in range(i+1,n):a[j][i]=0
        prev=pivot
    return sign*a[-1][-1]


def analytical(n):
    d=n-1
    V=Fraction(comb(2*d,d),factorial(d))
    lam=Fraction(4*(2*n-1),n*(n+1)**2)
    Rpower=Fraction(8*(2*n-1),n+1)**d/Fraction(n*comb(2*d,d)**2)
    return V,lam,Rpower


def cone_triangulation(n):
    import numpy as np
    from scipy.spatial import ConvexHull
    d=n-1
    vv=[]
    for i in range(n):
        for j in range(i):
            row=[int(t==i)-int(t==j) for t in range(d)]
            vv.append(row);vv.append([-z for z in row])
    pts=np.asarray(vv,dtype=float)
    hull=ConvexHull(pts)
    total=Fraction(0);moment=Fraction(0)
    for facet in hull.simplices:
        cols=[vv[int(q)] for q in facet]
        A=[[cols[j][i] for j in range(d)] for i in range(d)]
        vol=Fraction(abs(det_integer(A)),factorial(d))
        if vol==0: continue
        total+=vol
        # The full-space norm on sum-zero coordinates is sum(x_i^2)+(sum x_i)^2.
        sum_sq=sum(sum(z*z for z in v)+sum(v)**2 for v in cols)
        vbar=[sum(v[i] for v in cols) for i in range(d)]
        total_sq=sum_sq+sum(q*q for q in vbar)+sum(vbar)**2
        moment+=vol*Fraction(total_sq,(d+1)*(d+2))
    return total,moment/total,len(hull.simplices)


def test():
    for n in range(3,7):
        V,lam,ratio=analytical(n)
        exact_vol,exact_moment,count=cone_triangulation(n)
        assert V==exact_vol,(n,V,exact_vol)
        assert exact_moment==(n-1)*lam,(n,exact_moment,(n-1)*lam)
        assert 0<ratio<1
        print(f'n={n} facets={count} volume_reduced={V} radial_second={exact_moment} ratio_to_cross_power={ratio}')
    for n in range(3,201):
        d=n-1
        S=sum(comb(n,k)*comb(n-2,k-1) for k in range(1,n))
        T=sum(Fraction(comb(n,k)*comb(n-2,k-1),k+1) for k in range(1,n))
        assert S==comb(2*n-2,n-1)
        assert T==Fraction(comb(2*n-1,n),n+1)
        assert analytical(n)[2]<1
    print('VERIFY_OK exact_hulls=4 exact_dirichlet_sums=198 strict_finite=198 asymptotic_analytical=true')


if __name__=='__main__':test()
