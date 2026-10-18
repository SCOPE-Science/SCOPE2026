#!/usr/bin/env python3
"""Reproducible finite checks for the quadratic product projection kernel.

Run with Python >= 3.10 and NumPy. Finite checks are not a proof of
asymptotic convergence; the analytic argument is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
import math
import numpy as np


def moments(name, power):
    if power % 2:
        return F(0)
    k = power // 2
    if name == 'uniform':
        return F(1, 2 * k + 1)
    if name == 'arcsine':
        return F(math.comb(2 * k, k), 4**k)
    if name == 'mix':
        return (F(1, 2*k+1)+F(1))/2
    raise ValueError(name)


def parameters(name):
    s = moments(name, 2)
    t2 = moments(name, 4) - s * s
    assert s > 0 and t2 > 0
    return s, t2


def direct_kernel(x, y, name):
    s, t2 = parameters(name)
    ans = F(1)
    d = len(x)
    ans += sum((x[i]*y[i] / s for i in range(d)), F(0))
    ans += sum(((x[i]*x[i]-s)*(y[i]*y[i]-s) / t2 for i in range(d)), F(0))
    ans += sum((x[i]*x[j]*y[i]*y[j] / (s*s) for i in range(d) for j in range(i+1,d)),F(0))
    return ans


def square_kernel(x, y, name):
    s, t2 = parameters(name)
    S = sum((xx*yy for xx,yy in zip(x,y)),F(0))
    U = sum((xx*xx*yy*yy for xx,yy in zip(x,y)),F(0))
    return F(1) + S/s + sum(((xx*xx-s)*(yy*yy-s)/t2 for xx,yy in zip(x,y)),F(0)) + (S*S-U)/(2*s*s)


def poly_add(A, exp, val):
    A[exp] = A.get(exp, F(0)) + val


def poly_kernel_y(x, name):
    d=len(x)
    s,t2=parameters(name)
    P={tuple([0]*d):F(1)}
    for i in range(d):
        e=[0]*d; e[i]=1
        poly_add(P,tuple(e),x[i]/s)
        e[i]=2
        c=(x[i]*x[i]-s)/t2
        poly_add(P,tuple(e),c)
        poly_add(P,tuple([0]*d),-s*c)
    for i in range(d):
        for j in range(i+1,d):
            e=[0]*d;e[i]=e[j]=1
            poly_add(P,tuple(e),x[i]*x[j]/(s*s))
    return P


def integrate_square(P,name):
    ans=F(0)
    for e,a in P.items():
        for f,b in P.items():
            factor=F(1)
            for u,v in zip(e,f):
                factor*=moments(name,u+v)
            ans+=a*b*factor
    return ans


def numeric_kernel(x, Y, sigma2, tau2):
    # Equivalent square formula avoids forming d(d-1)/2 pair columns.
    S=Y@x
    U=(Y*Y)@(x*x)
    diag=((Y*Y-sigma2)@(x*x-sigma2))/tau2
    return 1+S/sigma2+diag+(S*S-U)/(2*sigma2*sigma2)


def monte_carlo(name,d,n=28000,seed=19):
    rng=np.random.default_rng(seed+d)
    x=np.ones(d)
    if name=='uniform':
        s,t2=1/3,4/45
    elif name=='arcsine':
        s,t2=1/2,1/8
    else:
        s,t2=2/3,7/45
    count=0;total=0.0
    while count<n:
        m=min(1400,n-count)
        if name=='uniform':
            Y=rng.uniform(-1,1,(m,d))
        elif name=='arcsine':
            Y=np.cos(rng.uniform(0,math.pi,(m,d)))
        else:
            Y=np.where(rng.random((m,d))<0.5,rng.uniform(-1,1,(m,d)),rng.choice([-1.,1.],(m,d)))
        val=np.abs(numeric_kernel(x,Y,s,t2))
        total+=float(np.sum(val));count+=m
    return total/(n*d)


def main():
    checks=0
    for name in ('uniform','arcsine','mix'):
        s,t2=parameters(name)
        assert moments(name,0)==1;checks+=1
        assert moments(name,1)==0;checks+=1
        assert moments(name,2)==s;checks+=1
        assert moments(name,4)-s*s==t2;checks+=1
        for d in range(1,5):
            x=[F(2*i-d,2*d+3) for i in range(d)]
            y=[F(3*i-d,d+4) for i in range(d)]
            assert direct_kernel(x,y,name)==square_kernel(x,y,name);checks+=1
            P=poly_kernel_y(x,name)
            assert integrate_square(P,name)==direct_kernel(x,x,name);checks+=1
        # Exact uniform basis orthogonality through degree two.
        assert (moments(name,4)-2*s*moments(name,2)+s*s)/t2==1;checks+=1
    target_u=6/math.sqrt(2*math.pi*math.e)
    target_c=4/math.sqrt(2*math.pi*math.e)
    target_m=3/math.sqrt(2*math.pi*math.e)
    results={}
    for name,target in [('uniform',target_u),('arcsine',target_c),('mix',target_m)]:
        vals=[]
        for d in (80,320):
            observed=monte_carlo(name,d)
            assert abs(observed-target)<0.20,(name,d,observed,target)
            checks+=1
            vals.append((d,observed))
        results[name]=[target,vals]
    print('PASS:',checks,'exact and stochastic consistency assertions')
    for name,(target,vals) in results.items():
        print(name,'theoretical_limit',round(target,9),'finite_dimension_estimates',vals)
    print('Limits follow from the triangular-array central limit theorem, not from these tests.')

if __name__=='__main__':
    main()
