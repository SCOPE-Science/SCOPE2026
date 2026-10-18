"""Numerical consistency checks for the odd-polygon edge-foot reconstruction theorem.
Not a replacement for the analytical proof.
"""
import math
import random


def geometry(phi, rad):
    n=len(phi)
    hs=[]; alphas=[]; betas=[]
    for i in range(n):
        j=(i+1)%n
        px,py=rad[i]*math.cos(phi[i]),rad[i]*math.sin(phi[i])
        qx,qy=rad[j]*math.cos(phi[j]),rad[j]*math.sin(phi[j])
        dx,dy=qx-px,qy-py
        t=-(px*dx+py*dy)/(dx*dx+dy*dy)
        assert 0<t<1, 'perpendicular projection did not land inside side'
        h=abs(px*qy-py*qx)/math.hypot(dx,dy)
        hs.append(h)
        a=math.acos(h/rad[i])
        b=math.acos(h/rad[j])
        alphas.append(a); betas.append(b)
        gap=(phi[j]-phi[i])%(2*math.pi)
        assert abs(a+b-gap)<2e-12, (a,b,gap)
    return hs,alphas,betas


def determinant_from_positive_factors(h, r):
    n=len(h)
    a=[];b=[]
    for i in range(n):
        j=(i+1)%n
        a.append(h[i]/math.sqrt(r[i]**2-h[i]**2))
        b.append(h[i]/math.sqrt(r[j]**2-h[i]**2))
    diag=math.prod(a)
    cyclic=math.prod(b)
    return diag+(-1)**(n-1)*cyclic


def main():
    rng=random.Random(20261013)
    odd_count=0
    for n in (3,5,7,9,11):
        for _ in range(500):
            phi=[2*math.pi*i/n for i in range(n)]
            r=[1+rng.uniform(-0.04,0.04) for i in range(n)]
            h,a,b=geometry(phi,r)
            determinant=determinant_from_positive_factors(h,r)
            assert determinant>0
            odd_count+=1
    # A concrete triangle with unequal support distances and strictly internal feet.
    points=[(2,0),(-1,2),(-1,-1)]
    phi=[math.atan2(y,x)%(2*math.pi) for x,y in points]
    r=[math.hypot(x,y) for x,y in points]
    h,_,_=geometry(phi,r)
    expected=(4/math.sqrt(13),1,2/math.sqrt(10))
    assert all(abs(h[i]-expected[i])<1e-12 for i in range(3))
    assert determinant_from_positive_factors(h,r)>0
    # Even parity: continuum of four-ray and four-distance matches.
    ray=[math.pi/4+i*math.pi/2 for i in range(4)]
    signatures=[]
    for t in (0.22,0.48,0.88,1.21):
        r=[1/math.cos(t) if i%2==0 else 1/math.sin(t) for i in range(4)]
        hs,_,_=geometry(ray,r)
        assert max(abs(x-1) for x in hs)<1e-12
        assert abs(determinant_from_positive_factors(hs,r))<1e-10
        signatures.append((r[0],r[1]))
    assert all(signatures[i]!=signatures[j] for i in range(4) for j in range(i+1,4))
    print('PASS: odd strict-foot angle and determinant tests:',odd_count)
    print('PASS: unequal-distance integer-coordinate triangle and even 4-ray family')


if __name__=='__main__':
    main()
