"""Independent numerical checks for a rotational Ornstein--Uhlenbeck observability theorem."""
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov


def cross_matrix(w):
    x, y, z = w
    return np.array([[0., -z, y], [z, 0., -x], [-y, x, 0.]])


def observation_matrix(normal):
    n = np.asarray(normal, dtype=float)
    n = n / np.linalg.norm(n)
    e = np.array([1., 0., 0.]) if abs(n[0]) < .9 else np.array([0., 1., 0.])
    e -= e.dot(n) * n
    e /= np.linalg.norm(e)
    f = np.cross(n, e)
    return np.stack((e, f))


def gaussian_pair_kl(F):
    I = np.eye(2)
    C = np.block([[I, F.T], [F, I]])
    R = np.block([[I, F], [F.T, I]])
    return .5 * (np.trace(np.linalg.solve(R, C)) - 4.)


def exact_pair_kl(F):
    f = (F[1, 0] - F[0, 1]) / 2.
    return 4 * f**2 * (1-np.linalg.det(F)) / np.linalg.det(np.eye(2)-F @ F.T)


def main():
    rng = np.random.default_rng(20261024)
    max_lyapunov = max_rodrigues = max_kl = max_antisym = max_alias = 0.
    for i in range(300):
        a = np.exp(rng.uniform(-2, 2))
        T = np.exp(rng.uniform(-2, 2))
        w = rng.normal(size=3)
        w *= np.exp(rng.uniform(-1, 1)) / np.linalg.norm(w)
        omega = np.linalg.norm(w)
        M = cross_matrix(w)
        A = -a * np.eye(3) + M
        covariance = solve_continuous_lyapunov(A, -2*T*np.eye(3))
        err = np.linalg.norm(covariance-(T/a)*np.eye(3),ord=np.inf)
        max_lyapunov = max(err,max_lyapunov)
        assert err < 1.e-10
        n = rng.normal(size=3)
        P = observation_matrix(n)
        n = np.cross(P[0], P[1])
        t = rng.uniform(0.05,2.0) / omega
        R = np.eye(3)+np.sin(omega*t)*M/omega+(1-np.cos(omega*t))*(M@M)/omega**2
        err = np.linalg.norm(expm(A*t)-np.exp(-a*t)*R, ord=np.inf)
        max_rodrigues = max(err,max_rodrigues)
        assert err < 1.e-12
        F = P @ expm(A*t) @ P.T
        v = np.exp(-a*t)*np.sin(omega*t)/omega*np.dot(w,n)
        antisym = .5*(F[1,0]-F[0,1])
        err = abs(antisym-v)
        max_antisym=max(max_antisym,err)
        assert err < 1.e-12
        k1=gaussian_pair_kl(F)
        k2=exact_pair_kl(F)
        err=abs(k1-k2)
        max_kl=max(max_kl,err)
        assert err < 1.e-8*(1+abs(k2)) and k2>=-1.e-12
        # The same full sampled process is reversible at every multiple of its half-turn.
        for m in (1,2,3):
            H=expm(A*m*np.pi/omega)
            err=np.linalg.norm(H-H.T,ord=np.inf)
            max_alias=max(max_alias,err)
            assert err < 1.e-10
    # A projection plane containing the rotation axis is reversible for every lag.
    for i in range(80):
        w=rng.normal(size=3)
        w=w/np.linalg.norm(w)
        n=rng.normal(size=3)
        n-=np.dot(n,w)*w
        n/=np.linalg.norm(n)
        P=observation_matrix(n)
        for t in (0.21,0.47,1.31):
            F=P@expm((-1.2*np.eye(3)+cross_matrix(w))*t)@P.T
            assert np.linalg.norm(F-F.T,ord=np.inf) < 3.e-14
    # Quantitative infinitesimal two-time irreversibility.
    for i in range(100):
        w=rng.normal(size=3)
        n=rng.normal(size=3)
        n/=np.linalg.norm(n)
        P=observation_matrix(n)
        a=0.5+rng.random()
        target=2*(np.dot(w,n))**2/a
        h=1.e-4
        F=P@expm((-a*np.eye(3)+cross_matrix(w))*h)@P.T
        estimated=exact_pair_kl(F)/h
        assert abs(target-estimated) <= .002*(1+target)
    print('PASS: 300 stationary-covariance/propagator/antisymmetry/Gaussian-KL/aliasing comparisons')
    print('PASS: 240 reversible-plane checks and 100 infinitesimal KL-rate checks')
    print('max stationary Lyapunov residual:',max_lyapunov)
    print('max Rodrigues exponential discrepancy:',max_rodrigues)
    print('max projected antisymmetry discrepancy:',max_antisym)
    print('max Gaussian-KL formula discrepancy:',max_kl)
    print('max sampled-half-turn antisymmetry discrepancy:',max_alias)
    print('Proof still requires exact Gaussian reversibility, drift, and matrix identities.')

if __name__=='__main__':
    main()
