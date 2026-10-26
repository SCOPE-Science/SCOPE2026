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

Run `python verify.py` using Python 3's standard library. The exact-rational checker independently constructs coupon-occupancy Markov transitions and inclusion--exclusion; checks expected times by occupancy recursion and coupon-arrival residues; and verifies the exact two-batch parity identity. A completed run returned `PASS 249 independent exact rational comparisons`.

The analytic theorem is not certified by these finite cases. Its critical steps are the independent coupon-tape stopping-time coupling, the exponential residue-equidistribution product bound, and the Bonferroni-controlled Taylor expansion of the missing-coupon factorial moments. The asymptotic assertion is for fixed batch size, and no unique finite crossing is claimed.
