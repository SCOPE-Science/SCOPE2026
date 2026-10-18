"""Reproduce exact finite-path heat-gradient identities and independent numerical tests.

Requires Python 3, NumPy and SciPy. All assertions concern finite test cases;
the theorem for every degree and time is proved separately in RESULT.md.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.special import i0e, i1e
from scipy.optimize import brentq

checks = 0

def close(a, b, tol=2e-10):
    global checks
    assert abs(a-b) <= tol * (1+abs(a)+abs(b)), (a,b)
    checks += 1

def ok(condition):
    global checks
    assert condition
    checks += 1

def generators(n):
    v = np.zeros((n,n))
    for j in range(n-1):
        v[j,j] -= 1
        v[j+1,j+1] -= 1
        v[j,j+1] += 1
        v[j+1,j] += 1
    m=n-1
    d=np.diag([-2.0]*m)
    if m>1:
        d += np.diag([1.0]*(m-1),1)+np.diag([1.0]*(m-1),-1)
    e=np.zeros((m,n))
    for j in range(m):
        e[j,j]=-1
        e[j,j+1]=1
    return v,d,e

def spectral(n,t,i):
    return (2/n)*sum(math.exp(-4*t*math.sin(math.pi*k/(2*n))**2)*math.sin(math.pi*k*i/n)**2 for k in range(1,n))

for n in range(2,17):
    v,d,e=generators(n)
    ok(np.allclose(e@v,d@e,rtol=0,atol=1e-14))
    mid={n//2} if n%2==0 else {(n-1)//2,(n+1)//2}
    for t in [0.025,0.15,0.5,1.,2.5,6.,20.]:
        h=expm(t*v)
        k=expm(t*d)
        ok(np.max(np.abs(e@h-k@e))<2e-11)
        ok(np.min(k)>-2e-13)
        row_abs=np.sum(np.abs(e@h),axis=1)
        best=np.max(row_abs)
        formula=2*np.max(np.diag(k))
        close(best,formula)
        close(best,2*k[n//2-1,n//2-1] if n%2==0 else 2*k[(n-1)//2-1,(n-1)//2-1])
        ok(all(k[j,j]<=np.max(np.diag(k))+1e-13 for j in range(n-1)))
        for i in range(1,n):
            vals=np.r_[0,k[i-1,:],0]
            turns=np.diff(vals)
            sig=turns[np.abs(turns)>1e-12]
            ok(all(not(sig[j]<0 and sig[j+1]>0) for j in range(len(sig)-1)))
            close(row_abs[i-1],np.sum(abs(np.diff(vals))))
            close(row_abs[i-1],2*np.max(k[i-1,:]))
            close(k[i-1,i-1],spectral(n,t,i))
        ok(best <= 2*i0e(2*t)+2e-12)

for t in [0.15,0.4,1.,2.,5.]:
    z=brentq(lambda z:i1e(z)/i0e(z)-(1-1/(2*z)),0.1,20)
    c=math.sqrt(2*z)*i0e(z)
    close(z/2,0.3949892106717840,1e-11)
    close(c,0.6630149334909870,1e-11)
    ok(c>1/math.sqrt(math.pi))
for n in [50,100,200]:
    for s in [0.01,0.05,0.2]:
        i=n//2
        left=n*(2*spectral(n,s*n*n,i))
        right=4*sum(math.exp(-math.pi**2*k*k*s) for k in range(1,200,2))
        ok(abs(left-right)<max(1.0/n,0.01))
print('PASS assertions', checks)
print('universal t*=0.3949892106717840; C*=0.6630149334909870')
