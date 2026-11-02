"""Supplementary numerical checks for the diagonal joint q-numerical-range theorem.

Requires Python >=3.9, NumPy. All tests are finite and are not a universal proof.
"""
import numpy as np


def factor(alpha, tol=1e-12):
    """Produce unit x,y with x[j]*conj(y[j])=alpha[j] for sum abs(alpha)<=1."""
    alpha = np.asarray(alpha, dtype=np.complex128)
    n = len(alpha)
    assert n >= 2
    s = np.sum(np.abs(alpha))
    assert s <= 1 + tol
    active = np.flatnonzero(np.abs(alpha) > 1e-13)
    x = np.zeros(n, dtype=np.complex128)
    y = np.zeros(n, dtype=np.complex128)
    if len(active) == 0:
        x[0] = 1
        y[1] = 1
    elif abs(s-1) < tol:
        x[active] = np.sqrt(np.abs(alpha[active]))
        y[active] = np.conjugate(alpha[active]) / x[active]
    elif len(active) == 1:
        k = active[0]
        ell = (k+1) % n
        x[k] = s
        x[ell] = np.sqrt(1-s*s)
        y[k] = np.conjugate(alpha[k])/s
    else:
        amp = np.abs(alpha[active])
        t0 = amp/s
        vertex = np.zeros(len(active)); vertex[0] = 1

        def energy(u):
            t = (1-u)*t0 + u*vertex
            return float(np.sum(amp*amp/t))

        lo, hi = 0.0, 1-1e-13
        assert energy(lo) < 1 < energy(hi)
        for _ in range(70):
            mid = (lo+hi)/2
            if energy(mid) <= 1:
                lo = mid
            else:
                hi = mid
        u = (lo+hi)/2
        t = (1-u)*t0 + u*vertex
        x[active] = np.sqrt(t)
        y[active] = np.conjugate(alpha[active])/x[active]
    return x, y


def check(alpha):
    x,y = factor(alpha)
    assert abs(np.linalg.norm(x)-1) < 2e-8
    assert abs(np.linalg.norm(y)-1) < 2e-8
    assert np.max(np.abs(x*np.conjugate(y)-alpha)) < 1e-8
    assert abs(np.vdot(y,x)-sum(alpha)) < 1e-8


def main():
    rng = np.random.default_rng(352031)
    checks = 0
    for n in range(2,10):
        for _ in range(120):
            x = rng.normal(size=n)+1j*rng.normal(size=n)
            x /= np.linalg.norm(x)
            y = rng.normal(size=n)+1j*rng.normal(size=n)
            y /= np.linalg.norm(y)
            alpha = x*np.conjugate(y)
            assert np.sum(np.abs(alpha)) <= 1+2e-14
            check(alpha)
            checks += 1
            # The coefficient body's convexity preserves feasibility.
            theta = rng.random()
            other = sum(alpha)*np.eye(1,n,dtype=np.complex128).ravel()
            beta = theta*alpha+(1-theta)*other
            assert np.sum(np.abs(beta)) <= 1+2e-14
            check(beta)
            checks += 1
    omega = np.exp(2j*np.pi/3)
    for r in (0.,0.025,0.25,0.5,0.9,0.999):
        for angle in (0.,0.41,2.7):
            z = np.exp(1j*angle)
            a = z*np.array([1+2*r,(1-r)*omega,(1-r)*omega**2])/3
            assert abs(sum(a)-z*r) < 1e-13
            assert abs(sum(abs(a))-1) < 1e-13
            check(a)
            phases = a/np.abs(a)
            mat = np.vstack((np.ones(3),phases.real,phases.imag))
            assert abs(np.linalg.det(mat)) > 1e-12
            checks += 1
    check(np.zeros(3,dtype=np.complex128)); checks+=1
    for q in (0.,0.12,0.9,1.):
        a = np.array([q,0,0], dtype=np.complex128)
        check(a); checks+=1
    print(f"PASS {checks} deterministic numerical cases")


if __name__ == '__main__':
    main()
