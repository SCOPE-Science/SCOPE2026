#!/usr/bin/env python3
"""Exact rational finite-prefix drift certificate for two circle maps."""
from fractions import Fraction as Q
from itertools import product

A = tuple(Q(x,100000) for x in (101275,101199,100542,101080,97952,98566,99446,99939))
S = Q(51,50)
LAMBDA = Q(3999,4000)


def update_prefix(word):
    """Return (doubling prefix, alternate-map prefix, depth change)."""
    assert len(word)==4 and set(word)<=set('01')
    shift = word[1:]
    if word[0] == '0':
        altered = '01' + word[1:]
        delta = 1
    elif word[1] == '0':
        altered = '1' + word[2:]
        delta = -1
    else:
        altered = '00' + word[2:]
        delta = 0
    return shift, altered[:3], delta


def certificate():
    for p in (Q(2,5),Q(1,2)):
        slacks=[]
        for digits in product('01', repeat=4):
            word=''.join(digits)
            doubling,alternate,delta=update_prefix(word)
            left=LAMBDA*A[int(word[:3],2)]
            right=p*A[int(doubling,2)]/S+(1-p)*(S**delta)*A[int(alternate,2)]
            slack=left-right
            assert slack>0, (p,word,slack)
            slacks.append(slack)
        print('EXACT_16_PREFIX_DRIFT_PASS',str(p),str(min(slacks)))


def circle_maps(a,n):
    """Exact rational maps on a reduced dyadic fraction a/2**n."""
    x=Q(a,2**n)
    D=(2*x)%1
    if x<Q(1,2): B=x/2+Q(1,4)
    elif x<Q(3,4):B=2*x-Q(1,2)
    else:B=x-Q(3,4)
    return D,B


def binary_digits(x):
    if x==0:return ''
    assert x.denominator & (x.denominator-1)==0
    n=x.denominator.bit_length()-1
    return format(x.numerator,'0%db'%n)


def direct():
    count=0
    for n in range(4,10):
        for a in range(1,2**n,2):
            word=binary_digits(Q(a,2**n))
            D,B=circle_maps(a,n)
            dword=binary_digits(D)
            bword=binary_digits(B)
            pred_d,pred_b,delta=update_prefix(word[:4])
            assert dword[:3]==pred_d and bword[:3]==pred_b
            assert len(dword)==n-1 and len(bword)==n+delta
            count+=1
    print('EXACT_DYADIC_MAP_PREFIX_AND_DEPTH_PASS',count)

if __name__=='__main__':
    certificate()
    direct()
    print('UNBOUNDED_DEPTH_AND_STATIONARY_EXISTENCE_USE_ANALYTIC_FOSTER_PROOF')
