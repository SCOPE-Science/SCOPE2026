"""Numerical cross-checks for the lossy bipartite walk's exact dwell-time law.
Requires Python 3, NumPy and SciPy; run: python check_critical_walk.py
"""
import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve_continuous_lyapunov

checks = 0
max_relative_error = 0.0

def verify(a, b, tol=1e-10):
    global checks, max_relative_error
    rel = abs(a-b)/max(1.0, abs(a), abs(b))
    max_relative_error = max(max_relative_error, rel)
    assert rel < tol, (a, b, rel)
    checks += 1

def lyapunov_survival(s, gamma, delta):
    H = np.array([[delta, s], [s, -0.5j*gamma]], dtype=complex)
    # X = integral_0^infty exp(A t) rho_0 exp(A* t) dt
    A = -1j*H
    X = solve_continuous_lyapunov(A, -np.diag([1., 0.]))
    return float(np.trace(X).real)

def exact_survival(s, gamma, delta):
    return 2/gamma + (delta*delta+gamma*gamma/4)/(gamma*s*s)

for s in (0.08, 0.25, 0.6, 1., 2.5):
    for gamma in (0.2, 1.3, 3.2):
        for delta in (-1.1, 0., 0.8):
            verify(lyapunov_survival(s, gamma, delta), exact_survival(s, gamma, delta), 2e-11)

def form_factor(k, f):
    return sum(z*np.exp(1j*j*k) for j, z in enumerate(f))

def integrated_weight(v, w, f):
    f = np.asarray(f, complex)
    return quad(lambda k: abs(form_factor(k, f))**2/abs(v+w*np.exp(1j*k))**2,
                -np.pi, np.pi, epsabs=3e-10, epsrel=3e-10, limit=250)[0]/(2*np.pi)

for v,w in ((1.,0.7),(1.4,0.4),(0.8,1.4)):
    for f in (np.array([1]), np.ones(2)/np.sqrt(2), np.array([1, -1])/np.sqrt(2)):
        I = integrated_weight(v,w,f)
        g,d = 1.3,0.8
        predicted = 2/g + (d*d+g*g/4)/g*I
        independent = 0.
        for k in (np.arange(512)+0.5)*2*np.pi/512-np.pi:
            independent += abs(form_factor(k,f))**2 * lyapunov_survival(abs(v+w*np.exp(1j*k)), g,d)/512
        verify(predicted, independent, 2e-9)

for L in range(2,25):
    length = L-1
    # Critical exact cancelling states f = (1+z)g.
    g = np.sin(np.pi*np.arange(1,L)/L)
    f = np.convolve(g,[1.,1.]); f /= np.linalg.norm(f)
    verify(form_factor(np.pi, f), 0., 2e-13)
    exact_I = 1./(4*np.cos(np.pi/(2*L))**2)
    via_norm = np.linalg.norm(g)**2/np.linalg.norm(np.convolve(g,[1.,1.]))**2
    verify(via_norm, exact_I, 2e-13)
    # The independent eigenvalue problem from the convolution operator.
    B=np.zeros((L,L-1))
    for j in range(L-1): B[j,j]=B[j+1,j]=1.
    lam = np.linalg.eigvalsh(B.conj().T@B)[-1]
    verify(lam,4*np.cos(np.pi/(2*L))**2,2e-13)
    if L <= 12:
        verify(integrated_weight(1.,1.,f),exact_I,2e-10)
    # Random cancelling envelopes always have greater inverse-coupling weight.
    for seed in range(4):
        rng=np.random.default_rng(100*L+seed)
        h=rng.normal(size=L-1)+1j*rng.normal(size=L-1)
        ff=B@h; ff/=np.linalg.norm(ff)
        I = np.linalg.norm(h)**2/np.linalg.norm(B@h)**2
        assert I+1e-12 >= exact_I
        checks += 1

# Exact two-site profile and optimal uniform loss rate.
for gamma in (0.25,1.,1.7,5.):
    delta=.73
    I=.5
    t=2/gamma + (delta*delta+gamma*gamma/4)*I/gamma
    verify(t, 2/gamma+(delta*delta+gamma*gamma/4)/(2*gamma))
I=.5
opt_gamma=2*np.sqrt(.73**2 + 2/I)
verify(2/opt_gamma+(.73**2+opt_gamma**2/4)*I/opt_gamma,
       np.sqrt(I*(2+.73**2*I)))
print('PASS: %d tests; maximum relative discrepancy %.3e' % (checks,max_relative_error))
