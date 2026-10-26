"""Independent finite-state and Fourier checks for the signed-spin ladder observable."""
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from math import sqrt,log,tanh

def exact_formula(m):
    q=(2-sqrt(3))**m
    return 8*m/(3*m+2*sqrt(3)*(1+q)/(1-q))

def direct_generator(m):
    n=2*m;size=2**n
    Q=lil_matrix((size,size),dtype=float)
    nbrs=[((i-1)%n,(i+1)%n,(i+m)%n) for i in range(n)]
    for mask in range(size):
        total=0.
        for i in range(n):
            si=(mask>>i)&1
            r=sum(si==((mask>>j)&1) for j in nbrs[i])/3
            if r:
                Q[mask^(1<<i),mask]+=r
                total+=r
        Q[mask,mask]-=total
    a=Q.tolil(); a[-1,:]=1
    rhs=np.zeros(size);rhs[-1]=1
    p=spsolve(a.tocsc(),rhs)
    ss=np.array([2*x.bit_count()-n for x in range(size)])
    var=np.dot(p,ss**2)-np.dot(p,ss)**2
    return var, p.min(), abs(p.sum()-1)

for m in (2,4,6):
    d,pmn,err=direct_generator(m)
    f=exact_formula(m)
    print('m',m,'var',d,'formula',f,'err',d-f,'min_prob',pmn,'sum_err',err)
    assert abs(d-f)<5e-8 and pmn>-1e-11
for m in (2,4,6,8,10,100):
    f=exact_formula(m)
    theta=np.pi*np.arange(2*m)/m
    eig=3+2*np.cos(theta)+(-1.)**np.arange(2*m)
    spectral=2*m/(6*np.mean(1/eig))
    print('spectral',m,f,spectral)
    assert abs(f-spectral)<1e-7
print('all checks passed')
