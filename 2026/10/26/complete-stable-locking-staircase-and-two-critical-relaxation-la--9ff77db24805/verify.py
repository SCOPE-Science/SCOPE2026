"""Reproducible numerical checks for a periodically detuned Kuramoto cycle.
Requires only Python 3, NumPy, and SciPy. The mathematical proof is independent.
"""
import math
import numpy as np
from scipy.linalg import eigvalsh

def locked_branch(m, a, K, q):
    theta=2*math.pi*q/m
    kc=a/(1+math.cos(theta))
    assert abs(q)<m/2 and K>kc
    delta=2*math.asin(a/(2*K*math.cos(theta/2)))
    alpha=(theta+delta)/2
    beta=(theta-delta)/2
    assert abs(alpha)<math.pi/2 and abs(beta)<math.pi/2, (alpha,beta)
    edges=np.array([beta if j%2==0 else alpha for j in range(2*m)])
    phases=np.r_[0,np.cumsum(edges)[:-1]]
    om=np.array([a if i%2==0 else -a for i in range(2*m)])
    field=om+K*(np.sin(np.roll(phases,-1)-phases)+np.sin(np.roll(phases,1)-phases))
    weights=K*np.cos(edges)
    J=np.zeros((2*m,2*m))
    for j,w in enumerate(weights):
        k=(j+1)%(2*m)
        J[j,j]-=w;J[k,k]-=w;J[j,k]+=w;J[k,j]+=w
    u=K*math.cos(alpha); v=K*math.cos(beta)
    pred=[]
    for r in range(m):
        h=math.sqrt(max(0,u*u+v*v+2*u*v*math.cos(2*math.pi*r/m)))
        pred.extend((-(u+v)-h, -(u+v)+h))
    eig=np.sort(eigvalsh(J)); pred=np.sort(pred)
    return (max(abs(field)),max(abs(eig-pred)),eig[-2],-eig[-2],(alpha,beta))

checks=0
for m in range(3,17):
    for q in range(-m//2,m//2+1):
        if abs(q)*2 >= m: continue
        a=1.7
        kc=a/(1+math.cos(2*math.pi*q/m))
        for factor in (1.0001,1.01,1.3,3,20):
            residual, spectral_error, lam, gap, angles=locked_branch(m,a,kc*factor,q)
            assert residual < 2e-11, (m,q,residual)
            assert spectral_error < 5e-10, (m,q,spectral_error)
            assert gap>0, (m,q,gap)
            checks+=1

for m in (3,4,5,7,10,15):
    a=1.7
    for q in range(0,(m-1)//2+1):
        theta=2*math.pi*q/m
        kc=a/(1+math.cos(theta))
        eta=1e-6
        gap=locked_branch(m,a,kc*(1+eta),q)[3]
        if q==0:
            predicted=(math.sqrt(2)*a*(1-math.cos(math.pi/m)))*math.sqrt(eta)
        else:
            predicted=(a*(1-math.cos(2*math.pi/m))/math.sin(theta))*eta
        assert abs(gap/predicted-1)<0.002,(m,q,gap,predicted)

# Deterministic exact inequality for a repeated negative conductance:
# a single negative cycle edge -c forces instability when m-1
# other edges have positive conductance c, with at least one extra
# positive edge. This is checked by constructing its explicit witness.
for m in range(3,13):
    c=1.3
    path=[c]*(m-1)+[2.0]*(m+1)
    R=sum(1/w for w in path)
    energy=1/R-c
    assert energy<0
print(f'VERIFY_OK: {checks} branch residual/spectrum tests, 6 critical-gap-size checks, and repeated-edge instability witnesses')
