#!/usr/bin/env python3
"""Independent exact finite checks for the inversion-graded strong-Bruhat cover enumerator.
Standard library only; run with Python 3.9+.
"""
from itertools import permutations
from fractions import Fraction
from math import factorial

def conv(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c

def qint(m):
    return [1]*m

def qfactorial(m):
    f=[1]
    for j in range(1,m+1):
        f=conv(f,qint(j))
    return f

def inv(seq):
    return sum(x > y for k,x in enumerate(seq) for y in seq[k+1:])

def count_direct(n):
    N = n*(n-1)//2
    W=[[0]*(N+1) for _ in range(n)]
    total=0
    for p in permutations(range(n)):
        r=inv(p)
        for i in range(n):
            for j in range(i+1,n):
                if p[i]>=p[j]:
                    continue
                swapped=list(p)
                swapped[i],swapped[j]=swapped[j],swapped[i]
                if inv(swapped)==r+1:
                    W[j-i][r]+=1
                    total+=1
    return W,total

def test(n):
    W,total=count_direct(n)
    N=n*(n-1)//2
    factq=qfactorial(n)
    for d in range(1,n):
        lhs=conv(W[d],conv(qint(d),qint(d+1)))
        rhs=[0]*(d-1)+[(n-d)*d*x for x in factq]
        while lhs and lhs[-1]==0: lhs.pop()
        while rhs and rhs[-1]==0: rhs.pop()
        assert lhs==rhs, ('q identity',n,d,lhs,rhs)
        assert W[d][:N]==list(reversed(W[d][:N])), ('span palindromicity',n,d)
    T=[sum(W[d][r] for d in range(1,n)) for r in range(N+1)]
    mean=Fraction(sum(T),factorial(n))
    H=sum((Fraction(1,k) for k in range(1,n+1)),Fraction(0))
    expected=(n+1)*H-2*n
    assert mean==expected,(n,mean,expected)
    covariance=Fraction(sum(r*T[r] for r in range(N+1)),factorial(n))-mean*Fraction(N,2)
    assert covariance==-mean/2,(n,covariance,mean)
    # First and last coefficients count only the adjacent covers of the extreme permutations.
    assert T[0]==n-1 and T[N-1]==n-1
    assert T[N]==0
    return {'n':n,'permutations':factorial(n),'cover_incidence_tests':factorial(n)*n*(n-1)//2,'total_cover_edges':total,'mean':str(mean),'covariance_with_inversions':str(covariance),'coefficient_first':T[:min(10,len(T))]}

if __name__=='__main__':
    tests=0
    for n in range(2,9):
        result=test(n)
        tests+=result['cover_incidence_tests']
        print(result)
    print('PASS: exact q-polynomial identities for every span n=2..8;')
    print('PASS: inversion-rank duality, uniform means, and covariances;')
    print('total directly checked position pairs:',tests)
