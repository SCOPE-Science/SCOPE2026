"""Reproduce finite exact checks for the cyclic median-filter saturation theorem.
No external packages or data are needed. Run with Python 3.
"""
from itertools import product

def arithmetic_saturation(r, n):
    m = 2*r+1
    assert r>=1 and n>=m
    if n == m:
        return True
    k = n-m
    q,t = divmod(2*r,k)
    return any(a*(q+1)+b*q==r for a in range(t+1) for b in range(k-t+1))

def local_count(r,n,mask,j=0):
    m=2*r+1
    result=0
    for i in range(n):
        win={(i+s)%n for s in range(-r,r+1)}
        if j not in win:continue
        below=sum((mask >> (u-1))&1 for u in win if u!=j)
        if below==r: result+=1
    return result

def exact_multiplicity(r,n):
    assert n<=17
    return max(local_count(r,n,b) for b in range(1 << (n-1)))

def equivalence_tests():
    cases=0
    for r in range(1,7):
        for n in range(2*r+1,18):
            if n>17:continue
            m=2*r+1
            C=exact_multiplicity(r,n)
            assert (C==m)==arithmetic_saturation(r,n),(r,n,C)
            if n==m+1:assert C==r+1,(r,n,C)
            if n%2==1:assert C==m,(r,n,C)
            if n>=4*r+1:assert C==m,(r,n,C)
            cases+=1
    assert exact_multiplicity(3,10)==6
    assert arithmetic_saturation(3,10) is False
    return cases

if __name__=='__main__':
    N=equivalence_tests()
    print('PASS:',N,'independent exhaustive small-parameter saturation comparisons')
    print('PASS: exceptional 7-site window / 10-site circle has multiplicity 6')
    for r in range(1,101):
        for n in range(2*r+1,6*r+21):
            m=2*r+1
            if n%2: assert arithmetic_saturation(r,n)
            if n>=4*r+1: assert arithmetic_saturation(r,n)
            if n==m+1: assert not arithmetic_saturation(r,n)
    print('PASS: 100-window-family arithmetic edge-case checks')
