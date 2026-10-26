#!/usr/bin/env python3
"""Exact finite checks for color-indicator covariance and precision on cycles.

No nonstandard packages or network connections are required.
"""
from fractions import Fraction as F
from itertools import product

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def parameters(n, q):
    b = q - 1
    r = F(-1, b)
    t = r ** n
    a = F(b, q*q) / (1 + b*t)
    g = (1-t)*(1+r)/(1-r)
    c = (b-1)*t
    h = (1-t)*(1-r*r)
    return r, t, a, g, c, h

def covariance(n, q):
    r, t, a, g, c, h = parameters(n,q)
    return [[a*(r**((j-i)%n)+r**(n-((j-i)%n))+c) for j in range(n)] for i in range(n)]

def precision(n, q):
    if (n,q)==(3,3):
        return None
    r, t, a, g, c, h = parameters(n,q)
    out=[]
    for i in range(n):
        row=[]
        for j in range(n):
            v=(1+r*r if i==j else 0)
            if (i-j)%n in (1,n-1): v-=r
            v=v/h-c/(g*(g+n*c))
            row.append(v/a)
        out.append(row)
    return out

def multiply(A,B):
    return [[sum(a*b for a,b in zip(A[i], [B[k][j] for k in range(len(B))])) for j in range(len(B[0]))] for i in range(len(A))]

def counts(n,q):
    z=0
    one=[0]*n
    pair=[[0]*n for _ in range(n)]
    for col in product(range(q),repeat=n):
        if any(col[i]==col[(i+1)%n] for i in range(n)):
            continue
        z+=1
        I=[int(v==0) for v in col]
        for i in range(n):
            one[i]+=I[i]
            for j in range(n):
                pair[i][j]+=I[i]*I[j]
    return z,one,pair

def run():
    # Direct enumeration is independent of transfer-matrix counting.
    for q in range(3,6):
        for n in range(3,8):
            z, one, pair=counts(n,q)
            check(z==(q-1)**n+(q-1)*(-1)**n, f'count:{n},{q}')
            K=covariance(n,q)
            for i in range(n):
                check(F(one[i],z)==F(1,q), f'marginal:{n},{q},{i}')
                for j in range(n):
                    observed=F(pair[i][j],z)-F(one[i]*one[j],z*z)
                    check(observed==K[i][j],f'covariance:{n},{q},{i},{j}')
    # Verify analytic precision and the complete sign law for a wider range.
    for q in range(3,8):
        for n in range(3,13):
            K=covariance(n,q)
            Q=precision(n,q)
            if (n,q)==(3,3):
                check(all(sum(K[i])==0 for i in range(n)), 'triangle singular')
                continue
            I=multiply(K,Q)
            for i in range(n):
                for j in range(n):
                    check(I[i][j]==(1 if i==j else 0),f'inversion:{n},{q},{i},{j}')
                    if i!=j:
                        neighbor=(i-j)%n in (1,n-1)
                        predicted=1 if neighbor or n%2==1 else -1
                        check((Q[i][j]>0 if predicted==1 else Q[i][j]<0),f'sign:{n},{q},{i},{j}')
            check(all(Q[i][i]==Q[0][0] and Q[i][i]>0 for i in range(n)), 'diagonal')
    print('VERIFIED_EXACT_ASSERTIONS',CHECKS)

if __name__=='__main__':
    run()
