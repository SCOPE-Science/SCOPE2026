"""Reproducibility checks for a conditionally reset nearest-neighbour quantum walk.

Requires numpy and scipy. All rates in the calculations have inverse-time units.
The mathematical proof uses renewal theory; these finite checks are corroborative.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import jv
from scipy import sparse
from scipy.sparse.linalg import expm_multiply


def sign_memory_kernel(R, t, gamma):
    z = gamma * t
    return float(jv(0, z)**2 + 2*sum(jv(j,z)**2 for j in range(1,R)) + jv(R,z)**2)


def laplace_kernel(R, q, gamma):
    # Equivalent to a convergent Laplace transform of a positive Bessel-square sum.
    return quad(lambda t: math.exp(-q*t)*sign_memory_kernel(R,t,gamma),
                0., np.inf, epsabs=2e-10, epsrel=2e-10, limit=450)[0]


def rate_and_amplitude(R, rate, gamma):
    q = brentq(lambda x: rate*laplace_kernel(R,x,gamma)-1.,
               1e-7*min(rate,gamma),rate, xtol=3e-13)
    mu = rate * quad(lambda t: t*math.exp(-q*t)*sign_memory_kernel(R,t,gamma),
                     0.,np.inf,epsabs=2e-9,epsrel=2e-9,limit=450)[0]
    return q, rate-q, 1./(rate*mu)


def renewal_grid(R, rate, gamma, T, dt):
    n = int(round(T/dt))
    times = np.arange(n+1)*dt
    c = np.array([sign_memory_kernel(R,t,gamma) for t in times])
    k = rate * np.exp(-rate*times) * c
    forcing = np.exp(-rate*times) * c
    f = np.empty(n+1)
    f[0] = 1.
    for i in range(1,n+1):
        total = dt*(np.dot(k[1:i],f[i-1:0:-1])+0.5*k[i]*f[0])
        f[i] = (forcing[i]+total)/(1.-dt*k[0]/2.)
    return f


def lindblad_sign(R, rate, gamma, t, L=16):
    """Independent finite-lattice jump-generator calculation, no renewal series."""
    ns=np.arange(-L,L+1); N=len(ns)
    H=sparse.diags([-gamma/2*np.ones(N-1),-gamma/2*np.ones(N-1)],
                   offsets=[-1,1],format='csr',dtype=complex)
    eye=sparse.eye(N,format='csr',dtype=complex)
    unit=sparse.eye(N*N,format='csr',dtype=complex)
    term=-1j*(sparse.kron(eye,H)-sparse.kron(H.T,eye))
    entries=[]; rows=[]; cols=[]
    for j,m in enumerate(ns):
        p_plus=1. if m>0 else (0.5 if m==0 else 0.)
        p_minus=1.-p_plus
        for r,p in ((R,p_plus),(-R,p_minus)):
            if p:
                ii=int(r+L); rows.append(ii+ii*N); cols.append(j+j*N); entries.append(p)
    T=sparse.coo_matrix((entries,(rows,cols)),shape=(N*N,N*N),dtype=complex).tocsr()
    G=term+rate*(T-unit)
    initial=np.zeros(N*N,dtype=complex)
    ii=R+L; initial[ii+ii*N]=1.
    rhovec=expm_multiply(G*t,initial)
    diag=np.asarray([rhovec[j+j*N] for j in range(N)])
    assert abs(np.sum(diag)-1.)<4e-9
    assert np.min(diag.real)>-2e-9
    return float(np.sum(diag[ns>0]).real-np.sum(diag[ns<0]).real)


def main():
    tests=0
    for R in [1,2,3,4]:
        for t in [0.12,0.5,1.5,3.,8.]:
            # Direct sum over evolved quantum-walk site occupations.
            z=1.3*t
            m=np.arange(-150,151)
            direct=float(np.sum(np.sign(m)*jv(m-R,z)**2))
            compact=sign_memory_kernel(R,t,1.3)
            assert abs(direct-compact)<3e-12,(R,t,direct,compact)
            tests+=1
    for R in [1,2,3]:
        for t in [0.2,1.,5.,30.]:
            assert 0 < sign_memory_kernel(R,t,1.) < 1.
            tests+=1
    for rate in [0.5,1.,2.,5.,10.,20.]:
        vals=[]
        for R in [1,2,3]:
            q,delta,prefactor=rate_and_amplitude(R,rate,1.)
            assert 0<q<rate and 0<delta<rate and prefactor>0
            assert abs(rate*laplace_kernel(R,q,1.)-1.)<2e-8
            vals.append(delta)
            tests+=2
        assert vals[0]>vals[1]>vals[2]
        tests+=1
    for R,T in [(1,30.),(2,65.)]:
        _,delta,A=rate_and_amplitude(R,1.,1.)
        for dt in [0.04,0.02,0.01]:
            f=renewal_grid(R,1.,1.,T,dt)
            assert abs(f[-1]*math.exp(delta*T)/A-1.)<0.015
            tests+=1
        # Independent time-continuous Lindblad generator vs renewal quadrature.
        f=renewal_grid(R,1.,1.,6.,0.01)
        master=lindblad_sign(R,1.,1.,6.,L=16)
        assert abs(f[-1]-master)<1.3e-4,(R,f[-1],master)
        tests+=1
    for R in [1,2,3]:
        leading=math.comb(2*R,R)/(4**R)
        _,delta,_=rate_and_amplitude(R,20.,1.)
        approx=leading*20.**(1-2*R)
        assert abs(delta/approx-1.)<0.025
        tests+=1
    print(f'PASS: {tests} finite consistency checks; analytic proof required for all asymptotic assertions.')
    for R in [1,2,3]:
        q,d,A=rate_and_amplitude(R,1.,1.)
        print(f'R={R}, lambda=gamma=1: q={q:.12f}, decay={d:.12f}, prefactor={A:.12f}')

if __name__=='__main__': main()
