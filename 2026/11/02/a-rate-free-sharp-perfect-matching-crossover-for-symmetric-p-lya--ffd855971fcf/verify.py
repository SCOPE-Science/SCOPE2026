"""Standalone numerical and exact checks for the Pólya-threshold matching crossover.
Only finite tests; the analytic theorem is established separately.
"""
from fractions import Fraction
from math import comb, sqrt, pi
from functools import lru_cache
from itertools import product
import math


def rising(a, j):
    t = Fraction(1)
    for x in range(j):
        t *= a + x
    return t


def matching_word(bits):
    # Edges i<j are present precisely when bits[j]=1.
    n = len(bits)
    neigh = [0]*n
    for j in range(1,n):
        if bits[j]:
            for i in range(j):
                neigh[i] |= 1<<j
                neigh[j] |= 1<<i
    @lru_cache(None)
    def rec(mask):
        if mask == 0:
            return True
        i = (mask & -mask).bit_length()-1
        options = neigh[i]&mask
        options &= ~(1<<i)
        while options:
            j = (options&-options).bit_length()-1
            if rec(mask ^ (1<<i) ^ (1<<j)):
                return True
            options &= options-1
        return False
    return rec((1<<n)-1)


def ballot_word(bits):
    level = 0
    for b in reversed(bits[1:]):
        level += 1 if b else -1
        if level < 0:
            return False
    return True


def exact_p(n, a):
    L=n-1
    den=rising(2*a,L)
    return sum(Fraction(comb(L,u)-comb(L,u+1))*rising(a,u)*rising(a,L-u)/den for u in range(n//2,L+1))


def direct_p(n,a):
    L=n-1
    den=rising(2*a,L)
    s=Fraction(0)
    for word in product((0,1),repeat=L):
        bits=(0,)+word
        if matching_word(bits):
            u=sum(word)
            s += rising(a,u)*rising(a,L-u)/den
    return s


def betaln(x, y):
    return math.lgamma(x)+math.lgamma(y)-math.lgamma(x+y)


def logsumexp(values):
    m=max(values)
    return m+math.log(sum(math.exp(v-m) for v in values))


def float_p(n,kap):
    L=n-1
    a=kap/2
    vals=[]
    for u in range(n//2,L+1):
        v=(2*u-L+1)/(u+1)
        lp=(math.lgamma(L+1)-math.lgamma(u+1)-math.lgamma(L-u+1)
            +betaln(a+u,a+L-u)-betaln(a,a))
        vals.append(lp+math.log(v))
    return math.exp(logsumexp(vals))


def main():
    checks=0
    for n in range(2,12,2):
        for word in product((0,1),repeat=n-1):
            bits=(0,)+word
            assert matching_word(bits)==ballot_word(bits),(n,bits)
            checks+=1
        for a in (Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2),Fraction(5)):
            ex=exact_p(n,a)
            direct=direct_p(n,a)
            assert ex == direct,(n,a,ex,direct)
            checks+=1
            approx=float_p(n,float(a*2))
            assert abs(approx-float(ex)) < 3.e-12,(n,a,ex,approx)
            checks+=1
    # Reflection identity at each endpoint count and exact normalization
    for n in range(2,250,2):
        L=n-1
        for u in range(n//2,L+1):
            lhs=comb(L,u)-comb(L,u+1)
            assert lhs*(u+1)==comb(L,u)*(2*u-L+1)
            checks+=1
        assert sum(comb(L,u)-comb(L,u+1) for u in range(n//2,L+1))==comb(L,n//2)
        checks+=1
    # Numerically check the crossover under beta mixing (relative error vanishes).
    tests=[]
    for n in (400,1000,3000):
        for kap in (sqrt(n), n/3, 2*n, n*n):
            val=float_p(n,kap)
            lead=sqrt(2/pi)*sqrt(1/n+1/kap)
            tests.append((n,round(kap,5),round(val,8),round(lead,8),round(val/lead,6)))
            assert abs(val/lead-1)<0.23,(n,kap,val,lead)
            checks+=1
    # Fixed concentration phase has a positive nonzero limit.
    p2=[float_p(n,2) for n in (100,400,1000,3000)]
    assert all(abs(v-(1-math.log(2))) < 0.018 for v in p2[-2:])
    checks+=2
    print('checks:',checks)
    print('n, kappa, exact_probability, leading_asymptotic, ratio:')
    for row in tests:
        print(*row)
    print('fixed_kappa_2_probs:',[round(v,8) for v in p2],'target:',round(1-math.log(2),8))

if __name__=='__main__':
    main()
