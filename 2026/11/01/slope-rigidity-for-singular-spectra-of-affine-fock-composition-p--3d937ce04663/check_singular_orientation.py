"""Supplementary finite-matrix checks for affine Fock composition products.

Requires Python 3 and NumPy. Finite matrix truncations are not proofs of the
infinite-dimensional singular-value identities, which have an analytic proof.
"""
import math
import numpy as np


def comp_matrix(a, b, dimension):
    """Compression of f(z) -> f(a*z+b) in e_n(z)=z**n/sqrt(n!)."""
    matrix = np.zeros((dimension, dimension), dtype=complex)
    for n in range(dimension):
        for k in range(n + 1):
            matrix[k, n] = (
                math.comb(n, k)
                * math.sqrt(math.factorial(k) / math.factorial(n))
                * a**k * b**(n-k)
            )
    return matrix


def log_scales(a, b, c, d):
    den = 2 * (1 - abs(a*c)**2)
    forward = (
        abs(a)**2 * abs(d)**2
        + abs(c)**2 * abs(b)**2
        + 2 * (b * d.conjugate()).real
    ) / den
    reverse = (
        abs(b)**2 + abs(d)**2
        + 2 * (c * a.conjugate() * b * d.conjugate()).real
    ) / den
    return forward, reverse


def quadratic_defect(a, b, c, d):
    return (
        (1 - abs(c)**2)*abs(b)**2 + (1 - abs(a)**2)*abs(d)**2
        + 2 * ((c*a.conjugate()-1)*b*d.conjugate()).real
    )


def run():
    cases = [
        (.3+.1j, .25+.15j, .45-.2j, -.2+.3j),
        (.5+0j, 1+0j, -.5+0j, 1+0j),
        (.5+0j, 1+0j, .5+0j, -1+0j),
        (0+0j, 1+0j, 0+0j, -1+0j),
        (.1+0j, 0+0j, .1+0j, 0+0j),
    ]
    verified = 0
    for a, b, c, d in cases:
        P, Q = comp_matrix(a, b, 64), comp_matrix(c, d, 64)
        S1 = np.linalg.svd(P @ Q.conj().T, compute_uv=False)
        S2 = np.linalg.svd(Q.conj().T @ P, compute_uv=False)
        l1, l2 = log_scales(a, b, c, d)
        for n in range(3):
            s1 = math.exp(l1)*abs(a*c)**n
            s2 = math.exp(l2)*abs(a*c)**n
            assert abs(S1[n] - s1) < 2.e-7 * max(1.,s1)
            assert abs(S2[n] - s2) < 2.e-7 * max(1.,s2)
            verified += 2
        assert abs(2*(1-abs(a*c)**2)*(l2-l1)-quadratic_defect(a,b,c,d))<1.e-12
        verified += 1
    a, c = .5+0j, -.5+0j
    assert quadratic_defect(a, 1+0j, c, 1+0j) < 0
    assert quadratic_defect(a, 1+0j, c, -1+0j) > 0
    verified += 2
    for a in [0+0j, .2+.3j, -.7+.05j]:
        for b, d in [(1+2j, 2-.4j), (-.1+.2j, -.1+.2j)]:
            target = (1-abs(a)**2)*abs(b-d)**2
            assert abs(quadratic_defect(a,b,a,d)-target) < 1.e-12
            verified += 1
    rng=np.random.default_rng(41)
    for _ in range(100):
        a=(rng.random()-.5)+1j*(rng.random()-.5)
        c=(rng.random()-.5)+1j*(rng.random()-.5)
        b=(rng.random()-.5)+1j*(rng.random()-.5)
        d=(rng.random()-.5)+1j*(rng.random()-.5)
        l1,l2=log_scales(a,b,c,d)
        assert abs(2*(1-abs(a*c)**2)*(l2-l1)-quadratic_defect(a,b,c,d))<1.e-12
        verified+=1
    print(f"PASS: {verified} finite numerical/algebraic checks")
    print("Limits: finite matrices confirm samples only; proof treats all admissible parameters.")


if __name__ == '__main__':
    run()
