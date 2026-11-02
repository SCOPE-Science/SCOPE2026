#!/usr/bin/env python3
"""Independent finite checks of 2-adic valuation phases of trinomial diagonals."""
from collections import Counter
from math import comb


def v2(x):
    if x == 0:
        return float('inf')
    x = abs(x)
    return (x & -x).bit_length() - 1


def values(b, c, length):
    """Integer recurrence from (1-2bz+(b^2-4c)z^2)^(-1/2)."""
    seq = [1]
    if length == 1:
        return seq
    seq.append(b)
    for n in range(2, length):
        numerator = (2*n-1)*b*seq[-1] - (n-1)*(b*b-4*c)*seq[-2]
        assert numerator % n == 0
        seq.append(numerator//n)
    return seq


def direct(n,b,c):
    return sum(comb(n,2*k)*comb(2*k,k)*b**(n-2*k)*c**k
               for k in range(n//2+1))


def predicted(n,B,C):
    if C >= 2*B:
        return n*B
    m,e=divmod(n,2)
    return m*C+e*B+m.bit_count()


def unit_mod4(n,b,c,B,C,x):
    """Check the stronger first odd-unit correction modulo four."""
    m,e=divmod(n,2)
    baseline=comb(2*m,m)*(c**m)*((2*m+1)*b if e else 1)
    order=v2(baseline)
    assert order == predicted(n,B,C)
    odd_baseline=baseline//(2**order)
    odd_value=x//(2**order)
    observed=(odd_value*pow(odd_baseline,-1,4))%4
    u=b//(2**B)
    w=c//(2**C)
    d=2*B-C
    expected=(1+m*m*(2**(d-1))*(u*u)*pow(w,-1,4))%4
    assert observed==expected,(n,b,c,observed,expected)


def main():
    coefficient_pairs=0
    index_checks=0
    unit_checks=0
    sum_checks=0
    for b in range(-22,23):
        if b==0:
            continue
        B=v2(b)
        for c in range(-24,25):
            if c==0:
                continue
            C=v2(c)
            if C==2*B-1:
                continue
            coefficient_pairs+=1
            seq=values(b,c,81)
            for n,x in enumerate(seq):
                want=predicted(n,B,C)
                assert v2(x)==want,(b,c,n,v2(x),want)
                index_checks+=1
                if C<=2*B-2:
                    unit_mod4(n,b,c,B,C,x)
                    unit_checks+=1
                if n<=9 and (abs(b)+abs(c))%5==0:
                    assert direct(n,b,c)==x
                    sum_checks+=1
    critical_witnesses=0
    for B in range(1,7):
        for r in range(1,12):
            u=3
            v=2**r-u*u
            b=2**B*u
            c=2**(2*B-1)*v
            seq=values(b,c,3)
            assert v2(b)==B and v2(c)==2*B-1
            assert v2(seq[2])==2*B+r
            critical_witnesses+=1
        b=2**B*3
        c=-2**(2*B-1)*9
        assert values(b,c,3)[2]==0
        critical_witnesses+=1
    density_checks=0
    for b,c in [(2,1),(2,7),(6,-1),(4,3),(-8,9),(12,-7)]:
        B=v2(b)
        for r in range(1,11):
            actual=Counter(v2(t) for t in values(b,c,2**r))
            expected=Counter()
            for j in range(r+B+1):
                def choose(jj):
                    return comb(r-1,jj) if 0<=jj<=r-1 else 0
                count=choose(j)+choose(j-B)
                if count:
                    expected[j]=count
            assert actual==expected,(b,c,r,actual,expected)
            density_checks+=1
    print('VERIFY_OK coefficient_pairs=',coefficient_pairs,
          'valuation_indices=',index_checks,
          'unit_mod4_checks=',unit_checks,
          'direct_multinomial_checks=',sum_checks,
          'critical_witnesses=',critical_witnesses,
          'dyadic_histograms=',density_checks)

if __name__=='__main__':
    main()
