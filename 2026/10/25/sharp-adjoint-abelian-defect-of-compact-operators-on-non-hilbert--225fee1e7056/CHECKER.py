#!/usr/bin/env python3
"""Finite reproducibility checks for a normalized-duality stability inequality.

The infinite-dimensional proof is analytical; these are consistency tests only.
"""
import cmath
import math
import random

def lp(z,p):
    return sum(abs(v)**p for v in z)**(1/p)

def dual(x,p):
    n=lp(x,p)
    if n==0:
        return [0j]*len(x)
    return [(abs(z)**(p-2))*z.conjugate()*n**(2-p) for z in x]

def t_apply(m,x):
    return [sum(a*b for a,b in zip(row,x)) for row in m]

def tp_apply(m,y):
    return [sum(m[i][j]*y[i] for i in range(len(m))) for j in range(len(m[0]))]

def defect(m,x,p):
    y=t_apply(m,x)
    jy=dual(y,p)
    tjx=tp_apply(m,dual(x,p))
    q=p/(p-1)
    return lp([a-b for a,b in zip(jy,tjx)],q)

def cp(p):
    return (p-2)/(p-1)*(p-1)**(-1/(p-2))

rng=random.Random(15422)
count=0
for p in (2.25,3.0,4.0,6.0,12.0):
    a=(p-1)**(-1/(p-2))
    b=(1-a**p)**(1/p)
    projection=[[1,0],[0,0]]
    x=[a+0j,b+0j]
    assert abs(lp(x,p)-1)<1e-12
    assert abs(defect(projection,x,p)-cp(p))<1e-11
    count+=1
    for j in range(180):
        n=4
        m=[[complex(rng.uniform(-1,1),rng.uniform(-1,1)) if i<3 and k<3 else 0j
            for k in range(n)] for i in range(n)]
        u=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(3)]+[0j]
        u=[v/lp(u,p) for v in u]
        v=[a*z for z in u]
        v[3]=b
        assert abs(lp(v,p)-1)<1e-11
        lhs=defect(m,v,p)
        tu=lp(t_apply(m,u),p)
        # Here T annihilates coordinate 4, and T' likewise annihilates its dual.
        exact_vec=[a*w-a**(p-1)*z for w,z in zip(dual(t_apply(m,u),p),tp_apply(m,dual(u,p)))]
        rhs=lp(exact_vec,p/(p-1))
        assert abs(lhs-rhs)<1e-10
        lower=a*tu-a**(p-1)*lp(tp_apply(m,dual(u,p)),p/(p-1))
        assert lhs+1e-10>=lower
        count+=2
print(f"PASS: {count} finite consistency assertions; analytic theorem independent of tests")
