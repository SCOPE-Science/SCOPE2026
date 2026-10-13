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

The proof is symbolic and valid for every integer \(k\ge3\) and \(\ell\ge1\). The computational replay is a finite stress test of the definitions, boundary cases, counting formula, and basis-membership corollaries.

The standalone checker constructs each graph, computes all vertex distances by breadth-first search, forms the distance signature of every edge for every candidate landmark set, and compares the direct definition with the claimed criterion. It also expands the closed-form polynomial independently by binomial coefficients and compares every coefficient.

Checked range: \(3\le k\le6\), \(1\le\ell\le5\), maximum graph order \(11\).

Expected replay line:

`VERIFY_OK k_range=3..6 ell_range=1..5 subset_checks=7440 criterion_checks=7440 coefficient_checks=170 minimum_checks=20 max_order=11`

The finite enumeration does not certify untested parameter values; those are covered by the proof in `RESULT.md`.
