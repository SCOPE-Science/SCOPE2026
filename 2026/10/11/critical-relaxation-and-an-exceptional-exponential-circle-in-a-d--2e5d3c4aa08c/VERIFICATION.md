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

Run `python verify.py` with Python 3.9 or later, in a directory containing this document and the accompanying `verify.py` script. The script requires only the Python standard library (`fractions`, `math`), reads no external files, and makes no network calls. It prints a PASS line after checking rational formal-series coefficients, coordinate-map identities, the four fixed phase classes, and selected long finite trajectories for steps on both sides of the logarithmic-coefficient zero.

The finite tests do not establish local attraction, global convergence, the equality of the exceptional stable set with an invariant circle, or any asymptotic constant. Those are proved in `RESULT.md` by exact reduction, inequalities, a summable remainder and a Lyapunov/finite-critical-set argument. Numeric trajectories have finite precision and finite horizon. In particular, a reported convergence of successive finite renormalizations is only a consistency check.

The first-public date associated with the motivating discrete-time phase-map preprint is September 19, 2026. Independent scientific audit and independent validation have not been performed.
