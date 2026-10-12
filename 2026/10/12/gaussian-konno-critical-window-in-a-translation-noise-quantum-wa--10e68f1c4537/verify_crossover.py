"""Finite-dimensional checks of the stochastic-translation quantum-walk identities.

Run: python verify_crossover.py
Requires: numpy >= 1.24.  No external data.
The weak-limit theorem is analytic; finite checks are corroboration only.
"""
import math
import numpy as np

CHECKS = 0


def check(condition, context):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(context)


def quantum_distribution(k, theta):
    """Propagate a pure two-state walk on [-k,k], without noise."""
    a = np.zeros((2, 2*k+1), dtype=complex)
    a[:, k] = [1/math.sqrt(2), 1j/math.sqrt(2)]
    c, s = math.cos(theta), math.sin(theta)
    for _ in range(k):
        z0 = c*a[0] + s*a[1]
        z1 = s*a[0] - c*a[1]
        b = np.zeros_like(a)
        b[0, 1:] = z0[:-1]
        b[1, :-1] = z1[1:]
        a = b
    return np.sum(np.abs(a)**2, axis=0)


def exact_mixture(t, theta, p):
    """Sum the independent classical-shift and pure-walk probabilities."""
    out = np.zeros(2*t+1)
    for k in range(t+1):
        weight = math.comb(t, k)*(1-p)**k*p**(t-k)
        if weight == 0:
            continue
        pure = quantum_distribution(k, theta)
        h = t-k
        for j in range(h+1):
            shift = 2*j-h
            x0 = t-k+shift
            out[x0:x0+2*k+1] += weight*math.comb(h,j)*2.0**(-h)*pure
    return out


def direct_channel(t, theta, p):
    """Iterate the full density-matrix Kraus channel, independently."""
    n = 2*t+1
    dim = 2*n
    psi = np.zeros(dim, dtype=complex)
    psi[t] = 1/math.sqrt(2)
    psi[n+t] = 1j/math.sqrt(2)
    rho = np.outer(psi, psi.conj())
    c, s = math.cos(theta), math.sin(theta)
    coin = [[c, s], [s, -c]]
    u = np.zeros((dim, dim), dtype=complex)
    right = np.zeros_like(u)
    left = np.zeros_like(u)
    for a in range(2):
        for j in range(n):
            if j < n-1:
                right[a*n+j+1, a*n+j] = 1
            if j > 0:
                left[a*n+j-1, a*n+j] = 1
            to = j+(1 if a == 0 else -1)
            if 0 <= to < n:
                for b in range(2):
                    u[a*n+to, b*n+j] = coin[a][b]
    for _ in range(t):
        rho = (1-p)*u@rho@u.conj().T + 0.5*p*(
            right@rho@right.conj().T+left@rho@left.conj().T)
    return np.real(np.diag(rho)[:n]+np.diag(rho)[n:])


def moments_up_to(kmax, theta):
    """Independent amplitude recursion for raw pure-walk moments."""
    xx = np.arange(-kmax, kmax+1, dtype=float)
    psi = np.zeros((2, 2*kmax+1), complex)
    psi[:, kmax] = [1/math.sqrt(2), 1j/math.sqrt(2)]
    m2 = np.zeros(kmax+1)
    m4 = np.zeros(kmax+1)
    c, s = math.cos(theta), math.sin(theta)
    for k in range(kmax+1):
        q = np.abs(psi[0])**2 + np.abs(psi[1])**2
        m2[k] = q@(xx**2)
        m4[k] = q@(xx**4)
        if k < kmax:
            rot0, rot1 = c*psi[0]+s*psi[1], s*psi[0]-c*psi[1]
            psi[:] = 0
            psi[0, 1:] = rot0[:-1]
            psi[1, :-1] = rot1[1:]
    return m2, m4


def poisson_binomial_weights(t, q, upper):
    """Stable binomial weights from a logarithmic recurrence around the mode."""
    k = np.arange(upper+1)
    if q == 0:
        z = np.zeros(upper+1);z[0] = 1;return z
    mode = min(int(math.floor((t+1)*q)), upper)
    logs = np.full(upper+1, -np.inf)
    logs[mode] = (math.lgamma(t+1)-math.lgamma(mode+1)-math.lgamma(t-mode+1)
                  +mode*math.log(q)+(t-mode)*math.log1p(-q))
    for j in range(mode+1, upper+1):
        logs[j] = logs[j-1]+math.log(t-j+1)-math.log(j)+math.log(q)-math.log1p(-q)
    for j in range(mode-1,-1,-1):
        logs[j] = logs[j+1]+math.log(j+1)-math.log(t-j)+math.log1p(-q)-math.log(q)
    return np.exp(logs)


def main():
    for theta in [0.29, math.pi/4, 1.12]:
        for t in range(1, 7):
            for p in [0.0, 0.17, 0.61, 0.94, 1.0]:
                d = direct_channel(t, theta, p)
                m = exact_mixture(t, theta, p)
                check(np.max(np.abs(d-m))<2e-12, ('channel/mixture', theta,t,p))
                check(abs(d.sum()-1)<2e-12, ('normalization', theta,t,p))
                check(np.max(abs(d-d[::-1]))<2e-12, ('symmetry', theta,t,p))
    for theta in [0.29, math.pi/4, 1.12]:
        s, c = math.sin(theta), math.cos(theta)
        v = np.linspace(-c, c, 200001)[1:-1]
        # The change of variables v=c*sin(z) avoids singular endpoints.
        z = (np.arange(200000)+0.5)*(math.pi/2)/200000
        vv = c*np.sin(z)
        w = (2*s/math.pi)/(1-vv**2)*(math.pi/2)/200000
        check(abs(w.sum()-1)<3e-10, ('Konno normalization',theta))
        check(abs((w*vv**2).sum()-(1-s))<3e-10,('Konno m2',theta))
        check(abs((w*vv**4).sum()-(1-1.5*s+0.5*s**3))<3e-10,
              ('Konno m4',theta))
        m2,m4 = moments_up_to(280, theta)
        check(abs(m2[280]/280**2-(1-s))<0.008,('pure m2 asymptotic',theta))
        check(abs(m4[280]/280**4-(1-1.5*s+0.5*s**3))<0.008,
              ('pure m4 asymptotic',theta))
        t, lam = 6400, 2.0
        k = np.arange(281)
        b = poisson_binomial_weights(t, lam/math.sqrt(t), 280)
        check(abs(b.sum()-1)<1e-9, ('binomial tail',theta))
        ex2 = (b*(t-k+m2)).sum()/t
        ex4 = (b*(3*(t-k)**2-2*(t-k)+6*(t-k)*m2+m4)).sum()/t**2
        check(abs(ex2-(1+lam**2*(1-s)))<0.04, ('critical m2',theta))
        check(abs(ex4-(3+6*lam**2*(1-s)+lam**4*(1-1.5*s+0.5*s**3)))<0.30,
              ('critical m4',theta))
        check(0.5*lam**4*(s-1)**2*(s-4)<0,('strict non-Gaussian kurtosis',theta))
    print('VERIFY_OK', CHECKS, 'independent Kraus/mixture, Konno moments, critical moments')


if __name__ == '__main__':
    main()
