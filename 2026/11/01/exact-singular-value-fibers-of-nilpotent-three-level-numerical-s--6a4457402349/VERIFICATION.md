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

# Reproducibility and limitations

Run `python check_shadow.py` using Python 3 and its standard library. It deterministically generates triangular nilpotent matrices at the two endpoint roots and intermediate root, compares their exact-formula trace moments, tests the determinant identity at complex parameters, checks trace and determinant of the nonzero squared singular values, and evaluates the square-root boundary limit.

Actual execution output: `PASS 9612 supplementary finite checks`.

The analytic proof of the infinitely many admissible real parameters and the asymptotic statement is in `RESULT.md`. Random finite numerical sampling alone would not prove the full interval, exact optimality, publication priority, or any theorem for all matrices. Numerical tolerances apply solely to the supplementary finite checks. No independent scientific audit has been conducted.
