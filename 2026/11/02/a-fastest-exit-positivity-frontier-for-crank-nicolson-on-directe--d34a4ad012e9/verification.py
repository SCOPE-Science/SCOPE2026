#!/usr/bin/env python3
"""Reproducible exact checks of Crank–Nicolson on one-way directed cycles.

The infinite-family theorem is proved analytically; these tests are finite corroboration.
"""
from fractions import Fraction as F
from itertools import product
from decimal import Decimal, localcontext


def invert(a):
    n=len(a)
    v=[[F(x) for x in a[i]]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(i for i in range(j,n) if v[i][j]!=0)
        v[j],v[k]=v[k],v[j]
        c=v[j][j]
        v[j]=[x/c for x in v[j]]
        for i in range(n):
            if i!=j:
                c=v[i][j]
                v[i]=[x-c*y for x,y in zip(v[i],v[j])]
    return [row[n:] for row in v]


def cycle_test(rates,t):
    n=len(rates)
    Q=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,r in enumerate(rates):
        Q[i][i]=-r
        Q[i][(i+1)%n]=r
    R=invert([[F(i==j)-t*Q[i][j] for j in range(n)] for i in range(n)])
    C=[[2*R[i][j]-F(i==j) for j in range(n)] for i in range(n)]
    z=[t*r/(1+t*r) for r in rates]
    B=F(1)
    for a in z: B*=a
    diag=[1/((1+t*r)*(1-B)) for r in rates]
    assert [R[i][i] for i in range(n)]==diag
    assert all(C[i][j]>0 for i in range(n) for j in range(n) if i!=j)
    assert all(sum(row)==1 for row in C)
    rmax=max(rates)
    i=rates.index(rmax)
    f=(1-t*rmax)
    for j,r in enumerate(rates):
        if j!=i:f*=1+t*r
    u=t**n
    for r in rates:u*=r
    f+=u
    den=F(1)
    for r in rates:den*=1+t*r
    den-=u
    assert C[i][i]==f/den
    assert min(C[j][j] for j in range(n))==C[i][i]
    assert (all(v>=0 for row in C for v in row))==(f>=0)
    return C[i][i]<0

samples=negative=0
for n in range(3,9):
    cases=[tuple(F(k) for k in r) for r in product((1,2,3),repeat=n)]
    # Use all cases through n=6, a deterministic spaced selection for n=7,8.
    if n>=7:cases=cases[::max(1,len(cases)//200)]
    for rates in cases:
        for t in (F(1,10),F(1,2),F(1),F(2)):
            negative+=cycle_test(rates,t)
            samples+=1

# For the uniform cycle, x_n=t_*r solves x-1=x^n/(1+x)^(n-1).
# Root sequences bracketed with high-precision Decimal without floating cancellation.
with localcontext() as ctx:
    ctx.prec=90
    vals=[]
    for n in range(3,51):
        lo=Decimal(1)
        hi=Decimal(2)
        for _ in range(340):
            x=(lo+hi)/2
            f=x-1-x**n/(1+x)**(n-1)
            if f>0:hi=x
            else:lo=x
        vals.append((n,(lo+hi)/2))
    assert all(vals[i][1]>vals[i+1][1] for i in range(len(vals)-1))
    x3=vals[0][1]
    assert abs(x3-(1+Decimal(5).sqrt())/2)<Decimal('1e-65')
    assert abs((vals[-1][1]-1)*2**(vals[-1][0]-1)-1)<Decimal('1e-10')
print('PASS rational_cycle_step_cases',samples,'negative_cases',negative,
      'high_precision_uniform_roots',len(vals),'last_scaled_gap',
      str((vals[-1][1]-1)*2**(vals[-1][0]-1)))
