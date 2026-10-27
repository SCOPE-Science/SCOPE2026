#!/usr/bin/env python3
"""Independent direct factor-set verification for three- and four-run binary words."""
from itertools import product
from math import comb

def is_palindrome_pair(s):
    for k in range(len(s)+1):
        if s[:k] == s[:k][::-1] and s[k:] == s[k:][::-1]:
            return True
    return False

def direct_count(s):
    factors = {""}
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            factor = s[i:j]
            if is_palindrome_pair(factor):
                factors.add(factor)
    return len(factors)

def four_formula(a,b,c,d):
    return (1 + max(a,c) + max(b,d) + a*b + b*c + c*d + a*c + b*d
            -min(a,c)*min(b,d) + (d if c <= a else 0)
            + (a if b <= d else 0) - (1 if c <= a and b <= d else 0))

def three_formula(a,b,c):
    return 1 + max(a,c) + b + a*b + b*c + a*c

def proposed(n):
    return (n*n+2*n+5)//3

def verify(max_n=13):
    result=[]; checked=0
    for n in range(4,max_n+1):
        largest=-1
        for a in range(1,n-2):
            for b in range(1,n-a-1):
                for c in range(1,n-a-b):
                    d=n-a-b-c
                    w='0'*a+'1'*b+'0'*c+'1'*d
                    brute=direct_count(w)
                    predicted=four_formula(a,b,c,d)
                    assert brute==predicted, (a,b,c,d,brute,predicted)
                    assert predicted < proposed(n), (a,b,c,d,predicted,proposed(n))
                    largest=max(largest,brute)
                    checked+=1
        result.append((n,largest,comb(n-1,3)))
    for n in range(3,max_n+1):
        k,r=divmod(n,3)
        a,b,c=((k,k,k) if r==0 else (k,k+1,k) if r==1 else (k+1,k+1,k))
        w='0'*a+'1'*b+'0'*c
        assert direct_count(w)==three_formula(a,b,c)==proposed(n)
    return result,checked

if __name__=='__main__':
    rows,count=verify()
    for n,m,c in rows: print('n=',n,'max four-run=',m,'four-run compositions=',c)
    print('EXACT_CHECK_OK',count,'four-run words, plus three-run witnesses')
