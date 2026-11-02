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

The claim follows from the resolvent and Laplace-Plancherel proof in `RESULT.md`. Run `python verify.py` with mpmath, numpy, scipy to check independent spectral integrals, closed forms, the unique root, the two-term distance asymptotic, and finite-time non-Hermitian Schrödinger dynamics.

Tests at finitely many positive parameters do not establish strict global uniqueness or monotonicity; those are analytic consequences of the positive exterior-band integral and positive series-coefficient argument. The long-distance expansion is pointwise in the two fixed positive physical parameters. No independent scientific audit has been performed.
