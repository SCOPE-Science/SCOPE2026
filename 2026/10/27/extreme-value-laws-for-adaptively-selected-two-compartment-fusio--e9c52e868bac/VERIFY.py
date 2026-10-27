#!/usr/bin/env python3
"""Deterministic finite-law consistency checks for adaptive two-compartment fusion."""
from fractions import Fraction
from itertools import product
from math import comb, exp, factorial, isclose


def optimal_increment(values):
    best = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            x, y = values[i], values[j]
            inc = min(max(x, 0), max(-y, 0)) + min(max(-x, 0), max(y, 0))
            best = max(best, inc)
    return best


def formula(C, p):
    return 1 - 2 * (1 - p)**C + (1 - 2 * p)**C


def multinomial_direct(C, p):
    q = 1 - 2*p
    return sum(
        comb(C,a)*comb(C-a,b)*p**(a+b)*q**(C-a-b)
        for a in range(1,C+1) for b in range(1,C-a+1)
    )


def poisson_pmf(lam, j):
    return exp(-lam)*lam**j/factorial(j)


def skellam_tail_convolution(lam, k, cut=65):
    probs = [poisson_pmf(lam,j) for j in range(cut)]
    return sum(probs[a]*sum(probs[:a-k+1]) for a in range(k,cut))


def skellam_tail_bessel(lam,k,cut=65):
    #  P(A-B>=k)=exp(-2lambda) sum_{d>=k} sum_{j>=0}
    #  lambda^(2j+d)/(j!(j+d)!). Independent series representation.
    return exp(-2*lam)*sum(
        sum(lam**(2*j+d)/(factorial(j)*factorial(j+d)) for j in range(cut))
        for d in range(k,cut)
    )


def main():
    count=0
    weights={-2:Fraction(1,9),-1:Fraction(2,9),0:Fraction(3,9),1:Fraction(2,9),2:Fraction(1,9)}
    for C in range(2,6):
        for k in (1,2):
            brute=sum(
                (Fraction(1) if optimal_increment(seq)>=k else Fraction(0)) *
                __import__('math').prod(weights[x] for x in seq)
                for seq in product(weights,repeat=C)
            )
            p=sum(w for d,w in weights.items() if d>=k)
            expected=formula(C,p)
            assert brute==expected,(C,k,brute,expected)
            assert brute==multinomial_direct(C,p)
            count+=2
    for lam in (0.25,0.5,1.0,2.0,3.0):
        for k in range(1,7):
            a=skellam_tail_convolution(lam,k)
            b=skellam_tail_bessel(lam,k)
            assert isclose(a,b,rel_tol=1e-11,abs_tol=1e-14),(lam,k,a,b)
            count+=1
        for C in (2,3,5,9):
            for k in range(1,5):
                p=skellam_tail_convolution(lam,k)
                a=formula(C,p)
                b=multinomial_direct(C,p)
                assert isclose(a,b,rel_tol=5e-10,abs_tol=2e-15),(lam,C,k,a,b)
                count+=1
    for values in ((3,-2,1),(-5,-2,0,6),(-4,-7,0),(-3,2,2,0),(-8,5,-3,11)):
        assert optimal_increment(values)==min(max(0,max(values)),max(0,-min(values)))
        count+=1
    print('PASS:',count,'deterministic identity/comparison checks')
    for lam in (0.5,1,3):
        p=skellam_tail_convolution(lam,1)
        print(f'lambda={lam:g}: P(best two-droplet fusion positive; C=2,5,20):',*[round(formula(c,p),9) for c in (2,5,20)])

if __name__=='__main__':
    main()
