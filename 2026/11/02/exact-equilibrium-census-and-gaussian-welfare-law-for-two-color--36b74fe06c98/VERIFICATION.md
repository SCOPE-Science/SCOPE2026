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

Run `python3 cyclic_swap_verifier.py` using Python 3 and its standard library. The script independently checks direct pairwise post-swap utility comparisons for all 32,760 binary words on labeled cycles of sizes 3 through 14; matches the equilibrium-run criterion and every fixed-composition count; verifies the exact transfer-matrix welfare polynomial on those sizes; and checks the total closed count and independent cyclic-run enumeration for sizes 3 through 33. All finite calculations use exact integers and direct integer comparisons. They verify finite instances and implementation consistency, not universal validity or limiting distributions. The proof uses cyclic composition counting, characteristic-polynomial factorization and the dominant-analytic-eigenvalue moment-generating-function argument for those infinite claims. External independent audit has not been performed.
