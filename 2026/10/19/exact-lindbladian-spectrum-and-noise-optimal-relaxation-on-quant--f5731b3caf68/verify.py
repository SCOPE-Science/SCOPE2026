"""Standalone consistency checks for the adjacency-star site-dephasing spectrum."""
import numpy as np
from scipy.linalg import eigvals
from numpy.polynomial.polynomial import polymul

def generator(n,g,gamma):
    dim=n+1
    H=np.zeros((dim,dim),complex)
    H[0,1:]=g
    H[1:,0]=g
    eye=np.eye(dim)
    A=-1j*(np.kron(eye,H)-np.kron(H.T,eye))
    d=np.fromfunction(lambda r,c: (r!=c).astype(float),(dim,dim))
    A-=gamma*np.diag(d.flatten(order='F'))
    return A

def predicted_roots(n,g,gamma):
    pT=np.roots([1,2*gamma,gamma**2+4*n*g*g,2*(n+1)*gamma*g*g])
    pS=np.roots([1,2*gamma,gamma**2+n*g*g,2*gamma*g*g])
    return np.r_[0, [-gamma]*(n*n-3*n+2),pT,np.tile(np.r_[-gamma+1j*np.sqrt(n)*g,-gamma-1j*np.sqrt(n)*g,pS],n-1)]

def gap_formula(n,g,gamma):
    # root between 0 and 2 gamma/n
    from scipy.optimize import brentq
    return brentq(lambda s:s*((gamma-s)**2+n*g*g)-2*gamma*g*g,0,2*gamma/n,xtol=1e-13)

cases=0
maxerror=0
for n in range(3,8):
    for g in (0.3,1.7):
        for gamma in (0.11,0.8,2.3,8.0):
            actual=eigvals(generator(n,g,gamma)); expect=predicted_roots(n,g,gamma)
            assert len(actual)==len(expect)==(n+1)**2
            from scipy.optimize import linear_sum_assignment
            row,col=linear_sum_assignment(abs(actual[:,None]-expect[None,:]))
            err=max(abs(actual[row]-expect[col])); maxerror=max(maxerror,err)
            assert err <1e-8,(n,g,gamma,err)
            gap=min(-z.real for z in actual if abs(z)>1e-8)
            s=gap_formula(n,g,gamma)
            assert abs(gap-s)<1e-8,(n,g,gamma,gap,s)
            cases+=1
opt_cases=0
for n in range(3,36):
    g=1.3
    gam_opt=(n-1)*g/np.sqrt(n-2); predicted=g/np.sqrt(n-2)
    s=gap_formula(n,g,gam_opt)
    assert abs(s-predicted)<1e-8
    for factor in (0.3,0.6,0.9,1.1,1.4,2.2,10):
        assert gap_formula(n,g,gam_opt*factor)<predicted
        opt_cases+=1
# Independent resolvent check for a single leaf initially excited.
contrast_cases=0
for n in range(3,9):
    d=n+1
    for g,gamma in ((0.8,1.4),(-0.7,3.2),(1.4,0.3)):
        L=generator(n,g,gamma)
        rho=np.zeros((d,d),complex);rho[1,1]=1
        for z in (0.25,1.1,4.5):
            state=np.linalg.solve(z*np.eye(d*d)-L,rho.flatten(order='F')).reshape(d,d,order='F')
            observed=state[1,1]-state[2,2]
            expected=((z+gamma)**2+(n-2)*g*g)/(z*((z+gamma)**2+n*g*g)+2*gamma*g*g)
            assert abs(observed-expected)<1e-10,(n,g,gamma,z,observed,expected)
            contrast_cases+=1
print('VERIFY_OK leaf_resolvents=',contrast_cases,'dense_liouvillian_spectra=',cases,'optimization_inequalities=',opt_cases,'max_eigenvalue_matching_error=',f'{maxerror:.2e}')
