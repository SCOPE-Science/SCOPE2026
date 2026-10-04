#!/usr/bin/env python3
import math

def coeffs(x):
    t=math.exp(-x)
    f=x**3+6*x**2+7*x+1
    g=x*(x+1)**2
    AL=(x+1)*t*(1-t)
    BL=1-(x+1)*t
    AN=f*t*(1-t)
    BN=f*(1-t)-g
    return t,f,g,AL,BL,AN,BN

def root(A,B,C):
    lo=0.0
    hi=max(1.0,C/B+1.0)
    while A*hi**3+B*hi-C<0:
        hi*=2
    for _ in range(120):
        mid=(lo+hi)/2
        if A*mid**3+B*mid-C<0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

def gamma2(x,d):
    t=math.exp(-x)
    return 1.0/(d*(1-t)*(1+d*t))

def bL2(x,d):
    return (1+1/x)/(d+math.sqrt(d))

def bN2(x,d):
    f=x**3+6*x**2+7*x+1
    g=x*(x+1)**2
    return (f/g)/(d+math.sqrt(d))

def main():
    equivalence_checks=0
    coefficient_checks=0

    for j in range(1,81):
        x=1.0+j*0.5
        t,f,g,AL,BL,AN,BN=coeffs(x)
        assert AL>0 and BL>0 and AN>0 and BN>0
        coefficient_checks+=1
        RL=root(AL,BL,x)
        RN=root(AN,BN,g)
        for d in range(2,121):
            lhsL=bL2(x,d)<=gamma2(x,d)
            rhsL=math.sqrt(d)<=RL+2e-12
            lhsN=bN2(x,d)<=gamma2(x,d)
            rhsN=math.sqrt(d)<=RN+2e-12
            assert lhsL==rhsL
            assert lhsN==rhsN
            equivalence_checks+=2

    # Exact integer brackets at |alpha|=4, x=16.
    x=16.0
    t,f,g,AL,BL,AN,BN=coeffs(x)
    def PL(s): return AL*s**3+BL*s-x
    def PN(s): return AN*s**3+BN*s-g
    assert PL(math.sqrt(255))<0<PL(math.sqrt(256))
    assert PN(math.sqrt(17))<0<PN(math.sqrt(18))

    # Large-amplitude ratio of continuous capacities approaches 16.
    ratios=[]
    for x in (25.0,36.0,49.0,64.0,100.0):
        t,f,g,AL,BL,AN,BN=coeffs(x)
        RL=root(AL,BL,x)
        RN=root(AN,BN,g)
        ratios.append((RL*RL)/(RN*RN))
    assert ratios[-1]>15.8
    assert abs(ratios[-1]-16)<abs(ratios[0]-16)

    print("VERIFY_OK")
    print("coefficient_checks =",coefficient_checks)
    print("feasibility_equivalence_checks =",equivalence_checks)
    print("alpha_4_linear_capacity = 255")
    print("alpha_4_nonlinear_capacity = 17")
    print("large_x_capacity_ratio =",ratios[-1])

if __name__=="__main__":
    main()
