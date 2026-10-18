"""Finite exact-arithmetic checks for unitary/exponential divisor-sum ratio fibers."""
from fractions import Fraction
from math import isqrt


def prime_spf(limit):
    spf = list(range(limit+1))
    for p in range(2, isqrt(limit)+1):
        if spf[p] == p:
            for k in range(p*p, limit+1, p):
                if spf[k] == k:
                    spf[k] = p
    return spf


def functions(n, spf):
    unit = expo = 1
    while n > 1:
        p = spf[n]
        a = 0
        v = 1
        while n % p == 0:
            n //= p
            a += 1
            v *= p
        unit *= 1 + v
        expo *= sum(p**d for d in range(1,a+1) if a%d == 0)
    return unit,expo


def main():
    bound = 100000
    spf=prime_spf(bound)
    vals=[None]+[functions(n,spf) for n in range(1,bound+1)]
    for y in (3,7,17,37):
        fibers={}
        count_big=0
        for n in range(2,bound+1):
            m=n
            biggest=0
            while m>1:
                p=spf[m]
                biggest=max(biggest,p)
                while m%p==0: m//=p
            if biggest<=y or n%(biggest*biggest)==0: continue
            count_big+=1
            m=n//biggest
            un,ex=vals[n]
            um,em=vals[m]
            assert (biggest+1)*um==un and biggest*em==ex
            ratio=Fraction(un,ex)
            predicted=Fraction(um,1)/(ratio*em-um)
            assert predicted==biggest
            key=(m,ratio)
            assert key not in fibers or fibers[key]==biggest
            fibers[key]=biggest
        print('THRESHOLD_CHECK',y,'cases',count_big,'injection_passed',len(fibers))
    matches=[n for n in range(1,bound+1) if vals[n][0]==vals[n][1]]
    assert matches[:4]==[1,20,45,320]
    print('EQUALITY_FIBER_CHECK',len(matches),'first',matches[:10]);print('VERIFY_OK')

if __name__=='__main__': main()
