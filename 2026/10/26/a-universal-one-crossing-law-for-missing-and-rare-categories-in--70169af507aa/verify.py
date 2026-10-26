"""Exact finite checks for the Dirichlet-multinomial vacancy/frequency crossing law."""
from fractions import Fraction
from math import factorial, comb
from itertools import product

def rise(x, n):
    value = Fraction(1)
    for j in range(n):
        value *= x + j
    return value

def weak_compositions(n, m):
    if m == 1:
        yield (n,)
    else:
        for t in range(n + 1):
            for suffix in weak_compositions(n - t, m - 1):
                yield (t,) + suffix

def dm_probability(counts, alpha):
    n = sum(counts)
    numerator = Fraction(factorial(n), 1)
    for k, a in zip(counts, alpha):
        numerator *= rise(a, k) / factorial(k)
    return numerator / rise(sum(alpha), n)

def check():
    checks = 0
    cases = [
        [Fraction(1), Fraction(1), Fraction(1)],
        [Fraction(1, 2), Fraction(3, 2), Fraction(2, 3)],
        [Fraction(2), Fraction(1), Fraction(3)],
        [Fraction(1), Fraction(2), Fraction(3), Fraction(1)],
        [Fraction(2, 3), Fraction(4, 3), Fraction(1), Fraction(5, 2)],
    ]
    for alpha in cases:
        m = len(alpha)
        T = sum(alpha)
        a, b = alpha[:2]
        c = T - a - b
        for n in range(1, 9):
            probabilities = [(counts, dm_probability(counts, alpha)) for counts in weak_compositions(n, m)]
            assert sum(p for _, p in probabilities) == 1
            checks += 1
            pA = sum(p for counts, p in probabilities if counts[0] == 0)
            assert pA == rise(T - a, n) / rise(T, n)
            checks += 1
            for r in range(1, n + 1):
                pB = sum(p for counts, p in probabilities if counts[1] == r)
                pAB = sum(p for counts, p in probabilities if counts[0] == 0 and counts[1] == r)
                formulaB = Fraction(comb(n, r)) * rise(b, r) * rise(T - b, n - r) / rise(T, n)
                formulaAB = Fraction(comb(n, r)) * rise(b, r) * rise(c, n - r) / rise(T, n)
                assert pB == formulaB and pAB == formulaAB
                checks += 2
                Q = pAB / (pA * pB)
                q_formula = rise(c, n-r)*rise(T, n)/(rise(T-b,n-r)*rise(T-a,n))
                assert Q == q_formula
                checks += 1
                if n > r:
                    q_prev = rise(c, n-r-1)*rise(T, n-1)/(rise(T-b,n-r-1)*rise(T-a,n-1))
                    step = (c+n-r-1)*(T+n-1)/((T-b+n-r-1)*(T-a+n-1))
                    assert Q == q_prev * step and 0 < step < 1
                    checks += 2
    for m in range(3, 40):
        for r in range(1, 9):
            T=Fraction(m); a=b=Fraction(1); c=T-a-b
            for n in range(r, r*m+r+3):
                Q = rise(c, n-r)*rise(T,n)/(rise(T-b,n-r)*rise(T-a,n))
                delta=Q-1
                explicit=Fraction(r*(m-1)-n,(m-1)*(m+n-r-2))
                assert delta == explicit
                checks += 1
    try:
        import mpmath as mp
        mp.mp.dps = 65
        for alpha, r in [('0.5', 2), ('1.5', 3), ('3.2', 1), ('0.2', 4)]:
            for u in (-3,0,3):
                for m in (1000,2000):
                    a=mp.mpf(alpha); T=m*a; c=(m-2)*a
                    n=r*m+u
                    val=mp.loggamma(c+n-r)-mp.loggamma(c)+mp.loggamma(T+n)-mp.loggamma(T)-mp.loggamma(T-a+n-r)+mp.loggamma(T-a)-mp.loggamma(T-a+n)+mp.loggamma(T-a)
                    predicted=-(a*u+r*(a+1)/2)/(a+r)
                    assert abs(val*m*m-predicted) < mp.mpf('0.03')
                    checks += 1
    except ImportError:
        pass
    print(f"PASS {checks} exact or high-precision assertions")

if __name__ == '__main__':
    check()
