#!/usr/bin/env python3
"""Independent finite tests for a two-parameter shortest-common-supersequence formula."""
from functools import lru_cache
from itertools import combinations,product
from math import comb

def is_subsequence(pattern,word):
    it=iter(word)
    return all(ch in it for ch in pattern)

def dp_shortest_and_count(a,b):
    @lru_cache(None)
    def solve(i,j):
        if i==len(a):return len(b)-j,1
        if j==len(b):return len(a)-i,1
        if a[i]==b[j]:
            k,c=solve(i+1,j+1)
            return k+1,c
        k,c=solve(i+1,j)
        l,d=solve(i,j+1)
        return min(k,l)+1,(c if k<=l else 0)+(d if l<=k else 0)
    return solve(0,0)

def expand(y,p,n):
    count={'0':0,'1':0};result=[];forced=0
    for sym in y:
        letter=sym
        while letter is not None:
            result.append(letter);count[letter]+=1
            if count[letter]%p==0 and count[letter]<p*n:
                forced+=1; letter='1' if letter=='0' else '0'
            else:letter=None
    return ''.join(result),forced

def compress(x,p,n):
    count={'0':0,'1':0};remove=set()
    for i,c in enumerate(x):
        count[c]+=1
        if count[c]%p==0 and count[c]<p*n:
            assert i+1<len(x)
            assert x[i+1]!=c
            remove.add(i+1)
    assert len(remove)==2*(n-1)
    return ''.join(c for i,c in enumerate(x) if i not in remove)

def valid_x(x,p,n):
    if len(x)!=2*p*n or x.count('0')!=p*n or x[-1]!='1':return False
    for c in '01':
        ps=[i for i,ch in enumerate(x) if ch==c]
        for k in range(1,n):
            if ps[k*p]==ps[k*p-1]+1:return False
    return True

cases=0;balanced=0;checked_words=0
for p in range(1,8):
    for n in range(1,13):
        a=('0'*p+'1')*n;b=('1'*p+'0')*n
        want=comb(2*((p-1)*n+1),(p-1)*n+1)
        got=dp_shortest_and_count(a,b)
        assert got==(2*p*n+1,want),(p,n,got,want)
        cases+=1
        h=(p-1)*n+1
        if h<=8:
            seen=set()
            for zeros in combinations(range(2*h-1),h):
                y=['1']*(2*h)
                for j in zeros:y[j]='0'
                yy=''.join(y)
                assert yy[-1]=='1' and yy.count('0')==h
                x,forced=expand(yy,p,n)
                assert forced==2*(n-1)
                assert valid_x(x,p,n)
                assert compress(x,p,n)==yy
                w=x+'0'
                assert is_subsequence(a,w) and is_subsequence(b,w)
                seen.add(x);balanced+=1
            assert len(seen)==comb(2*h-1,h)
        if p*n<=5:
            num=0
            for bits in product('01',repeat=2*p*n+1):
                w=''.join(bits);checked_words+=1
                if is_subsequence(a,w) and is_subsequence(b,w):num+=1
            assert num==want,(p,n,num,want)
print('PASS: DP parameter pairs:',cases)
print('PASS: balanced bridge bijections:',balanced)
print('PASS: brute tested short-length words:',checked_words)
