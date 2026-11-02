#!/usr/bin/env python3
"""Exact checks of the derangement cycle-count sign theorem; standard library only."""
from fractions import Fraction
from itertools import permutations
from math import factorial, exp

CHECKS = 0

def verify(condition, description):
    global CHECKS
    if not condition:
        raise AssertionError(description)
    CHECKS += 1

def table(theta, nmax):
    a = [Fraction(0)] * (nmax+1)
    b = [Fraction(0)] * (nmax+1)
    a[0] = 1
    for n in range(2,nmax+1):
        a[n] = (n-1)*(a[n-1]+theta*a[n-2])
        b[n] = (n-1)*(b[n-1]+theta*(b[n-2]+a[n-2]))
    return a, b

def cycle_lengths(p):
    n = len(p)
    seen = [False]*n
    sizes = []
    for i in range(n):
        if seen[i]: continue
        j = i
        m = 0
        while not seen[j]:
            seen[j] = True
            j = p[j]
            m += 1
        sizes.append(m)
    return sizes

def brute(n, theta):
    z=Fraction(0)
    ek=Fraction(0)
    ecr=[Fraction(0)]*(n+1)
    ecrk=[Fraction(0)]*(n+1)
    cases=0
    for p in permutations(range(n)):
        if any(p[i]==i for i in range(n)):
            continue
        lengths=cycle_lengths(p)
        w=theta**len(lengths)
        cases += 1
        z += w
        ek += w*len(lengths)
        for r in lengths:
            ecr[r] += w
            ecrk[r] += w*len(lengths)
    return z,ek,ecr,ecrk,cases

if __name__=='__main__':
    histories=0
    for theta in (Fraction(1,2),Fraction(1),Fraction(2)):
        a,b=table(theta,450)
        verify(a[0]==1 and a[1]==0 and a[2]==theta and a[3]==2*theta,'initial conditions')
        verify(b[2]==theta and b[3]==2*theta,'initial cycle moments')
        verify(Fraction(b[2],a[2])==1 and Fraction(b[3],a[3])==1,'plateau')
        for n in range(4,451):
            m=Fraction(b[n],a[n]); prev=Fraction(b[n-1],a[n-1]); prev2=Fraction(b[n-2],a[n-2])
            verify(0<m-prev<1,'strict increase')
            verify(0<m-prev2<1,'two-step bound')
            signs=[]
            for r in list(range(2,n-1))+[n]:
                remain=n-r
                score = 1+(Fraction(b[remain],a[remain]) if remain>=2 else 0)-m
                signs.append((r,score))
            verify(signs[0][1]>0 and signs[-1][1]<0,'opposite endpoints')
            verify(all(not (signs[i][1]<0 and signs[j][1]>0) for i in range(len(signs)) for j in range(i+1,len(signs))) if n<21 else all(signs[i][1]>=signs[i+1][1] for i in range(len(signs)-1)), 'single crossing')
        for n in range(2,9):
            z,ek,ecr,ecrk,cases=brute(n,theta);histories+=cases
            verify(z==a[n],f'weighted derangement mass theta={theta} n={n}')
            verify(ek==b[n],f'total cycles theta={theta} n={n}')
            for r in range(2,n+1):
                mark=theta*Fraction(factorial(n),r*factorial(n-r))*Fraction(a[n-r],a[n])
                calc=Fraction(ecr[r],z)
                verify(calc==mark,f'cycle expectation theta={theta} n={n} r={r}')
                if mark:
                    remain=n-r
                    meanrem=Fraction(b[remain],a[remain]) if remain>=2 else Fraction(0)
                    predicted=mark*(1+meanrem)
                    verify(Fraction(ecrk[r],z)==predicted, 'size bias identity')
                    covariance=Fraction(ecrk[r],z)-calc*Fraction(ek,z)
                    verify(covariance==mark*(1+meanrem-Fraction(b[n],a[n])), 'covariance formula')
                else:
                    verify(ecrk[r]==0, 'forbidden residual singleton')
        for n in (120,300,450):
            mean=Fraction(b[n],a[n])
            first=next(r for r in list(range(2,n-1))+[n] if 1+(Fraction(b[n-r],a[n-r]) if n-r>=2 else 0)-mean<=0)
            limit=1-exp(-1/float(theta))
            verify(abs(first/n-limit)<.04,f'asymptotic phase theta={theta} n={n}')
            if n==450:print('theta',theta,'n',n,'first nonpositive cycle length',first,'ratio',round(first/n,6),'limit',round(limit,6))
    print('PASS:',CHECKS,'exact assertions;',histories,'enumerated weighted derangements (counted across theta)')
