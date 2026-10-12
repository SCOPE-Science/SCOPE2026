"""Direct finite-dimensional checks for a two-site fermionic Lindblad spectrum theorem.

Run: python verify.py
Requires NumPy and SciPy; no external data are needed.
Finite tests are corroborations of the accompanying algebraic proof.
"""
import itertools
import math
import numpy as np
from scipy.linalg import expm

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
c = np.array([[0, 1], [0, 0]], dtype=complex)
K = np.kron
I4 = np.eye(4, dtype=complex)
Z1, Z2 = K(Z, I2), K(I2, Z)
Y1X2, X1Y2 = K(Y, X), K(X, Y)
Z12 = Z1 @ Z2
L1, L2 = K(c, I2), K(Z, c)
MAJORANAS = [K(X, I2), K(Y, I2), K(Z, X), K(Z, Y)]

MONOMIALS = []
for mask in range(16):
    inds = [j for j in range(4) if mask & (1 << j)]
    mon = I4.copy()
    for j in inds:
        mon = mon @ MAJORANAS[j]
    mon_partial_phase = 1j ** sum(j < 2 for j in inds)
    MONOMIALS.append((mon, mon_partial_phase))
assert np.max(np.abs(np.array([
    [np.trace(p.conj().T @ q)/4 for q, _ in MONOMIALS]
    for p, _ in MONOMIALS]) - np.eye(16))) < 1e-14


def partial_time_reverse_first_site(rho):
    result = np.zeros((4, 4), dtype=complex)
    for mon, phase in MONOMIALS:
        result += (np.trace(mon.conj().T @ rho) / 4) * phase * mon
    return result


def supergenerator(J, g1, g2):
    H = -J * K(X, X)
    gen = -1j * (K(I4, H) - K(H.T, I4))
    for g, op in [(g1, L1), (g2, L2)]:
        for jump in (op, op.conj().T):
            djump = jump.conj().T @ jump
            gen += g * (K(jump.conj(), jump) - .5*(K(I4, djump) + K(djump.T, I4)))
    return gen


def analytic_coefficients(J, g1, g2, t, s1, s2):
    delta = g2 - g1
    disc = 4*J*J - delta*delta/4
    if disc > 1e-13:
        omega = math.sqrt(disc)
        cval, sval = math.cos(omega*t), math.sin(omega*t)/omega
    elif disc < -1e-13:
        omega = math.sqrt(-disc)
        cval, sval = math.cosh(omega*t), math.sinh(omega*t)/omega
    else:
        cval, sval = 1., t
    d1 = math.exp(-(3*g1 + g2)*t/2)
    d2 = math.exp(-(g1 + 3*g2)*t/2)
    z1 = s1*d1*(cval + delta*sval/2)
    z2 = s2*d2*(cval - delta*sval/2)
    w1 = s1*d1*2*J*sval
    w2 = s2*d2*2*J*sval
    r = s1*s2*math.exp(-2*(g1+g2)*t)
    return z1, z2, w1, w2, r


def analytic_first_clocks(J, g1, g2):
    d = g2-g1
    if abs(d) < 1e-14:
        return math.pi/(4*J), math.pi/(4*J)
    if abs(d) < 4*J-1e-13:
        omega = math.sqrt(4*J*J-d*d/4)
        ang = math.atan(d/(2*omega))
        return (math.pi/2+ang)/omega, (math.pi/2-ang)/omega
    if abs(d) <= 4*J+1e-13:
        return ((math.inf, 1/(2*J)) if d>0
                else (1/(2*J), math.inf))
    nu = math.sqrt(d*d/4-4*J*J)
    fast = math.atanh(2*nu/abs(d))/nu
    return ((math.inf, fast) if d>0 else (fast, math.inf))


def expect(rho, op):
    return float(np.trace(rho @ op).real)

