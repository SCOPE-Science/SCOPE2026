"""Reproduce finite rational tests of longest-run/part-count covariance and numerical asymptotics."""
from fractions import Fraction
from itertools import product
from math import log, exp, floor, ceil


def direct(n):
    rows = []
    for bits in product((0, 1), repeat=n):
        k = sum(bits)
        run = best = 0
        for bit in bits:
            if bit == 0:
                run += 1
                best = max(best, run)
            else:
                run = 0
        rows.append((k, best))
    denom = len(rows)
    ek = Fraction(sum(k for k, l in rows), denom)
    el = Fraction(sum(l for k, l in rows), denom)
    ekl = Fraction(sum(k*l for k, l in rows), denom)
    return ekl - ek*el


def recurrence_rational(n):
    p = q = Fraction(1, 2)
    cov = Fraction(0)
    for r in range(1, n+1):
        epsilon = p*q**r
        epsprime = q**r - p*r*q**(r-1)
        f = [Fraction(1)]*(n+1)
        fp = [Fraction(0)]*(n+1)
        f[r] = 1-q**r
        fp[r] = r*q**(r-1)
        for j in range(r+1,n+1):
            f[j] = f[j-1] - epsilon*f[j-r-1]
            fp[j] = fp[j-1] - epsprime*f[j-r-1] - epsilon*fp[j-r-1]
        cov -= p*q*fp[n]
    return cov


def recurrence_float(n):
    total = 0.0
    for r in range(1,min(n,ceil(log(n,2))+32)+1):
        e=2.0**(-r-1)
        ep=(2-2*r)*e
        f=[1.]*(n+1)
        d=[0.]*(n+1)
        f[r]=1.-2.0**(-r)
        d[r]=r*2.0**(1-r)
        for j in range(r+1,n+1):
            f[j]=f[j-1]-e*f[j-r-1]
            d[j]=d[j-1]-ep*f[j-r-1]-e*d[j-r-1]
        total -= d[n]/4.
    return total


def pq(x):
    P=Q=0.0
    for k in range(-55,75):
        u=2.0**(x-k)
        z=u*exp(-u)
        P += z
        Q += (k-x)*z
    return P,Q


def period_formula(n):
    L=log(n,2)
    P,Q=pq(L%1.0)
    return -0.5*((L-2)*P+Q)


def run():
    checks=0
    for n in range(1,13):
        a=direct(n)
        b=recurrence_rational(n)
        assert a==b, (n,a,b)
        assert a<0
        checks+=1
    for n in (100,1000,10000):
        c=recurrence_float(n)
        asym=period_formula(n)
        assert c<0
        assert abs(c-asym) < 1.2/n, (n,c,asym,c-asym)
        print(f'n={n} exact_recurrence={c:.12f} two_term={asym:.12f} difference={c-asym:.10f}')
        checks+=1
    print('VERIFY_OK',checks,'tests plus',sum(2**n for n in range(1,13)),'enumerated bitstrings')

if __name__=='__main__':
    run()
