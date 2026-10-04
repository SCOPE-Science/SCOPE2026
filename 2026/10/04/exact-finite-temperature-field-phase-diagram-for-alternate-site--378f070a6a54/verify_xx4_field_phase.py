#!/usr/bin/env python3
import math

SQ2=math.sqrt(2.0)

def terms(J,B,T):
    beta=1.0/T
    j=J*beta
    b=B*beta
    k=math.cosh(2*SQ2*j)
    u=0.5*(1+math.exp(2*j+2*b)+math.exp(-2*j+2*b)+k)+math.exp(2*b)+math.exp(4*b)
    v=0.5*(1+math.exp(-2*j-2*b)+math.exp(2*j-2*b)+k)+math.exp(-2*b)+math.exp(-4*b)
    y=0.5*(-1+math.cosh(2*j+2*b)+math.cosh(2*j-2*b)+k)-math.cosh(2*b)
    Z=4*(1+math.cosh(2*b))+2*(math.cosh(4*b)+math.cosh(2*j+2*b)+math.cosh(2*j-2*b)+k)
    C=2.0/Z*max(abs(y)-math.sqrt(u*v),0.0)
    return u,v,y,Z,C

def coeffs(x):
    a=math.cosh(2*x)
    k=math.cosh(2*SQ2*x)
    L=(a-1)**2-2*(k+1)
    Q=4*a+2*k+2
    R=(a+1)**2
    return L,Q,R

def stable_concurrence(J,B,T):
    u,v,y,Z,Cnaive=terms(J,B,T)
    F=fpoly(J,B,T)
    if F<=0:
        return 0.0
    return 2.0/Z * F/(abs(y)+math.sqrt(u*v))

def fpoly(J,B,T):
    x=abs(J)/T
    c=math.cosh(2*abs(B)/T)
    L,Q,R=coeffs(x)
    return L*c*c-Q*c-R

def xstar():
    lo,hi=0.0,3.0
    for _ in range(100):
        m=(lo+hi)/2
        g=math.sinh(m)**2-math.cosh(SQ2*m)
        if g>0: hi=m
        else: lo=m
    return (lo+hi)/2

XS=xstar()

def threshold(J,T):
    x=abs(J)/T
    L,Q,R=coeffs(x)
    if L<=0:
        return math.inf
    disc=Q*Q+4*L*R
    # stable positive root, both formulas agree but this avoids loss when L is small.
    c=(Q+math.sqrt(disc))/(2*L)
    return 0.5*T*math.acosh(c)

def phase_positive(J,B,T):
    if T >= abs(J)/XS:
        return False
    return abs(B)>threshold(J,T)

def main():
    identity_checks=0
    phase_checks=0
    tail_checks=0

    # Published formula -> exact quadratic phase discriminant.
    for J in (-1.0,-0.7,0.7,1.0):
        for T in (0.3,0.5,0.9,1.4):
            for B in (0.0,0.02,0.15,0.6,1.3,2.5):
                u,v,y,Z,C=terms(J,B,T)
                F=y*y-u*v
                G=fpoly(J,B,T)
                scale=max(1.0,abs(F),abs(G))
                assert abs(F-G) <= 3e-8*scale, (J,T,B,F,G)
                identity_checks+=1
                pred=phase_positive(J,B,T)
                assert (F>0)==pred, (J,T,B,F,pred)
                Cs=stable_concurrence(J,B,T)
                assert (Cs>0)==pred, (J,T,B,Cs,pred)
                phase_checks+=1

    # Unique universal temperature ceiling.
    assert abs(XS-1.4195389207530745)<2e-14
    tstar=1/XS
    assert abs(tstar-0.7044540909589810)<2e-14

    # Low-T threshold asymptotic.
    low_ratios=[]
    for x in (6.0,8.0,10.0):
        T=1/x
        B=threshold(1.0,T)
        asym=SQ2*T*math.exp(-(2-SQ2)*x)
        low_ratios.append(B/asym)
    assert abs(low_ratios[-1]-1)<abs(low_ratios[0]-1)
    assert abs(low_ratios[-1]-1)<8e-4

    # High-field tail coefficient.
    for J,T in ((1.0,0.5),(-1.0,0.3),(1.4,0.6)):
        x=abs(J)/T
        A=math.cosh(2*x)-1-2*math.cosh(SQ2*x)
        assert A>0
        ratios=[]
        for B in (3.0,4.0,5.0):
            C=stable_concurrence(J,B,T)
            asym=A*math.exp(-2*B/T)
            ratios.append(C/asym)
        assert abs(ratios[-1]-1)<abs(ratios[0]-1)
        assert abs(ratios[-1]-1)<2e-4
        tail_checks+=1

    # Explicit counterexamples to finite field cutoffs in the source plots.
    assert stable_concurrence(1.0,0.05,0.1) > 0.0
    assert stable_concurrence(1.0,2.0,0.5) > 0.0

    print("VERIFY_OK")
    print("quadratic_identity_checks =",identity_checks)
    print("phase_sign_checks =",phase_checks)
    print("low_T_threshold_ratio =",low_ratios[-1])
    print("high_field_tail_cases =",tail_checks)
    print("x_star =",format(XS,".16f"))
    print("T_star_over_absJ =",format(1/XS,".16f"))
    print("C_J1_T01_B005 =",format(stable_concurrence(1.0,0.05,0.1),".16e"))
    print("C_J1_T05_B2 =",format(stable_concurrence(1.0,2.0,0.5),".16e"))

if __name__=="__main__":
    main()
