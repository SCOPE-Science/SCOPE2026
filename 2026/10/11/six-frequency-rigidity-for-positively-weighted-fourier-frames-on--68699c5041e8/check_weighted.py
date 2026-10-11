#!/usr/bin/env python3
"""Independent direct finite-grid checks of weighted three-site Fourier tightness.
Requires Python's standard library only. Finite checks do not prove all primes.
"""
import math,itertools,cmath


def strict_center_weights(p, tri):
    # Determine barycentric coordinates by cross products, independently
    # of the cyclic-gap formula used in the theorem.
    z=[cmath.exp(2j*math.pi*t/p) for t in tri]
    a=z[1]-z[0]; b=z[2]-z[0]
    det=a.real*b.imag-a.imag*b.real
    if abs(det)<1e-11: raise AssertionError('collinear sampled roots')
    u=(-z[0].real*b.imag+z[0].imag*b.real)/det
    v=(a.real*(-z[0].imag)-a.imag*(-z[0].real))/det
    return (1-u-v,u,v)


def check(p):
    from math import comb
    k=(p-1)//2
    triangles=[]
    for tri in itertools.combinations(range(p),3):
        gaps=(tri[1]-tri[0], tri[2]-tri[1],p+tri[0]-tri[2])
        geo=all(g<=k for g in gaps)
        ws=strict_center_weights(p,tri)
        pos=all(x>1e-10 for x in ws)
        assert geo==pos,(p,tri,gaps,ws)
        if pos:
            assert abs(sum(ws)-1)<1e-10
            assert abs(sum(ws[j]*cmath.exp(2j*math.pi*tri[j]/p) for j in range(3)))<1e-10
            triangles.append((tri,ws))
    want=p*(p*p-1)//24
    assert len(triangles)==want,(p,len(triangles),want)
    root=lambda j:cmath.exp(2j*math.pi*j/(2*p))
    tests=0
    for ev,evw in triangles:
        for od,odw in triangles:
            # Even frequencies 2k; odd frequencies 2k+1, with independent weights.
            lam=[2*t for t in ev]+[2*t+1 for t in od]
            w=[v/2 for v in evw]+[v/2 for v in odw]
            assert len(set(lam))==6 and all(x>0 for x in w)
            S=(0,p,1)
            for i in range(3):
                for j in range(3):
                    v=sum(w[u]*root(lam[u])**(S[i]-S[j]) for u in range(6))
                    assert abs(v-(1 if i==j else 0))<2e-10,(p,ev,od,i,j,v)
            tests+=1
    print(f'p={p} triangles_each_parity={len(triangles)} optimal_masks={tests} Gram_checks={9*tests}')

if __name__=='__main__':
    for p in (3,5,7,11):check(p)
