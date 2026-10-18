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

# Verification and reproducibility

The exact published-model branch matrices reduce to the scalar even-step recurrence under the stated threshold condition. Every proof step is reproduced in `RESULT.md`: finite-time entry into fair-switching regime, two-step Euclidean contraction, stationary product measure, interval-image separation and overlap, a nonatomicity argument, and finite-graph pair-law singularity. The sharp formulas for \(d=1/2\) require no floating-point computation.

Execute `python check.py` in a standard Python 3 environment. It uses only the standard library. It checks five exact rational parameters across both sides of the support transition, exact critical density normalization, fifteen conditional-moment formulas, and the relevant parity-index disjointness. It also performs a seeded numerical trajectory sanity check. The observed result was `VERIFY_OK`.

The finite checker verifies algebra and representative trajectories, **not** all real parameters or arbitrarily long time horizons. Fractal dimension uses the proved strong separation criterion and the classical dimension theorem. Unproved: absolute continuity when \(d>1/2\); extension to state-dependent branch probabilities; independent novelty certification.
