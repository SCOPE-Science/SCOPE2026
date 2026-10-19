#!/usr/bin/env python3
"""Independent finite-dimensional checks for the single-link discriminant spectrum."""
import math
import numpy as np

def predicted(n,m):
    k=n-m
    p=1/(n-1)
    if k==2:
        return sorted([1.]*m + [0.,0.])
    b=k-2
    a=1/math.sqrt((n-1)*(n-2))
    disc=math.sqrt(((b-1)*p)**2+8*b*a*a)
    plus=((b-1)*p+disc)/2
    minus=((b-1)*p-disc)/2
    return sorted([1.]*m+[plus,minus,0.]+[-p]*(b-1))

def actual(n,m):
    k=n-m
    C=np.zeros((n,n))
    for i in range(m): C[i,i]=1
    for i in range(m,n):
        for j in range(i+1,n):
            if i==m and j==m+1:continue
            if i in (m,m+1) or j in (m,m+1):
                v=1/math.sqrt((n-1)*(n-2))
            else:v=1/(n-1)
            C[i,j]=C[j,i]=v
    return np.linalg.eigvalsh(C)

assertions=0
for n in range(4,56):
    for m in range(0,n-1):
        k=n-m
        if k<2:continue
        ev=actual(n,m)
        pv=predicted(n,m)
        assert len(ev)==len(pv)==n
        assert max(abs(x-y) for x,y in zip(ev,pv))<1e-12,(n,m,ev,pv)
        assertions+=1
        if k>=3:
            b=k-2
            p=1/(n-1)
            a=1/math.sqrt((n-1)*(n-2))
            tr=(b-1)*p
            d=math.sqrt(tr*tr+8*b*a*a)
            pos=(tr+d)/2
            neg=(tr-d)/2
            L=(k-1)*p
            delta=L-pos
            val=2*m/((n-1)**2*(n-2))/(L-neg)
            assert abs(delta-val)<1e-12,(n,m,delta,val)
            assert abs(delta)<1e-12 if m==0 else delta>0
            assertions+=2
            dr=2*p/(k*(n-2))*(m+(k-2)*(math.sqrt(n-1)-math.sqrt(n-2))**2)
            assert dr>delta+1e-15,(n,m,dr,delta)
            assertions+=1
# Asymptotic rates, tolerance relative 0.05
for m in [0,1,2,4,9]:
    n=10000; k=n-m; b=k-2; p=1/(n-1); a=1/math.sqrt((n-1)*(n-2));
    tr=(b-1)*p; disc=math.sqrt(tr**2+8*b*a*a);neg=(tr-disc)/2
    delta=(2*m/((n-1)**2*(n-2)))/((k-1)*p-neg)
    assert abs(delta*n**3-2*m)<.07
    dr=2*p/(k*(n-2))*(m+(k-2)*(math.sqrt(n-1)-math.sqrt(n-2))**2)
    assert abs(dr*n**3-(2*m+.5))<.07
    assertions+=2
for alpha in [.1,.25,.5,.75,.9]:
    n=10000;m=round(alpha*n);k=n-m;b=k-2;p=1/(n-1);a=1/math.sqrt((n-1)*(n-2));
    tr=(b-1)*p;neg=(tr-math.sqrt(tr**2+8*b*a*a))/2
    delta=2*m/((n-1)**2*(n-2))/((k-1)*p-neg)
    assert abs(delta*n*n -2*alpha/(1-alpha))<.04
    assertions+=1
print('PASS',assertions, 'independent symmetric eigenspectra, exact shifts, strict Rayleigh bounds, asymptotics')
