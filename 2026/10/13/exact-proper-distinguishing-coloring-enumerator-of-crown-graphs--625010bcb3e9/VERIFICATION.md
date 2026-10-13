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

## Actual verification

The attached `verify.py` was executed under Python 3 and returned:

`VERIFY_OK exhaustive_orders=3,4 palette_ranges=0..5 assignments= 483494 proper_checked= 37328 threshold_orders=4..23 order3_optimal=408 order5_mixed_optimal=3600 order7_mixed_optimal=604800`

The program enumerates every labeled assignment to all \(2n\) vertices for \(n=3,4\), \(0\le q\le5\), applies the actual edge constraints, and independently tests all \(2n!\) automorphisms. It checks every coefficient of the shared-color refinement and tests the exact optimal-color formula for \(4\le n\le23\). The runtime counts assignments, not unlabeled color classes.

## Unproved limits

These finite computations do not prove arbitrary-parameter claims: the proof uses the full automorphism group, injective rectangle assignments, inclusion-exclusion, and extremal rectangle capacity. No independent audit or external certification is asserted.
