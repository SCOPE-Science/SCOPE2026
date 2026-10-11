#!/usr/bin/env python3
import math
import numpy as np

PI=math.pi

def formula(n):
    if n%2==0:
        a=PI/n
        return 1/3 + 1/(3*math.sin(a)**2) + n*(2+1/math.tan(a))/(3*PI)
    b=PI/(2*n)
    return 1/3 + 1/(12*math.sin(b)**2) + n*(4+1/math.tan(b))/(6*PI)

def planar_formula(n):
    if n%2==0:
        m=n; R=1/math.sin(PI/n)
    else:
        m=2*n; R=1/(2*math.sin(PI/(2*n)))
    return R*R*(0.5 + m*math.sin(2*PI/m)/(4*PI))

def vertices(n):
    R=1/(2*math.sin(PI/n))
    t=2*PI*np.arange(n)/n
    return np.column_stack((R*np.cos(t),R*np.sin(t)))

# Direct planar angular integration of widths.
M=180000
th=2*PI*(np.arange(M)+0.5)/M
D=np.column_stack((np.cos(th),np.sin(th)))
for n in (3,4,5,6,7,8,11):
    V=vertices(n)
    h=np.max(D@V.T,axis=1)
    hm=np.max((-D)@V.T,axis=1)
    w=h+hm
    m1=float(np.mean(w)); m2=float(np.mean(w*w))
    assert abs(m1-n/PI)<3e-9,(n,m1,n/PI)
    assert abs(m2-planar_formula(n))<2e-8,(n,m2,planar_formula(n))

# Cube specialization.
assert abs(formula(4)-(1+4/PI))<2e-15

# Deterministic Fibonacci sphere for direct 3D support widths.
def fibsphere(N):
    k=np.arange(N,dtype=float)
    z=1-2*(k+0.5)/N
    g=(1+math.sqrt(5))/2
    t=2*PI*k/g
    r=np.sqrt(np.maximum(0,1-z*z))
    return np.column_stack((r*np.cos(t),r*np.sin(t),z))

U=fibsphere(150000)
for n in (3,4,5,6,9,10):
    V2=vertices(n)
    top=np.column_stack((V2,np.full(n,0.5)))
    bot=np.column_stack((V2,np.full(n,-0.5)))
    V3=np.vstack((top,bot))
    h=np.max(U@V3.T,axis=1)
    hm=np.max((-U)@V3.T,axis=1)
    val=float(np.mean((h+hm)**2))
    assert abs(val-formula(n))<3e-5,(n,val,formula(n))

print('VERIFY_OK')
print('planar_first_second_moments = passed')
print('cube_specialization = passed')
print('spatial_fibonacci_quadrature = passed')
