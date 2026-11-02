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

The proof derives the conditional variance of a Gaussian quadratic form, evaluates two exact angular integrals, and factors a one-variable variance difference. The supplied `verify.py` was run against these package files and passed symbolic polynomial equalities, exact matrix-projector identities, independent quadrature, and seeded finite-sample sanity checks. The simulation checks are finite and do not certify the theorem; the proof is algebraic and analytic.

This checks only the specified Gaussian three-query estimators and the spectral family. No finite-precision, general-dimensional, Rademacher-probe, or independent external scientific verification has been performed.
