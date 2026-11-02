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

Run `python artifacts/verify.py` with a standard Python interpreter. It reports `VERIFY_OK 3269` after exact rational tests of the moment balance, critical-rate algebra and characteristic polynomial, plus finite-step integration checks of representative stable, marginal and unstable regimes.

These checks do not independently certify asymptotic stability or originality. Those claims are supported in RESULT.md by the explicit invariant-sector matrices, Routh–Hurwitz inequalities, and irreducible Metzler spectral argument. The finite integration uses deterministic fourth-order Runge–Kutta discretization of exact moment ODEs; it is not a stochastic simulation of sample paths. No independent audit has been performed.
