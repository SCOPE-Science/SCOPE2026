"""Finite numerical checks for homogeneous-tree path summation.

Pure Python 3 standard library. Run: python verify_tree_hardy.py
This script tests finite matrices and asymptotic residuals; it does not
replace the proofs for every branching factor, exponent, and height.
"""
from decimal import Decimal, localcontext
from math import sqrt


def small_root_and_eigenvalue(b, n):
    assert b >= 2 and n >= 5
    with localcontext() as c:
        c.prec = 90
        B = Decimal(b)
        q = B ** (-(n + 1))
        a = B - 1
        def F(t):
            return t * ((1 - t) ** (2*n+1) + B*q) - a*q
        lo = Decimal(0)
        hi = 2*a*q
        assert F(lo) < 0 < F(hi), (b, n)
        for _ in range(320):
            mid = (lo + hi)/2
            if F(mid) > 0:
                hi = mid
            else:
                lo = mid
        t = (lo + hi)/2
        lam = t*(a-B*t)/(1-t)
        return lam, q


def eigen_norm_by_matrix_power(b, n, iterations=500):
    """Evaluate H*H by forward ancestor sums, then backward subtree sums."""
    parents = [-1]
    layers = [[0]]
    for depth in range(2, n+1):
        nodes=[]
        for u in layers[-1]:
            for _ in range(b):
                nodes.append(len(parents))
                parents.append(u)
        layers.append(nodes)
    # This is a single root-child branch; the complete tree has b identical blocks.
    m=len(parents)
    g = [1.0/sqrt(m)]*m
    for _ in range(iterations):
        f=[0.0]*m
        for j,p in enumerate(parents):
            f[j]=g[j]+(f[p] if p>=0 else 0.0)
        h=f[:]
        for j in range(m-1,0,-1):
            h[parents[j]]+=h[j]
        norm=sqrt(sum(x*x for x in h))
        g=[x/norm for x in h]
    f=[0.0]*m
    for j,p in enumerate(parents):
        f[j]=g[j]+(f[p] if p>=0 else 0.0)
    return sqrt(sum(x*x for x in f))


def lp_upper_lower(b, n, p):
    S=0.0
    lower_numer=0.0
    upper_power=0.0
    for j in range(1,n+1):
        S+=b**(-j/(p-1.0))
        lower_numer+=b**j*S**p
        upper_power+=b**j*S**(p-1)
    return (lower_numer/S)**(1.0/p), upper_power**(1.0/p)


def check():
    assertions=0
    for b in (2,3,4):
        for n in (5,6,7,9):
            lam,q=small_root_and_eigenvalue(b,n)
            direct=eigen_norm_by_matrix_power(b,n)
            expected=1.0/sqrt(float(lam))
            assert abs(direct/expected-1.0)<1e-11, (b,n,direct,expected)
            assertions+=1
    for b in (2,3,5):
        for n in (10,15,20,30,40):
            lam,q=small_root_and_eigenvalue(b,n)
            q=float(q); lam=float(lam)
            lam_scale=(b-1)**2*q
            expected=lam_scale*(1+(2*n*(b-1)-2)*q)
            # A fixed-b analytic expansion with O_b(n^2 q^2) relative error.
            relative_residual=abs(lam/lam_scale-expected/lam_scale)
            assert relative_residual <= 100*b*b*n*n*q*q,(b,n,relative_residual)
            assertions+=1
    for b in (2,3,5):
        for p in (1.5,2.0,3.0,5.0):
            target=((b-1)*(b**(1/(p-1))-1)**(p-1))**(-1/p)
            prev_lower=0
            for n in (10,30,80):
                low,high=lp_upper_lower(b,n,p)
                norm_factor=b**((n+1)/p)
                low/=norm_factor; high/=norm_factor
                assert low<=high*(1+1e-12),(b,n,p,low,high)
                assert high <= target*(1+0.2),(b,n,p,high,target)
                assert low <= target*(1+0.2),(b,n,p,low,target)
                assert low>=prev_lower*(1-0.02),(b,n,p,prev_lower,low)
                prev_lower=low
                assertions+=4
            # At sufficiently great depth the rigorous two-sided bounds pin
            # down the same normalizing constant.
            assert abs(high-target)/target<0.018, (b,p,high,target)
            assert abs(low-target)/target<0.018, (b,p,low,target)
            assertions+=2
    print('PASS: {} finite numerical consistency assertions.'.format(assertions))
    print('These calculations do not certify the infinite-depth theorems.')

if __name__=='__main__':
    check()
