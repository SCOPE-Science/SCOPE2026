"""Separate finite-volume checks for time-decaying radiation walls.

Requires numpy and scipy. Runs a conservative Robin-flux discretization,
which is separate from the continuum Neumann-kernel proof.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh


def shape(x, length, a_left, a_right, diffusion):
    y = x / length
    f_left = 1/3 - y + y*y/2
    f_right = -1/6 + y*y/2
    return -(a_left * f_left + a_right * f_right) / diffusion


def run_case(length=1.3, diffusion=0.75, strength=0.55,
             power=1.7, a_left=0.9, a_right=0.4,
             n=160, times=(60.0, 120.0, 240.0)):
    dx = length/n
    xx = (np.arange(n) + 0.5)*dx
    u0 = (1 + .3*np.cos(2*np.pi*xx/length) + .17*np.cos(np.pi*xx/length))/length
    u0 = u0/(np.sum(u0)*dx)
    main = np.full(n, -2*diffusion/dx**2)
    main[0] = -diffusion/dx**2
    main[-1] = -diffusion/dx**2
    off = np.full(n-1, diffusion/dx**2)
    baseline = diags([off, main, off], [-1, 0, 1], format='csr')
    def rate(t):return strength*(1+t)**(-power)
    def eff(r):return r/(1+r*dx/(2*diffusion))
    def rhs(t, u):
        z = baseline @ u
        z[0] -= eff(a_left*rate(t))*u[0]/dx
        z[-1] -= eff(a_right*rate(t))*u[-1]/dx
        return z
    ts = [0, *times]
    sol = solve_ivp(rhs, [0, max(times)], u0, method='BDF',
                    t_eval=ts, rtol=2e-10, atol=2e-12)
    assert sol.success, sol.message
    errors=[]
    for t, v in zip(sol.t[1:], sol.y.T[1:]):
        mass = dx*np.sum(v)
        assert 0 < mass <= 1+2e-9, (t,mass)
        q=v/mass
        r=rate(t)
        ratio=(q-1/length)/r
        expected=shape(xx,length,a_left,a_right,diffusion)
        max_err=np.max(abs(ratio-expected))
        # Two independent boundary fluxes, and their sum.
        fl=eff(a_left*r)*v[0]
        fr=eff(a_right*r)*v[-1]
        predicted=(a_left+a_right)*mass*r/length
        flux_ratio=(fl+fr)/predicted
        errors.append((t,mass,max_err,flux_ratio))
    return errors


if __name__=='__main__':
    cases=[(0.9,0.4,1.7), (1.0,0.0,2.2), (1.0,1.0,1.45)]
    out=[]
    for a,b,p in cases:
        z=run_case(a_left=a,a_right=b,power=p)
        print('case',a,b,p,'(t,mass,profile_error,flux_ratio)',z)
        # With 160 cells, the O(dx) boundary interpolation and O(dx^2)
        # interior errors can dominate at very late times.
        assert abs(z[-1][3]-1)<0.002
        assert z[-1][2]<0.018
        assert z[-1][2]<z[0][2]+0.012
        out.extend(z)
    print('PASSED:',len(out),'time-point checks; max late error',max(run_case(a_left=a,a_right=b,power=p)[-1][2] for a,b,p in cases))
