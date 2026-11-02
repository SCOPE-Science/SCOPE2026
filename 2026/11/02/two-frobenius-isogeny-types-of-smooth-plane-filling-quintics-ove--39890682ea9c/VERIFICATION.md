---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and scientific limits

Execute `python3 verify_orbits.py`, `python3 verify_points_polynomial.py`, `python3 verify_points_independent.py`, and `python3 verify_weil.py`; each is standalone and requires only the Python standard library. Their expected final success tags are, respectively, `MATRIX_CLASSIFICATION_OK`, `POLYNOMIAL_BASIS_COUNTS_OK`, `INDEPENDENT_POINT_COUNTS_OK`, and `WEIL_CERTIFICATE_OK`.

The matrix script enumerates all \(3^9=19683\) ternary matrices, tests irreducibility of degree-three characteristic polynomials by the absence of roots over \(\mathbb F_3\), establishes the eight polynomial multiplicities, and computes the rank-eight polynomial representation and two affine-root classes. The polynomial-basis counter independently counts all affine and infinite points over \(\mathbb F_{3^n}\) for \(n=1,2,3,4,5,6\). The second counter implements primitive-power finite fields and directly evaluates the companion-matrix quintic, verifying the same complete point counts. The final script reconstructs the genus-six Weil numerators using Newton identities and functional equation and certifies GF(2) irreducibility by repeated squaring and Euclidean gcds. Actual executions produced all four success tags.

Numerical computations are exhaustive in the declared finite ranges; the claim for arbitrarily large extensions follows from the established zeta-function functional equation. The classification of geometric smoothness is taken from the cited source rather than inferred from local counts. The isogeny assertions invoke established finite-field isogeny classification. Independent external audit is not performed.
