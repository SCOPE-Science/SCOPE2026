"""Independent checks for stationary two-time correlations of an inertial velocity-jump oscillator.

Requires NumPy and SciPy; uses a Gaussian OU surrogate only for the two-point law.
"""
import math
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov
from scipy.integrate import quad
from scipy.optimize import brentq


def coefficients(beta, omega, k, force):
    omega0_sq = beta*beta + omega*omega
    plus = (beta+k)**2 + omega*omega
    minus = (beta-k)**2 + omega*omega
    slow = force*force/(plus*minus)
    variance = force*force*(2*beta+k)/(2*beta*omega0_sq*plus)
    cosine = variance-slow
    sine = (k*slow+beta*cosine)/omega
    amplitude = math.hypot(cosine, sine)
    return slow, cosine, sine, variance, amplitude


def covariance(t, beta, omega, k, force):
    slow, cosine, sine, _, _ = coefficients(beta, omega, k, force)
    return slow*math.exp(-k*t) + math.exp(-beta*t)*(cosine*math.cos(omega*t)+sine*math.sin(omega*t))


def matrix_covariance(t, beta, omega, k, force):
    natural_sq = beta*beta+omega*omega
    M = np.array([[0,1,0],[-natural_sq,-2*beta,force],[0,0,-k]],float)
    Q = np.diag([0.,0.,2*k])
    S = solve_continuous_lyapunov(M, -Q)
    return (expm(M*t) @ S)[0,0]


def spectral_covariance(t, beta, omega, k, force):
    natural_sq = beta*beta+omega*omega
    def f(x):
        return (2*k*force*force) / ((k*k+x*x)*((natural_sq-x*x)**2+4*beta*beta*x*x))
    # Oscillatory cosine transform is independent of the OU matrix method.
    result, error = quad(f, 0, np.inf, weight='cos', wvar=t, epsabs=4e-11, limit=600)
    return result/math.pi


def first_root(beta, omega, k, force):
    slow, cosine, sine, _, amp = coefficients(beta, omega, k, force)
    if not k>beta: raise ValueError('first_root requires k>beta')
    t_low = max(0.0, math.log(slow/amp)/(k-beta))
    t_hi = t_low + 2*math.pi/omega + 1e-8
    grid = np.linspace(0,t_hi,30000)
    values = np.array([covariance(float(t),beta,omega,k,force) for t in grid])
    crossings = np.flatnonzero(values[1:]*values[:-1]<0)
    if not len(crossings): raise AssertionError('No sign change')
    n = int(crossings[0])
    return brentq(lambda t: covariance(t,beta,omega,k,force), grid[n],grid[n+1],xtol=1e-12),t_low


def test():
    rng = np.random.default_rng(202610)
    maxerr=0.0
    for j in range(200):
        beta=float(np.exp(rng.uniform(-1,1)))
        omega=float(np.exp(rng.uniform(-1,1)))
        k=float(np.exp(rng.uniform(-1.5,1.5)))
        force=float(np.exp(rng.uniform(-1,1)))
        time=float(rng.uniform(0,5)/max(beta,k))
        a=covariance(time,beta,omega,k,force)
        b=matrix_covariance(time,beta,omega,k,force)
        err=abs(a-b)/max(1.,abs(b))
        maxerr=max(maxerr,err)
        assert err<2e-11,(j,a,b,err)
        if j<35:
            c=spectral_covariance(time,beta,omega,k,force)
            assert abs(a-c)/max(1.,abs(a))<1e-8,(j,a,c)
        A,B,H,_,R=coefficients(beta,omega,k,force)
        rexp=(k*math.sqrt(((k-beta)**2+omega*omega)*((k+beta)**2+omega*omega)) /
              (2*beta*omega*math.sqrt(beta*beta+omega*omega)))
        assert abs(R/A-rexp)<1e-10*max(1.,rexp)
    print('200 independent 3x3 Lyapunov/matrix checks and 35 spectral integrals PASSED, max relative error:', maxerr)

    beta=1.0;omega=1.0;force=1.3
    critical_amplitude=math.sqrt(omega*omega+4*beta*beta)/(2*math.sqrt(beta*beta+omega*omega))
    c=math.log(1/critical_amplitude)
    assert 0<critical_amplitude<1
    for k in [0.2,0.5,0.9,1.0]:
        vals=[covariance(float(t),beta,omega,k,force) for t in np.linspace(0,150,10000)]
        assert min(vals)>0
    print('Positive critical covariance, amplitude ratio:',critical_amplitude)
    print('Onset coefficient log(1/ratio):',c)
    for eps in [0.10,0.05,0.02,0.01,0.005]:
        first, cutoff = first_root(beta,omega,beta+eps,force)
        assert cutoff<=first<=cutoff+2*math.pi/omega + 1e-7
        assert abs(eps*first-c) < 20*eps
        near_before=covariance(first-0.001,beta,omega,beta+eps,force)
        near_after=covariance(first+0.001,beta,omega,beta+eps,force)
        assert near_before>0 and near_after<0
        print('epsilon',eps,'first reversal',round(first,10),'analytic bracket',round(cutoff,10), 'scaled',round(eps*first,10))
    for k in [1.1,1.5,3.0]:
        vals=[covariance(float(t),beta,omega,k,force) for t in np.linspace(200,250,1000)]
        assert min(vals)<0 and max(vals)>0
    print('Infinite-lag oscillation signs at large finite times PASSED')

    # Positivity lemma: for q=k/beta <=1 and x=(omega/beta)^2,
    # nonnegative sine coefficient implies squared oscillatory amplitude < slow amplitude squared.
    for j in range(500):
        bb=float(np.exp(rng.uniform(-2,2)))
        ww=float(np.exp(rng.uniform(-4,3)))
        kk=bb*float(rng.uniform(0.002,1.))
        AA,BB,HH,_,RR=coefficients(bb,ww,kk,1.)
        if HH>=0:
            assert RR/AA < 1.+2e-13
        else:
            dimensionless_exp=(bb-kk)/ww
            assert 0< -BB/AA <1
            assert 0< -HH/AA <dimensionless_exp
        for t in np.linspace(0,25/bb,70):
            assert covariance(float(t),bb,ww,kk,1.)>0
    print('500 global underdamped slow-switch parameter positivity tests PASSED')

    # Separate non-oscillatory mechanical regimes, computed without the underdamped formula.
    for mechanical_beta in [1.,1.2,2.]:
        for switching in [0.1,0.5,1.,3.,6.]:
            natural_sq=1.
            M=np.array([[0,1,0],[-natural_sq,-2*mechanical_beta,1.],[0,0,-switching]],float)
            S=solve_continuous_lyapunov(M,-np.diag([0.,0.,2*switching]))
            for t in np.linspace(0,45,95):
                val=(expm(M*t) @ S)[0,0]
                if val< -5e-15: raise AssertionError((mechanical_beta,switching,t,val))
    print('Critical and overdamped stationary covariance nonnegativity checks PASSED')

if __name__=='__main__': test()
