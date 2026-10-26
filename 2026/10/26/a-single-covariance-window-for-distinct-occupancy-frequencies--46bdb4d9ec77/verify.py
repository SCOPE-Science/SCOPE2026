"""Exact independent checks for cross-frequency occupancy covariance.

Requires only the Python standard library. Execute: python verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb

checks = 0


def fall(n, k):
    answer = 1
    for t in range(k):
        answer *= n - t
    return answer


def moments(n, m, r, s):
    a = Fraction(m-1,m)
    b = Fraction(m-2,m)
    pr = Fraction(comb(n,r),m**r)*a**(n-r)
    ps = Fraction(comb(n,s),m**s)*a**(n-s)
    prs = Fraction(comb(n,r)*comb(n-r,s),m**(r+s))*b**(n-r-s)
    return m*pr, m*ps, m*(m-1)*prs


def ratio(n,m,r,s):
    return Fraction(fall(n-r,s)*m**(n-1)*(m-2)**(n-r-s),
                    fall(n,s)*(m-1)**(2*n-r-s-1))


# Independent direct enumeration of allocations, not using the moment formula.
for m in range(3,6):
    for n in range(2,8):
        histogram = Counter()
        for assignment in product(range(m), repeat=n):
            loads = Counter(assignment)
            hist = Counter(loads.values())
            histogram[tuple(hist.get(k,0) for k in range(1,n+1))] += 1
        total = m**n
        for r in range(1,n):
            for s in range(r+1,n+1):
                if r+s>n:
                    continue
                x = sum(c*vec[r-1] for vec,c in histogram.items())
                y = sum(c*vec[s-1] for vec,c in histogram.items())
                xy = sum(c*vec[r-1]*vec[s-1] for vec,c in histogram.items())
                er,es,ers = moments(n,m,r,s)
                assert Fraction(x,total)==er
                assert Fraction(y,total)==es
                assert Fraction(xy,total)==ers
                assert ers/(er*es)==ratio(n,m,r,s)
                checks+=4

# Independent two-formula adjacent-ratio checks across a broader parameter grid.
for m in range(3,12):
    for r in range(1,9):
        for s in range(r+1,12):
            for n in range(r+s,r+s+14):
                t = ratio(n,m,r,s)
                tnext = ratio(n+1,m,r,s)
                q = Fraction(m*(m-2),(m-1)**2)
                adjacent = q*(1+Fraction(r*s,(n+1)*(n+1-r-s)))
                assert tnext/t==adjacent
                assert ratio(n+2,m,r,s)/tnext<adjacent
                checks+=2

# Exact three-regime certificate, with no floating-point approximations.
for n,expected in [(9,-1),(20,1),(70,-1)]:
    t=ratio(n,10,1,8)
    sign=(t>1)-(t<1)
    assert sign==expected
    er,es,ers=moments(n,10,1,8)
    cov=ers-er*es
    assert (cov>0)-(cov<0)==expected
    checks+=2

# Near-thermodynamic sign samples to corroborate (not prove) asymptotics.
for m in [20,50,100]:
    for n,mulsign in [(2*m,1),(4*m,1),(8*m,-1)]:
        t=ratio(n,m,1,8)
        assert (t>1)-(t<1)==mulsign
        checks+=1

print(f"PASS: {checks} exact assertions, including independent allocation enumeration")
