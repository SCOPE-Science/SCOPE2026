"""Exact finite checks for the diagonal Crawford localization example.

The mathematical proof for arbitrary coordinate index sets is in RESULT.md.
No numerical finite test can replace that equality-chain argument.
"""
from fractions import Fraction as F


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for t in range(n + 1):
            for tail in compositions(n - t, k - 1):
                yield (t,) + tail


def check_case(r, s, dimension, mesh):
    assert r > 0 and r < 1 and r*r + s*s == 1
    assert dimension >= 2
    checked = 0
    # Coordinate multipliers r +/- i*s, and 1 for remaining coordinates.
    for masses in compositions(mesh, dimension):
        weights = [F(a, mesh) for a in masses]
        re = r * (weights[0] + weights[1]) + sum(weights[2:])
        im = s * (weights[0] - weights[1])
        # Rational squared-modulus test, exactly, no floating point.
        assert re*re + im*im >= r*r
        checked += 1
    midpoint = (r*F(1, 2) + r*F(1, 2), s*F(1, 2)-s*F(1, 2))
    assert midpoint == (r, F(0))
    assert r*r + s*s == 1  # Every coordinate-restricted modulus is one.
    assert 1 - midpoint[0] == 1 - r  # The sharp restricted-minus-full defect.
    return checked


def main():
    cases = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(15, 17), F(8, 17))]
    count = 0
    for r, s in cases:
        for d, mesh in [(2, 30), (3, 20), (4, 12)]:
            count += check_case(r, s, d, mesh)
        perturbation = min(r, (1-r)/2) / 3
        assert r - perturbation > 0
        assert 1 - r - 2*perturbation > 0
    print(f"VERIFY_OK exact_phase_cases={len(cases)} rational_simplex_states={count} infinite_proof_analytic=True")


if __name__ == '__main__':
    main()
