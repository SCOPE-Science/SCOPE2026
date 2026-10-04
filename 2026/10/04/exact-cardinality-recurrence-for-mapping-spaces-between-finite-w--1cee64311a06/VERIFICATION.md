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

The proof is symbolic and applies to every positive source-level vector and target-level vector. Its critical step is the common-upper-bound classification for the image of one source level: at the maximum occupied target level, either there is one occupied point, which remains an allowed upper bound, or there are at least two incomparable occupied points, in which case no point on that same target level is a common upper bound.

`artifacts/verify.py` implements two independent procedures: the transfer recurrence and direct enumeration of all functions with an explicit order-preservation test. It compares them for all \(225\) ordered pairs of weak-order compositions with total source and target size at most four. It also checks the larger anchors \(44\), \(738\), \(143\), and \(17\) stated in the result.

Finite enumeration is not used to infer the theorem for unbounded sizes. The checker is a reproducibility aid for boundary cases, singleton levels, and indexing.

No claim is made about the order structure or homotopy type of the resulting mapping space.
