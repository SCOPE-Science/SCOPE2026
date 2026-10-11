#!/usr/bin/env python3
"""Numerically reproduce the scalar periodic equation and period-derivative identity."""
import math

PI=math.pi

def rk4_step(t, y, h, q):
    def rhs(x,z):
        return q*math.sin(2*x)-2*q*math.sin(x)**2*z
    k1=rhs(t,y)
    k2=rhs(t+h/2,y+h*k1/2)
    k3=rhs(t+h/2,y+h*k2/2)
    k4=rhs(t+h,y+h*k3)
    return y+h*(k1+2*k2+2*k3+k4)/6

def solve(q, n=16000):
    if q <= 0 or n % 2: raise ValueError('q positive; n even')
    h=PI/n
    z=0.0
    for j in range(n): z=rk4_step(j*h,z,h,q)
    # Homogeneous monodromy over pi is exact.
    w0=z/(-math.expm1(-PI*q))
    h=2*PI/n
    values=[w0]
    z=w0
    for j in range(n):
        z=rk4_step(j*h,z,h,q)
        values.append(z)
    def simpson(fun):
        a=fun(0,values[0])+fun(n,values[-1])
        for j in range(1,n): a+=(4 if j%2 else 2)*fun(j,values[j])
        return a*h/3
    square=simpson(lambda j,w: math.sin(j*h)**2*w*w)
    pairing=simpson(lambda j,w: .5*w*math.sin(2*j*h))
    mismatch=abs(square-pairing)
    assert abs(z-w0) < 1e-9*(1+abs(w0)), (q,'periodicity',z,w0)
    assert square>0, (q,'not positive')
    assert mismatch < 5e-8*max(1,abs(square)), (q,'identity',square,pairing)
    return square,pairing

if __name__=='__main__':
    for q in (.04,.16,1.0,4.0):
        square,pairing=solve(q)
        print('q=',q,'squared integral=',format(square,'.12g'),
              'forcing pairing=',format(pairing,'.12g'),
              'ratio to q^2=',format(square/(q*q),'.12g'))
    small,_=solve(.005)
    assert abs(small/(.005**2)-PI/16)<2e-4
    print('CHECK_OK')
