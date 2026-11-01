#!/usr/bin/env python3
"""Supplementary finite checks for projective Gaussian Fock concentration bands.

Uses the Python standard library only. The analytical proof is in RESULT.md.
"""
import math
from fractions import Fraction


def exact_binom_cdf(m, p, k):
    return sum(Fraction(math.comb(m, j)) * p**j * (1-p)**(m-j)
               for j in range(k+1))


def exact_beta_band(m, k, a, b):
    # Derivative of the polynomial CDF is the beta density with shapes
    # (k+1, m-k).  This is an independent antiderivative evaluation.
    def beta_cdf(x):
        return sum(Fraction(math.comb(m, j)) * x**j * (1-x)**(m-j)
                   for j in range(k+1, m+1))
    return beta_cdf(b) - beta_cdf(a)


def enumerate_intervals(m, a, b):
    # Multinomial categories: below a, between a and b, above b.
    out = []
    for low in range(m+1):
        for middle in range(m-low+1):
            high = m-low-middle
            weight = (Fraction(math.factorial(m), math.factorial(low)
                     *math.factorial(middle)*math.factorial(high))
                     * a**low * (b-a)**middle * (1-b)**high)
            if weight:
                out.append((low, low+middle, weight))
    return out


def symmetric_difference(a1, b1, a2, b2):
    s1 = set(range(a1,b1))
    s2 = set(range(a2,b2))
    return len(s1.symmetric_difference(s2))


def binom_cdf_list(m, p):
    # Recursion from a mode avoids underflow at high degree.
    if p == 0:
        return [1.0]*(m+1)
    if p == 1:
        return [0.0]*m+[1.0]
    mode = min(m, int((m+1)*p))
    v = [0.0]*(m+1)
    v[mode] = 1.0
    for k in range(mode-1, -1, -1):
        v[k] = v[k+1] * ((k+1)/(m-k)) * ((1-p)/p)
    for k in range(mode+1,m+1):
        v[k] = v[k-1] * ((m-k+1)/k) * (p/(1-p))
    total = math.fsum(v)
    cum = 0.0
    cdf = []
    for x in v:
        cum += x / total
        cdf.append(min(1.0, cum))
    cdf[-1] = 1.0
    return cdf


def spectral_defect(n,a,b):
    m = n+1
    ca,cb = binom_cdf_list(m,a),binom_cdf_list(m,b)
    vals = [max(0.0,min(1.0,ca[k]-cb[k])) for k in range(m)]
    return math.fsum(x*(1-x) for x in vals), math.fsum(vals)


def H(t,c):
    s = math.sqrt(t*(1-t))
    q = c/(2*s)
    return c*math.erfc(q)-2*s/math.sqrt(math.pi)*math.expm1(-q*q)


def main():
    assertions = 0
    # Rational checks: beta-band, binomial CDF, trace.
    for m in range(1,14):
        for a,b in ((Fraction(1,5),Fraction(4,5)),
                    (Fraction(1,3),Fraction(1,2))):
            vals=[]
            for k in range(m):
                x=exact_beta_band(m,k,a,b)
                y=exact_binom_cdf(m,a,k)-exact_binom_cdf(m,b,k)
                assert x == y
                vals.append(x)
                assertions += 1
            assert sum(vals)==m*(b-a)
            assertions += 1
            if m <= 6:
                intervals=enumerate_intervals(m,a,b)
                half_sym=Fraction(1,2)*sum(
                    symmetric_difference(p,q,r,s)*w*z
                    for p,q,w in intervals for r,s,z in intervals)
                defect=sum(x*(1-x) for x in vals)
                assert half_sym == defect
                assertions += 1
    # High-degree finite numerical observations (not a limit proof).
    for t in (0.22,0.5,0.73):
        for c in (0.3,0.8,1.8,3.0):
            n=16000
            a,b=t,t+c/math.sqrt(n+1)
            v,tr=spectral_defect(n,a,b)
            if b < 1:
                assert abs(tr-(n+1)*(b-a)) < 1e-7
                assert abs(v/math.sqrt(n+1)-H(t,c)) < 0.032
                assertions += 2
    # Separated boundary reference: a and b fixed.
    for a,b in ((0.2,0.7),(0.35,0.65)):
        n=16000
        v,tr=spectral_defect(n,a,b)
        target=(math.sqrt(a*(1-a))+math.sqrt(b*(1-b)))/math.sqrt(math.pi)
        assert abs(v/math.sqrt(n+1)-target) < 0.018
        assertions += 1
    print('PASS:', assertions, 'finite assertions; infinite limits use the analytic proof')

if __name__ == '__main__':
    main()
