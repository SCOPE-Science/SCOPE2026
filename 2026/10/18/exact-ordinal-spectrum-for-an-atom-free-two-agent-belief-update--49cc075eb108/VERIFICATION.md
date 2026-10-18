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

# Reproduction and limits

Execute `python3 verify.py` with Python 3 and no third-party packages. The script constructs every finite descending-sequence tree for prescribed ranks 0 through 8, verifies both \(K45\) relations by equality of successor sets across each arrow, computes \(\chi=\Diamond_a\top\wedge\Diamond_b\top\) directly from current rows, and iterates arrow-target restriction. At each stage it compares *all* rows to the symbolic formula for the surviving ordinal-rank targets; it also checks a strict change at each earlier stage and completely empty relations at the predicted fixed stage. The observed carrier sizes are 1, 2, 4, 8, 16, 32, 64, 128 and 256, and all tests print `VERIFY_OK`.

The proof of the universal cardinal upper bound and of the full lower spectrum is symbolic and requires ordinary transfinite induction in ZFC. The finite program neither enumerates infinite structures nor establishes the uncountable claims. The representation allows nonserial worlds and does not assert equivalence for serial \(KD45\) or reflexive \(S5\) models. Literature originality remains subject to independent expert review.
