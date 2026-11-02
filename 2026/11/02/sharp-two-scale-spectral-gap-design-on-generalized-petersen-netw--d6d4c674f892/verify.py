#!/usr/bin/env python3
"""Reproduces finite checks of weighted generalized Petersen spectral bounds.

Requires Python 3.9+ and NumPy. The analytic proof is contained in RESULT.md;
finite tests and numerical eigensolvers do not establish the asymptotic theorem.
"""
import math
import random
import numpy as np

PI = math.pi

def modes(n, a, b, c):
    vals = [2.0 * c]
    for k in range(1, n):
        e = 4.0 * math.sin(PI*k/n)**2
        d = 4.0 * math.sin(2*PI*k/n)**2
        A, B = a*e, b*d
        vals.append(c + (A+B)/2.0 - math.hypot(c, (A-B)/2.0))
    return vals

def upper(n):
    e = 4.0*math.sin(PI/n)**2
    d = 4.0*math.sin(2.0*PI/n)**2
    s = math.sqrt(d)
    return d/((1+s)**2+1), e*(1+s)**2 < d

def dense(n, a, b, c):
    L = np.zeros((2*n,2*n))
    for j in range(n):
        for u, v, w in ((j,(j+1)%n,a),(n+j,n+(j+2)%n,b),(j,n+j,c)):
            L[u,u]+=w; L[v,v]+=w; L[u,v]-=w; L[v,u]-=w
    return L

def check():
    rng=random.Random(20261030)
    count=0
    for n in range(5,27):
        for _ in range(7):
            arr=[0.1+rng.random() for z in range(3)]; sm=sum(arr); a,b,c=[t/sm for t in arr]
            ev=np.linalg.eigvalsh(dense(n,a,b,c))
            val=min(modes(n,a,b,c))
            assert abs(ev[1]-val)<2e-11, (n,ev[1],val)
            assert abs(ev[0])<2e-11
            count+=2
    # Independent nonuniform edge weights: no cyclic symmetry is assumed.
    for n in range(13, 34):
        cap, good = upper(n)
        assert good
        for _ in range(5):
            weights = [rng.random() for _ in range(3*n)]
            scale = n/sum(weights)
            weights = [w*scale for w in weights]
            L = np.zeros((2*n, 2*n))
            for j in range(n):
                for x, y, w in ((j,(j+1)%n,weights[j]),
                                (n+j,n+(j+2)%n,weights[n+j]),
                                (j,n+j,weights[2*n+j])):
                    L[x,x]+=w; L[y,y]+=w
                    L[x,y]-=w; L[y,x]-=w
            gap = np.linalg.eigvalsh(L)[1]
            assert 0 <= gap < cap + 2e-11, ('nonuniform',n,gap,cap)
            count += 1
    for n in range(13,2501):
        cap,valid=upper(n)
        assert valid, ('upper-vector condition',n)
        for _ in range(2):
            a,b,c=[rng.random() for _ in range(3)]
            s=a+b+c; a,b,c=a/s,b/s,c/s
            assert min(modes(n,a,b,c)) <= cap+1e-11, ('upper',n,a,b,c)
            count+=1
        count+=1
    for n in (50,100,101,200,201,500,501,1000,1001,2000,2001,4000,4001):
        alpha=(5 if n%2==0 else 4)*PI*PI
        a=alpha/n**2; c=2*PI/n; b=1-a-c
        gap=min(modes(n,a,b,c))
        cap,_=upper(n)
        assert b>0 and 0 < gap < cap
        assert gap == min(modes(n,a,b,c))
        correction=(8*PI*PI/n**2-gap)*n**3
        assert abs(correction-32*PI**3)<(8000/n+25), (n,correction)
        # Most-binding Fourier blocks are k=1,n-1 for sufficiently large n.
        if n>=500:
            vals=modes(n,a,b,c)
            assert abs(vals[1]-gap)<1e-10 and abs(vals[n-1]-gap)<1e-10
        count+=5
    print('PASS',count,'deterministic checks; max n = 4001')

if __name__=='__main__': check()
