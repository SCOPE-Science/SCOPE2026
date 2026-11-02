"""Finite independent numerical checks for symmetric opposite-pole Cauchy Gabor windows.
Run: python3 checker.py. Standard library only. Tests are supplementary, not a proof.
"""
import cmath
import math
import random


def zak(a, c, x, omega):
    z1 = x - 1j*a
    z2 = x + 1j*a
    return math.pi*(cmath.exp(1j*math.pi*z1*(1-2*omega))/cmath.sin(math.pi*z1)
                    +c*cmath.exp(1j*math.pi*z2*(1-2*omega))/cmath.sin(math.pi*z2))


def rational_intensity(a, c, t, y):
    p=math.pi*a
    H=math.sinh(p)
    J=math.cosh(p)
    return math.pi**2*(t*J*J*(y+c/y)**2+(1-t)*H*H*(y-c/y)**2)/(H*H+t)**2


def sharp_lower(a, c):
    p=math.pi*a
    H=math.sinh(p)
    J=math.cosh(p)
    if math.exp(-2*p)<=c<=math.exp(2*p):
        return 0.0
    if c<math.exp(-2*p):
        return math.pi**2*math.exp(-2*p)*min((1-c*math.exp(2*p))**2/H**2,
                                           (1+c*math.exp(2*p))**2/J**2)
    return math.pi**2*math.exp(2*p)*min((c*math.exp(-2*p)-1)**2/H**2,
                                      (c*math.exp(-2*p)+1)**2/J**2)


def check():
    rng=random.Random(260826)
    tests=0
    for a in [0.075,0.2,0.5,1.0]:
        p=math.pi*a
        cs=[math.exp(k*p) for k in [-6,-4,-3,-2,-1,0,1,2,3,4,6]]
        for c in cs:
            true_min=sharp_lower(a,c)
            for _ in range(150):
                x=rng.random();w=rng.random()
                y=math.exp(p*(1-2*w))
                direct=abs(zak(a,c,x,w))**2
                algebra=rational_intensity(a,c,math.sin(math.pi*x)**2,y)
                assert abs(direct-algebra)<=2e-9*(1+max(direct,algebra))
                assert direct>=true_min-2e-9*(1+true_min)
                tests+=2
            # Construct the endpoint or zero exactly, independently from the sampled grid.
            if true_min>0:
                y=math.exp(-p) if c<math.exp(-2*p) else math.exp(p)
                recovered=min(rational_intensity(a,c,t,y) for t in [0.,1.])
                assert abs(recovered-true_min)<2e-9*(1+true_min)
            else:
                recovered=rational_intensity(a,c,0.,math.sqrt(c))
                assert abs(recovered)<2e-9*(1+c*c)
            tests+=1
            # Reciprocity from exact reflection of the window.
            reciprocal=sharp_lower(a,1/c)*c*c
            assert abs(reciprocal-true_min)<2e-9*(1+max(true_min,reciprocal))
            tests+=1
        # Check the optimized energy-normalized bound and the two extremizers.
        best=2*math.pi*a/math.cosh(4*p)
        for c in [math.exp(-4*p),math.exp(4*p)]:
            normalized=sharp_lower(a,c)/(math.pi/a*(1+c*c))
            assert abs(normalized-best)<2e-10*(1+best)
            tests+=1
        for _ in range(300):
            c=math.exp(rng.uniform(-12*p,12*p))
            normalized=sharp_lower(a,c)/(math.pi/a*(1+c*c))
            assert normalized<=best+2e-10*(1+best)
            tests+=1
    # Conditional Fourier series compared with the explicit csc identity.
    for sign in [-1,1]:
        a=.27;x=.231;w=.381;z=x+1j*sign*a
        closed=math.pi*cmath.exp(1j*math.pi*z*(1-2*w))/cmath.sin(math.pi*z)
        N=6000
        sums=sum(cmath.exp(2j*math.pi*n*w)/(n+z) for n in range(-N,N+1))
        assert abs(sums-closed)<.0002
        tests+=1
    # For arbitrary complex coefficients, the constructed phase cancels the two poles.
    for a in [0.12,0.38]:
        p=math.pi*a
        for x in [0.08,0.29,0.5,0.73,0.93]:
            y=math.exp(.31*p)
            sp=cmath.sin(math.pi*(x+1j*a))
            sm=sp.conjugate()
            c=-y*y*sp/sm
            omega=(1-math.log(y)/p)/2
            assert abs(zak(a,c,x,omega))<1e-10*(1+abs(c))
            tests+=1
    print(f'PASS {tests} supplementary checks; finite checks do not prove the theorem')

if __name__=='__main__':
    check()
