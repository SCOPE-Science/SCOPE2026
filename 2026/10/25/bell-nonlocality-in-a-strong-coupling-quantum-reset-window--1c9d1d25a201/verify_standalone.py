"""Reproduce the Bell-correlation identity and scaling checks for a reset Ising pair.
Requires numpy. All parameters are dimensionless (Omega=1).
"""
import numpy as np

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.array([[1,0],[0,-1]],complex)
PAULI=(X,Y,Z)
P0=np.zeros((4,4),complex)
P0[3,3]=1

def direct_correlation(alpha,R):
    H=-alpha*np.kron(Z,Z)+(np.kron(X,I)+np.kron(I,X))/2
    en,V=np.linalg.eigh(H)
    in_eig=V.conj().T@P0@V
    # Exact Poisson age average, computed by independent spectral diagonalization.
    rho=V@(in_eig*R/(R+1j*(en[:,None]-en[None,:])))@V.conj().T
    T=np.array([[np.trace(rho@np.kron(a,b)).real for b in PAULI] for a in PAULI])
    return T,rho

def closed_correlation(alpha,R):
    h=4*alpha**2+R**2+4
    d=(1+R**2)**2+4*alpha**2*R**2
    a=-2*alpha*R/d
    b=2*alpha*R**2/d
    c=2/h
    e=1-c
    return np.array([[0,a,b],[a,c,-R/h],[b,-R/h,e]])

def bell(T):
    s=np.linalg.svd(T,compute_uv=False)
    return 2*np.hypot(s[0],s[1])

def run():
    rng=np.random.default_rng(20261024)
    checked=0
    for _ in range(400):
        alpha=10**rng.uniform(-2,2)
        R=10**rng.uniform(-2,2)
        calc,rho=direct_correlation(alpha,R)
        formula=closed_correlation(alpha,R)
        np.testing.assert_allclose(calc,formula,rtol=2e-9,atol=1e-11)
        np.testing.assert_allclose(rho,rho.conj().T,atol=1e-13)
        np.testing.assert_allclose(np.trace(rho),1,atol=1e-12)
        if np.linalg.eigvalsh(rho).min() < -1e-12:
            raise AssertionError('nonphysical state')
        checked+=1
    # Exact algebraic lower bound at the explicitly guaranteed region.
    for alpha in (2,2.1,3,5,10,20,100):
        R=1/(2*alpha)
        T=closed_correlation(alpha,R)
        assert T[2,2] >= 0.9-1e-12
        assert abs(T[0,1]) >= 256/545-1e-12
        assert T[2,2]**2+T[0,1]**2 > 1
        assert bell(T)>2
    # Singular scaling limit at fixed s=alpha*R.
    for s in (.1,.25,.5,1,2):
        limit=2*np.sqrt(1+(2*s/(1+4*s*s))**2)
        errors=[]
        for alpha in (100,300,1000):
            errors.append(abs(bell(closed_correlation(alpha,s/alpha))-limit))
        assert errors[2]<3e-5 and errors[2]<errors[1]<errors[0]
    assert abs(2*np.sqrt(1+(2*.5/(1+4*.5**2))**2)-np.sqrt(5))<1e-14
    # Rates approaching either endpoint at fixed alpha are Bell-local.
    for alpha in (0.1,0.5,1,2,3,10):
        assert bell(closed_correlation(alpha,1e-8))<2
        assert bell(closed_correlation(alpha,1e4))<2
    print(f'PASS: {checked} independent spectral-vs-rational Pauli checks; '
          'explicit finite-coupling Bell witness; 15 scaling checks; endpoint Bell locality.')
    for a in (2,3,10,100):
        print(f'alpha={a:g}, R={1/(2*a):.8g}, CHSH={bell(closed_correlation(a,1/(2*a))):.12f}')
    print('scaling supremum',np.sqrt(5))

if __name__=='__main__':run()
