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

# Reproducibility

The file `verification.py` is self-contained except for Python 3.9+ with `numpy`, `sympy`, and `mpmath` installed. Run `python verification.py` from the directory containing this document. Successful output is exactly `PASS: 57 independent symbolic and numerical checks`.

The executed checks independently integrate the unit-ball overlap in dimension three, verify continuity through three derivatives and the jump in the fourth derivative, compare 27 values of the piecewise profile with angular quadrature, compare 18 exact moving-spheroid probabilities with the leading coefficient, calculate constants in dimensions two through four, and check sample strict Schur inequalities.

Analytic verification of the full dimension range rests on the lens-volume calculation, angular factorization, majorization argument, and beta-coordinate rescaling detailed in `RESULT.md`. Finite calculations are not exhaustive proofs and do not establish publication priority. The approximation in the result is not asserted when contraction parameters diverge with the distance-to-diameter scale. Independent mathematical audit has not been performed.
