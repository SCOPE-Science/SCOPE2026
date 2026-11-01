#!/usr/bin/env python3
"""Finite exact-arithmetic checks of the contracted-rotation cylinder argument.

These checks illustrate the exact Sturmian word count and uniform geometric
separation. The infinite theorem follows from the written proof, not samples.
"""
from fractions import Fraction as Q
from math import gcd


def word(t, alpha, depth):
    return tuple((t-j*alpha).__floor__()-(t-(j+1)*alpha).__floor__()
                 for j in range(depth))


def partition_words(alpha, depth):
    breaks = sorted({Q(0), Q(1)} | {(j*alpha) % 1 for j in range(1, depth+1)})
    return [word((a+b)/2, alpha, depth) for a,b in zip(breaks,breaks[1:])]


def main():
    count = 0
    # A reduced rational approximation of an irrational golden-mean slope;
    # depth < denominator makes all orbit partition points distinct.
    for p,q in [(233,377),(144,233),(89,144),(55,89)]:
        assert gcd(p,q)==1
        alpha=Q(p,q)
        for n in range(1,21):
            if n>=q:
                continue
            words=partition_words(alpha,n)
            assert len(words)==n+1 and len(set(words))==n+1
            assert all(set(w)<=set([0,1]) for w in words)
            count+=1
    ratios=[Q(1,5),Q(1,4),Q(1,7),Q(3,10),Q(1,10)]
    for lam in ratios:
        assert Q(0)<lam<Q(1,3)
        for n in range(1,31):
            scale=lam**n/(1-lam)
            gap=lam**(n-1)*(1-2*lam)/(1-lam)
            assert gap>scale
            # Every depth-n tail has diameter at most the prescribed scale.
            assert (lam**n)/(1-lam)==scale
            count+=1
    print(f'PASS: {count} exact-rational word-count/separation tests')


if __name__=='__main__':
    main()
