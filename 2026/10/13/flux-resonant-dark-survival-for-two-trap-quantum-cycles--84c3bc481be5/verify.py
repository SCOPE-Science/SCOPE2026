"""Independent matrix and Fourier checks of two-sink magnetic-cycle trapping."""
import math
import numpy as np
from scipy.linalg import null_space


def predicted(n, d, alpha):
    g = math.gcd(n, 2*d)
    h = math.gcd(n, d)
    out = np.zeros(n)
    if alpha == 0:
        m = (g-1)//2
        for j in range(n):
            if (2*j) % g != 0:
                out[j] = g/(2*n)
        return m, out
    if alpha == 0.5 and (n//h) % 2:
        m = h//2
        for j in range(n):
            if n%2:
                out[j] = h/(2*n) if j%h else 0
            else:
                if j%h == 0:
                    out[j] = 0
                elif j%h == h//2:
                    out[j] = h/n
                else:
                    out[j] = h/(2*n)
        return m, out
    return 0, out


def independent_spectral_projector(n, d, alpha):
    phase = np.exp(-2j*np.pi*alpha/n)
    H = np.zeros((n,n), dtype=complex)
    for j in range(n):
        H[(j+1)%n, j] += phase
        H[j,(j+1)%n] += phase.conjugate()
    eig, U = np.linalg.eigh(H)
    projector = np.zeros((n,n),complex)
    i = 0
    while i<n:
        k = i+1
        while k<n and abs(eig[k]-eig[i])<1e-8:
            k+=1
        B=U[:,i:k]
        W=null_space(B[[0,d],:],rcond=1e-8)
        V=B@W
        projector += V@V.conj().T
        i=k
    return projector


def main():
    c=0
    for n in range(3,25):
        for d in range(1,n):
            for a in [0.,0.5,0.113]:
                m,prob=predicted(n,d,a)
                P=independent_spectral_projector(n,d,a)
                assert abs(P.trace().real-m)<2e-8, (n,d,a,m,P.trace())
                assert np.max(abs(P.diagonal().real-prob))<2e-8, (n,d,a,prob,P.diagonal())
                assert abs(prob[0])<1e-10 and abs(prob[d])<1e-10
                assert abs(sum(prob)-m)<1e-8
                c+=1
    # Genuine non-Hermitian semigroup checks at finite but sufficiently large time.
    from scipy.linalg import expm
    samples=[(9,3,0.,1,.6,1.7),(9,3,.5,1,1.3,.8),
             (12,4,.5,2,.9,1.4),(12,3,0.,1,1.,1.),
             (12,6,.5,1,1.2,.7),(11,3,.31,2,1.5,.9),
             (15,5,.5,7,1.,1.)]
    for n,d,a,j,g0,gd in samples:
        phase = np.exp(-2j*np.pi*a/n)
        H=np.zeros((n,n),complex)
        for k in range(n):
            H[(k+1)%n,k]+=phase
            H[k,(k+1)%n]+=phase.conjugate()
        D=np.zeros((n,n));D[0,0]=g0;D[d,d]=gd
        amp=expm(-1j*(H-1j*D)*500.)[:,j]
        measured=np.vdot(amp,amp).real
        target=predicted(n,d,a)[1][j]
        assert abs(measured-target)<3e-6, (n,d,a,j,measured,target)
    print('VERIFY_OK independent_eigenspaces=',c,
          'matrix_semigroups=',len(samples),'trapping_formula=passed')

if __name__=='__main__': main()
