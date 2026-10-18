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

The standalone `verify.py` is embedded with this result. With SymPy installed, execute `python verify.py` to check the exact five-stage recurrence and the relevant algebraic identities. Its output counts exact symbolic and finite-enumeration tests. Numerical evaluations near the exceptional step are corroborative only. The universal classification, the variance identity for arbitrary horizons, and the quadratic stationary-variance pole have analytic derivations in `RESULT.md`.

The source's undamped parameter choice is essential; applying these calculations to a damped, adapted or decreasing-step version requires a new analysis. Publication-priority checks compare relevant accessible primary articles and mathematical records, but independent scientific audit has not been performed.
