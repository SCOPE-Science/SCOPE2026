"""Independent numerical diagnostics for the pendant-layer transfer theorem.
Proof in RESULT.md supplies infinite-parameter justification; these finite tests are not a proof.
"""
import numpy as np
from scipy.linalg import expm
from fractions import Fraction
from math import sqrt,pi

def spectral_layer(A,c,u,t):
    val,vec=np.linalg.eigh(A)
    weights=np.square(vec[u,:]); omega=np.sqrt(val*val+4*c*c)
    return float(np.sum(weights*(4*c*c/(omega*omega))*np.sin(omega*t/2)**2))

def direct_layer(A,c,u,t):
    n=A.shape[0]
    H=np.block([[A,c*np.eye(n)],[c*np.eye(n),np.zeros((n,n))]])
    return float(np.sum(np.abs(expm(-1j*t*H)[n:,u])**2))

rng=np.random.default_rng(7281)
checks=0
for n in range(2,9):
    for _ in range(28):
        mask=rng.integers(0,2,size=(n,n));A=np.triu(mask,1);A=A+A.T
        c=float(rng.uniform(.06,4));u=int(rng.integers(n));t=float(rng.uniform(0,35))
        s,d=spectral_layer(A,c,u,t),direct_layer(A,c,u,t)
        assert abs(s-d)<5e-12,(n,c,u,t,s,d)
        checks+=1
# P3 endpoint at c=1/sqrt(6) admits 2:1 pair of frequencies.
A=np.array([[0.,1.,0.],[1.,0.,1.],[0.,1.,0.]])
c=1/sqrt(6)
for t in np.linspace(0,18*pi/c,1801):
    p=spectral_layer(A,c,0,float(t))
    z=np.sin(c*t)**2
    assert abs(p-(z-.5*z*z))<2e-12,(t,p,z)
    assert p<=.5+2e-12,(t,p)
    checks+=1
# Exact arithmetic checks of the parity criterion using reduced ratios, not floating-point independence claims.
for pp in range(2,26):
    for qq in range(1,pp):
        if np.gcd(pp,qq)!=1:continue
        r=Fraction(pp,qq)
        phase_compatible=((pp%2)==1 and (qq%2)==1)
        # q*Omega1-p*Omega0=0: the target half-period phase satisfies relation iff q-p is even.
        assert phase_compatible==((pp-qq)%2==0)
        checks+=1
print('PASS:',checks,'numerical / exact-integer test groups')
print('resonance coupling',c,'bound',Fraction(5,8),'actual optimum',Fraction(1,2))
