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

Run `python3 check_two_erasure.py` with the Python standard library. The checker reconstructs the reindexed alternating nodal weights and reports 244 exact-rational and numerical assertions: finite-grid cardinal quotient comparisons, alternating infinite-denominator representations, odd/even coefficient inequalities, finite-mesh norm approximations, and inverse-square spacing scaling.

The mathematical proof is given in `RESULT.md`, including its quantified assumptions, alternating-series positivity, strict convexity, localization estimates and asymptotic expansions. Numerical checks on finitely many grids cannot establish the all-\(N\) and all-\(h\) conclusions. No independent validation or external audit has been performed.
