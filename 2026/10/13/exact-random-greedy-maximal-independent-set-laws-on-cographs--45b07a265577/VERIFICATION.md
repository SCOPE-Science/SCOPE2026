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

The universal proof is analytic. Its critical checks are:

1. At a disjoint-union cotree node, induced relative orders on child vertex sets are independent and uniform, so both maximal-independent-set structure and greedy probabilities factor as products.
2. At a join node, the child containing the globally earliest vertex is chosen with probability \(n_i/n\); that accepted vertex blocks every other child.
3. Conditional on selecting child \(i\), the relative order inside that child remains uniform, so the child process is the ordinary random greedy process on that induced cograph.
4. Uniformity of a product law forces uniformity in each factor; uniformity at a join forces both uniform child laws and equality of \(n_i/m_i\) across children.
5. These rules induct over every cotree and establish all stated quantifiers.

The standalone `artifacts/verify.py` independently enumerates all labeled graphs through six vertices, recognizes cographs by recursive graph/complement decomposition, computes the cotree law with exact rational arithmetic, and compares it with a brute-force enumeration of every vertex permutation. It also compares the recursive uniformity flag against direct equality of all terminal probabilities.

Recorded replay:

`ALL CHECKS PASSED`

`labeled_cographs_checked=6039`

`vertex_permutations_checked=4020821`

`orders=1..6`

`counts=1:1,2:2,3:8,4:52,5:472,6:5504`

Scientific limit: the finite replay is corroborative only and does not extend the theorem beyond the analytically proved cograph domain.
