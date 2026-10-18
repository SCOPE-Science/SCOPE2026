#!/usr/bin/env python3
"""Reproducible checks for quantile-selected planar Kaczmarz on equispaced rows.
All equations examined here are deterministic; numeric checks supplement the proof.
"""
import cmath
import math
import random

ATOL = 3e-10
assertions = 0

def check(p, msg='check failed'):
    global assertions
    assertions += 1
    if not p:
        raise AssertionError(msg)

def rows(m):
    return [(math.cos(math.pi*j/m), math.sin(math.pi*j/m)) for j in range(m)]

def norm2(e):
    return e[0]*e[0]+e[1]*e[1]

def selected(e, a, r):
    z=sorted(((v[0]*e[0]+v[1]*e[1])**2, j) for j,v in enumerate(a))
    threshold=z[r-1][0]
    return [j for v,j in z if v<=threshold+2e-13*max(1.0,norm2(e))]

def step(e, a, j):
    s=e[0]*a[j][0]+e[1]*a[j][1]
    return (e[0]-s*a[j][0], e[1]-s*a[j][1])

def fraction(e,a,r):
    J=selected(e,a,r)
    return (sum(norm2(step(e,a,j)) for j in J)/len(J))/norm2(e)

def F(m,r):
    return 0.5+math.sin(math.pi*r/m)/(2*r*math.sin(math.pi/m))

def B(m,r):
    if r<m and r%2==0:
        return F(m,r+1)
    return F(m,r)

def critical_error(m,r,scale=1):
    # phi is the direction of the ERROR PERPENDICULAR, centered at r nearest rows.
    phi=(r-1)*math.pi/(2*m)
    return (scale*math.cos(phi+math.pi/2),scale*math.sin(phi+math.pi/2))

def norm_error_at_time(e0,a,r,t):
    # Enumerate all row-index transitions, merging orientations after first step.
    if t==0:return norm2(e0)
    J=selected(e0,a,r)
    energy_by_row={}
    for j in J:
        e1=step(e0,a,j)
        energy_by_row[j]=energy_by_row.get(j,0)+norm2(e1)/len(J)
    for _ in range(1,t):
        new={}
        for i,weighted in energy_by_row.items():
            ee=(-a[i][1],a[i][0])
            eligible=selected(ee,a,r)
            for j in eligible:
                multiplier=norm2(step(ee,a,j))
                new[j]=new.get(j,0)+weighted*multiplier/len(eligible)
        energy_by_row=new
    return sum(energy_by_row.values())

random.seed(34215)
for m in range(2,24):
    a=rows(m)
    # Finite tight frame: sum a_j a_j^T = mI/2.
    check(abs(sum(x*x for x,y in a)-m/2)<ATOL)
    check(abs(sum(y*y for x,y in a)-m/2)<ATOL)
    check(abs(sum(x*y for x,y in a))<ATOL)
    for r in range(1,m+1):
        q=F(m,r); b=B(m,r)
        check(0.49<=q<=1.00000001)
        check(0.49<=b<=1.00000001)
        e=critical_error(m,r)
        # Exact sharp worst initial angle; ties accepted in addition to r are excluded here.
        check(len(selected(e,a,r))==r,(m,r,'wrong count at minimizer',selected(e,a,r)))
        check(abs(fraction(e,a,r)-q)<ATOL,(m,r,'first sharp',fraction(e,a,r),q))
        for i in range(m):
            e_axis=(-a[i][1],a[i][0])
            check(abs(fraction(e_axis,a,r)-b)<ATOL,(m,r,i,'axis rate',fraction(e_axis,a,r),b))
            check(len(selected(e_axis,a,r))==r+(r<m and r%2==0),(m,r,i,'axis selected length'))
        for t in range(1,5):
            exact=norm_error_at_time(e,a,r,t)
            goal=q*b**(t-1)
            check(abs(exact-goal)<ATOL,(m,r,t,exact,goal))
        for _ in range(10):
            phi=random.uniform(-math.pi,math.pi)
            e=(math.cos(phi),math.sin(phi))
            check(fraction(e,a,r)<=q+ATOL,(m,r,phi,'upper envelope'))
            J=selected(e,a,r)
            check(len(J)>=r)
            for j in J:
                e2=step(e,a,j)
                if norm2(e2)>1e-24:
                    check(abs(fraction(e2,a,r)-b)<ATOL,(m,r,phi,'two-step identity'))

for m in [20,50,100,1000]:
    for r in [2,3,4,5]:
        if r>=m:continue
        asymptotic=(r*r-1)*math.pi**2/(12*m*m)
        exact=1-F(m,r)
        if m>=100:
            check(abs(exact/asymptotic-1)<0.008,(m,r,exact,asymptotic))

# The projective continuum limit is the sine-integral expression.
for q in [.1,.25,.5,.73,.97]:
    m=2000
    r=round(m*q)
    target=.5+math.sin(math.pi*q)/(2*math.pi*q)
    check(abs(F(m,r)-target)<5e-7)
    check(abs(B(m,r)-target)<0.0007)

print('PASS:',assertions,'deterministic checks; sharp first-step, post-step, full-horizon, and asymptotic identities verified')
