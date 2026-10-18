"""Independent finite exact integration checks for circular Voronoi cell-threshold dependence.

Run: python3 check_voronoi.py
Uses only the Python standard library. The infinite-size assertions rely on the
proof in RESULT.md, not on these finite checks.
"""
from fractions import Fraction as F
from math import comb, exp
from decimal import Decimal, localcontext


def power_poly(c, d, k):
    """Coefficients of (c+d*x)^k over the rationals."""
    return [F(comb(k, j))*c**(k-j)*d**j for j in range(k+1)]


def multiply(p, q):
    r = [F(0)] * (len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return r


def integrate_poly(p, a, b):
    return sum((v * (b**(j+1)-a**(j+1)) / (j+1) for j, v in enumerate(p)), F(0))


def direct_marginal(n, q):
    if n == 2:
        return F(1) if q<1 else F(0)
    p = multiply([F(0),F((n-1)*(n-2))], power_poly(F(1),F(-1),n-3))
    return integrate_poly(p,q,F(1))


def direct_adjacent(n,q):
    if n==2:
        return F(1) if q<1 else F(0)
    poly1 = [F(n-1)*x for x in power_poly(F(1),F(-1),n-2)]
    part1 = integrate_poly(poly1,q,F(1))
    lo=max(F(0),2*q-1)
    poly2=[F(n-1)*x for x in power_poly(1-2*q,F(1),n-2)]
    part2=integrate_poly(poly2,lo,q) if lo<q else F(0)
    return part1+part2


def direct_disjoint(n,q):
    assert n>=4
    if q>=F(1,2):return F(0)
    if n==4:
        poly=multiply([F(0),F(6)],power_poly(F(1),F(-1),1))
    else:
        # Marginal density of the first two-gap sum multiplied by
        # conditional beta survival for the second, disjoint two-gap sum.
        poly=multiply(multiply([F(0),F((n-1)*(n-2))],power_poly(1-q,F(-1),n-4)),
                      [1+(n-4)*q,F(-1)])
    return integrate_poly(poly,q,1-q)


def closed_marginal(n,q):
    return (1-q)**(n-2)*(1+(n-2)*q)


def closed_adjacent(n,q):
    return 2*(1-q)**(n-1)-max(F(0),1-2*q)**(n-1)


def closed_disjoint(n,q):
    z=max(F(0),1-2*q)
    return (z**(n-1)+2*(n-1)*q*z**(n-2)+(n-1)*(n-2)*q*q*z**(n-3))


def main():
    tested = 0
    signs = 0
    for n in range(3,23):
        for den in (7,11,16):
            for num in range(1,den):
                q=F(num,den)
                p=closed_marginal(n,q)
                ja=closed_adjacent(n,q)
                assert direct_marginal(n,q)==p,(n,q,'marginal')
                assert direct_adjacent(n,q)==ja,(n,q,'adjacent')
                tested+=2
                ca=ja-p*p
                if n==3: assert ca<0
                if n==4:
                    assert (ca==0)==(q==F(1,2))
                    assert ca>=0
                    expect=(q**3*(2-q)*(1-2*q)**2 if q<=F(1,2)
                            else (1-q)**3*(1+q)*(2*q-1)**2)
                    assert ca==expect
                if n>=5: assert ca>0
                signs+=1
                if n>=4:
                    jd=closed_disjoint(n,q)
                    assert direct_disjoint(n,q)==jd,(n,q,'disjoint')
                    assert jd-p*p<0,(n,q,'disjoint sign')
                    tested+=1;signs+=1
    # Dirichlet component moment check: adjacent, diagonal, disjoint linear covariances.
    for n in range(4,40):
        var=(n-2)/(2*n*n*(n+1))
        cov_adj=(n-4)/(4*n*n*(n+1))
        cov_non=-1/(n*n*(n+1))
        assert var>0 and cov_non<0
        if n==4: assert cov_adj==0
        else: assert cov_adj>0
    # Exact two-seed degeneration.
    assert direct_adjacent(2,F(1,3))==1
    # Poisson limit for the adjacent upper-tail covariance.
    import math
    for x in (0.2,0.8,1.5,3.0):
        with localcontext() as ctx:
            ctx.prec=90
            xd=Decimal(str(x)); n=Decimal(25000)
            q=xd/n
            a=(1-q)**(int(n)-2)*(1+(n-2)*q)
            j=2*(1-q)**(int(n)-1)-(1-2*q)**(int(n)-1)
            cadj=j-a*a
            jd=(1-2*q)**(int(n)-1)+2*(n-1)*q*(1-2*q)**(int(n)-2)+(n-1)*(n-2)*q*q*(1-2*q)**(int(n)-3)
            cnon=jd-a*a
            target_adj=math.exp(-2*x)*(2*math.exp(x)-2-2*x-x*x)
            target_non=-x**4*math.exp(-2*x)
            assert abs(float(cadj)-target_adj)<2e-4
            assert abs(float(n*cnon)-target_non)<5e-4
    print('PASS:',tested,'exact closed-form/integration equalities;', signs,
          'strict-sign checks; 36 moment-sign checks; 8 asymptotic comparisons.')

if __name__=='__main__':main()
