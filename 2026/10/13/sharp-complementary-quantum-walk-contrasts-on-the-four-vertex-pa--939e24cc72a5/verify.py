#!/usr/bin/env python3
"""Independent finite-time checks for the four-site path and its complement."""
from cmath import exp
from math import sin, cos, sqrt, pi
from random import Random

N = 4
A = [[0.0]*N for _ in range(N)]
for j in range(N - 1):
    A[j][j+1] = A[j+1][j] = 1.0
B = [[1.0 - float(i == j) - A[i][j] for j in range(N)] for i in range(N)]


def mm(x,y):
    return [[sum(x[i][k]*y[k][j] for k in range(N)) for j in range(N)] for i in range(N)]


def expmatrix(H,t):
    """Scaled Taylor with squaring; deliberately independent of the 2x2 block proof."""
    L=9
    K=40
    Q = [[1.0+0.0j if i==j else 0.0j for j in range(N)] for i in range(N)]
    term = [row[:] for row in Q]
    base = [[1j*t*H[i][j]/(2**L) for j in range(N)] for i in range(N)]
    for k in range(1,K+1):
        product = mm(term, base)
        term = [[product[i][j]/k for j in range(N)] for i in range(N)]
        Q = [[Q[i][j]+term[i][j] for j in range(N)] for i in range(N)]
    for _ in range(L):
        Q=mm(Q,Q)
    return Q


def expected(i,j,t):
    cc=cos(sqrt(5)*t/2)
    ss=sin(sqrt(5)*t/2)
    C=cos(t/2)
    S=sin(t/2)
    same=(i in (0,3))==(j in (0,3))
    if same:
        f=abs(sin(t))*sqrt(cc**2 + ss**2/5)
        if i==j:
            a=abs(cc*C);b=abs(ss*S)/sqrt(5)
        else:
            a=abs(cc*S);b=abs(ss*C)/sqrt(5)
        g=2*min(a,b); sigma=2*max(a,b);rho=abs(a*a-b*b)
    else:
        f=2/sqrt(5)*abs(ss*cos(t))
        g=2/sqrt(5)*abs(ss)*(abs(C)-abs(S))
        g=abs(g)
        sigma=2/sqrt(5)*abs(ss)*(abs(C)+abs(S))
        rho=4/5*ss*ss*abs(C*S)
    return f,g,sigma,rho


def observed(i,j,t,U,V):
    x=abs(U[i][j]);y=abs(V[i][j])
    return (abs(V[i][j]-exp(-1j*t)*U[i][j].conjugate()), abs(x-y), x+y, x*y)


def main():
    rng=Random(20261009)
    times=[0.,0.01,0.1,0.5,1.,pi/2,pi,pi*sqrt(5),-4.,9.2,25.]
    times.extend(rng.uniform(-25,25) for _ in range(190))
    count=0
    for t in times:
        U=expmatrix(A,t);V=expmatrix(B,t)
        for i in range(N):
            for j in range(N):
                val=observed(i,j,t,U,V);form=expected(i,j,t)
                for obs,expct in zip(val,form):
                    assert abs(obs-expct)<2e-11,(i,j,t,obs,expct)
                    count+=1
                assert abs(U[i][j]-U[j][i])<2e-11
                assert abs(V[i][j]-V[j][i])<2e-11
    # Check analytical sharp bounds via an independent dense grid in two independent phases.
    BOUNDS_SAME=(1.0,2/(1+sqrt(5)),2.0,1.0)
    BOUNDS_CROSS=(2/sqrt(5),2/sqrt(5),2*sqrt(2/5),2/5)
    for k in range(501):
        a=2*pi*k/501
        for j in range(233):
            b=2*pi*j/233
            # Dense torus test; a is phase sqrt(5)t/2 and b is phase t/2.
            s,c=sin(a),cos(a);S,C=sin(b),cos(b)
            same=(abs(sin(2*b))*sqrt(c*c+s*s/5),2*min(abs(c*C),abs(s*S)/sqrt(5)),2*max(abs(c*C),abs(s*S)/sqrt(5)),abs((c*C)**2-(s*S)**2/5))
            cross=(2/sqrt(5)*abs(s*cos(2*b)),2/sqrt(5)*abs(s)*abs(abs(C)-abs(S)),2/sqrt(5)*abs(s)*(abs(C)+abs(S)),4/5*s*s*abs(C*S))
            assert all(v<=bnd+1e-12 for v,bnd in zip(same,BOUNDS_SAME))
            assert all(v<=bnd+1e-12 for v,bnd in zip(cross,BOUNDS_CROSS))
    print(f'VERIFY_OK: {count} direct matrix/closed-form comparisons; 116733 torus bound pairs; analytic density proof required for sharpness.')

if __name__=='__main__':main()
