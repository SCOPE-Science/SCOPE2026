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

# Verification notes

Run `python3 checker.py` with Python 3. The expected terminal line is `ALL_CHECKS_OK sharp_instances=16 checked_edges=4816`.

The script uses finite enumerations to test the displayed continuous rank and explicit extremal chains. It is not an exhaustive enumeration of \(\omega^\omega\); the universal upper bound is proved by the rightmost-low-coordinate potential and sharpness by an infinite-sequence construction with a finite number of moves. The proof covers every integer \(m,k\ge1\), including the empty-edge case \(k=1\).

Prior-work comparison: the original Section 2.2 construction supplies a nonsharp general bound; the older Borel antichain results are qualitative, not an exact rank calculation for these truncations. Historical priority is subject to discovery of equivalent earlier work. No independent audit has yet been performed.
