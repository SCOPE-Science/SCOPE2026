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

# Reproducibility and limits

Run `python3 verify_matrix_logistic.py` using Python 3's standard library. The program uses `fractions.Fraction` for exact rational matrices and checks eight exact fixed points for three distinct positive gain eigenvalues (including a non-diagonal gain matrix), the nine independent real Hermitian multiplier slots at each point, all unstable indices, a repeated-gain rank-one projection, mixed-gain sinks, and exact boundary multipliers. Its successful terminal message is `All exact rational checks passed.`

The code tests finite witnesses, not every allowed dimension or continuous parameter. The universal statements rely on the positive square-root uniqueness argument and the all-mode derivative formula in `RESULT.md`. The criterion addresses local hyperbolic stability and not the global invariant measure. Independent audit status is not performed.
