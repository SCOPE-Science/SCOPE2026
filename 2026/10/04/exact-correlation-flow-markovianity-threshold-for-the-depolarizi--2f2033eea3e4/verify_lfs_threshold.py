#!/usr/bin/env python3
import math

LN2=math.log(2.0)

def threshold(z):
    return (1.0-z*z)/math.sqrt(3.0*(1.0+2.0*z*z))

def ratio(q,r):
    # Stable form of I_r/(q I_q), 0<q<1, 0<=r<=1.
    x=2.0*q*(1.0+r)/(1.0-q)
    y=2.0*q*(1.0-r)/(1.0-q)
    D=(1.0+2.0*r)*math.log1p(x)+(1.0-2.0*r)*math.log1p(y)
    s=2.0*q*r/(1.0+q)
    L=math.log1p(s)-math.log1p(-s) if s<1.0 else float('inf')
    return 2.0*L/D if D>0.0 else 0.0

def geometric(z,y):
    k=1.0-z*z
    return 2.0*k*math.sqrt(y*(1.0-y))/(3.0-2.0*k*y)

def derivatives(u,gamma,z):
    q=math.exp(-gamma*u)
    r=math.sqrt(math.cos(u)**2+z*z*math.sin(u)**2)
    if q==0.0:
        return 0.0
    # Stable I_q and I_r.
    if q>=1.0:
        q=1.0-1e-15
    x=2.0*q*(1.0+r)/(1.0-q)
    y=2.0*q*(1.0-r)/(1.0-q)
    D=(1.0+2.0*r)*math.log1p(x)+(1.0-2.0*r)*math.log1p(y)
    Iq=D/(4.0*LN2)
    s=2.0*q*r/(1.0+q)
    L=math.log1p(s)-math.log1p(-s)
    Ir=q*L/(2.0*LN2)
    k=1.0-z*z
    rp=0.0 if r==0.0 else -k*math.sin(u)*math.cos(u)/r
    return -gamma*q*Iq+rp*Ir

def main():
    ratio_checks=0
    for iq in range(1,100):
        q=iq/100.0
        for ir in range(101):
            r=ir/100.0
            lhs=ratio(q,r)
            rhs=2.0*r/(1.0+2.0*r*r)
            assert lhs <= rhs+2e-12
            ratio_checks+=1

    geom_checks=0
    for iz in range(101):
        z=iz/100.0
        ystar=3.0/(2.0*(2.0+z*z))
        exact=threshold(z)
        assert abs(geometric(z,ystar)-exact)<3e-13
        for iy in range(1001):
            y=iy/1000.0
            assert geometric(z,y)<=exact+3e-13
            geom_checks+=1

    assert abs(threshold(0.0)-1.0/math.sqrt(3.0))<1e-15
    assert threshold(1.0)==0.0

    hierarchy_checks=0
    for iz in range(1,101):
        z=iz/100.0
        lfs=threshold(z)
        lpp=(1.0-z*z)/(3.0*z)
        assert lfs<=lpp+2e-14
        hierarchy_checks+=1

    # Above the boundary: direct rate sampling cannot find a positive interval.
    time_checks=0
    for z in (0.0,0.2,0.5,0.8,0.95):
        g=1.01*threshold(z)
        for j in range(1,20001):
            u=j*0.01
            x=derivatives(u,g,z)
            assert x <= 2e-12
            time_checks+=1

    # Below the boundary: repeated maximizing phases eventually give positivity.
    positive_witnesses=0
    for z in (0.0,0.2,0.5,0.8,0.95):
        star=threshold(z)
        g=0.90*star
        ystar=3.0/(2.0*(2.0+z*z))
        theta=math.asin(math.sqrt(ystar))
        found=False
        for n in range(80):
            u=math.pi-theta+2.0*math.pi*n
            if derivatives(u,g,z)>1e-16:
                found=True
                break
        assert found
        positive_witnesses+=1

    print('VERIFY_OK')
    print('ratio_bound_checks =',ratio_checks)
    print('geometric_max_checks =',geom_checks)
    print('hierarchy_checks =',hierarchy_checks)
    print('above_threshold_time_checks =',time_checks)
    print('below_threshold_positive_witnesses =',positive_witnesses)
    print('universal_threshold =',threshold(0.0))

if __name__=='__main__':
    main()
