#!/usr/bin/env python3
"""Exact finite checks of an algebraic generating function for Dyck word complexity.

The infinite theorem rests on the analytic proof, not this finite checker.
"""
from collections import defaultdict
from itertools import product


def direct_words(m, n):
    count = 0
    for w in product(range(2*m), repeat=n):
        stack = []
        for letter in w:
            if letter < m:
                stack.append(letter)
            elif stack:
                if stack[-1] != letter-m:
                    break
                stack.pop()
        else:
            count += 1
    return count


def weighted_coarse(m, n):
    states = {(0,0):1}
    for _ in range(n):
        after=defaultdict(int)
        for (height, maximum), multiplicity in states.items():
            after[(height-1, maximum)]+=m*multiplicity
            after[(height+1, max(maximum, height+1))]+=multiplicity
        states=after
    return sum(multiplicity*m**maximum for (_, maximum), multiplicity in states.items())


def algebraic_coefficients(m, size):
    # q=t(1+M*q^2) as a formal series; F=(1-q)/((1-(M+1)t)(1-Mq)).
    q=[0]*(size+1)
    for degree in range(1,size+1):
        q[degree]=(1 if degree==1 else 0)+m*sum(q[i]*q[degree-1-i] for i in range(degree))
    denominator=[0]*(size+1)
    denominator[0]=1
    for degree in range(1,size+1):
        denominator[degree]=-m*q[degree]-(m+1 if degree==1 else 0)+m*(m+1)*q[degree-1]
    ans=[0]*(size+1)
    for degree in range(size+1):
        ans[degree]=(1 if degree==0 else 0)-q[degree]-sum(denominator[k]*ans[degree-k] for k in range(1,degree+1))
    return ans


def main():
    checks=0
    for m, limit in [(2,9),(3,7),(4,5)]:
        coefs=algebraic_coefficients(m,18)
        for n in range(limit+1):
            a,b,c=direct_words(m,n),weighted_coarse(m,n),coefs[n]
            assert a==b==c,(m,n,a,b,c)
            checks+=1
        for n in range(limit+1,19):
            assert weighted_coarse(m,n)==coefs[n],(m,n)
            checks+=1
        print('M=',m,'n0..9=',coefs[:10])
    assert algebraic_coefficients(2,9)==[1,4,14,48,160,528,1720,5568,17888,57216]
    print('PASS: {} exact three-method/weighted-series comparisons'.format(checks))

if __name__=='__main__':
    main()