checks = 0
for J, (g1, g2), t, n1, n2 in itertools.product(
    (0.7, 1.0),
    ((0., 0.), (.13, .83), (.5, 4.5), (.01, 6.2), (5., 1.), (1., 1.)),
    (0., .1, .3, .5, .85, 1.2),
    (0, 1), (0, 1)
):
    initial_index = 2*n1+n2
    rho_initial = np.zeros((4, 4), complex)
    rho_initial[initial_index, initial_index] = 1.
    vec = expm(supergenerator(J,g1,g2)*t) @ rho_initial.reshape(16,order='F')
    rho = vec.reshape((4,4),order='F')
    z1,z2,w1,w2,r = analytic_coefficients(J,g1,g2,t,(-1)**n1,(-1)**n2)
    rho_analytic = (I4+z1*Z1+z2*Z2+w1*Y1X2+w2*X1Y2+r*Z12)/4
    assert np.linalg.norm(rho-rho_analytic) < 3e-10, (J,g1,g2,t,n1,n2)
    checks += 1
    assert abs(r-z1*z2-w1*w2) < 2e-10
    checks += 1
    assert abs(expect(rho,Z1)-z1) < 1e-10 and abs(expect(rho,Z2)-z2) < 1e-10
    checks += 1
    twist = partial_time_reverse_first_site(rho) @ Z1
    assert np.linalg.norm(twist-twist.conj().T) < 1e-10
    A = math.sqrt((1+r)**2+(w1-w2)**2)
    B = math.sqrt((1-r)**2+(w1+w2)**2)
    explicit_eigenvalues = np.sort(np.array([
        (-z1-z2-A)/4, (-z1-z2+A)/4,
        (-z1+z2-B)/4, (-z1+z2+B)/4
    ]))
    assert np.max(np.abs(np.linalg.eigvalsh(twist)-explicit_eigenvalues)) < 2e-10
    checks += 1
    sv = np.linalg.svd(twist,compute_uv=False)
    dominant_gap = ((A+abs(z1+z2))-(B+abs(z1-z2)))/4
    if z1*z2 > 1e-7:
        assert dominant_gap>0 and sv[0]-sv[1]>1e-9
    elif z1*z2 < -1e-7:
        assert dominant_gap<0 and sv[0]-sv[1]>1e-9
    checks += 1

# Evaluate the exact analytic phase-transition clocks, including both exceptional points.
for J, (g1,g2) in itertools.product(
    (0.7,1.,1.4), ((0.,0.),(.2,1.1),(1.5,0.),(.0,5.),(2.,6.),(6.,2.),(.1, 4.1),(.3,6.3))
):
    t1,t2 = analytic_first_clocks(J,g1,g2)
    for k,t in enumerate((t1,t2)):
        if math.isfinite(t):
            z1,z2,*_ = analytic_coefficients(J,g1,g2,t,1,1)
            assert abs((z1,z2)[k]) < 5e-9, (J,g1,g2,k,t)
            checks += 1
    d=abs(g2-g1)
    q=d/(4*J)
    if q<1-1e-12:
        expected=math.acos(q)/(2*J*math.sqrt(1-q*q))
    elif q>1+1e-12:
        expected=math.acosh(q)/(2*J*math.sqrt(q*q-1))
    else:
        expected=1/(2*J)
    assert abs(min(t1,t2)-expected)<3e-11, (J,g1,g2)
    checks+=1

# At first finite parity crossing: exactly degenerate leading twisted singular levels.
for g1,g2 in [(0.,0.),(.13,.83),(2.,6.),(6.,2.),(.01,6.2)]:
    for n1,n2 in itertools.product((0,1),repeat=2):
        t=min(analytic_first_clocks(1.,g1,g2))
        rho0=np.zeros((4,4),complex)
        rho0[2*n1+n2,2*n1+n2]=1.
        evolved=(expm(supergenerator(1.,g1,g2)*t)@
                 rho0.reshape(16,order='F')).reshape((4,4),order='F')
        singular=np.linalg.svd(partial_time_reverse_first_site(evolved)@Z1,compute_uv=False)
        assert abs(singular[0]-singular[1]) < 2e-10
        checks+=1
print('VERIFY_OK', checks, 'direct matrix/Lindblad/singular-spectrum checks')
