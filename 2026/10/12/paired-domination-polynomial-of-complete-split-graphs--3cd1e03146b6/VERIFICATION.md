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

The package includes `verify.py`, which independently reconstructs the complete split graph \(K_r\vee\overline{K_n}\), tests domination directly, and tests perfect matchability by recursive matching search rather than by using the closed-form criterion.

The checker exhausts every subset for all \(1\le r,n\le7\), compares the direct paired-domination predicate with the theorem criterion, compares the resulting cardinality counts with the coefficient formula, verifies that the minimum size is \(2\) with \(\binom{r}{2}+rn\) minimum sets, and verifies that every larger paired-dominating set contains a paired-dominating two-set.

Packaged replay output:

`VERIFY_OK r_range=1..7 n_range=1..7 subset_checks=64516 criterion_checks=64516 coefficient_checks=162 paired_set_minimality_checks=22507 max_order=14`

The exhaustive range is finite and is not used as a proof for arbitrary parameters. The all-orders proof is the matching argument in `RESULT.md`.
