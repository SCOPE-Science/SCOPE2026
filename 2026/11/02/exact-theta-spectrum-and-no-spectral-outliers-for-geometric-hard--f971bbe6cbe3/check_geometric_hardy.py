"""Independent finite-matrix checks for geometric Hardy-kernel spectrum.
Requires Python 3, numpy, and mpmath. Finite tests do not certify the operator theorem.
"""
import numpy as np
import mpmath as mp

checks = 0

def verify(statement, message):
    global checks
    assert statement, message
    checks += 1

for q in (0.08, 0.2, 0.4):
    t = mp.sqrt(mp.mpf(str(q)))
    low = float(mp.jtheta(4, 0, t)**2)
    high = float(mp.jtheta(3, 0, t)**2)
    L = -np.log(q)
    h_fourier_plus = 1 + 2 * sum(1 / np.cosh(k*L/2) for k in range(1, 100))
    h_fourier_minus = 1 + 2 * sum((-1)**k / np.cosh(k*L/2) for k in range(1, 100))
    verify(abs(h_fourier_plus - high) < 2e-12, (q, 'Fourier maximum'))
    verify(abs(h_fourier_minus - low) < 2e-12, (q, 'Fourier minimum'))
    for c in (0.25, 1.0, 1.85):
        for N in (8, 22, 58):
            x = c * q**np.arange(N)
            r = 1-x
            s = np.sqrt(x*(2-x))
            G = s[:,None] * s[None,:] / (x[:,None]+x[None,:]-x[:,None]*x[None,:])
            H = 2*np.sqrt(x[:,None]*x[None,:])/(x[:,None]+x[None,:])
            t_x = 1/x-0.5
            J = 1/(t_x[:,None]+t_x[None,:])
            d = np.sqrt(1-x/2)
            R = d[:,None]*d[None,:]*(1+J)
            G_from_factor = (d[:,None]*d[None,:])*H*(1+J)
            verify(np.max(np.abs(G-G_from_factor))<2e-11, (q,c,N,'factorization'))
            verify(np.max(np.abs(np.diag(R)-1))<2e-13, (q,c,N,'correlation diagonal'))
            verify(np.linalg.eigvalsh(R)[0]>-1e-11, (q,c,N,'correlation positivity'))
            evals=np.linalg.eigvalsh(G)
            verify(evals[0]>=low-2e-10 and evals[-1]<=high+2e-10,(q,c,N,'theta bounds',evals[0],evals[-1],low,high))
            verify(np.linalg.eigvalsh(J)[0]>-1e-10,(q,c,N,'Cauchy positivity'))
            verify(np.max(np.abs(np.diag(G)-1))<1e-12,(q,c,N,'normalization'))
print('PASS:',checks,'finite assertions')
