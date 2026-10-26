#!/usr/bin/env python3
"""Independent finite tests for a sparse binary Abelian/ordinary-border classification."""
from itertools import combinations
from math import comb


def ordinary_bordered(w):
    n = len(w)
    return any(w[:k] == w[n-k:] for k in range(1, n))


def abelian_bordered(w):
    n = len(w)
    left = right = 0
    for k in range(1, n):
        left += w[k-1]
        right += w[n-k]
        if left == right:
            return True
    return False


def classify_sparse_four(a,b,c,d):
    return a>d and a+b<=c+d and b!=d


def word_four(a,b,c,d):
    return (0,)*a+(1,)+(0,)*b+(1,)+(0,)*c+(1,)+(0,)*d+(1,)


def direct_weight_four(n):
    count = 0
    for ps in combinations(range(n),4):
        w = tuple(int(i in ps) for i in range(n))
        exceptional = abelian_bordered(w) and not ordinary_bordered(w)
        if w[0] == 0 and w[-1] == 1:
            a,b,c,d = ps[0],ps[1]-ps[0]-1,ps[2]-ps[1]-1,ps[3]-ps[2]-1
            assert exceptional == classify_sparse_four(a,b,c,d), (n,ps)
        if exceptional:
            count += 1
    return count


def series_product_coeffs(nmax):
    # Independently expand 4*z^8 / ((1-z)*(1-z^2)^2*(1-z^4)).
    c = [0]*(nmax+1)
    c[0]=4
    for step in (1,2,2,4):
        for i in range(step,nmax+1):
            c[i] += c[i-step]
    return [c[n-8] if n>=8 else 0 for n in range(nmax+1)]


def independent_param_count(n):
    # e>=1, f>=0, b,d>=0, b!=d and n=4+2(e+b+d)+f.
    m=n-4
    return 2*sum(1 for e in range(1,m//2+1)
                 for b in range(m//2-e+1)
                 for d in range(m//2-e-b+1)
                 if b!=d)


def main():
    small_words=0
    for n in range(1,31):
        for r in range(min(3,n)+1):
            for ps in combinations(range(n),r):
                w=tuple(int(i in ps) for i in range(n))
                assert ordinary_bordered(w)==abelian_bordered(w),(n,ps)
                small_words+=1
    nmax=26
    coeff=series_product_coeffs(180)
    count_four=0
    for n in range(4,nmax+1):
        observed=direct_weight_four(n)
        assert observed==coeff[n],(n,observed,coeff[n])
        count_four+=comb(n,4)
    for n in range(0,121):
        assert independent_param_count(n)==coeff[n],(n,independent_param_count(n),coeff[n])
    assert coeff[8:23] == [4,4,12,12,28,28,52,52,88,88,136,136,200,200,280]
    print('PASS: sparse_r<=3_words=',small_words)
    print('PASS: weight_four_words=',count_four)
    print('PASS: lengthwise_gf_and_params_to_n=',120)
    print('PASS: coefficient_sample=',coeff[8:23])

if __name__=='__main__':main()
