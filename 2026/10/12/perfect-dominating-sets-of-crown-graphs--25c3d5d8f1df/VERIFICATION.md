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

The symbolic proof in `RESULT.md` is the primary verification. It derives the necessary and sufficient equations for every unselected vertex and exhausts the resulting cardinality cases.

`verify.py` independently constructs \(\operatorname{Cr}_n\) for every \(3\le n\le8\), enumerates all subsets, checks the exact perfect-domination definition, compares the complete coefficient vector with the theorem, checks that every accepted set belongs to the claimed structural type, and checks induced connectivity.

Replay output:

`VERIFY_OK n_range=3..8 subset_checks=87360 perfect_sets=51 coefficient_checks=72 classification_checks=51 connectivity_checks=51 max_order=16`

The exhaustive range is finite and is used only to detect boundary or implementation mistakes. It does not replace the all-parameter proof.
