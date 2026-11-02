"""Exact-rational checks for first-Hermite disk concentration spectral selection.

This script only tests finite cases. Infinite-dimensional conclusions rely on
separate analytic arguments.
"""
from fractions import Fraction
from math import factorial, exp, lgamma, sqrt, pi


def b(j, x):
    """a_j=1-exp(-x)*b(j,x) for the first Hermite localization level."""
    if j == 0:
        return 1 + x
    s = sum((x ** m / factorial(m) for m in range(j)), Fraction(0))
    return s - (j - 1 - x) * x ** j / factorial(j)


def delta_b(j, x):
    # b(j+1)-b(j) is minus the eigenvalue increment after exp(-x) removal.
    return x**j * (x-j) * (x-j-1) / factorial(j+1)


def check():
    count = 0
    # Exact symbolic-in-the-variable identities verified at rational arguments.
    for den in (2,3,5,7,11):
        for num in range(1, min(den*14, 95)):
            x = Fraction(num, den)
            k = num // den
            for j in range(0, min(28, k+8)):
                assert b(j+1,x)-b(j,x) == delta_b(j,x)
                count += 1
            # Compare every possible Hermite mode in a finite but sufficiently wide set.
            cap = max(35, k+24)
            values = [b(j,x) for j in range(cap)]
            lowest_b_indices = sorted(range(cap),key=lambda j:(values[j],j))
            if num % den:
                N=k+1
                expected=list(range(k))+[k+1]
                assert set(lowest_b_indices[:N])==set(expected), (x,lowest_b_indices[:N],expected)
                assert b(k+1,x) < b(k,x)
                count += 2
                if k>=1:
                    assert b(k-1,x) < b(k+1,x)
                    count += 1
                assert b(k+1,x) < b(k+2,x)
                count += 1
                # The selected gain equals one single Poisson mass times two geometric gaps.
                assert b(k,x)-b(k+1,x) == x**k*(x-k)*(k+1-x)/factorial(k+1)
                count += 1
            else:
                assert b(k-1,x)==b(k,x)==b(k+1,x)
                assert all(values[j]<values[j+1] for j in range(cap-1) if j not in (k-1,k))
                count += 2
            # operator norm: j=1 for x<1, j=0 for x>1; three-way tie at 1.
            top = [j for j in range(cap) if values[j]==min(values)]
            assert top == ([1] if x<1 else [0] if x>1 else [0,1,2]),(x,top)
            count+=1
    # Leading asymptotic coefficient of the single-mode exchange gain.
    for k in (50, 100, 200, 500, 1000):
        for d in (.2, .5, .8):
            x=k+d
            p=exp(-x+k*__import__('math').log(x)-lgamma(k+1))
            gain=p*d*(1-d)/(k+1)
            leading=d*(1-d)/(sqrt(2*pi)*k**1.5)
            assert abs(gain/leading-1)<2/k,(k,d,gain/leading)
            count+=1
    print(f"PASS {count} finite exact rational and supplementary asymptotic assertions")


if __name__=='__main__':
    check()
