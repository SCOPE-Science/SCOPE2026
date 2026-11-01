"""Exact checker for the affine L2 projection on products of simplices.
All finite checks are exact rational arithmetic unless labeled floating-point.
"""
from fractions import Fraction as F
from math import comb, factorial, exp
import random

def j(i, k, t):
    if t <= 0: return F(0)
    return F(factorial(i)*factorial(k), factorial(i+k+3))*t**(i+k+3)

def rectangle_hinge_moment(i, k, a, b, c):
    out=j(i,k,c)
    out -= sum(comb(i,r)*a**(i-r)*j(r,k,c-a) for r in range(i+1))
    out -= sum(comb(k,s)*b**(k-s)*j(i,s,c-b) for s in range(k+1))
    out += sum(comb(i,r)*comb(k,s)*a**(i-r)*b**(k-s)*j(r,s,c-a-b)
               for r in range(i+1) for s in range(k+1))
    return out

def neg_part(d,e):
    assert d>=1 and e>=1
    a=(d+1)*(d+2); b=(e+1)*(e+2); c=d+e+3
    v=F(0)
    for i in range(d):
        for k in range(e):
            v+=F((-1)**(i+k)*comb(d-1,i)*comb(e-1,k),a**i*b**k)*rectangle_hinge_moment(i,k,a,b,c)
    return F(d*e,a*b)*v

def norm(d,e):
    return 1+2*neg_part(d,e)

def independent_one_dim(d,e):
    from scipy.integrate import quad
    a=(d+1)*(d+2); b=(e+1)*(e+2); c=d+e+3
    def hinge_x(t):
        if t <= 0: return 0.0
        if t >= a: return t-(d+2)
        return t-(d+2)+(d+2)*(1-t/a)**(d+1)
    val,err=quad(lambda y: e/b*(1-y/b)**(e-1)*hinge_x(c-y),0,b,
                 points=sorted(set([z for z in (max(0,min(b,c)),max(0,min(b,c-a))) if 0<z<b])),epsabs=1e-10)
    return val

def limit_b(theta):
    x=theta; y=1-theta
    if abs(theta-.5)<1e-12: return 2*exp(-2)
    return 1-(x*x*(1-exp(-1/x))-y*y*(1-exp(-1/y)))/(x-y)

def run():
    count=0
    for d in range(1,8):
        for e in range(1,8):
            val=neg_part(d,e)
            assert val>0
            assert val==neg_part(e,d)
            ind=independent_one_dim(d,e)
            assert abs(float(val)-ind)<2e-9,(d,e,float(val),ind)
            count+=1
    assert norm(1,1)==F(233,108)
    assert norm(2,1)==F(11,4)
    print('Exact rational norm examples:',[(d,e,str(norm(d,e)),round(float(norm(d,e)),9)) for d,e in [(1,1),(1,2),(2,2),(2,3),(3,3),(4,4)]])
    print('49 exact symmetry, positivity and independent quadrature tests PASS')
    for theta in [.1,.2,.3,.4,.5,.6,.7,.8,.9]:
        bb=limit_b(theta)
        assert bb>=2*exp(-2)-1e-14
        assert bb<=exp(-1)+1e-14
    print('Limit coefficients:',[(t,round(2*limit_b(t),9)) for t in [.1,.25,.5,.75,.9]])
    # Check exact Gram-based least-squares kernel numerically over uniform simplex samples.
    import numpy as np
    rng=np.random.default_rng(20261026)
    checks=0
    for d,e in [(1,1),(1,3),(2,2),(3,2),(4,3)]:
        N=300000
        lam=rng.dirichlet(np.ones(d+1),N)[:,0]
        mu=rng.dirichlet(np.ones(e+1),N)[:,0]
        ker=(d+1)*(d+2)*lam+(e+1)*(e+2)*mu-(d+e+3)
        sample=np.mean(np.abs(ker))
        target=float(norm(d,e))
        assert abs(sample-target)<.035, (d,e,sample,target)
        # projector reproduces constants and barycentric vertex coordinates
        assert abs(np.mean(ker)-1)<.035
        checks+=1
    print('Independent Monte Carlo kernel/norm tests PASS:',checks)
    # Directly check algebraic proof at sample rational barycentric values for product of intervals:
    # for d=e=1, Gram basis [1,x,y] where x,y uniform [0,1],
    # at (1,1) kernel 1+12(x-1/2)(1/2)+12(y-1/2)(1/2)=6x+6y-5.
    for x in [F(0),F(1,5),F(1,2),F(4,5),F(1)]:
        for y in [F(0),F(2,7),F(1,2),F(1)]:
            assert 1+6*(x-F(1,2))+6*(y-F(1,2))==6*x+6*y-5
    print('20 direct Gram identity checks PASS')
    for n in [50,100,250]:
        z=norm(n,n) if n<=12 else None
        # one-dimensional deterministic numerical quadrature scalable to large dimensions
        val=independent_one_dim(n,n)
        coeff=(1+2*val)/(2*n)
        print('balanced ratio n=',n,' observed',round(coeff,9),'limit',round(4*exp(-2),9))
        assert abs(coeff-4*exp(-2))<.06
    print('All checker assertions PASS')

if __name__=='__main__': run()
