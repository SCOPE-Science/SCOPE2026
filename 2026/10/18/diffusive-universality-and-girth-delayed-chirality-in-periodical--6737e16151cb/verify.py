"""Independent finite checks of magnetic-cycle dephased-walk formulas.
Run: python verify.py (requires numpy and scipy).
Finite tests corroborate, but do not prove, the all-order statements.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.special import jv

checks = 0

def channel(n, tau, flux, hop=1.):
    H = np.zeros((n, n), complex)
    ph = np.exp(1j*flux/n)
    for j in range(n):
        H[(j+1)%n,j] += hop*ph
        H[j,(j+1)%n] += hop*ph.conjugate()
    U = expm(-1j*tau*H)
    return np.abs(U)**2

def reference(n, tau, hop=1.):
    z=2*hop*tau
    return np.array([sum(jv(k,z)**2 for k in range(-180,181) if k%n==d) for d in range(n)])

for n in range(3,14):
    for flux in [0., .71, 1.57, 2.41]:
        for tau in [.06, .28, .74]:
            Q=channel(n,tau,flux)
            p=reference(n,tau)
            assert np.max(abs(Q.sum(axis=0)-1))<2e-12
            assert np.max(abs(Q[:,0]-np.roll(Q[:,1],-1)))<2e-12
            assert np.isclose(p.sum(),1,atol=2e-13)
            T=2*math.exp(tau)*tau**math.ceil(n/2)/math.factorial(math.ceil(n/2))
            B=2*math.exp(tau)-1
            delta=.5*sum(abs(Q[:,0]-p))
            assert delta < B*T+T*T+3e-12,(n,flux,tau,delta,B*T+T*T)
            asym=np.max(abs(Q-Q.T))
            assert asym<2*math.exp(4*tau)*(4*tau)**n/math.factorial(n)+1e-12
            if n%2==0 or flux==0.:
                assert asym<2e-12,(n,flux,asym)
            checks+=5

for n in (3,5,7,9):
    for flux in (.41,1.27,2.8):
        for tau in (.09,.13,.18):
            Q=channel(n,tau,flux)
            observed=Q[1,0]-Q[0,1]
            lead=4*(-1)**((n-1)//2)*np.sin(flux)*tau**n/math.factorial(n-1)
            assert abs(observed/lead-1)<.12,(n,flux,tau,observed/lead)
            checks+=1

# Diffusive-scale profile is independent of flux: test dense maps for moderate n.
def circle_heat_tv(s, hop_tau, resolution=8192):
    grid=np.arange(resolution)/resolution
    h=np.ones(resolution)
    for j in range(1,45):
        h += 2*np.exp(-4*np.pi**2*(hop_tau**2)*s*j*j)*np.cos(2*np.pi*j*grid)
    return .5*np.mean(abs(h-1))

for n in [51,101,151]:
    for flux in [0., 1.9]:
        tau=.55;s=.29;t=int(s*n*n)
        # Circulant Markov eigenvalues via column FFT. Amplify eigenvalues by t.
        Q=channel(n,tau,flux)
        eig=np.fft.fft(Q[:,0])
        dist=np.fft.ifft(eig**t).real
        tv=.5*sum(abs(dist-1/n))
        ideal=circle_heat_tv(s,tau)
        assert abs(tv-ideal)<.025,(n,flux,tv,ideal)
        checks+=1
print('VERIFY_OK',checks,'finite identities and mixing comparisons')
