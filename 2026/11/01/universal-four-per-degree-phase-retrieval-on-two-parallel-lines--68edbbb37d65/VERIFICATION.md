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

# Reproducibility and verification

Run `python3 checker.py` with a standard Python 3 interpreter. The checker is self-contained and uses only `fractions`, `math`, and `random` from the standard library. It performed 390 deterministic trials covering integer upper degree bounds 1 through 6, arbitrary distinct real abscissae on each line, distinct integer heights, polynomials of lower degree, and the zero polynomial. In each trial it tested the two leading-coefficient invariants, exact first-line interpolation, and exact second-line interpolation using rational arithmetic. The finite tests passed.

The universal injectivity theorem is proved analytically in RESULT.md; it does not depend on finite enumeration. To verify the decisive step independently, observe that any rational function of modulus one along both horizontal lines satisfies two rational reflection identities, hence has a nonzero imaginary period, hence is constant. The interpolation stage uses precisely \(2d+1\) and \(2d-1\) distinct nodes and requires no generic-position assumptions.

The independent-audit status remains not performed. Numeric stability, robust noisy inversion, and nonlinear sample-count optimality were not checked or claimed.
