#!/usr/bin/env python3
"""Exhaustive small-case verification of a three-subsequence universality formula."""
from itertools import combinations, product
from collections import Counter
from math import comb

def exception_formula(a,b,c):
    h=a*b
    return (int(0<=c<=b)+int(0<=c<=a)+int(h-b<=c<=h)
          +int(h-a<=c<=h)+int(c%a==0)+int(c%b==0)
          -3*int(c==0)-3*int(c==h)-int(c==1)-int(c==h-1)
          -int(c==a)-int(c==b)-int(c==h-a)-int(c==h-b))

def is_subsequence(pattern, word):
    j=0
    for x in word:
        if j<len(pattern) and x==pattern[j]:j+=1
    return j==len(pattern)

def run():
    words_checked=0
    pairs=0
    patterns=[''.join(p) for p in product('01',repeat=3)]
    for a in range(3,10):
        for b in range(3,10):
            if a+b>15:continue
            grouped=Counter()
            for zeros in combinations(range(a+b),a):
                w=['1']*(a+b)
                for i in zeros:w[i]='0'
                word=''.join(w)
                z=0;c=0
                for letter in word:
                    if letter=='0':z+=1
                    else:c+=z
                nonuniversal=any(not is_subsequence(p,word) for p in patterns)
                grouped[(c,nonuniversal)]+=1
                words_checked+=1
            assert sum(grouped.values())==comb(a+b,a)
            for c in range(a*b+1):
                actual=grouped[(c,True)]
                expected=exception_formula(a,b,c)
                assert actual==expected,(a,b,c,actual,expected)
                assert 0<=expected<=2
            assert sum(grouped[(c,True)] for c in range(a*b+1))==3*(a+b)-6
            pairs+=1
    print('PASS: %d binary words, %d multiplicity pairs; exact fiber formula, <=2 bound and global count' % (words_checked,pairs))

if __name__=='__main__':run()
