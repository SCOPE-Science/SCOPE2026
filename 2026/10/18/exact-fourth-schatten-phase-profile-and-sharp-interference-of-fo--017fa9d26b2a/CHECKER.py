"""Finite diagnostic checks for the fourth-order-nilpotent Schatten profile.

Run: python CHECKER.py (requires NumPy). Finite tests are not infinite proofs.
"""
import numpy as np


def fourth_power_schatten(a):
    gram = a.conj().T @ a
    return float(np.trace(gram @ gram).real)


def properties(a, t, theta):
    s = 1 - t
    z = np.exp(1j * theta)
    r = t * z * a + s / z * a.conj().T
    gamma = np.trace(np.linalg.matrix_power(a, 3) @ a.conj().T)
    b = ((t**4 + s**4) * fourth_power_schatten(a)
         + 4 * t*t*s*s * np.linalg.norm(a @ a, "fro")**2)
    predicted = b + 4*t*s*(t*t+s*s) * np.real(z*z*gamma)
    actual = fourth_power_schatten(r)
    assert abs(actual - predicted) < 1e-8 * (1 + actual + abs(predicted))
    assert abs(gamma) <= np.linalg.norm(a, "fro")**4 / 16 + 1e-9
    return gamma, b


def test():
    rng = np.random.default_rng(220121)
    count = 0
    for widths in ((1,1,1,1), (1,2,2,1), (2,1,3,2), (1,1,1,5)):
        n = sum(widths)
        pieces = []
        j = 0
        for w in widths:
            pieces.append(np.arange(j, j+w)); j += w
        for _ in range(60):
            a = np.zeros((n,n), dtype=complex)
            for i in range(4):
                for j in range(i+1,4):
                    block = rng.normal(size=(widths[i], widths[j])) + 1j*rng.normal(size=(widths[i],widths[j]))
                    a[np.ix_(pieces[i], pieces[j])] = block
            assert np.linalg.norm(np.linalg.matrix_power(a,4)) < 1e-9
            for t in (0, 0.15, 0.5, 0.87, 1):
                for theta in (0, 0.31, 1.2, 2.6):
                    properties(a,t,theta); count+=1
    # Sharp example with shortcut (not circle covariant).
    a = np.zeros((4,4), complex)
    a[0,1] = 0.5; a[1,2] = 0.5j; a[2,3] = -0.5; a[0,3] = 0.5
    assert abs(np.linalg.norm(a,"fro") - 1) < 1e-12
    gam = np.trace(np.linalg.matrix_power(a,3) @ a.conj().T)
    assert abs(abs(gam) - 1/16) < 1e-12
    for t in (0.1, 0.25, 0.5, 0.9):
        s = 1-t
        angmax = -np.angle(gam)/2
        angmin = angmax + np.pi/2
        hi = fourth_power_schatten(t*np.exp(1j*angmax)*a + s*np.exp(-1j*angmax)*a.conj().T)
        lo = fourth_power_schatten(t*np.exp(1j*angmin)*a + s*np.exp(-1j*angmin)*a.conj().T)
        assert abs(hi-lo - 0.5*t*s*(t*t+s*s)) < 1e-12
        count += 1
    # Cube-zero nilpotent: all phases equal.
    b = np.zeros((4,4), complex)
    b[0,1]=1+2j; b[1,2]=-3j; b[0,2]=2
    vals = [fourth_power_schatten(0.39*np.exp(1j*x)*b + 0.61*np.exp(-1j*x)*b.conj().T)
            for x in (0,.3,1.5,2.7)]
    assert max(vals)-min(vals) < 1e-9
    count+=1
    print('FOURTH_NILPOTENT_PHASE_PROFILE_OK',count)


if __name__ == '__main__':
    test()
