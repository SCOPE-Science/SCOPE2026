#!/usr/bin/env python3
"""Independent numerical checks for the triaxial central-section radius formula."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipe


def exact_cdf(a, b, c, r):
    if not (a > b > c > 0):
        raise ValueError('Require strictly ordered positive semiaxes')
    if r <= b:
        return 0.0
    if r >= a:
        return 1.0
    alpha, beta, gamma, t = a**-2, b**-2, c**-2, r**-2
    A, B, C = t-alpha, beta-t, gamma-t
    def integ(phi):
        q = A*(math.cos(phi)**2/B + math.sin(phi)**2/C)
        return math.sqrt(q/(1+q))
    return 1.0-2/math.pi*quad(integ, 0, math.pi/2, epsabs=2e-13, epsrel=2e-13)[0]


def upper_constant(a,b,c):
    alpha, beta, gamma = a**-2,b**-2,c**-2
    m=1-(beta-alpha)/(gamma-alpha)
    return (2/math.pi)*math.sqrt(2/(a**3*(beta-alpha)))*ellipe(m)


def direct_section_radius(a,b,c,n):
    n=np.asarray(n,dtype=float)
    n=n/np.linalg.norm(n)
    # independent Householder/QR basis for the orthogonal complement
    seed=np.eye(3)[:,int(np.argmin(np.abs(n)))]
    e=seed-n*(n@seed)
    e=e/np.linalg.norm(e)
    f=np.cross(n,e)
    U=np.column_stack([e,f])
    D=np.diag([1/a**2,1/b**2,1/c**2])
    w=np.linalg.eigvalsh(U.T@D@U)
    return 1/math.sqrt(w[0])


def run_tests():
    count=0
    rng=np.random.default_rng(20261031)
    for a,b,c in [(3.,2.,1.),(7.,5.,2.),(1.4,1.1,0.6),(1.002,1.001,1.0)]:
        rs=np.linspace(b,a,101)
        vals=[exact_cdf(a,b,c,float(x)) for x in rs]
        assert vals[0]==0 and vals[-1]==1
        assert np.all(np.diff(vals)>0)
        count+=100
        # Independent geometry: CDF event exactly equals cone inequality.
        for n in rng.normal(size=(5000,3)):
            n=n/np.linalg.norm(n)
            r=direct_section_radius(a,b,c,n)
            for x in (b+(a-b)*0.2,b+(a-b)*0.5,b+(a-b)*0.8):
                t=x**-2
                A=t-a**-2
                B=b**-2-t
                C=c**-2-t
                cone=(n[0]**2 >= A*(n[1]**2/B+n[2]**2/C))
                assert bool(cone)==bool(r<=x) or abs(r-x)<1e-11, (a,b,c,r,x)
                count+=1
        # Haar Monte Carlo vs independent quadrature; sampling uncertainty accepted.
        normals=rng.normal(size=(16000,3))
        direct=np.array([direct_section_radius(a,b,c,n) for n in normals])
        for x in (b+0.25*(a-b), b+0.5*(a-b), b+0.75*(a-b)):
            p=exact_cdf(a,b,c,x)
            phat=float(np.mean(direct<=x))
            assert abs(phat-p)<0.035, (p,phat)
            count+=1
        coef=upper_constant(a,b,c)
        for h in [1e-4,1e-5]:
            if h<a-b:
                approx=(1-exact_cdf(a,b,c,a-h))/math.sqrt(h)
                assert abs(approx/coef-1)<0.03,(coef,approx)
                count+=1
        # Strict decrease in c for fixed a,b, at each interior r.
        c0,c1=c*0.75,c*1.05
        if c1<b:
            for x in [b+(a-b)*0.1,b+(a-b)*0.4,b+(a-b)*0.9]:
                assert exact_cdf(a,b,c0,x)>exact_cdf(a,b,c1,x)
                count+=1
    # axisymmetric limiting formula (known prior result): a>b=c.
    for a,b in [(3.,2.),(9.,1.5)]:
        for x in np.linspace(b+0.001*(a-b),a-0.001*(a-b),10):
            expected=1-math.sqrt((x**-2-a**-2)/(b**-2-a**-2))
            actual=exact_cdf(a,b,b*(1-1e-7),x)
            assert abs(expected-actual)<1e-6,(actual,expected)
            count+=1
    print('PASS:',count,'deterministic, exact-cone-vs-direct-eigenvalue, numerical-quadrature and Haar checks')
    print('reference F(2.5) for (3,2,1):', exact_cdf(3,2,1,2.5))
    print('reference upper-tail constant:',upper_constant(3,2,1))

if __name__=='__main__':
    run_tests()
