"""Exact finite-time check for a random expanding/contracting interval map.

Requires Python 3 standard library only. The integration method enumerates
piecewise-affine branches independently of the ballot-number formula.
"""
from fractions import Fraction as Q
from math import comb, erf, exp, pi, sqrt


def integrate_branches(n, p):
    q = 1-p
    states = [(Q(0), Q(1), Q(1), Q(0), Q(1))]
    # (left endpoint, right endpoint, slope, intercept, branch probability)
    for _ in range(n):
        next_states = []
        for lo, hi, a, b, weight in states:
            next_states.append((lo, hi, a / 2, b / 2, weight * q))
            t = (Q(1, 2) - b) / a
            if t > lo:
                v = min(t, hi)
                if v > lo:
                    next_states.append((lo, v, 2 * a, 2 * b, weight * p))
            if t < hi:
                v = max(t, lo)
                if v < hi:
                    next_states.append((v, hi, 2 * a, 2 * b - 1, weight * p))
        states = next_states
    assert sum((weight*(hi-lo) for lo,hi,a,b,weight in states), Q(0)) == 1
    return sum((weight * (a*(hi*hi-lo*lo)/2 + b*(hi-lo))
                for lo,hi,a,b,weight in states), Q(0))


def ballot_mean(n, p):
    q = 1-p
    c = q/(2*p)
    assert c != 1
    m = n+1
    total = Q(0)
    for k in range(1, m+1):
        if (m-k) % 2:
            continue
        prob = comb(m, (m+k)//2) * p**((m+k)//2) * q**((m-k)//2)
        total += Q(k, m) * prob * (1-c**k)/(1-c)
    return total/(2*p)


if __name__ == '__main__':
    num = 0
    for p in (Q(2,5),Q(1,2),Q(3,5)):
        for n in range(9):
            a, b = integrate_branches(n,p), ballot_mean(n,p)
            assert a==b, (p,n,a,b)
            num +=1
    print('PASS: exact branch integration agrees with ballot identity:',num,'cases')
    for alpha in (-1.0,0.0,1.0):
        f = sqrt(2/pi)*exp(-2*alpha*alpha)+2*alpha*(1+erf(sqrt(2)*alpha))
        print('Gaussian crossover:',alpha,format(f,'.12f'))
