#!/usr/bin/env python3
"""Independent numerical consistency checks for the two-tributary linear-reservoir theorem.

The exhaustive parameter theorem is proved analytically in RESULT.md;
finite evaluations here are corroborating calculations, not a substitute.
"""
import math
from fractions import Fraction

COUNT = 0

def require(ok, why="assertion"):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(why)

def close(a, b, atol=1e-11, rtol=1e-11):
    require(abs(a-b) <= atol + rtol*max(abs(a),abs(b)), (a,b))

def mode(r):
    require(r > 0)
    if abs(r-1) < 1e-12:
        return 1.
    return math.log(r)/(r-1.)

def routed(x,r):
    if x < 0:
        return 0.
    if abs(r-1) < 1e-12:
        return x*math.exp(-x)
    # stable evaluation near r=1
    return r*math.exp(-x)*(-math.expm1(-(r-1.)*x))/(r-1.)

def slope(x,r):
    if abs(r-1) < 1e-12:
        return (1.-x)*math.exp(-x)
    return r/(r-1.)*(-math.exp(-x)+r*math.exp(-r*x))

def peak(beta,r,d):
    require(beta>=1 and r>0 and d>=0)
    t=d
    if slope(d,r) > beta:
        # This branch necessarily has r>beta>=1, so denominator >0.
        t=math.log(r*r/(r+(r-1)*beta*math.exp(d)))/(r-1)
        require(t>d)
        close(slope(t,r),beta*math.exp(d-t),atol=2e-10)
    return routed(t,r)+beta*math.exp(d-t),t

def unmodified(beta,d):
    return beta+math.exp(-d)

def max_harm_formula(r):
    m=mode(r)
    return (math.exp(-2) if r==1 else math.exp(-2*m)/r)

# Hand-checkable exact rational tests of the convolution and maximal penalty.
q=Fraction
require(2*(q(1,2)-q(1,4)) == q(1,2), 'r=2 threshold')
require(2*(q(1,4)-q(1,16)) - q(1,4) == q(1,8), 'r=2 maximal harm')
require((q(1,4)-q(1,16)) + q(1,4) - q(1,16) == q(3,8), 'r=1/2 convolution')
require((q(1,4)-q(1,16)) - q(1,16) == q(1,8), 'r=1/2 maximal harm')
require(q(3,8)-q(1,4)==q(1,8))

rs=(0.03,0.1,0.2,0.5,0.9,1.,1.1,2.,3.,5.,10.,50.,100.)
betas=(1.,1.01,1.5,2.,4.,12.)
for r in rs:
    m=mode(r)
    require(m>0)
    close(routed(m,r),math.exp(-m),atol=2e-12)
    close(slope(m,r),0.,atol=2e-12)
    for beta in betas:
        for scale in (0.,0.01,0.1,0.4,0.75,0.99,1.,1.01,1.2,1.5,2.,3.,5.,10.):
            d=m*scale
            p,t=peak(beta,r,d)
            base=unmodified(beta,d)
            require(p>=beta,'post-arrival maximum')
            require(t>=d,'peak time')
            if scale<1.:
                require(p < base-1e-13 or abs(p-base)<1e-13, 'wrong safe side')
            elif scale==1.:
                close(p,base,atol=5e-11)
            else:
                require(p>base,'wrong harmful side')
                close(p-base,routed(d,r)-math.exp(-d),atol=5e-11)
                close(t,d,atol=1e-11)
            # independent dense finite grid; cannot prove continuous maximum
            candidates=[d+i*(max(10.,3*m))/(250.) for i in range(251)]
            for x in candidates:
                actual=routed(x,r)+beta*math.exp(d-x)
                require(actual <= p+1e-10, (r,beta,d,x,actual,p))
        dm=2*m
        p,t=peak(beta,r,dm)
        close(p-unmodified(beta,dm),max_harm_formula(r),atol=3e-11)
        close(t,dm)
        require(p-unmodified(beta,dm) <= math.exp(-2)+2e-12)
    # Global maximum of harmful excess occurs at twice the modal lag.
    for multiple in (1.,1.1,1.5,1.9,2.,2.1,3.,5.,8.):
        d=multiple*m
        excess=routed(d,r)-math.exp(-d)
        require(excess <= max_harm_formula(r)+3e-12)
close(max_harm_formula(1.),math.exp(-2))
close(max_harm_formula(2.),1/8)
close(max_harm_formula(.5),1/8)
close(max_harm_formula(3.),1/9)

# Piecewise special-case reference example, equal arrival pulse volumes.
close(unmodified(1.,2.),1+math.exp(-2))
close(peak(1.,1.,2.)[0],1+2*math.exp(-2))
print('VERIFY_OK assertions=',COUNT)
