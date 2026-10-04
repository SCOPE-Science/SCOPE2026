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

The proof is symbolic and does not depend on finite computation. A standalone exhaustive checker supplies supplementary regression evidence.

For every integer partition of every order from \(2\) through \(9\) with at least two parts, the checker constructs the corresponding complete multipartite graph and tests every labeling by \(\{0,1,2\}\). It compares:

1. the literal total Roman definition against the part-profile criterion;
2. brute-force weight counts against an independent expansion of the closed polynomial;
3. the brute-force minimum against \(\min\{N,4,\min_i n_i+2\}\).

A successful replay prints:

`VERIFY_OK profiles=87 labelings=748341 coefficient_checks=1369 minimum_checks=87 max_order=9`

The finite range is not an exhaustive proof of the infinite theorem. The infinite theorem is justified by the exact adjacency argument in `RESULT.md`.
