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

Run `python3 verify_transition.py` with an unmodified Python 3 standard library installation. The program checks finite-dimensional and finite-volume numerical regressions for the log-cosh radius formulas, contact constructions and monotonicity. Expected terminal message: `LOGCOSH_PARALLELOTOPE_SHARP_PROFILE_REGRESSIONS_OK`.

The analytic proof in RESULT.md establishes the full parameter theorem. In particular, a finite grid cannot prove inequalities for arbitrary real parameters, the uniqueness of all contact directions, or optimality among all ellipsoids; these follow instead from strict concavity and the finite-group averaging argument. The numerical checker is not an independent validation or a formal theorem certificate.
