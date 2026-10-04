#!/usr/bin/env python3
import math

def yfun(m,R,z):
    k=math.sqrt(max(0.0,m*m-z*z))
    if k < 1e-12:
        return 4.0*math.pi*R**3
    return 2.0*math.pi*R*R*(-math.expm1(-2.0*k*R))/k

def fpos(m,R,z):
    return yfun(m,R,z)*(m-z)

def root_energy(m,R,lam):
    lo=-m
    hi=m
    for _ in range(160):
        mid=(lo+hi)/2.0
        if lam*fpos(m,R,mid) > 1.0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

def main():
    m=1.7
    R=0.8
    lc=1.0/(8.0*math.pi*m*R**3)
    l0=1.0/(2.0*math.pi*R**2*(1.0-math.exp(-2.0*m*R)))
    assert lc > 0.0 and l0 > lc
    e1=root_energy(m,R,2.0*lc)
    assert -m < e1 < m
    assert abs((2.0*lc)*fpos(m,R,e1)-1.0) < 5e-13
    ez=root_energy(m,R,l0)
    assert abs(ez) < 2e-12
    # Corroborate the threshold quadratic constant using decreasing epsilons.
    cthr=32.0*math.pi**2*m*R**4
    ratios=[]
    for rel in (2e-3,1e-3,5e-4):
        eps=lc*rel
        e=root_energy(m,R,lc+eps)
        ratios.append((e+m)/(eps*eps*cthr))
    assert abs(ratios[-1]-1.0) < abs(ratios[0]-1.0)
    assert abs(ratios[-1]-1.0) < 0.08
    # Corroborate the strong-coupling constant.
    ratios2=[]
    for mult in (1e3,3e3,1e4):
        lam=lc*mult
        e=root_energy(m,R,lam)
        ratios2.append((m-e)*4.0*math.pi*R**3*lam)
    assert abs(ratios2[-1]-1.0) < abs(ratios2[0]-1.0)
    assert abs(ratios2[-1]-1.0) < 0.03
    print("VERIFY_OK lc=%.15g lambda0=%.15g E_2lc=%.15g threshold_ratio=%.9f strong_ratio=%.9f" %
          (lc,l0,e1,ratios[-1],ratios2[-1]))

if __name__ == '__main__':
    main()
