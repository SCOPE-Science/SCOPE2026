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

# Reproducibility and scientific limits

Run `python verify.py` after installing the packages in `requirements.txt`. The script checks direct matrix inversion against the exact even/odd weight decomposition over several kernel widths and nuggets, and numerically cross-checks two error-function identities, the sharp tail coefficient and the scaled nugget-variance limit. The final extracted-package execution printed `PASS: 47 independent formula/numerical tests`.

At \(\alpha=\sigma=1\), the analytic one-sided collision-tail coefficient is approximately \(0.198298962676\), and the ridge coefficient is approximately \(0.124378134669\). The numerical integrations use smooth quadrature transformations near the random-node collision diagonal. Assertions use finite tolerances because numerical convergence at a singular limit is not exact arithmetic.

The theorem and its all-parameter moment assertions are not proved by a finite collection of tests. Their justification is the direct integral and dominated-convergence argument in `RESULT.md`. Independent validation has not been performed.
