"""Independent numerical and rational checks for the finite radiation mobility-share theorem.

Run with Python 3: python verify.py
No third-party packages or external data are used.
"""
from fractions import Fraction
import math
import random


def probability(m, a, n, c):
    total = a + n + c
    return n * m * (m + total) / (total * (m + a) * (m + a + n))


def derivative_numerator(m, a, n, c):
    b = a + n
    total = b + c
    return (a-c)*m*m + 2*a*b*m + total*a*b


def optimum(a, n, c):
    assert a > 0 and n > 0 and c > a
    b = a + n
    return (a*b + math.sqrt(a*b*c*(n+c))) / (c-a)


def maximal_ratio(a, n, c):
    b = a + n
    return ((math.sqrt(b*(n+c)) - math.sqrt(a*c))/n)**2


def check_exact_example():
    a, n, c, m = (Fraction(v) for v in (1,1,8,2))
    P = probability(m, a, n, c)
    assert P == Fraction(1,5)
    assert derivative_numerator(m,a,n,c)==0
    assert n/(a+n+c)==Fraction(1,10)
    raw=[]
    before=Fraction(0)
    for destination in (a,n,c):
        raw.append(m*destination/((m+before)*(m+before+destination)))
        before+=destination
    scale=(m+before)/before
    assert [z*scale for z in raw]==[Fraction(2,5),Fraction(1,5),Fraction(2,5)]
    assert sum(raw)==before/(m+before)
    # The unique above-baseline crossover occurs at m=ab/(c-a)=2/7.
    assert probability(Fraction(2,7),a,n,c)==Fraction(1,10)
    print('exact three-destination example, finite normalization: passed')


def check_random():
    rng=random.Random(6814221)
    for _ in range(4200):
        a=10**rng.uniform(-1.3,2)
        n=10**rng.uniform(-1.2,2)
        c=10**rng.uniform(-1.3,2)
        m=10**rng.uniform(-2,3)
        S=a+n+c
        p=probability(m,a,n,c)
        eq=n/S
        assert 0 < p < 1
        # identity furnishing the exact comparison with the large-origin baseline
        diff = ((c-a)*m-a*(a+n))/((m+a)*(m+a+n))
        assert math.isclose(p/eq-1, diff, rel_tol=1e-8,abs_tol=1e-11)
        # derivative's sign is independently checked via a symmetric difference
        h=m*1e-5
        numeric=(probability(m+h,a,n,c)-probability(m-h,a,n,c))/(2*h)
        exact=eq*derivative_numerator(m,a,n,c)/((m+a)**2*(m+a+n)**2)
        assert math.isclose(numeric,exact,rel_tol=7e-6,abs_tol=1e-10)
        if c>a:
            ms=optimum(a,n,c)
            assert math.isclose(derivative_numerator(ms,a,n,c),0.0,abs_tol=2e-7*max(1,ms*ms*(c-a)))
            at=probability(ms,a,n,c)
            assert at>eq
            assert at>probability(ms/2,a,n,c)
            assert at>probability(ms*2,a,n,c)
            assert math.isclose(at/eq,maximal_ratio(a,n,c),rel_tol=1e-8,abs_tol=1e-10)
        else:
            assert derivative_numerator(m,a,n,c)>0
            assert p<eq
    print('4200 randomized parameter and derivative identities: passed')


def check_boundaries():
    a,n=2.,3.
    for eps in (1e-2,1e-3,1e-4):
        c=a+eps
        ms=optimum(a,n,c)
        ratio=maximal_ratio(a,n,c)
        assert abs(ms*eps/(2*a*(a+n))-1)<0.008
        assert abs((ratio-1)*4*a*(a+n)/(eps*eps)-1)<0.015
    for m in (0.2,1,5,100):
        assert probability(m,0,2,5)>probability(m*2,0,2,5)
        assert probability(m,2,3,2)<probability(m*2,2,3,2)
        assert probability(m,2,3,0)<probability(m*2,2,3,0)
        assert probability(m,0,2,0)==1
    print('boundary cases and critical onset: passed')


if __name__=='__main__':
    check_exact_example()
    check_random()
    check_boundaries()
    print('ALL CHECKS PASSED')
