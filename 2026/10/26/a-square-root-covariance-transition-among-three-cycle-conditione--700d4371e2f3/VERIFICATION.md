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
# Verification

Reproduce using `python verify.py` from Python 3 standard library. Output observed: `exhaustive conditional covariance comparisons 55`, `exact harmonic-Stirling sign comparisons 24517`, and `asymptotic scale sanity checks 4; critical constant 0.749306001288449`. The first suite exhaustively enumerates all three-cycle permutations through eight labels; the second uses exact rational arithmetic up to 90 labels. The final four approximate checks corroborate signs only. The proof of the asymptotic sign law and its strict critical boundary is analytic, not experimental. External independent audit has not been performed.
