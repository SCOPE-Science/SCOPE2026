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

The fully self-contained proof in `RESULT.md` derives the identity for every real matrix and all specified integers, independently of any finite computation. Reproduce finite consistency checks with `python verify_orth_diag.py` after installing the dependency in `requirements.txt`. It checks random orthogonal projectors, the exact normalized-estimator algebra, critical single-probe and full-basis cases, beta moment identities, and distributional simulations. The original embedded verifier passed 15,138 checks.

Finite Monte Carlo data cannot establish the exact distribution for all matrices, establish divergent moments, prove strict tail inequalities at arbitrarily large thresholds, or certify mathematical novelty. All those conclusions are assessed from the proof and full-text literature comparisons in the main result and review.
