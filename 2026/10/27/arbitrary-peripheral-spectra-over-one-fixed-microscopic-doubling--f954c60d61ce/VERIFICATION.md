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

# Verification notes

Run `python3 verify.py` with Python 3.9 or later. Only the Python standard library is needed. The checker builds the coefficients of two real cubic polynomials from exactly represented rational or conjugate-pair roots, establishes the companion characteristic coefficients using exact `fractions.Fraction` arithmetic, and approximates all 18 linear-response matrix entries independently via two-sided perturbations of pushforward integrals over 8192 equally spaced periodic quadrature nodes. It prints a precise `VERIFY_OK` marker if all tests pass.

The proof, not this finite numerical check, establishes the theorem for every real monic polynomial degree, every perturbation in the stated neighborhood and every spectral value outside the radius-one-half disk. The checker does not test generic irrational coefficients or nonlinear stability.

Limitations: periodic-grid quadrature and floating-point finite differences are numerical checks, not a certificate for the universal Fréchet expansion. The analytic companion identity and resolvent argument in RESULT.md are the actual proof.
