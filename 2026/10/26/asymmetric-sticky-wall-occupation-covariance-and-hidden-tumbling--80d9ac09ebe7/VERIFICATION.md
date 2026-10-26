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

# Reproduction and limits

Run `python checker.py` (requires Python, NumPy, SciPy and SymPy). Exact symbolic identities establish all three covariance-matrix entries, every wall generator and interior Poisson equation, and the strictly negative bulk-tumbling derivative of the off-diagonal coefficient. Independent upwind finite continuous-time chains for three unequal-wall parameter choices and four meshes of 40, 80, 160, and 320 cells give decreasing errors compared with the symbolic continuum values. Their output is saved verbatim as `checker_output.txt`. Numerical discretization and finitely many examples are corroboration only; the complete proof is the generator-and-martingale argument in RESULT.md.

The independent review/audit channel is not performed. No first-passage, finite-sample estimator, or distribution-free universality is asserted.
