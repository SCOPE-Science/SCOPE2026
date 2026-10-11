#!/usr/bin/env python3
"""Finite numerical checks of stated signed-shift identities; not an infinite proof."""
import math

def defect(a,b,p):
    return (p-1)/p*abs(a)**p+abs(b)**p/p-(abs(a)**(p-2)*a if a else 0.0)*b

def radius_pairing(x,p):
    y=x[1:]+[-x[0]]
    return sum((abs(a)**(p-2)*a if a else 0.0)*b for a,b in zip(x,y))

def sine_vector(n,p):
    return [math.sin(math.pi*j/n)**(2/p) for j in range(n)]

def check():
    count=0
    for p in (1.25,1.5,2.0,3.0,4.0,6.0):
        for n in (4,8,16,32,64,128):
            x=sine_vector(n,p)
            y=x[1:]+[-x[0]]
            norm=sum(abs(z)**p for z in x)
            assert abs(norm-n/2)<1e-9
            s=sum(defect(a,b,p) for a,b in zip(x,y))
            q=radius_pairing(x,p)
            assert abs((norm-q)-s)<1e-8
            assert s>=-1e-9
            c=2*(p-1)/p**2*math.pi**2
            gap_upper=n*n*s/norm
            if n>=64: assert abs(gap_upper-c) < 1.25
            if p==2:
                # Constant-curvature Hilbert identity: exact maximum for even n.
                expected=math.cos(math.pi/n)
                assert abs((q/norm)-expected)<1e-10
            count+=5
        for odd in (3,5,7,9):
            x=[(-1)**j for j in range(odd)]
            assert radius_pairing(x,p)==-float(odd)
            count+=1
    for p in (1.2,2.0,3.0,5.0):
        for a in (-2.,-1.,0.,1.,2.):
            for b in (-2.,-1.,0.,1.,2.):
                assert defect(a,b,p)>=-1e-10
                count+=1
    print('VERIFY_OK checks=', count)
if __name__=='__main__':check()
