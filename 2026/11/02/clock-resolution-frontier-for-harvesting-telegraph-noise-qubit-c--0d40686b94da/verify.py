#!/usr/bin/env python3
"""Independent checks for Gaussian pulse-clock sensitivity in stationary RTN dephasing.
Usage: python verify.py
This is finite numerical corroboration, not a substitute for the analytic proof.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.special import roots_hermitenorm
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

RNG = np.random.default_rng(20261031)
N_CHECKS = 0

def close(a,b,tol=1e-10):
    global N_CHECKS
    assert abs(a-b) < tol, (a,b,tol)
    N_CHECKS += 1

def factor(t,xi,nu):
    delta=math.sqrt(4*nu*nu-xi*xi)
    return math.exp(-xi*t)*(math.cos(delta*t)+xi/delta*math.sin(delta*t))

def from_noise_generator(t,eps,xi,nu):
    # Weighted conditional (1,0) coherences of the two-state telegraph chain.
    mat=np.array([[1j*2*(eps+nu)-xi,xi],
                  [xi,1j*2*(eps-nu)-xi]],dtype=complex)
    return sum(expm(mat*t)@np.array([.25,.25]))

def peak(xi,omega):
    t=math.atan(omega/xi)/omega
    return t,math.exp(-xi*t)*omega/math.hypot(xi,omega)

def gh_avg(xi,nu,omega,x,sigma,feedback=False,n=140):
    z,weights=roots_hermitenorm(n)
    t=np.maximum(0.0,x+sigma*z)
    delta=math.sqrt(4*nu*nu-xi*xi)
    vals=np.exp(-xi*t)*(np.cos(delta*t)+(xi/delta)*np.sin(delta*t))*np.sin(omega*t)
    if feedback: vals=np.abs(vals)
    return np.dot(weights,vals)/math.sqrt(2*math.pi)

def nearest_clock_time(xi,nu,omega,phase=0.0):
    d=math.sqrt(4*nu*nu-xi*xi)
    shift=math.atan(xi/d)
    tx,H=peak(xi,omega)
    k=round((d*tx-shift-phase)/math.pi)
    return (shift+phase+k*math.pi)/d

def b_series(s):
    if s==0:return 1.0
    phis=np.linspace(0,math.pi,2001)
    val=np.full(len(phis),2/math.pi)
    for k in range(1,1000):
        a=(4/math.pi)*((-1)**(k-1))/(4*k*k-1)*math.exp(-2*k*k*s*s)
        val+=a*np.cos(2*k*phis)
        if abs(a)<1e-16 and k>20:break
    return float(val.max())

# Exact telegraph chain independent of the closed-form dephasing equation.
for _ in range(130):
    eps=RNG.uniform(.12,1.75)
    xi=RNG.uniform(.08,2.)
    nu=RNG.uniform(xi*.6+0.05,xi*.6+6.)
    t=RNG.uniform(0,5)
    v=from_noise_generator(t,eps,xi,nu)
    expected=.5*complex(math.cos(2*eps*t),math.sin(2*eps*t))*factor(t,xi,nu)
    close(v,expected,1e-12)
    # The x-pulse rotates the pre-pulse Bloch y coordinate into conserved z.
    theta=RNG.uniform(-math.pi/2,math.pi/2)
    rho=np.array([[.5,np.conj(v)],[v,.5]],dtype=complex)
    sx=np.array([[0.,1.],[1.,0.]])
    U=math.cos(theta)*np.eye(2)-1j*math.sin(theta)*sx
    post=U@rho@U.conj().T
    close((post[0,0]-post[1,1]).real, 2*v.imag*math.sin(2*theta),1e-12)

# Basic Gaussian convolution is independent of analytic reduction.
for _ in range(110):
    xi=RNG.uniform(.15,1.3); nu=RNG.uniform(3,14)
    omega=RNG.uniform(.4,2.5); x=RNG.uniform(.4,2.8)
    sigma=RNG.uniform(0,.085)
    v=gh_avg(xi,nu,omega,x,sigma)
    delta=math.sqrt(4*nu*nu-xi*xi)
    R=math.hypot(1,xi/delta); shift=math.atan(xi/delta)
    smooth=math.exp(-xi*x)*math.sin(omega*x)
    approx=R*math.exp(-.5*(delta*sigma)**2)*smooth*math.cos(delta*x-shift)
    lipschitz=math.hypot(xi,omega)
    assert abs(v-approx)<=R*lipschitz*sigma*math.sqrt(2/math.pi)+1e-11
    N_CHECKS+=1

# The exact first-lobe global envelope is attained asymptotically by dense RTN revivals.
for xi,omega in [(0.3,1.4),(.8,.6),(1.2,2.3)]:
    tH,H=peak(xi,omega)
    for nu in [12,25,55,110,225]:
        delta=math.sqrt(4*nu*nu-xi*xi)
        t0=nearest_clock_time(xi,nu,omega)
        actual=abs(factor(t0,xi,nu)*math.sin(omega*t0))
        assert actual<=math.hypot(1,xi/delta)*H+1e-11
        assert H-actual<1.0/delta**2 * (xi*xi+omega*omega)*H*3+H*xi*xi/delta**2+1e-10
        N_CHECKS+=2

# The critical clock-width profile: the Gaussian convolution and its informed counterpart.
for xi,omega in [(.3,1.4),(.7,1.8),(1.1,.65)]:
    tH,H=peak(xi,omega)
    for nu in [45,90,180]:
        delta=math.sqrt(4*nu*nu-xi*xi)
        for a in [0.,.15,.35,.6]:
            sigma=a/nu
            t0=nearest_clock_time(xi,nu,omega)
            blind=abs(gh_avg(xi,nu,omega,t0,sigma,n=200))
            target=H*math.exp(-2*a*a)
            assert abs(blind-target) < .12/nu +.012, (xi,omega,nu,a,blind,target)
            N_CHECKS+=1
            # Timed feedback may choose the sign of the pulse independently each shot.
            informed=gh_avg(xi,nu,omega,t0,sigma,feedback=True,n=200)
            assert informed+2e-11 >= blind
            N_CHECKS+=1
            if a==0:close(informed,blind,1e-10)

# Exact Fourier coefficients for the periodic sign-alignment factor.
for s in [.1,.3,.6,1.0,2.0,3.0]:
    b=b_series(s)
    assert b>=math.exp(-s*s/2)-1e-14
    if s>=.3: assert b>math.exp(-s*s/2)+1e-10
    assert b<=1+1e-10
    N_CHECKS+=2
    # Gauss-weighted integration at the reference phase, numerically independent of series.
    test=quad(lambda z:math.exp(-z*z/2)/math.sqrt(2*math.pi)*abs(math.cos(s*z)),-12,12,
              epsabs=2e-11,limit=500)[0]
    assert b+1e-6>=test
    N_CHECKS+=1

# Direct long-time output from a propagated pair of weighted density matrices.
# The z-component is unaffected by the later dephasing, even though the
# off-diagonal components retain conditional correlations until relaxation.
for _ in range(60):
    eps=RNG.uniform(.2,1.5);xi=RNG.uniform(.2,1.4);nu=RNG.uniform(xi,3.5)
    t=RNG.uniform(.1,2.);theta=RNG.uniform(-.7,.7)
    # Conditional off-diagonals computed independently above.
    pre=from_noise_generator(t,eps,xi,nu)
    z=2*pre.imag*math.sin(2*theta)
    close(z, factor(t,xi,nu)*math.sin(2*eps*t)*math.sin(2*theta),1e-11)

print('PASS',N_CHECKS,'deterministic numerical and algebraic cross-checks')
