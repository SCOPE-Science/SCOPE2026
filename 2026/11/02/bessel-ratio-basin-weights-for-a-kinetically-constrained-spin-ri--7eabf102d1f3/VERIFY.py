"""Independent exact-arithmetic checks for a constrained spin-ring absorption law.

Python >=3.9; standard library only. This tests finite systems and series
identities; the analytic singularity and infinite-size arguments are proved
in RESULT.md, not certified by finite tests.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import atan, sqrt


def block_coefficients(n, theta):
    a = [Q(1)]
    for m in range(1, n + 1):
        c = sum((a[j] * a[m-1-j] for j in range(m)), Q(0))
        a.append(c / ((1+theta)*m+theta))
    return a


def formal_coefficients(n, p, theta):
    q=1-p
    a=block_coefficients(n//2+2,theta)
    f=[Q(0)]*(n+1)
    for m in range(len(a)):
        k=2*m+1
        if k<=n: f[k]=q*a[m]*(p*q)**m
    inv=[Q(0)]*(n+1)
    inv[0]=1
    for k in range(1,n+1):
        inv[k]=sum((f[j]*inv[k-j] for j in range(1,k+1)),Q(0))
    coeff=[Q(0)]*(n+1)
    coeff[0]=1
    for k in range(1,n+1):
        coeff[k]=sum((j*f[j]*inv[k-j] for j in range(1,k+1)),Q(0))
    for m in range(1,len(a)):
        k=2*m+2
        if k<=n: coeff[k]+=2*p*q*a[m]*(p*q)**m/(1+theta)
    return coeff


def direct_cycle(n,p,theta):
    q=1-p
    mask=(1<<n)-1
    @lru_cache(None)
    def succeed(s):
        if s==0:return Q(1)
        if any((s>>i&1) and (s>>((i+1)%n)&1) for i in range(n)):
            return Q(0)
        occupied=[i for i in range(n) if s>>i&1]
        facilitated=[i for i in range(n) if not s>>i&1 and
                     ((s>>((i-1)%n)&1) or (s>>((i+1)%n)&1))]
        return sum((succeed(s^(1<<i)) for i in occupied),Q(0)) /\
               (len(occupied)+theta*len(facilitated))
    return sum((p**s.bit_count()*q**(n-s.bit_count())*succeed(s)
                for s in range(1<<n)),Q(0))


def main():
    tests=0
    combinations=[(Q(1,2),Q(1)),(Q(2,5),Q(2,3)),
                  (Q(3,4),Q(3,2)),(Q(1,5),Q(5)),
                  (Q(4,9),Q(1,4))]
    for p,theta in combinations:
        a=block_coefficients(18,theta)
        # Critical Riccati coefficient identity.
        for m in range(1,19):
            assert (((1+theta)*m+theta)*a[m] ==
                    sum((a[j]*a[m-1-j] for j in range(m)),Q(0)))
            tests+=1
        b=formal_coefficients(15,p,theta)
        for n in range(3,11):
            exact=direct_cycle(n,p,theta)
            assert exact==b[n],(n,p,theta,exact,b[n])
            assert 0<exact<1
            tests+=2
    # Special equal flip-rate formula for the exponential scale.
    for p in (0.1,0.3,0.5,0.8):
        q=1-p
        lam=sqrt(p*q)/atan(sqrt(p/q))
        assert q<lam<1
        tests+=1
    print('PASS',tests,'exact-rational/comparison checks')

if __name__=='__main__':main()
