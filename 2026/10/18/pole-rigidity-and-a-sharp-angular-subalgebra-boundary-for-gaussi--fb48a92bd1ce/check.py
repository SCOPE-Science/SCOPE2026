"""Finite numerical diagnostics for Gaussian Fock Toeplitz dilation formulae.

Run with Python 3 and mpmath: python check.py.
The analytic theorem and density assertions require the proofs in RESULT.md.
"""
import cmath
import math
import mpmath as mp

mp.mp.dps = 45
checks = 0


def require(cond, message):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(message)


# Exact formula for the radial Toeplitz moments, numerically integrated.
points = [0.3, 0.2 + 0.15j, 0.5 + 0.5j, 0.75 + math.sqrt(3) * 0.25j]
for lam in points:
    require(lam.real + 1e-12 >= abs(lam) ** 2, 'admissibility')
    L = mp.mpc(lam.real, lam.imag)
    for k in range(7):
        def integrand(t):
            return (1 / L) * mp.exp(-t / L) * t**k / mp.factorial(k)
        val = mp.quad(integrand, [0, 1, 5, 15, mp.inf])
        require(abs(val - L**k) < mp.mpf('1e-25'), f'radial-moment {lam=} {k=}')

# The half-plane analytic-obstruction location for forbidden parameters.
for lam in [-0.4, 0.7j, 0.6 + 0.7j, -0.1 + 0.1j]:
    require((1 / lam).real < 1, f'forbidden pole {lam=}')

# Positive cosine residues for rational angular parameters.
def positive_residues(q):
    return {j for j in range(q) if (4 * j < q) or (4 * j > 3 * q)}

for q in range(1, 129):
    predicted = 1 + 2 * ((q - 1) // 4)
    got = len(positive_residues(q))
    require(got == predicted, f'density rational {q=}')
    for r in [0.17, 0.61, 0.9]:
        # With positive phase the radial factor is exponentially small eventually.
        threshold = min((math.cos(2 * math.pi * j / q)
                         for j in positive_residues(q)), default=1)
        m = 1
        while r**m > threshold * 0.5:
            m += 1
        for k in range(m, m + 2 * q):
            j = k % q
            phase_admissible = (j in positive_residues(q))
            actual = (math.cos(2 * math.pi * j / q) >= r**k)
            # Avoid floating-point noise for exactly-zero cosine residues.
            if 4 * j == q or 4 * j == 3 * q:
                actual = False
            require(actual == phase_admissible, f'eventual residue {q=} {r=} {k=}')
    if q >= 5:
        witnesses = [j for j in range(q) if (8*j >= q and 4*j < q)]
        require(bool(witnesses), f'square-instability witness {q=}')
    else:
        require(positive_residues(q) == {0}, f'finite subgroup {q=}')

# Explicit bounded-symbol Toeplitz operator with a non-Toeplitz square.
r = 0.2
lam = r * cmath.exp(2j * math.pi / 5)
require(lam.real > abs(lam)**2, 'Toeplitz first power')
require((lam**2).real < abs(lam**2)**2, 'non-Toeplitz square')
print('PASS', checks, 'finite diagnostics')
