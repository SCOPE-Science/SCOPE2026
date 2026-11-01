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

# Reproduction and verification

The accompanying standalone Python 3 standard-library program `artifacts/verify.py` separately builds shortest-path distances on the full vertices for \(2\le m,k\le6\), evaluates the original zero-sum powered-distance form directly, and compares it against each algebraic block of the reduction. It separately checks the strict-definiteness inequalities, determinant root locations, parameter monotonicity, and both sharp first-order asymptotic constants for large finite parameters. The verified console output was:

`VERIFY_OK assertions=1257 m=2..6 k=2..6 exact_decomposition_and_asymptotic_checks`

Run from the directory containing `RESULT.md` using `python3 artifacts/verify.py`. It requires no external data or third-party libraries. Floating-point threshold tests use a deterministic bisection and an explicit numerical tolerance; they do **not** certify inequalities for arbitrarily large integers or prove the uniqueness statement. The all-parameter proof and the strict integral Gram inequality are supplied in `RESULT.md`. Independent audit and validation are not performed.
