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
# Reproducibility and verification

Run `python verify.py` with a standard Python 3 interpreter. The deterministic test compares greedy against exact signed-gap dynamic programming over all 32,767 fixed words of length 0–14 drawn from {1,2}. A second independent dynamic program optimizes both item order and allocations for each of 289 count pairs with 0 ≤ a,b ≤ 16. It checks greedy cost 6 versus optimal cost 4 for the word (1,1,3,1), and confirms greedy optimality for all shorter words over {1,3}.

Expected exact output:

`VERIFY_OK fixed_words=32767 free_count_pairs=289 sharp_fixed_counterexample=(1,1,3,1)`

The program is a finite test, not a proof of the unbounded theorem; the folded-state exchange and block lower-bound constructions supply the mathematical proof. Verification makes no claim of an independent scientific audit.
