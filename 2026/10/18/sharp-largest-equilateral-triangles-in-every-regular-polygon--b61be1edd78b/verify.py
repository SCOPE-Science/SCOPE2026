#!/usr/bin/env python3
"""Reproducibility checks for the regular-polygon equilateral triangle theorem.
The theorem is proved in RESULT.md; finite tests are supporting diagnostics.
Only the Python standard library is required.
"""
import math
from itertools import combinations

PI = math.pi

def exact_profile(m):
    if m % 3 == 0:
        return 1.0
    delta = PI / (3*m)
    alpha = PI/m
    beta = (2*((m-1)//3)+1)*alpha
    return (math.cos(alpha)-math.cos(beta))/(math.cos(delta)-math.cos(beta))

def max_support(m, theta, cx, cy, radius):
    alpha = PI/m
    a = math.cos(alpha)
    return max(cx*math.cos((2*k+1)*alpha)+cy*math.sin((2*k+1)*alpha)
               +radius*max(math.cos((2*k+1)*alpha-theta-2*j*PI/3) for j in range(3))-a
               for k in range(m))

def determinant3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

def lp_profile(m, theta):
    alpha = PI/m
    a = math.cos(alpha)
    rows = []
    for k in range(m):
        phi = (2*k+1)*alpha
        support = max(math.cos(phi-theta-2*j*PI/3) for j in range(3))
        rows.append((math.cos(phi),math.sin(phi),support))
    best = 0.0
    for inds in combinations(range(m),3):
        v,w,z=(rows[j] for j in inds)
        den=determinant3(v,w,z)
        if abs(den)<1.e-11:
            continue
        centerx=a*determinant3((1,v[1],v[2]),(1,w[1],w[2]),(1,z[1],z[2]))/den
        centery=a*determinant3((v[0],1,v[2]),(w[0],1,w[2]),(z[0],1,z[2]))/den
        rr=a*determinant3((v[0],v[1],1),(w[0],w[1],1),(z[0],z[1],1))/den
        if rr <= best + 1.e-10:
            continue
        if all(row[0]*centerx+row[1]*centery+row[2]*rr <= a+1.e-9 for row in rows):
            best=rr
    return best

def main():
    witness_count = 0
    for m in range(4,301):
        if m%3==0:
            continue
        alpha=PI/m
        delta=alpha/3
        beta=(2*((m-1)//3)+1)*alpha
        s=1 if m%3==1 else -1
        a=math.cos(alpha)
        rr=exact_profile(m)
        assert 0 < rr < 1
        assert max_support(m,0,1-rr,0,rr) < 4.e-12, (m,'infeasible')
        L=-a/math.cos(beta)
        D=-math.sin(alpha)/math.sin(beta)
        assert L+1.e-12 >= abs(D)
        A=a+L*math.cos(delta)
        B=math.sin(alpha)+s*D*math.sin(delta)
        assert B>A*math.tan(delta/2), (m,'orientation gap')
        assert abs(rr-a*(1+L)/A) < 1.e-12
        for theta in (delta/4,delta/2,3*delta/4,delta):
            dual_bound=a*(1+L)/(A*math.cos(theta)+B*math.sin(theta))
            assert dual_bound < rr - 1.e-14, (m,theta,dual_bound,rr)
        witness_count+=1
    lp_count=0
    for m in range(3,19):
        delta=PI/(3*m)
        for frac in (0,.25,.5,.75,1):
            theta=frac*delta
            observed=lp_profile(m,theta)
            bound=exact_profile(m)
            if frac == 0:
                assert abs(observed-bound) < 2.e-8,(m,frac,observed,bound)
            elif m%3 != 0:
                assert observed < bound-1.e-9,(m,frac,observed,bound)
            else:
                assert observed<=bound+2.e-8
            lp_count+=1
    print('VERIFY_OK analytic_witness_cases=%d independent_LP_orientations=%d' % (witness_count,lp_count))

if __name__ == '__main__':
    main()
