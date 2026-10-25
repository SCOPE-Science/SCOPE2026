#!/usr/bin/env python3
"""Independent arithmetic checks of an exact fastest-mixing formula.
This program checks only finite cases; the accompanying analytic proof handles all n.
"""
import math


def predicted(n):
    assert isinstance(n, int) and n >= 3
    if n <= 7:
        x = 1.0/n
        rho = 1/math.sqrt(n)
    else:
        disc = n*n - 8*n + 8
        # Rationalized expression for the smaller positive root.
        x = 2.0/(2*(n-1)+math.sqrt(disc))
        rho = (n-2)*x/2
    y = (2-n*x)/(2*(n-1))
    return x,y,rho


def eigenvalues(n,x,y):
    A=1-(n-1)*x
    B=1-x-2*(n-1)*y
    center=(A+B)/2
    radius=math.hypot((A-B)/2, math.sqrt(n-1)*x)
    d=1-x-(n-1)*y
    return (1.0, 1-n*x, center+radius, center-radius, d)


def symmetric_slem(n,x,y):
    return max(abs(v) for v in eigenvalues(n,x,y)[1:])


def gradient_certificate(n,x,r):
    A=1-(n-1)*x
    K=2*(n-1)*(1-n*x)/((n-2)*r)
    s=1/(1+K)
    t=(K-A/r)*s
    alpha=(s-t)/2
    beta=(s+t)/2
    gamma=K*s
    u=(-(n-2)*A/2+(n-1)*x)/r
    v=(n-1)*A/r
    gx=alpha*(-n/2+u)+beta*(n/2+u)-gamma
    gy=alpha*(-(n-1)+v)+beta*((n-1)+v)-gamma*(n-1)
    return alpha,beta,gamma,gx,gy


def main():
    for n in range(3,501):
        x,y,r=predicted(n)
        assert 0<x<=1/(n-1)+1e-13
        assert 0<y<(1-x)/(n-1)+1e-13
        ev=eigenvalues(n,x,y)
        assert abs(symmetric_slem(n,x,y)-r)<1e-10
        if n>=8:
            alpha,beta,gamma,gx,gy=gradient_certificate(n,x,r)
            assert min(alpha,beta,gamma)>-1e-10
            assert abs(alpha+beta+gamma-1)<1e-10
            assert max(abs(gx),abs(gy))<5e-9
            assert abs(ev[2]-r)<1e-9 and abs(ev[3]+r)<1e-9
            assert abs(ev[4]-r)<1e-9
    for n in (3,4,7,8,9,10,20,50):
        x,y,r=predicted(n)
        worst_delta = 0.0
        # Fixed deterministic rectangular grid. This does not prove optimality.
        for k in range(81):
            xx=k/(80*(n-1))
            for j in range(81):
                yy=(1-xx)*j/(80*(n-1))
                worst_delta=max(worst_delta,r-symmetric_slem(n,xx,yy))
        assert worst_delta<1e-10
        print(f'n={n} x={x:.12g} y={y:.12g} rho={r:.12g} grid_opt_excess={worst_delta:.1e}')
    print('finite numerical identity checks pass; infinite optimality is proved separately')

if __name__=='__main__':main()
