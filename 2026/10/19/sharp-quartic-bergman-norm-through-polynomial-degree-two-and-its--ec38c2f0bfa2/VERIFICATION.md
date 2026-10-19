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

# Verification and reproducibility

The standalone `verify.py` requires `sympy>=1.12` and the Python standard library; run `python verify.py` in this directory. Its output is preserved in `verification-output.txt`.

Exact symbolic checks factor the derivative of the reduced one-parameter quotient, identify the unique positive parameter root, verify the optimal auxiliary-magnitude identity modulo the cubic, verify the algebraic minimal-polynomial identity for the sharp fourth-power constant, and check the maximizing value. Those symbolic checks cover every real parameter through rational polynomial identities with explicit positive denominators; they do not assume an enumeration of sample points.

Independent numerical tests use deterministic complex polynomial coefficients and disk polar quadrature for 400 cases, compare the exact fourth-moment coefficient formula, and test the resulting ratio against the symbolic bound. They also evaluate the exact extremizer numerically. The tests are finite and do not establish sharpness by themselves. The proof in `RESULT.md` supplies the global inequality and equality classification.

The noncoverage comparison of the closest public quadratic Hardy L6 result is scientific best knowledge; no independent originality confirmation or external mathematical audit has been performed.
