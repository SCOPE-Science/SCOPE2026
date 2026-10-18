#!/usr/bin/env python3
"""Independent midpoint Crofton integration by cut-edge enumeration.
Run: python3 checker.py. No third-party dependencies.
"""
import math

PI=math.pi
SQ3=math.sqrt(3)
EDGES=((0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4),(4,2))

def formulas(h):
    s=math.sqrt(1+h*h)
    A=math.atan(SQ3*h/s)
    I=SQ3/2*math.atan(1/(2*h))+s*A-PI*h/3
    K=-SQ3/2*math.atan(1/(2*h))+s*math.atan(s/(SQ3*h))-PI*h/6
    D=PI*h+3*I
    C=3*SQ3*PI/4
    return ((D-C)/D,3*(I-K)/D,3*(C/3-I)/D,3*K/D)

def enumeration(h,nphi=720,nz=320):
    sums=[0.0]*4
    total=0.0
    # Uniform spherical integration: azimuth phi uniform, z=cos(theta) uniform.
    for j in range(nphi):
        phi=2*PI*(j+0.5)/nphi
        cc=(math.cos(phi),math.cos(phi-2*PI/3),math.cos(phi-4*PI/3))
        for k in range(nz):
            z=-1+(2*k+1)/nz
            rr=math.sqrt(1-z*z)
            v=(-h*z,h*z,rr*cc[0],rr*cc[1],rr*cc[2])
            order=sorted(range(5), key=v.__getitem__)
            last=v[order[0]]
            total+=v[order[-1]]-last
            below=0
            for rank in range(4):
                below|=1<<order[rank]
                new=v[order[rank+1]]
                crossings=0
                for a,b in EDGES:
                    crossings+=bool(below&(1<<a))!=bool(below&(1<<b))
                assert 3<=crossings<=6
                sums[crossings-3]+=new-last
                last=new
    return tuple(x/total for x in sums)

def run():
    checks=0
    for h in (0.2,0.65,1.0,1.211448,2.5,6.0):
        a=formulas(h)
        b=enumeration(h,360,180)
        errors=[abs(x-y) for x,y in zip(a,b)]
        assert max(errors)<0.0008,(h,a,b,errors)
        assert abs(sum(a)-1)<1e-12
        assert all(0<x<1 for x in a)
        checks+=4
    # Monotonicity and unique maximum are proved in the paper; this is diagnostic.
    hstar=1.2114481799
    for delta in (0.001,0.1,0.3):
        assert formulas(hstar)[2]>formulas(hstar-delta)[2]
        assert formulas(hstar)[2]>formulas(hstar+delta)[2]
        checks+=2
    print('BIPYRAMID_CROFTON_CHECK_OK comparison_items=%d samples_per_shape=%d' %(checks,360*180))
if __name__=='__main__':run()
