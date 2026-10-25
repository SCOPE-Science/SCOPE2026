"""Numerical reproducibility checks for a resonant quadratic two-mode battery."""
import numpy as np
from scipy import sparse
from scipy.integrate import solve_ivp
from scipy.linalg import expm, solve_continuous_lyapunov
from scipy.sparse.linalg import expm_multiply

J = np.kron(np.eye(2), np.array([[0., 1.], [-1., 0.]]))
PARTIAL_TRANSPOSE = np.diag([1., 1., 1., -1.])


def drift(gamma, pump, coupling):
    d = gamma / 2.
    A = np.array([[pump-d, 0, 0, coupling],
                  [0, -pump-d, -coupling, 0],
                  [0, coupling, 0, 0],
                  [-coupling, 0, 0, 0]], dtype=float)
    return A, np.diag([d, d, 0., 0.])


def limit(gamma, pump):
    d = gamma / 2.
    vp = d / (2. * (d-pump))
    vm = d / (2. * (d+pump))
    return np.diag([vp, vm, vm, vp])


def covariance(t, gamma, pump, coupling):
    A, _ = drift(gamma, pump, coupling)
    Vinf = limit(gamma, pump)
    E = expm(t*A)
    return Vinf + E @ (.5*np.eye(4)-Vinf) @ E.T


def ppt_nu(V):
    W = PARTIAL_TRANSPOSE @ V @ PARTIAL_TRANSPOSE
    vals = np.sort(np.abs(np.linalg.eigvals(1j*J @ W)))
    return float(vals[0])


def logneg(V):
    return max(0., -np.log(2.*ppt_nu(V)))


def stationary_checks():
    rng = np.random.default_rng(20231024)
    max_err = 0.
    for _ in range(96):
        gamma = rng.uniform(.65, 3.5)
        pump = rng.uniform(.06, .83) * gamma/2.
        coupling = rng.uniform(.14, 3.0)
        A, D = drift(gamma, pump, coupling)
        V = limit(gamma, pump)
        err = np.linalg.norm(A@V+V@A.T+D, ord=np.inf)
        other = solve_continuous_lyapunov(A, -D)
        residual = np.linalg.norm(other-V,ord=np.inf)
        eigmax = max(np.real(np.linalg.eigvals(A)))
        max_err=max(max_err,err,residual)
        assert err < 2.e-12 and residual < 2.e-11
        assert eigmax < 0
        assert np.max(np.abs(V[:2,2:])) == 0
        assert np.linalg.det(V[:2,:2]) > .25
        assert abs(ppt_nu(V)-np.sqrt(np.linalg.det(V[:2,:2]))) < 1.e-12
    print('96 independent stationary Lyapunov and PPT comparisons passed; max error',max_err)


def dynamic_checks():
    rng=np.random.default_rng(2023)
    for _ in range(28):
        gamma = rng.uniform(.7, 2.9)
        pump = rng.uniform(.04, .8)*gamma/2.
        coupling=rng.uniform(.3,2.3)
        A,D=drift(gamma,pump,coupling)
        for t in (.15, .75, 1.8):
            numeric=solve_ivp(lambda _,v:(A@v.reshape(4,4)+v.reshape(4,4)@A.T+D).flatten(),
                              (0.,t), (.5*np.eye(4)).flatten(),rtol=8.e-11,atol=2.e-12)
            assert numeric.success
            actual=numeric.y[:,-1].reshape(4,4)
            expected=covariance(t,gamma,pump,coupling)
            assert np.linalg.norm(actual-expected,ord=np.inf)<3.e-9
    print('84 independent time-ODE versus exact covariance comparisons passed')


def birth_and_death():
    for gamma,pump,coupling in ((2.,.2,1.),(1.,.25,.7),(.8,.12,.8),
                                (2.2,.25,1.8),(1.,.4,.25)):
        for t in (.003,.006,.012):
            nu=ppt_nu(covariance(t,gamma,pump,coupling))
            assert nu < .5
            coeff=(.5-nu)/t**2
            assert abs(coeff/(coupling*pump/2.)-1.) < .035
        A,_=drift(gamma,pump,coupling)
        rate=-max(np.real(np.linalg.eigvals(A)))
        assert rate>0
        tlate=max(100.,40./rate)
        n=ppt_nu(covariance(tlate,gamma,pump,coupling))
        d=gamma/2.
        expected=d/(2.*np.sqrt(d*d-pump*pump))
        assert abs(n-expected) < 3.e-11
        assert n > .5
        for t in (tlate,tlate*1.5,tlate*2.):
            assert logneg(covariance(t,gamma,pump,coupling))==0
    print('Short-time entanglement coefficient and eventual PPT gap passed in 5 regimes')


def independent_fock_check():
    # A finite-dimensional Hilbert-space computation, distinct from Gaussian covariance evolution.
    N=7
    gamma,pump,coupling=2.,.2,1.
    ann=sparse.diags(np.sqrt(np.arange(1,N)),1,shape=(N,N),format='csc')
    ident=sparse.eye(N,format='csc',dtype=complex)
    c=sparse.kron(ann,ident,format='csc')
    h=sparse.kron(ident,ann,format='csc')
    dim=N*N
    I=sparse.eye(dim,format='csc',dtype=complex)
    H=coupling*(c.getH()@h+h.getH()@c)+(.5j*pump)*(c.getH()@c.getH()-c@c)
    pop=c.getH()@c
    L=(-1j*(sparse.kron(I,H,format='csc')-sparse.kron(H.T,I,format='csc'))
      +gamma*(sparse.kron(c.conjugate(),c,format='csc')
              -.5*sparse.kron(I,pop,format='csc')-.5*sparse.kron(pop.T,I,format='csc')))
    init=np.zeros(dim*dim,complex)
    init[0]=1.
    diffs=[]
    for t in (.3, 1., 2.):
        state=expm_multiply(t*L,init)
        rho=state.reshape((dim,dim),order='F')
        assert abs(np.trace(rho)-1)<1.e-9
        rho_pt=rho.reshape((N,N,N,N)).transpose(0,3,2,1).reshape(dim,dim)
        vals=np.linalg.eigvalsh((rho_pt+rho_pt.conj().T)/2.)
        measured=np.log(np.sum(np.abs(vals)))
        predicted=logneg(covariance(t,gamma,pump,coupling))
        diffs.append(abs(measured-predicted))
        assert abs(measured-predicted)<5.e-5
    print('Independent truncated Fock-space Lindblad negativity comparisons passed;',
          'maximum discrepancy',max(diffs))


if __name__=='__main__':
    stationary_checks()
    dynamic_checks()
    birth_and_death()
    independent_fock_check()
    print('ALL CHECKS PASSED (finite numerical corroboration only)')
