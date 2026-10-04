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

The symbolic proof reduces the definition to two exact part-profile tests. For a proper set \(D\), the complement is connected exactly when it is a singleton or meets at least two parts. The set \(D\) dominates exactly when it meets at least two parts or is one whole part. The polynomial follows by subtracting three disjoint failure families from all subsets.

`verify.py` independently constructs the graph from each nondecreasing part profile of order at most \(10\), tests every subset against the literal definition, and compares with the criterion and the claimed coefficients. It also checks the published scalar complete-multipartite minimum and the published star polynomial as external consistency checks.

Expected successful output:

`VERIFY_OK profiles=128 subset_checks=64916 valid_sets=56680 coefficient_checks=1179 gamma_checks=128 star_checks=9 max_order=10`

The finite verification is not an exhaustive proof for unbounded order. The arbitrary-order claim rests on the symbolic argument in `RESULT.md`.
