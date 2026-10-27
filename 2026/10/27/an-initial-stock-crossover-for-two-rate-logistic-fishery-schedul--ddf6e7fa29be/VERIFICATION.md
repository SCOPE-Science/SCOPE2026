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
# Reproducibility and scientific boundaries

The analytic identity and unique-root proof are in `RESULT.md`, using only the constant-effort logistic flow and elementary differentiation, monotone l'Hôpital reasoning and strict log concavity. The attached `verify_harvest.py` recomputes cumulative catch both by separate stage flows and the closed formula with 2,000 reproducible parameter choices, and checks the prescribed threshold signs and terminal-stock inequality. The code uses only Python's standard library and outputs the numerical example quoted in the paper.

Finite numerical evidence cannot establish an infinite-parameter uniqueness theorem; the proof supplies that step. No independent audit has been performed. The scientific limitations and the uncertain completeness of the literature comparison are given in `RESULT.md` and `REVIEW.md`.
