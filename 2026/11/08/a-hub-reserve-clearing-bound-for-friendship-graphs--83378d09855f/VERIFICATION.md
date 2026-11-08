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

The self-contained program `artifacts/verify.py` was executed with Python 3 from this package. It recursively enumerates every legal pebbling move, exploiting the strict decrease of total pebble count. It independently checks all labelled configurations of sizes \(4r-1\) and \(4r\) for \(r=2,3\), and all hub-positive configurations at the lower of these two sizes. It found exactly four and six unstackable configurations respectively at the preceding size, each having the stated concentrated pattern, and no uncleared configuration at the proposed upper threshold.

The infinite \(4r\) bound is obtained from the induction in `RESULT.md`, not from finite enumeration. No executable is claimed to provide an infinite proof. The proof's local sequences and the residual-three-pebble adjustment are independently inspectable in `RESULT.md`. Historical priority and all independent external verification remain open.
