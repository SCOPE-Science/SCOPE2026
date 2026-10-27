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

# Reproducibility checks

Run `python3 verify.py` from the folder containing the proof and this program (standard Python 3, no third-party dependencies). The program exactly enumerates 6,104 possible parent-choice configurations across 35 rational attachment schedules, for three through seven vertices, and compares expectation and variance to the martingale-innovation recurrence. It additionally computes five finite-scale variance diagnostics for `p_j = c / (j**a+c)` with `c = 0.8`, `n = 300000`, and `a` in `{0.35,0.50,0.60,2/3,0.80}`. The diagnostics are not infinite proofs; near the 2/3 threshold normalized constants can converge very slowly.

The analytical proof supplies all noncomputational implications: square-summability of innovations implies the auxiliary \(\sum_j v_j/j^2\) bound; recurrence barriers establish asymptotic coefficients in each regime; Riemann sums plus dominated convergence produce variance growth. Other shapes or non-\(L^2\) convergence at \(Q=\infty\) are not established. Independent audit has not been performed.
