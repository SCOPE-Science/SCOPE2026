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

`verify.py` enumerates all labelings of total weight at most \(4\) on \(\operatorname{Cr}_n\) for \(3\le n\le12\). For every zero-labeled vertex it tests every positive neighboring defender, performs the one-unit transfer, and checks whether the resulting positive support dominates the graph. It then verifies the minimum weight, exact classification, total counts, and the count of \(\{0,1\}\)-valued minima.

Recorded output:

`VERIFY_OK n_range=3..12 candidate_checks=62077 wrdf_checks=61987 classification_checks=11624 count_checks=20 binary_checks=10 max_order=24`

The computation is finite evidence for the checked range and is not used as a proof for all \(n\); the all-\(n\) result rests on the support lemma and exhaustive symbolic case analysis in `RESULT.md`.
