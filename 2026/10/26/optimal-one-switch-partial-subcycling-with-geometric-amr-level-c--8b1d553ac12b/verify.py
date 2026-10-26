"""Exact-rational checks of a one-switch AMR time-subcycling cost theorem."""
from fractions import Fraction
from itertools import product


def steps(bits, r):
    """Return update counts for levels 0..L with L fixed fine steps."""
    L = len(bits)
    n = [r**L for _ in range(L + 1)]
    for i in range(L, 0, -1):
        n[i-1] = n[i] // (r if bits[i-1] else 1)
    return n


def cost(bits, r, rho, h):
    n = steps(bits, r)
    w = [rho**i for i in range(len(n))]
    return sum(a*b for a,b in zip(n,w)) + h*sum(bits[i-1]*n[i]*w[i] for i in range(1,len(n)))


def theta(i, r, rho):
    return (Fraction(r-1,r)*sum((rho**(-j) for j in range(1,i+1)), Fraction(0)))


def claimed_suffix_cost(k, L, r, rho, h):
    return (r**k)*sum((rho**i for i in range(k+1)),Fraction(0)) + (1+h)*sum((r**i*rho**i for i in range(k+1,L+1)),Fraction(0))


def check():
    checks=0
    for r in (2,3,4):
        for rho in (Fraction(1),Fraction(2),Fraction(3),Fraction(5,2)):
            for L in range(1,9):
                thresholds=[theta(i,r,rho) for i in range(1,L+1)]
                h_values={Fraction(0),Fraction(1,1000),Fraction(1,3),Fraction(7,10),Fraction(2),Fraction(10)}
                h_values.update(thresholds)
                for t in thresholds:
                    h_values.add(t/2)
                    h_values.add(t+Fraction(1,1000))
                for h in h_values:
                    if h<0: continue
                    items=[(cost(bits,r,rho,h),bits) for bits in product((0,1),repeat=L)]
                    mincost=min(c for c,_ in items)
                    actual={bits for c,bits in items if c==mincost}
                    suffix={tuple((0,)*k+(1,)*(L-k)) for k in range(L+1) if claimed_suffix_cost(k,L,r,rho,h)==mincost}
                    assert actual==suffix,(r,rho,L,h,actual,suffix)
                    assert mincost==min(claimed_suffix_cost(k,L,r,rho,h) for k in range(L+1))
                    checks+=1
    print('EXACT_RATIONAL_ENUMERATION_PASS', checks)
    print('maximum_hierarchy_depth=8; refinement ratios=2,3,4; geometric factors=1,2,3,5/2')
    print('verification_is_finite; universal claim follows by algebraic proof')

if __name__=='__main__':
    check()
