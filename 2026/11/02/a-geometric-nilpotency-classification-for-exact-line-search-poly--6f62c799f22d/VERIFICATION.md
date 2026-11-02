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

# Reproducibility and scope

Run `python verify.py` with Python 3.10 or newer and SymPy 1.12 or newer (`requirements.txt`). The script evaluates 1840 exact symbolic/rational assertions and should print a PASS line. It checks the explicit one-sweep and two-sweep Taylor coefficients, actual feasible step bounds in the away-step algorithm, the forward-only clipping distinction, and exact projector identities for many rational triangles and positive-definite metrics.

These computations are exact arithmetic, not floating-point simulations, but are finite tests. The theorem covering all nondegenerate triangles and positive-definite metrics is justified by the analytic derivative, projector product, and metric-circle arguments in `RESULT.md`. No independent scientific audit or external validation has been performed.
