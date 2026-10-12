"""Finite cross-checks for Poisson-order modal-scale identities.

Usage: python3 verify.py
Only Python 3 standard library is required. This verifies finite algebraic
instances, not the infinite asymptotic theorem proved in RESULT.md.
"""
from fractions import Fraction
from math import comb, factorial, log, pi, sqrt, isclose


def h_recurrence(k, rate, last):
    """Return exp(k*rate) times the compound Poisson masses, via pgf derivative."""
    a = [Fraction(1)]
    for n in range(1, last + 1):
        a.append(rate * sum(j * a[n-j] for j in range(1, min(k, n)+1)) / n)
    return a


def h_product(k, rate, last):
    """Independently multiply exp(rate*z^j) truncations for j=1,...,k."""
    a = [Fraction(0)] * (last + 1)
    a[0] = Fraction(1)
    for j in range(1, k+1):
        b = [Fraction(0)] * (last + 1)
        for i, old in enumerate(a):
            if not old:
                continue
            term = Fraction(1)
            for m in range(0, (last-i)//j + 1):
                b[i+j*m] += old*term
                term *= rate / (m+1)
        a = b
    return a


def q(k, rate):
    """The polynomial h_k(k;rate), independent finite combinatorial formula."""
    return sum((Fraction(comb(k-1, m-1)) * rate**m / factorial(m)
                for m in range(1,k+1)), Fraction(0))


def q_float(k, rate):
    """Nonoverflowing positive-series calculation of Q_k."""
    term = rate
    out = term
    for m in range(1, k):
        term *= (k-m)*rate / (m*(m+1))
        out += term
        if term < 1e-17*out:
            break
    return out


def root_r(k):
    lo, hi = 0., 1.
    assert q_float(k,lo) < 1 < q_float(k,hi)
    for _ in range(85):
        mid = (lo+hi)/2
        if q_float(k,mid)>1:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def F(u):
    term = u
    val = term
    for m in range(1,1000):
        term *= u/(m*(m+1))
        val += term
        if term < 1e-16*val:
            break
    return val


def check():
    trials=0
    for k in range(2,10):
        for a,b in ((1,10),(1,4),(2,5),(3,2)):
            lam=Fraction(a,b)
            R=h_recurrence(k,lam,3*k+2)
            P=h_product(k,lam,3*k+2)
            assert R==P,(k,lam)
            assert R[k]==q(k,lam)
            trials+=1
    k,lam =15,Fraction(501,2000)
    R=h_recurrence(k,lam,25)
    P=h_product(k,lam,25)
    assert R==P
    assert R[15] < 1 < R[25]
    assert R[15]==q(15,lam)
    print('k15 rate=501/2000: exact h15=',float(R[15]),' exact h25=',float(R[25]))
    roots=[]
    for k in (2,3,4,10,15,50,100,1000,10000):
        r=root_r(k)
        roots.append(r)
        assert abs(q_float(k,r)-1)<4e-13
        u=k*r
        ff=F(u)
        assert k<=ff+1e-8
        assert ff-k <= (u/(2*k))*ff + 1e-8
        L=log(k)
        asym= (L-(log(L)/2)+log(2*sqrt(2*pi)))**2/(4*k) if k>=2 else 0
        print('k=',k,'r=',format(r,'.12g'),'asym_pt=',format(asym,'.12g'),'F_bound_ratio=',format((ff-k)/ff,'.4g'))
    assert all(a>b for a,b in zip(roots,roots[1:])),roots
    assert abs(roots[0]-(sqrt(3)-1)) < 1e-13
    print('VERIFY_OK rational_coefficient_comparisons=',trials,
          'exact_k15_obstruction=True root_monotonicity_finite=True Bessel_series_bounds_finite=True')

if __name__=='__main__':
    check()
