"""Independent numerical checks for the even squared-cycle mixing formulas."""
import math
import numpy as np
from scipy.optimize import linprog

count=0
for n in range(8,121,2):
    q=2*(1-math.cos(2*math.pi/n))
    x=np.cos(2*math.pi*np.arange(1,n//2+1)/n)
    U=2*(1-x)
    V=4*(1-x*x)
    j=math.ceil(n/4)
    d=math.cos(2*math.pi*j/n)
    E=4*q
    M=2*q*(1-d)+4*(1-d*d)
    a,b=2*q/(E+M),2/(E+M)
    h=1-2*(a+b)
    assert h>0 and a>0 and b>0
    lam=1-a*U-b*V
    mu=(M-E)/(M+E)
    assert abs(np.max(np.abs(lam))-mu)<1e-10
    assert abs(lam[0]-mu)<1e-10
    assert abs(lam[-1]-mu)<1e-10
    assert abs(lam[j-1]+mu)<1e-10
    count+=4
    if n%4==0:
        assert abs(a-q/(2+3*q))<1e-11
        assert abs(b-1/(2+3*q))<1e-11
        assert abs(h-a)<1e-11
    else:
        s=math.sin(math.pi/n)
        den=1+5*s*s+2*s**3
        assert abs(a-2*s*s/den)<1e-11
        assert abs(b-1/(2*den))<1e-11
        assert abs(h-s*s*(1+2*s)/den)<1e-11
    count+=3
    # An independently optimized Fourier linear program: maximize spectral gap.
    one=np.ones(len(U))
    A_ub=np.vstack([np.column_stack([-U,-V,one]),
                    np.column_stack([U,V,one]),
                    [2,2,0]])
    b_ub=np.concatenate([np.zeros(len(U)),2*one,[1]])
    lp=linprog([0,0,-1],A_ub=A_ub,b_ub=b_ub,
               bounds=[(0,None),(0,None),(0,None)],method='highs')
    assert lp.success
    assert abs(lp.x[0]-a)<1e-8
    assert abs(lp.x[1]-b)<1e-8
    assert abs(lp.x[2]-(1-mu))<1e-8
    count+=4
    # The full n-by-n transition matrix gives the same SLEM.
    P=np.eye(n)*h
    for k in range(n):
        for delta,p in ((-1,a),(1,a),(-2,b),(2,b)):
            P[k,(k+delta)%n]+=p
    eig=np.linalg.eigvalsh(P)
    assert abs(np.max(np.abs(eig[:-1]))-mu)<1e-8
    assert abs(np.min(P))<1e-13
    assert np.max(np.abs(P.sum(axis=1)-1))<1e-12
    count+=3
print('VERIFY_OK',count,'checks')
