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

# Verification details

The standalone `checker.py` reconstructs all ordered group-drawing sequences for 58 small parameter triples and compares the covariance calculated from first principles with the exact rational expression. It checked 169 covariance entries over 259368 enumerated sequences, then tested the 6-coupon packet-size sign reversal and verified strict single-switch behavior for a larger grid of exact rational evaluations. The algebraic proof is independent of this finite verification.

Usage: `python3 checker.py`. Requires Python 3 standard library only.

Limitations: exhaustive finite sampling is not an infinite-parameter proof. No independent scientific audit has been performed.
