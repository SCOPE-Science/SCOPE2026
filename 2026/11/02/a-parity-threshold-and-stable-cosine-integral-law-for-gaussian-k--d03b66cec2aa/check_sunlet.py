#!/usr/bin/env python3
"""Independent numerical replay of the sunlet power-distance Fourier symbols.
Standard-library only; finite tests corroborate but do not certify asymptotics.
"""
import cmath, math
from itertools import product


def a(n,j): return min(j % n, (-j) % n)

def entries(n,k,p):
    A=E=0.
    L=-2.
    for j in range(1,n):
        t=a(n,j)
        c=math.cos(2*math.pi*k*j/n)
        A+=t**p*c
        E+=((t+1)**p-t**p)*c
        L+=(t**p-2*(t+1)**p+(t+2)**p)*c
    return A,1+E,L

def cycle_exact(n,k):
    if n%2==0:
        return 0.0 if k%2==0 else -1/(math.sin(math.pi*k/n)**2)
    if k%2==0:
        return -1/(4*math.cos(math.pi*k/(2*n))**2)
    return -1/(4*math.sin(math.pi*k/(2*n))**2)

def sym_max_eigen(n,k,p):
    A,E,L=entries(n,k,p)
    return (A+L+math.sqrt((A-L)**2+4*E**2))/2

def threshold(n):
    def maxval(p):
        return max([entries(n,0,p)[2]] +
                   [sym_max_eigen(n,k,p) for k in range(1,n//2+1)])
    lo,hi=1.,2.
    assert maxval(lo)<1e-8 and maxval(hi)>0.
    for _ in range(54):
        mid=(lo+hi)/2
        if maxval(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

checks=0
for n in range(3,48):
    for k in range(1,n):
        A,E,L=entries(n,k,1)
        assert abs(A-cycle_exact(n,k))<2e-9,(n,k,A,cycle_exact(n,k))
        assert abs(E)<2e-9 and abs(L+2)<2e-9,(n,k,E,L)
        checks+=3
    assert abs(entries(n,0,1)[2]+2)<1e-10
    checks+=1

# Verify the 2-by-2 symbols against the original 2n-by-2n distance matrix.
for n in (3,4,5,6,7,8,9,11,13,17,19):
    for p in (1.0,1.08,1.5,2.0):
        for k in range(1,n):
            w=cmath.exp(2j*math.pi*k/n)
            # root amplitude=1 and leaf amplitude=0; recover H11.
            v=[w**i for i in range(n)]+[0j]*n
            # root amplitude=-1 and leaf amplitude=1; recover H22.
            z=[-w**i for i in range(n)]+[w**i for i in range(n)]
            def quad(x,y):
                s=0j
                for ix in range(2*n):
                    for iy in range(2*n):
                        i,j=ix % n,iy % n
                        ai,aj=int(ix>=n),int(iy>=n)
                        if ix==iy: d=0
                        elif i==j: d=1
                        else:d=a(n,i-j)+ai+aj
                        s+=x[ix].conjugate()*d**p*y[iy]
                return s/n
            A,E,L=entries(n,k,p)
            assert abs(quad(v,v)-A)<1e-7
            assert abs(quad(v,z)-E)<1e-7 # v is root; z=leaf-root
            assert abs(quad(z,z)-L)<1e-7
            checks+=3

print('checks',checks)
for n in (3,4,5,6,7,8,9,11,15,25,45,101,201):
    if n%2: t=threshold(n)
    else:t=1.
    print(n,format(t,'.12f'),format(n*n*(t-1),'.9f'))

# High accuracy reference via numerical quadrature (trapezoid, independent of scipy).
N=200000
step=2*math.pi/N
integral=0.0
for j in range(1,N+1):
    x=j*step
    integrand=(1-math.cos(x))/x
    integral+=(integrand if j<N else integrand/2)
Cin=integral*step
Cstar=2*math.pi**2/Cin
assert 8.09<Cstar<8.11
assert abs(threshold(201)-1-Cstar/201**2)<3e-6
print('asymptotic constant',format(Cstar,'.9f'))
