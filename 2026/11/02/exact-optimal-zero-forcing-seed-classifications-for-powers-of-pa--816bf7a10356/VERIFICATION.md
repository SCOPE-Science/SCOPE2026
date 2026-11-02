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

# Verification of exact optimal zero-forcing classifications

Run `python3 verify.py` with Python's standard library only. The program independently constructs the graph adjacencies, follows ordinary black-vertex/unique-white-neighbour propagation, constructs predicted minimum sets and compares them with exhaustive enumeration over subsets of the known minimum sizes. It also verifies the predicted seed multiplicities and checks further constructed examples.

Recorded exact output:

`VERIFY_OK exhaustive_cases=83 examined_minimum_cardinality_subsets=102073 additional_constructive_cases=96`

The exhaustive cases range over path powers with \(1\le k\le5\) and \(k+2\le n<\min(k+10,17)\), and cycle powers with \(1\le k\le5\) and \(2k+1\le n<\min(2k+10,18)\), where nonempty. Larger constructive checks include \(1\le k\le12\). Parameter values outside the theorem are tested for boundary consistency, not asserted as new. Exhaustive finite results cannot prove the all-parameter classification. The mathematical proof uses the first-step degree argument, explicit propagation, and cyclic-interval intersection counting. No independent audit or external certification has been performed.
