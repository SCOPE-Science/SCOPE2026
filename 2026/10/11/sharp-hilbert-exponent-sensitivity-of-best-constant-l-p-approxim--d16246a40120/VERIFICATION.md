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
# Verification

The standalone standard-library program `verify.py` checks the root of the defining transcendental equation, the two equality atoms' mean and variance, the two equivalent formulas for the sharp coefficient, a finite grid of the scalar inequality, and direct two-point \(p\)-mean differences for exponents near \(2\). It additionally checks a rounded empirical approximation at four sample sizes. Run `python3 verify.py`; expected success marker is `EXPONENT_SENSITIVITY_CHECK_OK`.

The proof of universal bounded-distribution validity, uniqueness of maximizing scalar points, all equality cases, and the \(O(n^{-2})\) empirical upper deficit is entirely analytic in `RESULT.md`. Finite grids are not exhaustive and cannot establish any such universal statement. This record is not an independent audit.
