"""Standalone numerical corroboration for the clipped-ball symmetric-core theorem.

Uses only Python's standard library. Finite tests do not replace the analytic proof.
"""
import math
import random


def simpson(fun, a, b, steps=500):
    if b <= a:
        return 0.0
    if steps % 2:
        steps += 1
    h = (b-a)/steps
    total = fun(a)+fun(b)
    for k in range(1,steps):
        total += (4 if k % 2 else 2)*fun(a+k*h)
    return total*h/3


def f(n, t):
    return max(0.0, 1-t*t)**((n-1)/2)


def center(n,a):
    q=2**(-2/(n-1))
    if a<=-math.sqrt(1-q):
        return 0.0
    return (2*a+math.sqrt(q*a*a+(4-q)*(1-q)))/(4-q)


def axial_score(n,a,s):
    w=min(s-a, 1-abs(s))
    if w<=0.0:
        return 0.0
    return simpson(lambda u:f(n,abs(s)+u),0.,w,400)


def planar_offset_score(a,s,z):
    lo=max(a,2*s-1.)
    hi=min(1.,2*s-a)
    if hi<=lo:
        return 0.0
    def slice_len(x):
        r1=math.sqrt(max(0.,1-x*x))
        r2=math.sqrt(max(0.,1-(2*s-x)**2))
        return max(0.,min(r1,2*z+r2)-max(-r1,2*z-r2))
    # Exact 2-D core area is the integral of this interval intersection length.
    return simpson(slice_len,lo,hi,1200)


def main():
    count=0
    for n in [2,3,4,5,7,10]:
        q=2**(-2/(n-1))
        t=-math.sqrt(1-q)
        for a in [-1., -.99, -.8, -.4, 0., .2, .65, .9, t-.0001,t,t+.0001]:
            s=center(n,a)
            assert max(0.,a)-1e-13<=s<=.5*(1+a)+1e-12
            if a>t:
                assert abs((4-q)*s*s-4*a*s+a*a+q-1)<1e-11
            optimum=axial_score(n,a,s)
            for k in range(251):
                x=a+(1-a)*k/250
                assert axial_score(n,a,x)<=optimum+2e-5,(n,a,s,x)
                count+=1
    rng=random.Random(329785)
    nonaxial=0
    for a in [-.9,-.6,-.2,0.,.3,.7]:
        predicted_area=4*axial_score(2,a,center(2,a))
        for _ in range(70):
            s=a+(1-a)*rng.random()
            z=(rng.random()-.5)*1.6
            area=planar_offset_score(a,s,z)
            assert area<=predicted_area+2e-5,(a,s,z,area,predicted_area)
            nonaxial+=1
    # In dimension 3 the exact hemisphere fraction simplifies to 2/sqrt(7).
    s=center(3,0.)
    assert abs(s-1/math.sqrt(7))<1e-14
    assert abs(3*s-7*s**3-2/math.sqrt(7))<1e-14
    print('VERIFY_OK',count,'axial tests,',nonaxial,'nonaxial 2-D tests')

if __name__=='__main__':
    main()
