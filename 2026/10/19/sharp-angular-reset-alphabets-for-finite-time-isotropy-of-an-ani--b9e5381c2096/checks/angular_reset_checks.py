#!/usr/bin/env python3
"""Standalone moment checks for a passive anisotropic colloid with angular resetting.
Dependencies: Python 3.10+, NumPy, SciPy. All comparisons use finite truncation-free moment ODEs.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp

DROT = .4
RATE = 1.1
D0 = 1.8
DELTA = .7


def harmonics(angles, weights, m):
    return {n: sum(float(w) * np.exp(2j * n * a) for a, w in zip(angles, weights)) for n in range(-m, m+1)}


def moments(angle, t, angles, weights, order=3):
    """Exact closed-system ODE for E[(integral_0^t cos(2(theta_s-angle)) ds)^j]."""
    mu = harmonics(angles, weights, order)
    pi = {n: RATE / (RATE + 4 * DROT * n*n) * mu[n] for n in mu}
    ind = [(j, n) for j in range(order+1) for n in range(-order+j, order-j+1)]
    ix = {v: i for i, v in enumerate(ind)}
    init = np.array([pi[n] if j == 0 else 0 for j, n in ind], dtype=np.complex128)
    def ode(_, U):
        out = np.empty_like(U)
        for j, n in ind:
            val = -(RATE + 4*DROT*n*n)*U[ix[(j,n)]] + RATE*mu[n]*U[ix[(j,0)]]
            if j:
                val += .5*j*(np.exp(-2j*angle)*U[ix[(j-1,n+1)]] + np.exp(2j*angle)*U[ix[(j-1,n-1)]])
            out[ix[(j,n)]] = val
        return out
    sol = solve_ivp(ode,(0,t),init,rtol=2e-12,atol=2e-13,method='DOP853')
    assert sol.success
    ans=[]
    for k in range(1,order+1):
        val = sum(math.comb(k,j)*(D0*t)**(k-j)*DELTA**j * sol.y[ix[(j,0)],-1] for j in range(k+1))
        ans.append(float((math.factorial(2*k) / (2**k*math.factorial(k))) * 2**k * val.real))
    return ans


def H(t):
    w=RATE+4*DROT
    return t/w + np.expm1(-w*t)/w**2


def test():
    checks=0
    angles2=[0,math.pi/2]; w2=[.5,.5]
    angles3=[.23+j*math.pi/3 for j in range(3)]; w3=[1/3]*3
    angles4=[.05+j*math.pi/4 for j in range(4)]; w4=[.25]*4
    for aa, ww, maxj in [(angles2,w2,1),(angles3,w3,2),(angles4,w4,3)]:
        mu=harmonics(aa,ww,3)
        for j in range(1,maxj+1):
            assert abs(mu[j])<2e-14; checks+=1
        for t in [.1,.5,1.2,3.]:
            vals=[moments(phi,t,aa,ww,order=3) for phi in np.linspace(0,math.pi,9,endpoint=False)]
            for k in range(maxj):
                assert max(abs(x[k]-vals[0][k]) for x in vals)<2e-9;checks+=1
    # The second cumulant is isotropic but fourth is not for the two-axis protocol.
    for t in [.15,.8,2.]:
        for phi in [0.,.21,math.pi/4,.7]:
            m2,m4,_=moments(phi,t,angles2,w2)
            zeta=RATE/(RATE+16*DROT)
            predicted=12*DELTA**2*H(t)*(1+zeta*math.cos(4*phi))
            actual=m4-3*m2*m2
            assert abs(predicted-actual)<2e-9,(t,phi,predicted,actual)
            checks+=1
    # Every three-axis isotropic fourth cumulant remains strictly positive and non-Gaussian.
    for t in [.15,.8,2.]:
        for phi in [0.,.28,.63]:
            m2,m4,_=moments(phi,t,angles3,w3)
            assert abs(m4-3*m2*m2-12*DELTA**2*H(t))<2e-9
            assert m4-3*m2*m2>0
            checks+=2
    # Sixth moments expose the hidden three-axis anisotropy at small time.
    phi0=angles3[0]
    t=.004
    sixth1=moments(phi0,t,angles3,w3)[2]
    sixth2=moments(phi0+math.pi/6,t,angles3,w3)[2]
    predicted_difference=60*DELTA**3*(RATE/(RATE+36*DROT))*t**3
    assert abs((sixth1-sixth2)/predicted_difference-1)<.045,(sixth1-sixth2,predicted_difference)
    checks+=1
    # Algebraic zero-moment and sharp support checks.
    for m in range(1,8):
        ang=np.array([.17+j*math.pi/(m+1) for j in range(m+1)])
        mu=harmonics(ang,[1/(m+1)]*(m+1),m+1)
        assert all(abs(mu[j])<1e-13 for j in range(1,m+1))
        assert abs(abs(mu[m+1])-1)<1e-13
        checks+=m+1
        # Gram matrix is the identity; a measure with fewer than m+1 atoms cannot factor it.
        V=np.array([[np.exp(2j*k*x)/math.sqrt(m+1) for x in ang] for k in range(m+1)])
        assert np.max(abs(V@V.conj().T-np.eye(m+1)))<1e-12
        checks+=1
    print(f'PASS: {checks} independent numerical/algebraic assertions')
    print('two-axis fourth cumulant at t=1: ', moments(0,1,angles2,w2)[1]-3*moments(0,1,angles2,w2)[0]**2)
    print('three-axis fourth cumulant at t=1:', moments(0,1,angles3,w3)[1]-3*moments(0,1,angles3,w3)[0]**2)
    print('three-axis sixth directional difference at t=.004:',sixth1-sixth2)

if __name__=='__main__':test()
