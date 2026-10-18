#!/usr/bin/env python3
"""Finite checks for the Gaussian geometry of star cosmological polytopes.

Requires only Python's standard library. Numerical sampling corroborates the
identities; it does not prove the limiting assertions.
"""
import math
import random


def vertices(m):
    d = 2*m + 1
    ans = []
    for i in range(m):
        for a,b,c in ((1,1,-1),(1,-1,1),(-1,1,1)):
            v=[0.0]*d
            v[0]=a
            v[i+1]=b
            v[m+i+1]=c
            ans.append(tuple(v))
    return ans


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def direct(g,v):
    vals=[dot(g,x) for x in v]
    j=max(range(len(vals)),key=lambda i: vals[i])
    return vals[j],j


def reduced(g,m):
    z=g[0]
    xi=[(g[1+i]-g[1+m+i])/math.sqrt(2) for i in range(m)]
    yi=[(g[1+i]+g[1+m+i])/math.sqrt(2) for i in range(m)]
    M=max(map(abs,xi));N=max(yi)
    return max(z+math.sqrt(2)*M,-z+math.sqrt(2)*N),M,N


def cdf_integrand(g,t,m):
    # Exact conditional integrand of the finite Gaussian support CDF.
    if g>t:return 0.0
    F_M=math.erf((t-g)/2)**m
    F_N=(0.5*(1+math.erf((t+g)/2)))**m
    return math.exp(-g*g/2)/math.sqrt(2*math.pi)*F_M*F_N


def simpson(f,a,b,n):
    assert n%2==0
    h=(b-a)/n
    s=f(a)+f(b)
    for k in range(1,n):
        s+=(4 if k%2 else 2)*f(a+k*h)
    return h*s/3


def main():
    rng=random.Random(611082)
    tested=0
    for m in range(1,21):
        vs=vertices(m)
        assert len(vs)==3*m
        for _ in range(180):
            g=[rng.gauss(0,1) for _ in range(2*m+1)]
            h,j=direct(g,vs)
            k,M,N=reduced(g,m)
            assert abs(h-k)<2e-12,(m,h,k)
            z=g[0]
            alternate=(M+N)/math.sqrt(2)+abs(z+(M-N)/math.sqrt(2))
            assert abs(h-alternate)<2e-12
            # Width must depend only on the intrinsic projection.
            gmean=sum(g)/len(g)
            gh=[x-gmean for x in g]
            w=h+direct([-x for x in g],vs)[0]
            w_h=direct(gh,vs)[0]+direct([-x for x in gh],vs)[0]
            assert abs(w-w_h)<2e-12
            # The winning family agrees with the two-branch comparison.
            branch_one=(z+math.sqrt(2)*M > -z+math.sqrt(2)*N)
            assert (j%3 in (0,1))==branch_one
            tested+=1
    # Integrate the exact finite CDF; compare independent simulations.
    for m in (1,2,4):
        vs=vertices(m)
        for t in (-0.5,0,0.7,1.5):
            val=simpson(lambda g:cdf_integrand(g,t,m),-11,min(t,11),6000)
            hits=0
            reps=22000
            for _ in range(reps):
                g=[rng.gauss(0,1) for _ in range(2*m+1)]
                hits+=direct(g,vs)[0]<=t
            empirical=hits/reps
            assert abs(val-empirical)<0.025,(m,t,val,empirical)
    # m=1 is an equilateral triangle: all three angular probabilities 1/3.
    v=vertices(1)
    lens=[sum(x*x for x in p) for p in v]
    distances=[sum((v[i][k]-v[j][k])**2 for k in range(3))
               for i in range(3) for j in range(i+1,3)]
    assert lens==[3.0]*3 and distances==[8.0]*3
    assert abs(((2/3)**2/2+(1/3)**2)-1/3)<1e-14
    # Diagnostic only: a common hub coordinate leaves order-one fluctuation.
    for m in (500,3000):
        discrepancies=[]
        for _ in range(800):
            z=rng.gauss(0,1)
            x=[rng.gauss(0,1) for _ in range(m)]
            y=[rng.gauss(0,1) for _ in range(m)]
            M=max(map(abs,x));N=max(y)
            h=max(z+math.sqrt(2)*M,-z+math.sqrt(2)*N)
            discrepancies.append(h-2*math.sqrt(math.log(m))-abs(z))
        print('asymptotic diagnostic m=',m,'mean error=',sum(discrepancies)/len(discrepancies))
    print('VERIFY_OK deterministic support/width checks:',tested,
          '; finite CDF numerical checks:',12)


if __name__=='__main__':
    main()
