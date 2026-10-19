#!/usr/bin/env python3
"""Independent arithmetic checks of the three-state entropy/oscillation frontier.
Only Python's standard library is needed; finite tests supplement an analytic proof.
"""
from fractions import Fraction as F
from math import sqrt,log,isclose
from random import Random

def generator(a,b,c,k):
    # row-generator, cyclic positive-flow orientation: 1->2, 2->3, 3->1.
    return [[-a-c, a+k, c-k], [a-k,-a-b,b+k], [c+k,b-k,-b-c]]

def det(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
       -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
       +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def leading2(m):
    return sum(m[i][i]*m[j][j]-m[i][j]*m[j][i] for i,j in ((0,1),(0,2),(1,2)))

def physical(a,b,c,k):
    assert min(a,b,c)>abs(k)
    return (2*abs(k)/3)*sum(log((z+abs(k))/(z-abs(k))) for z in (a,b,c)) if k else 0.

def expected(a,b,c,k):
    s=a+b+c
    delta=a*a+b*b+c*c-a*b-b*c-c*a
    v=3*k*k-delta
    assert v>0
    w=sqrt(v)
    assert s>sqrt(3)*w
    floor=2*w/sqrt(3)*log((s+sqrt(3)*w)/(s-sqrt(3)*w))
    return w,floor

def main():
    count=0
    # Exact characteristic polynomial and invariant stationary distribution.
    for aa in range(2,9):
      for bb in range(2,9):
       for cc in range(2,9):
        for kk in range(-1,2):
         a,b,c,k=F(aa,5),F(bb,5),F(cc,5),F(kk,5)
         m=generator(a,b,c,k)
         assert all(sum(row)==0 for row in m)
         assert all(sum(m[i][j] for i in range(3))==0 for j in range(3))
         assert det(m)==0
         S=a+b+c
         delta=a*a+b*b+c*c-a*b-b*c-c*a
         assert sum(m[i][i] for i in range(3))==-2*S
         assert leading2(m)==S*S-delta+3*k*k
         count+=1
    rng=Random(1707)
    comparison=0
    # Nonhomogeneous, strictly oscillatory examples with systematic random rates.
    for _ in range(20000):
        S=rng.uniform(0.02,5.0)
        a,b,c=(S/3)*(1+rng.uniform(-0.27,0.27)) ,0,0
        b=(S-a)*rng.uniform(0.45,0.55)
        c=S-a-b
        k=rng.uniform(0.01,0.98)*min(a,b,c)
        delta=a*a+b*b+c*c-a*b-b*c-c*a
        if 3*k*k<=delta:continue
        w,floor=expected(a,b,c,k)
        sigma=physical(a,b,c,k)
        assert sigma>=floor-1e-12*max(1.,sigma)
        assert sigma>floor+1e-10*max(1.,sigma)
        assert isclose(w*w,3*k*k-delta,rel_tol=1e-12)
        comparison+=1
    assert comparison>1000
    # Exact attainability for arbitrary positive S and 0<omega<S/sqrt(3).
    for j in range(1,400):
        S=.02+j*.005
        w=S/sqrt(3)*(j+1)/402
        k=w/sqrt(3)
        a=b=c=S/3
        ww,floor=expected(a,b,c,k)
        assert isclose(w,ww,rel_tol=3e-11,abs_tol=2e-8)
        assert isclose(physical(a,b,c,k),floor,rel_tol=3e-8,abs_tol=3e-8)
        count+=1
    # At every fixed oscillatory spectral pair, vary the edge heterogeneity
    # without changing either eigenvalue or the uniform stationary activity.
    fiber_cases = 0
    for S in (0.7, 1.0, 3.0, 11.0):
      for fraction in (0.05, 0.2, 0.45, 0.8, 0.97):
        omega = fraction * S / sqrt(3)
        A = S/3
        ucrit = (sqrt(3*A*A - 2*omega*omega/3)-A)/2
        assert 0<ucrit<A
        previous = physical(A,A,A,omega/sqrt(3))
        for j in range(1,500):
            u=ucrit*j/500
            a,b,c=A+2*u,A-u,A-u
            k=sqrt(omega*omega/3+3*u*u)
            assert k<b
            w,floor=expected(a,b,c,k)
            assert isclose(w,omega,rel_tol=1e-10,abs_tol=1e-8)
            assert isclose(a+b+c,S,rel_tol=1e-12)
            ep=physical(a,b,c,k)
            assert ep>previous
            previous=ep
            assert ep>floor-1e-8
            fiber_cases+=1
        # At a sequence arbitrarily close to the finite boundary,
        # entropy grows without limit; this is illustration, not proof.
        u=ucrit*(1-1e-11)
        a,b,c=A+2*u,A-u,A-u
        k=sqrt(omega*omega/3+3*u*u)
        assert physical(a,b,c,k)> previous
    print('PASS fixed-complex-spectrum fiber comparisons:',fiber_cases)
    print('PASS exact generator/characteristic checks:',7**3*3)
    print('PASS heterogeneous oscillatory comparisons:',comparison)
    print('PASS exact saturating cycle parameter grid:',399)
    print('PASS total independent test groups:',count+comparison+fiber_cases)
if __name__=='__main__':main()
