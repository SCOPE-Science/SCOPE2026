"""Finite diagnostics for the degree-two Hardy/Bergman restriction constant.

The accompanying analytical proof establishes the infinite parameter claim.
"""
import cmath
import math
import random

PI = math.pi

def tau_root():
    lo, hi = 0.0, PI/2.0
    for _ in range(110):
        m = (lo+hi)/2
        if math.cos(m)>m:
            lo=m
        else:
            hi=m
    return (lo+hi)/2

def poly_norm(coeff, count=16384):
    total = 0.0
    for k in range(count):
        z=cmath.exp(2j*PI*k/count)
        total+=abs(coeff[0]+z*(coeff[1]+z*coeff[2]))
    return total/count

def h_to_a_ratio(coeff, count=16384):
    return abs(sum(coeff))/(2*poly_norm(coeff,count))

def explicit_norm(a):
    assert 0<=a<=2
    return (2/PI)*(math.sqrt(max(0.0,4-a*a))+a*math.asin(a/2))

def test():
    assertions=0
    tau=tau_root()
    a=2*math.sin(tau)
    sharp=PI/(4*tau)
    assert abs(math.cos(tau)-tau)<1e-14; assertions+=1
    assert 1.062<sharp<1.064; assertions+=1
    assert sharp>PI/3; assertions+=1
    assert abs(h_to_a_ratio((1,a,1))-sharp)<1e-7; assertions+=1
    for k in range(101):
        x=2*k/100
        assert abs(poly_norm((1,x,1),32768)-explicit_norm(x)) < 1e-7; assertions+=1
        assert (x+2)/(2*explicit_norm(x))<=sharp+1e-10; assertions+=1
    rng=random.Random(763901)
    for k in range(190):
        coeff=[complex(rng.uniform(-2,2),rng.uniform(-2,2)) for _ in range(3)]
        if abs(sum(coeff))<1e-12:
            continue
        rr=h_to_a_ratio(coeff,32768)
        assert rr<=sharp+1e-8,(coeff,rr,sharp);assertions+=1
        norm_poly=poly_norm(coeff,32768)
        normalized=[v/sum(coeff) for v in coeff]
        u=(normalized[0].real+normalized[2].real)/2
        sym=(u,1-2*u,u)
        symnorm=poly_norm(sym,32768)
        assert symnorm<=norm_poly/abs(sum(coeff))+1e-7,(coeff,symnorm,norm_poly); assertions+=1
    # Test the all-p scalar envelope and its near-Hilbert slope.
    values=[1.0,1.2,1.5,1.8,2.0,2.3,3.0]
    angles=[2*PI*k/4096 for k in range(4096)]
    xx=[1-math.cos(t) for t in angles]
    for p in values:
        def obj(lam):
            return sum(abs(1-lam*x)**p for x in xx)/len(xx)
        lo,hi=.5,1.0
        for _ in range(46):
            x1=lo+(hi-lo)/3; x2=hi-(hi-lo)/3
            if obj(x1)<obj(x2): hi=x2
            else: lo=x1
        lam=(lo+hi)/2
        opt=(1+p)**(-1/p)/obj(lam)**(1/p)
        assert .5<lam<1;assertions+=1
        for j in range(35):
            testlam=.5+j/70
            assert obj(lam)<=obj(testlam)+2e-8;assertions+=1
        assert opt>0;assertions+=1
        if p==2:
            assert abs(lam-2/3)<1e-7 and abs(opt-1)<1e-7;assertions+=1
    slope=7/12-math.log(3)/2
    assert .03402<slope<.03404; assertions+=1
    # For the first homogeneous degree, the endpoint sharp ratio is pi/3.
    assert abs((2.0/3.0)*2/poly_norm((1,1,0))-PI/3)<1e-7; assertions+=1
    print('CHECKS_PASSED',assertions)
    print('TAU',format(tau,'.16f'))
    print('OPTIMAL_MIDDLE_COEFFICIENT',format(a,'.16f'))
    print('SHARP_QUADRATIC_CONSTANT',format(sharp,'.15f'))
    print('LINEAR_WITNESS_CONSTANT',format(PI/3,'.15f'))

if __name__=='__main__':
    test()
