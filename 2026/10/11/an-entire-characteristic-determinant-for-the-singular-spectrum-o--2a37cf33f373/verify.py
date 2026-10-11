from fractions import Fraction as Q
import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh

def derivatives(a,d,M):
    coeff=[Q(1)]
    for k in range(1,M+1):
        n=a+2*k
        coeff.append(coeff[-1]/(n*(n-1)*(n-2)*(n-3)))
    vals=[Q(0)]*(M+1)
    for k,c in enumerate(coeff):
        n=a+2*k
        if n>=d:
            mult=1
            for j in range(d):mult*=n-j
            vals[k]=c*mult
    return vals

def conv(v,w,M):return [sum(v[j]*w[k-j] for j in range(k+1)) for k in range(M+1)]
M=3
u22=derivatives(2,2,M);u23=derivatives(2,3,M);u32=derivatives(3,2,M);u33=derivatives(3,3,M)
f=[a-b for a,b in zip(conv(u22,u33,M),conv(u32,u23,M))]
print('F coefficients',f,'normalized', [x/12 for x in f]);assert f[:3]==[Q(12),Q(-2),Q(1,40)]
print('trace kernel',Q(1,6),'trace B2',Q(17,720)); assert Q(1,36)-2*Q(1,480)==Q(17,720)
mp.mp.dps=35

def uder(a,d,z):
    c=mp.mpf(1);s=mp.mpf(0)
    for k in range(140):
        n=a+2*k
        term=c*mp.rf(n-d+1,d) if n>=d else mp.mpf(0)
        s+=term
        if k>15 and abs(term)< mp.mpf('1e-33')*max(1,abs(s)):break
        N=n+2
        c*=z/(N*(N-1)*(N-2)*(N-3))
    return s

def F(z):return uder(2,2,z)*uder(3,3,z)-uder(3,2,z)*uder(2,3,z)
roots=[]
for left,right in ((5,8),(90,110),(480,520),(1500,1650)):
    root=mp.findroot(F,(left,right));roots.append(root)
    assert abs(F(root))<mp.mpf('1e-23')
print('roots',[str(z) for z in roots]); sigs=[float(1/mp.sqrt(x)) for x in roots];print('singular values',sigs)
N=350
g,w=leggauss(N);x=(g+1)/2;w=w/2
xx=x[:,None]; yy=x[None,:]
mi=np.minimum(xx,yy); ma=np.maximum(xx,yy)
K=mi/2-mi**2/(6*ma)
QK=K*np.sqrt(w[:,None]*w[None,:])
eigs=eigh(QK,subset_by_index=[N-4,N-1],eigvals_only=True)[::-1]
print('Nyström sigma',np.sqrt(eigs),'diff', np.sqrt(eigs)-sigs)
assert max(abs(np.sqrt(eigs)-sigs))<3e-5
print('VERIFY_OK exact coefficients, exact kernel traces, 4 entire roots, 4 Nyström approximations')
