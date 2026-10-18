"""Independent numerical checks of the incremental opinion linearization."""
import math
import numpy as np
from scipy.optimize import brentq


def dynamics(p, k):
    m = float(np.dot(np.arange(-k,k+1),p))
    a,b=(k+m)/(2*k),(k-m)/(2*k)
    out=np.zeros(len(p))
    for i in range(2*k+1):
        if i<2*k:
            out[i]-=a*p[i];out[i+1]+=a*p[i]
        if i>0:
            out[i]-=b*p[i];out[i-1]+=b*p[i]
    return out


def spectral_root(k):
    def mismatch(lam):
        t=math.acosh(1+lam)
        z=k*t
        return lam-2/(2*k+1)*(1-1/(k*(lam+math.sinh(t)/math.tanh(z))))
    return brentq(mismatch,1.e-14,2/(2*k+1),xtol=1e-15,rtol=9e-15)


def check():
    for k in range(1,15):
        n=2*k+1
        p=np.full(n,1/n)
        eps=2e-6
        J=np.column_stack([(dynamics(p+eps*np.eye(n)[j],k)-dynamics(p-eps*np.eye(n)[j],k))/(2*eps) for j in range(n)])
        vals=np.linalg.eigvals(J)
        pos=[z for z in vals if z.real>1e-7]
        zeros=[z for z in vals if abs(z)<1e-7]
        assert len(pos)==1 and len(zeros)==1,(k,vals)
        lam=spectral_root(k)
        assert abs(pos[0].real-lam)<1e-7,(k,pos,lam)
        t=math.acosh(1+lam)
        h=np.sinh(np.arange(-k,k+1,dtype=float)*t)
        assert np.linalg.norm(J@h-lam*h)<1.e-6,(k,np.linalg.norm(J@h-lam*h))
        assert abs(np.sum(h))<1e-9
    for k in (100,1000,10000):
        lam=spectral_root(k)
        assert abs((1-k*lam)*math.sqrt(k)-1/math.sqrt(2))<0.10,(k,lam)
        t=math.acosh(1+lam)
        for x in (0.25,0.5,1.):
            d=int(x*math.sqrt(k))
            ratio=math.exp(-d*t)*(1-math.exp(-2*(k-d)*t))/(1-math.exp(-2*k*t))
            assert abs(ratio-math.exp(-math.sqrt(2)*x))<.15,(k,x,ratio)
    print('PASS: 14 independently differentiated Jacobians, spectra/eigenvectors; 3 large-k and boundary-layer tests')
    print('selected',[(k,spectral_root(k)) for k in (1,2,3,10,100,1000,10000)])

if __name__=='__main__':check()
