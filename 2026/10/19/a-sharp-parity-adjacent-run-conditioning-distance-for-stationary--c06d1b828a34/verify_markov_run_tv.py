"""Independent finite checks for two-state Markov occupancy/run parity, plus asymptotic numerical tests.
Run: python verify_markov_run_tv.py (Python 3.9+ standard library only).
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb, lgamma, log, exp, sqrt, pi


def enumerate_joint(n, a, b):
    pi0, pi1 = b / (a + b), a / (a + b)
    P = ((1 - a, a), (b, 1 - b))
    out = defaultdict(lambda: F(0))
    for word in product((0, 1), repeat=n):
        k = sum(word)
        r = 1 + sum(word[j] != word[j - 1] for j in range(1, n))
        weight = pi1 if word[0] else pi0
        for j in range(1, n):
            weight *= P[word[j - 1]][word[j]]
        out[k, r] += weight
    return out


def finite_tilt(n, s, a, b, k):
    return (b * (n-k-s)/(1-a) + a * (k-s)/(1-b))/(2*s)


def logsumexp(log_values):
    top = max(log_values)
    return top + log(sum(exp(x-top) for x in log_values))


def conditional_even(n, s, a, b):
    q = (1-b)/(1-a)
    ks = list(range(s, n-s+1))
    logs = [(lgamma(k)-lgamma(s)-lgamma(k-s+1) +
             lgamma(n-k)-lgamma(s)-lgamma(n-k-s+1) + k*log(q)) for k in ks]
    z = logsumexp(logs)
    ps = [exp(v-z) for v in logs]
    ts = [finite_tilt(n,s,a,b,k) for k in ks]
    mean_t = sum(p*t for p,t in zip(ps,ts))
    tv = sum(p*abs(t/mean_t-1) for p,t in zip(ps,ts))/2
    return tv


def asymptotic_coefficient(rho, a, b):
    q = (1-b)/(1-a)
    lo, hi = rho, 1-rho
    for _ in range(90):
        x = (lo+hi)/2
        val = q*x*(1-x-rho) - (x-rho)*(1-x)
        if val > 0: lo=x
        else: hi=x
    x = (lo+hi)/2
    sigma = 1/sqrt(rho/(x*(x-rho)) + rho/((1-x)*(1-x-rho)))
    t = (b*(1-x-rho)/(1-a) + a*(x-rho)/(1-b))/(2*rho)
    slope = (a/(1-b)-b/(1-a))/(2*rho)
    return abs(slope)*sigma/(t*sqrt(2*pi))


def main():
    checks=0
    pairs=((F(1,4),F(1,3)),(F(2,3),F(1,3)),(F(3,5),F(1,5)),
           (F(1,3),F(1,3)),(F(2,5),F(2,3)),(F(5,6),F(4,5)))
    for n in range(3,9):
        for a,b in pairs:
            joint=enumerate_joint(n,a,b)
            for s in range(1,(n-1)//2+1):
                for k in range(s,n-s+1):
                    assert joint[k,2*s] > 0 and joint[k,2*s+1] > 0
                    assert joint[k,2*s+1]/joint[k,2*s] == finite_tilt(n,s,a,b,k)
                    checks+=1
    experiments=((.2,.4,.2),(.7,.2,.3),(.2,.2,.2),(.2,.8,.2),(.7,.3,.35))
    for a,b,rho in experiments:
        c=asymptotic_coefficient(rho,a,b)
        n=4000; s=round(rho*n)
        observed=sqrt(n)*conditional_even(n,s,a,b)
        if c == 0:
            assert abs(observed) < 1e-10, (a,b,rho,c,observed)
        else:
            assert abs(observed-c) < 0.001, (a,b,rho,c,observed)
        checks+=1
    print('PASS',checks,'independent finite/limit checks')


if __name__ == '__main__':
    main()
