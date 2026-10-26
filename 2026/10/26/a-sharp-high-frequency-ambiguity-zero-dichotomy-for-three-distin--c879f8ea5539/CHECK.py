"""Independent finite checks of three-exponential ambiguity formulas."""
import numpy as np
from scipy.optimize import root, brentq

def amplitudes(a,b,r):
    return {a:1/((b-a)*(a+r)),b:-1/((b-a)*(b+r))},1/((a+r)*(b+r))

def ambiguity(T,w,a,b,r):
    K,c=amplitudes(a,b,r)
    z=1j*w
    s=c*c*np.exp(-(2*r-z)*T/2)/(2*r-z)
    for q,k in K.items():
        h=r-q-z
        s+=c*k*np.exp(-(r+q)*T/2)*2*np.sinh(h*T/2)/h
    for q,k in K.items():
        for p,l in K.items():
            s+=k*l*np.exp(-q*T-z*T/2)/(q+p+z)
    return s

def rho(T,a,b,r):
    return ((b+r)*np.exp((r-a)*T)-(a+r)*np.exp((r-b)*T))/(b-a)

if __name__=='__main__':
    a,b,r=2.,3.,1.
    target=np.log(3.)
    assert abs(rho(target,a,b,r)-1)<1e-12
    assert rho(.2,a,b,r)>1 and rho(2,a,b,r)<1
    for n in (2,5,10,30,60):
        initial=(target,(2*n+1)*np.pi/target)
        sol=root(lambda v:(ambiguity(v[0],v[1],a,b,r).real,
                           ambiguity(v[0],v[1],a,b,r).imag),initial,tol=1e-10)
        residual=abs(ambiguity(*sol.x,a,b,r))
        print('n=%d delay=%.12f omega=%.12f residual=%.3e'%(n,*sol.x,residual))
        assert sol.success and residual<1e-12 and abs(sol.x[0]-target)<.1
    for r in (2.,2.5,3.,4.):
        assert all(rho(T,a,b,r)>1 for T in (.01,.3,1.,3.))
    print('finite analytical-identity and numerical checks passed')
