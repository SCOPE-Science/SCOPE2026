#!/usr/bin/env python3
"""Independent quadrature and finite-spectrum checks for bandlimited EW resetting."""
from math import pi, atan, sqrt
from fractions import Fraction

def excess(x,n=360):
    if n%2: raise ValueError('even n')
    u=[i/n for i in range(n+1)]
    w=[(1 if i in (0,n) else (4 if i%2 else 2))/(3*n) for i in range(n+1)]
    mu=atan(1/sqrt(x))/sqrt(x)
    c=0.
    for i in range(n+1):
        ai=x+u[i]**2
        for j in range(n+1):
            c += w[i]*w[j]/(ai*(x+u[j]**2)*(x+u[i]**2+u[j]**2))
    return 3*x*c/mu**2

xs=[0.001,0.01,0.1,1,10,100]
ks=[excess(x) for x in xs]
assert all(ks[i] < ks[i+1] for i in range(len(ks)-1)),ks
assert abs(ks[0]-(12/pi-3))<0.05
assert abs(ks[-1]-3)<0.03
assert abs(ks[-1]-(3-2/100))<0.002

# Contrasting general two-mode OU: a strictly monotonic crossover is NOT
# automatic for arbitrary spectral weights or unequal damping rates.
def general_kurtosis(rate):
    r=Fraction(rate)
    lam=[Fraction(1),Fraction(100)]
    weight=[Fraction(1),Fraction(1,100)]
    mean=sum((weight[i]*lam[i]/(r+lam[i]) for i in range(2)),Fraction(0))
    variance=sum((weight[i]*weight[j]*r*lam[i]*lam[j]/
                  ((r+lam[i]+lam[j])*(r+lam[i])*(r+lam[j]))
                  for i in range(2) for j in range(2)),Fraction(0))
    return 3*variance/mean**2
assert general_kurtosis(10)>general_kurtosis(20)>general_kurtosis(50)
assert general_kurtosis(70)>general_kurtosis(50)
print('PASS numeric EW crossover:')
for x,k in zip(xs,ks): print(f'x={x:.3g}: excess={k:.12g}')
print('PASS exact-rational nonmonotone two-mode control:',*[str(general_kurtosis(r)) for r in (10,20,50,70)])
