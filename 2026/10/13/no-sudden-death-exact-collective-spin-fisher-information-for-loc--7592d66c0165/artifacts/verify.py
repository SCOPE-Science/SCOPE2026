"""Independent finite-dimensional checks for collective-rotation QFI of noisy one-excitation states.
Use: python3 wqfi_verify.py. Requires NumPy.
"""
import numpy as np
from functools import reduce

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1.0, -1.0]).astype(complex)


def kron_all(mats):
    return reduce(np.kron, mats)


def collective(n, pauli):
    return sum(kron_all([pauli if k == j else I for k in range(n)]) / 2 for j in range(n))


def noisy_states(n, p):
    dim = 2 ** n
    w = np.zeros(dim, complex)
    for j in range(n):
        w[1 << j] = 1 / np.sqrt(n)
    vac = np.zeros(dim, complex); vac[0] = 1
    pure = np.outer(w, w.conj())
    proj_one = np.diag([int(i.bit_count() == 1) for i in range(dim)]).astype(complex)
    dep = (1 - p) ** 2
    phase = dep * pure + (1 - dep) * proj_one / n
    amp = (1 - p) * pure + p * np.outer(vac, vac.conj())
    return phase, amp


def qfi(rho, generator):
    vals, vecs = np.linalg.eigh(rho)
    vals = np.maximum(vals, 0.0)
    g = vecs.conj().T @ generator @ vecs
    numer = (vals[:, None] - vals[None, :]) ** 2
    denom = vals[:, None] + vals[None, :]
    factors = np.divide(2 * numer, denom, out=np.zeros_like(numer), where=denom > 1e-12)
    return float(np.sum(factors * np.abs(g)**2).real)


def assert_close(x, y, msg):
    if abs(x-y) > 2e-8:
        raise AssertionError(f'{msg}: {x:.14g} versus {y:.14g}')



def direct_kraus_state(n, p, kind):
    dim = 1 << n
    w = np.zeros(dim, complex)
    for j in range(n):
        w[1 << j] = 1/np.sqrt(n)
    rho = np.outer(w, w.conj())
    proj0 = np.array([[1, 0], [0, 0]], complex)
    proj1 = np.array([[0, 0], [0, 1]], complex)
    lower = np.array([[0, 1], [0, 0]], complex)
    if kind == 'phase':
        ks = [np.sqrt(1-p)*I, np.sqrt(p)*proj0, np.sqrt(p)*proj1]
    elif kind == 'amplitude':
        ks = [proj0+np.sqrt(1-p)*proj1, np.sqrt(p)*lower]
    else:
        raise ValueError(kind)
    for site in range(n):
        embedded = [kron_all([k if site==j else I for j in range(n)]) for k in ks]
        rho = sum(k @ rho @ k.conj().T for k in embedded)
    return rho

def main():
    count = 0
    kraus_checks = 0
    for n in range(2, 7):
        gx, gy, gz = (collective(n, v) for v in (X, Y, Z))
        for p in [0, 0.001, .1, .25, .5, .75, .9, .999, 1]:
            rho_pd, rho_ad = noisy_states(n, p)
            for typ, rho in [('phase', rho_pd), ('amplitude', rho_ad)]:
                vals=np.linalg.eigvalsh(rho)
                assert vals[0]>-1e-12 and abs(np.trace(rho)-1)<1e-12
                qx, qy, qz = (qfi(rho, g) for g in (gx, gy, gz))
                if typ=='phase':
                    expect=n+2*(n-1)*(1-p)**2
                else:
                    expect=n*(2*p-1)**2+2*(n-1)*(1-p)
                assert_close(qx, expect, f'{n=} {p=} {typ=} x')
                assert_close(qy, expect, f'{n=} {p=} {typ=} y')
                assert_close(qz, 0, f'{n=} {p=} {typ=} z')
                count += 3
    for n in range(2, 5):
        for p in (0.0, 0.2, 0.5, 0.8, 1.0):
            phase, amp = noisy_states(n, p)
            for kind, expected in [('phase', phase), ('amplitude', amp)]:
                direct = direct_kraus_state(n, p, kind)
                if not np.allclose(direct, expected, atol=1e-11, rtol=0):
                    raise AssertionError((n, p, kind, np.max(np.abs(direct-expected))))
                kraus_checks+=1
    print(f'VERIFY_OK full_spectrum_axis_cases={count} Kraus_outputs={kraus_checks} N=2..6 p=9 both_channels')

if __name__=='__main__': main()
