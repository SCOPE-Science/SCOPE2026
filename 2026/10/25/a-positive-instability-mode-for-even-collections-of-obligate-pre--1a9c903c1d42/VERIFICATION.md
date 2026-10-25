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

# Verification record

The self-contained `verify.py` uses exact symbolic arithmetic to reconstruct an admissible two-three-cycle network, prove \(Bx^*=a\), check every strict sign and verify the full Jacobian characteristic factorization and its positive eigenvector. It additionally checks representative synthetic positive equilibria with varied interaction magnitudes and cycle lengths by computing the Perron spectral-radius crossing and comparing it with the Jacobian spectrum. Reproduction: `python verify.py`. The analytic all-parameter proof in RESULT.md is required; finite numerical samples do not constitute exhaustive verification.

The reviewed scope is deterministic continuous-time generalized Lotka–Volterra coexistence. No independent scientific audit has been performed.
