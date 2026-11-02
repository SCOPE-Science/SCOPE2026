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

The stationary complex-moment formulas were reconstructed from a renewal-age integral and independently from an Ito-generator moment recursion. The algebraic expressions agree exactly, including the thermal-noise term in the trace.

The standalone `verify.py` (Python 3 standard library only) ran from the new scientific package, reporting `PASS: 550 exact-rational and numerical consistency checks`. Rational calculations check the closed complex mean, raw second complex moment, centered anisotropy, full centered trace, and strict positivity of the coordinate variances for multiple positive parameter choices. Bisection checks exercise the cubic-root sign, uniqueness-compatible monotonicity, and two limiting asymptotic scales.

These finite checks are not a proof of a universal statement. The written proof supplies exponential-renewal integration, Brownian-angular pair correlations, reflection symmetry, strict polynomial derivative, monotonicity in velocity relaxation, and asymptotic balances. No independent audit, experimental validation, or formal certification is claimed.
