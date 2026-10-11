#!/usr/bin/env python3
import math

def polygon_norm(z, n):
    theta = math.pi/(4*n)
    c = math.cos(theta)
    x,y = z
    vals=[]
    for k in range(4*n):
        a=2*k*theta
        vals.append((x*math.cos(a)+y*math.sin(a))/c)
    return max(vals)

def check(n):
    theta=math.pi/(4*n)
    x=(math.cos(theta), math.sin(theta))
    y=(math.cos(theta),-math.sin(theta))
    nx=polygon_norm(x,n); ny=polygon_norm(y,n)
    s=(x[0]+y[0],x[1]+y[1])
    d=(x[0]-y[0],x[1]-y[1])
    ns=polygon_norm(s,n); nd=polygon_norm(d,n)
    target=1/(math.cos(theta)**2)
    got=(ns*ns+nd*nd)/4
    assert abs(nx-1)<2e-12 and abs(ny-1)<2e-12
    assert abs(ns-2)<2e-12
    assert abs(nd-2*math.tan(theta))<2e-12
    assert abs(got-target)<5e-12
    # Sample the norm sandwich. This is not the proof of the continuum bound.
    for j in range(720):
        a=2*math.pi*j/720
        z=(math.cos(a),math.sin(a))
        p=polygon_norm(z,n)
        assert p >= 1-2e-12
        assert p <= 1/math.cos(theta)+2e-12

for n in range(1,65):
    check(n)
print('VERIFY_OK')
