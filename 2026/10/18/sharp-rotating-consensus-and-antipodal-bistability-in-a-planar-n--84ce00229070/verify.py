"""Finite diagnostic tests for a normalized two-agent planar recurrence.

All infinite-time conclusions require the analytic argument in RESULT.md.
"""
import cmath
import math
import random


def angle_map(t, L, h):
    left = math.atan((h+t)/L)
    right = math.atan((h-t)/L)
    delta = 0.5*(left-right)
    omega = 0.5*(left+right)
    return math.tan(delta), omega


def direct_map(phi, delta, L, h):
    x = cmath.exp(1j*(phi+delta))
    y = cmath.exp(1j*(phi-delta))
    # The complex coefficient is a+i*b with 1+eta*a=L, eta*b=h.
    shared = ((L-1)+1j*h)*(x+y)/2
    u = x+shared
    v = y+shared
    xn,yn = u/abs(u),v/abs(v)
    return xn,yn


def wrapped_diff(a, b):
    return math.atan2(math.sin(a-b), math.cos(a-b))


def main():
    rng=random.Random(731405)
    checks=0
    for _ in range(10000):
        L=math.exp(rng.uniform(-2.0, 1.5))
        h=rng.uniform(-3,3)
        t=rng.uniform(-20,20)
        phi=rng.uniform(-math.pi,math.pi)
        delta=math.atan(t)
        tn,omega=angle_map(t,L,h)
        xn,yn=direct_map(phi,delta,L,h)
        xx=cmath.exp(1j*(phi+omega+math.atan(tn)))
        yy=cmath.exp(1j*(phi+omega-math.atan(tn)))
        assert abs(xn-xx)<3e-12 and abs(yn-yy)<3e-12
        checks+=1
        if abs(t)>1e-7:
            S=(L-(L*L+h*h))+(1-L)*t*t
            sign=(tn-t)*t
            if abs(S)>1e-8:
                assert (sign>0)==(S>0), (L,h,t,S,tn)
            checks+=1
    # Every proposed phase regime has its predicted direction of motion.
    for L,h in [(1.5,0.7),(1.0,0.5),(0.7,0.1),(0.7,math.sqrt(0.21)),(0.7,0.9)]:
        K=L*L+h*h
        star=math.sqrt((K-L)/(1-L)) if L<1 and K>L else None
        for t in [0.1,0.5,1,2,5,10,100]:
            tn,_=angle_map(t,L,h)
            prediction=(L-K)+(1-L)*t*t
            assert (tn>t)==(prediction>0) or abs(tn-t)<1e-10
            checks+=1
        if star is not None:
            t2,_=angle_map(star,L,h)
            assert abs(star-t2)<2e-13
            checks+=1
    # Verify the singular critical coefficient without confusing it with
    # a finite-time proof.
    for h in [0.2,0.5,1,2]:
        L=1
        for t in [1e2,5e2,1e3,3e3]:
            tn,_=angle_map(t,L,h)
            # Use relative error, since subtraction magnifies rounding.
            assert abs((t*t-tn*tn)/(2*h*h)-1)<2e-3
            checks+=1
    # In the special zero-skew cases the map is an identity when L=1.
    for t in [-4,-1,0,1,4]:
        tn,w=angle_map(t,1.0,0.0)
        assert abs(t-tn)<1e-14 and abs(w)<1e-14
        checks+=1
    print(f'CHECK_OK finite_diagnostics={checks}')

if __name__=='__main__':
    main()
