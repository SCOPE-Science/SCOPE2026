"""Independent finite-N checks of flux-selective two-site detection on a tight-binding cycle."""
import math
import numpy as np
from scipy.linalg import expm


def predicted(N, d, j, flux):
    if flux not in (0, 1):
        return 0, 0.0
    if flux == 0:
        g = math.gcd(N, 2*d)
        s = 1 + (N % 2 == 0)
        dim = (g-s)//2
        weight = g/(2*N) if (2*j) % g != 0 else 0.0
    else:
        g = math.gcd(N,d)
        if (N//g) % 2 == 0:
            return 0, 0.0
        if N % 2 == 1:
            dim = (g-1)//2
            weight = g/(2*N) if j % g != 0 else 0.0
        else:
            dim = g//2
            if j % g == 0:weight=0.0
            elif j % g == g//2:weight=g/N
            else:weight=g/(2*N)
    return dim, weight


def analytic_dark_vectors(N, d, flux):
    if flux not in (0,1):return np.zeros((N,0),dtype=complex)
    occupied=set()
    out=[]
    for k in range(N):
        l=(-k-flux)%N
        if l==k or k in occupied or l in occupied:continue
        occupied|={k,l}
        if ((k-l)*d)%N==0:
            j=np.arange(N)
            out.append((np.exp(2j*np.pi*k*j/N)-np.exp(2j*np.pi*l*j/N))/np.sqrt(2*N))
    return np.stack(out,axis=1) if out else np.zeros((N,0),dtype=complex)


def Hmat(N, flux, J=1.0):
    phi=flux*np.pi
    T=np.zeros((N,N),dtype=complex)
    for j in range(N):T[(j+1)%N,j]=1
    return -J*(np.exp(-1j*phi/N)*T+np.exp(1j*phi/N)*T.conj().T)

checks=0
for N in range(3,37):
    for d in range(1,N):
        for flux in (0,1):
            V=analytic_dark_vectors(N,d,flux)
            gotdim=V.shape[1]
            wantdim=predicted(N,d,0,flux)[0]
            assert gotdim==wantdim,(N,d,flux,gotdim,wantdim)
            checks+=1
            if gotdim:
                assert np.max(np.abs(V.conj().T@V-np.eye(gotdim)))<2e-13
                assert np.linalg.norm(V[[0,d],:])<2e-13
                H=Hmat(N,flux)
                assert np.max(np.abs(H@V-V*np.diag(V.conj().T@H@V)[None,:]))<2e-12
            w=np.sum(abs(V)**2,axis=1)
            for j in range(N):
                want=predicted(N,d,j,flux)[1]
                assert abs(w[j]-want)<2e-13,(N,d,j,flux,w[j],want)
                checks+=1
    for d in range(1,N):
        hasdarkany=any(predicted(N,d,0,flux)[0]>0 for flux in (0,1))
        assert hasdarkany==(math.gcd(N,d)>1), (N,d,hasdarkany)
        checks+=1

for N,d,j,flux,lam in [(4,2,1,0,0.8),(6,2,1,1,1.5),(9,3,1,1,1.0),(12,4,2,1,1.0),(6,3,1,0,1.0),(6,3,1,1,1.0),(5,2,1,0.36,1.0)]:
    H=Hmat(N,flux)
    P=np.zeros((N,N),complex)
    P[0,0]=P[d,d]=1
    A=-1j*H-lam/2*P
    ket=np.zeros(N,complex)
    ket[j]=1
    surv=np.linalg.norm(expm(300*A)@ket)**2
    expect=predicted(N,d,j,flux)[1]
    assert abs(surv-expect)<1e-8,(N,d,j,flux,surv,expect)
    checks+=1
# Generic nonresonant projective-monitoring survival, checked independently.
for N,d,j,flux in [(6,2,1,1),(6,3,1,0),(6,2,1,0),(9,3,1,1),(5,2,1,.31)]:
    H=Hmat(N,flux)
    Q=np.eye(N,dtype=complex)
    Q[0,0]=Q[d,d]=0
    Q=Q@expm(-1j*.731*H)
    psi=np.zeros(N,dtype=complex)
    psi[j]=1
    for _ in range(4000):
        psi=Q@psi
    want=predicted(N,d,j,flux)[1]
    assert abs(np.linalg.norm(psi)**2-want)<1e-8, (N,d,j,flux)
    checks+=1
print(f'PASS {checks} exact-arithmetic/Fourier, absorbing and projective evolution checks')
