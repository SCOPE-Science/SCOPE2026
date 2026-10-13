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

The bundled checker `verify_wed_matching_deleted.py` builds \(K_{a,b}-M_t\) directly from the definition and performs two independent finite stress tests.

First, for every \(1\le a\le b\le4\) and every \(0\le t\le a\), it enumerates every edge subset, tests edge domination, tests inclusion-minimality by deleting each chosen edge, records all cardinalities of minimal edge dominating sets, and compares well-edge-domination with the theorem.

Second, for every theorem-negative parameter triple with \(2\le a\le12\) and \(a\le b\le15\), it constructs two explicit minimal edge dominating sets of different sizes using the witnesses from the analytic case proof and verifies both domination and minimality from scratch.

Replayed output:

`ALL CHECKS PASSED; exhaustive_cases=30; subset_candidates=136249; negative_witness_cases=655; negative_witness_sets=1310; exhaustive_range=1<=a<=b<=4; witness_range=2<=a<=12,a<=b<=15`

These checks test finite instances and proof witnesses only. They do not certify the infinite theorem; the infinite quantifiers are discharged by the analytic support-pattern proof in `RESULT.md`.
