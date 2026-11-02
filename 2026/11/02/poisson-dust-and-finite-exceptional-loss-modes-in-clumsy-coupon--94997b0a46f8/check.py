#!/usr/bin/env python3
"""Reproducibility checks for finite-defect clumsy coupon collection.

All identities checked here are finite exact computations or numerical
cross-checks. The asymptotic theorem is proved analytically in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
import math

checks=0

def check(condition, description):
    global checks
    assert condition, description
    checks += 1


def solve_linear(a, b):
    n=len(b)
    mat=[list(a[i])+[b[i]] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if mat[i][j])
        mat[j],mat[pivot]=mat[pivot],mat[j]
        div=mat[j][j]
        mat[j]=[v/div for v in mat[j]]
        for i in range(n):
            if i==j:continue
            mult=mat[i][j]
            if mult:
                mat[i]=[mat[i][k]-mult*mat[j][k] for k in range(n+1)]
    return [row[-1] for row in mat]


def matrix_pgf(p,z):
    n=len(p)
    states=list(range(1,1<<n)); idx={mask:i for i,mask in enumerate(states)}
    a=[[F(int(i==j)) for j in range(len(states))] for i in range(len(states))]
    b=[F(0) for _ in states]
    for mask in states:
        i=idx[mask]
        for j,q in enumerate(p):
            for next_mask,prob in ((mask|(1<<j),q),(mask&~(1<<j),1-q)):
                val=z*prob/n
                if next_mask==0:b[i]+=val
                else:a[i][idx[next_mask]]-=val
    f=solve_linear(a,b)
    mass=[]
    for mask in range(1<<n):
        pr=F(1)
        for j,q in enumerate(p):pr*=q if mask&(1<<j) else 1-q
        mass.append(pr)
    return mass[0]+sum(mass[mask]*f[idx[mask]] for mask in states)


def closed_pgf(p,z):
    n=len(p)
    a=[F(1)]
    for q in p:
        b=[F(0)]*(len(a)+1)
        for k,v in enumerate(a):
            b[k]+=v*(1-q);b[k+1]+=v*q
        a=b
    s=F(n)*(1-z)/z
    return a[0]/sum(v*s/(s+k) for k,v in enumerate(a))

for n in range(1,5):
    for p in product((F(0),F(1,5),F(2,5)), repeat=n):
        if n>=4 and p.count(F(0))<1:continue
        for z in (F(1,3),F(2,3)):
            q1=matrix_pgf(p,z)
            q2=closed_pgf(p,z)
            check(q1==q2,(n,p,z,q1,q2))

# Poisson-dust (r=0) and fixed-outlier (r=1) elementary transform checks.
for q in (F(1,8),F(1,3),F(1,2),F(3,4)):
    for s in (F(1,2),F(1),F(3)):
        # q_1=q, dust=0. Its limit is a mixture of zero and Exp(1-q).
        stationary_laplace=(1-q)/((1-q)+q*s/(s+1))
        mixture_laplace=(1-q)+q*(1-q)/(1-q+s)
        check(stationary_laplace==mixture_laplace,(q,s))
        check(1-q != math.exp(-float(q)),('atoms',q))

# For a finite number of fixed exceptional coupons, the integral gives an
# exact Laplace transform of the independent refresh CTMC started stationary.
def simpson(fun,a,b,n=6000):
    assert n%2==0
    h=(b-a)/n
    acc=fun(a)+fun(b)
    for j in range(1,n):acc+=(4 if j%2 else 2)*fun(a+j*h)
    return acc*h/3

def integral_laplace(q,c,s):
    pi0=math.prod(1-x for x in q)*math.exp(-c)
    def f(t):
        u=math.exp(-t)
        return s*math.exp(-s*t+c*(u-1))*math.prod(1-x+x*u for x in q)
    return pi0/simpson(f,0,50,4000)

def finite_laplace(q,c,m,s):
    p=q+[c/(m-len(q))]*(m-len(q))
    pi0=math.prod(1-x for x in q)*(1-c/(m-len(q)))**(m-len(q))
    sm=m*math.expm1(s/m)
    def f(t):
        u=math.exp(-t)
        small=1-c/(m-len(q))*(1-u)
        return sm*math.exp(-sm*t)*math.prod(1-x+x*u for x in q)*small**(m-len(q))
    return pi0/simpson(f,0,50,4000)

for q,c in (([],0.75),([0.4],0.7),([0.2,0.35],1.1)):
    for s in (1.,2.):
        target=integral_laplace(q,c,s)
        vals=[finite_laplace(q,c,m,s) for m in (128,512,2048)]
        check(abs(vals[-1]-target)<0.005, (q,c,s,target,vals))
        check(abs(vals[2]-target)<abs(vals[0]-target),(q,c,s,target,vals))
        for v in vals:check(0<v<=1,(q,c,s,v))

# The limit's mass at zero distinguishes fixed defects from the pure dust law.
for q,c in (([.5],0.),([.25,.35],.8),([.1,.2,.3],1.)):
    atom=math.exp(-c)*math.prod(1-x for x in q)
    check(abs(atom-math.exp(-c-sum(q)))>1e-5,(q,c))
print(f'PASS: {checks} finite exact or numerical assertions')
