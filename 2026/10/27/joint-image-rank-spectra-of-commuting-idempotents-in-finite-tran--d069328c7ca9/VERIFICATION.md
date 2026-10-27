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

Run `python3 verify_joint_ranks.py` from the package root. It uses only Python's standard library and produces the included `verify_joint_ranks.out` exactly. The checker builds every total map in sizes zero through six, composes actual transformations to test idempotence and commutation, and bins by the three image ranks. Independently, it implements the root-block count via a labeled set recurrence, comparing every nonzero and zero coefficient across the complete histograms. It checks the exact support condition and interchange symmetry for sizes one through eight.

The counts of ordered commuting idempotent pairs for sizes zero through eight are `1, 1, 7, 58, 601, 7616, 113989, 1963060, 38178193`. The complete brute-force checks terminate at size six; they do not establish the unbounded theorem. The unbounded argument is the fiber decomposition and the labeled exponential formula in `RESULT.md`.

The external literature comparison covers two freely accessible relevant full-text articles and a directly related abstract whose full text was unavailable. Historical novelty is not independently certified.
