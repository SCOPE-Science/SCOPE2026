"""Standalone finite-size checks for classical planar/Heisenberg ring susceptibilities.
Uses only standard NumPy/SciPy. Run: python odd_ring_susceptibility_check.py
"""
import numpy as np
from scipy.optimize import minimize


def xy_energy_and_gradient(a,n,J,h):
    diff=np.roll(a,-1)-a
    E=J*np.cos(diff).sum()-h*np.cos(a).sum()
    # derivative from (i-1,i) cos(theta_i-theta_{i-1}) and (i,i+1) cos(theta_{i+1}-theta_i)
    grad=J*(np.sin(diff)-np.roll(np.sin(diff),1))+h*np.sin(a)
    return float(E),grad


def test():
    checks=0
    for n in (3,5,7,9,11):
        k=(n-1)//2
        q=2*np.pi*k/n
        c=np.cos(np.pi/n)
        lam=2*(1+c)
        basis=np.sin(q*np.arange(n)+0.371)
        L=2*np.eye(n)-np.roll(np.eye(n),1,axis=0)-np.roll(np.eye(n),-1,axis=0)
        assert np.max(np.abs(L@basis-lam*basis))<3e-13
        assert abs(basis@basis-n/2)<2e-13
        checks+=2
        chi_xy=n/(4*c*(1+c))
        chi_hei=n/(2*(1+c))
        assert abs(chi_xy/chi_hei-1/(2*c))<1e-13
        checks+=1
        for J in (0.7,1,2.3):
            chi=chi_xy/J
            for h in (.002,.005,.01):
                # Optimize over the complete N-dimensional XY angular torus.
                best=float('inf')
                for shift in (0.2, 0.8, 1.7):
                    x=q*np.arange(n)+shift-h*np.sin(q*np.arange(n)+shift)/(J*c*lam)
                    sol=minimize(lambda y: xy_energy_and_gradient(y,n,J,h),x,jac=True,
                         method='BFGS',options={'gtol':1e-10,'maxiter':600})
                    best=min(best,sol.fun)
                    if np.linalg.norm(xy_energy_and_gradient(sol.x,n,J,h)[1])>2e-5:
                        raise AssertionError('stationarity')
                E0=-n*J*c
                observed=-2*(best-E0)/(h*h)
                assert abs(observed/chi-1)<.02,(n,J,h,chi,observed)
                checks+=1
    assert abs(1/(2*np.cos(np.pi/5))-(np.sqrt(5)-1)/2)<1e-13
    checks+=1
    print('PASS',checks,'checks (Fourier, ratios, direct nonlinear minimizations)')

if __name__=='__main__':
    test()

# Additional sharp global checks; these are corroboration, not substitutes for proof.
def global_gap_checks():
    checks=0
    for n in (5,7,9):
        c=np.cos(np.pi/n)
        J=1.0
        hsat=2*J*(1+c)
        q=2*np.pi*((n-1)//2)/n
        for f in (.08,.2,.5,.8):
            h=f*hsat
            candidates=[]
            for shift in (0.15,1.2,2.7):
                a=q*np.arange(n)+shift
                opt=minimize(lambda x:xy_energy_and_gradient(x,n,J,h),a,jac=True,method='BFGS',options={'gtol':1e-10,'maxiter':700})
                candidates.append(opt.fun)
            heis=-n*J*c-n*h*h/(4*J*(1+c))
            assert min(candidates)>heis+1e-8,(n,h,min(candidates),heis)
            checks+=1
    for n in (4,6,8,10):
        J=1.0
        for h in (0.,.17,1.0,3.,4.,6.):
            u=min(h/4,1.)
            # Alternating transverse components and a longitudinal field projection.
            phases=np.arctan2(np.where(np.arange(n)%2==0,1.,-1.)*np.sqrt(1-u*u),u)
            actual=xy_energy_and_gradient(phases,n,J,h)[0]
            optimal=-n*J-n*h*h/(8*J) if h<=4*J else n*J-n*h
            assert abs(actual-optimal)<5e-12,(n,h,actual,optimal)
            checks+=1
    print('PASS',checks,'global gap and equality checks')

if __name__=='__main__':
    global_gap_checks()
