---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope

Run `python3 verify.py` with Python 3 standard library, from the directory containing the script. The verifier enumerates nine finite level-size vectors, reconstructs the poset and upper cones, brute-forces the condition `f(up(x)) == up(f(x))`, independently constructs all predicted normal-form maps, and asserts equality of the resulting sets. It then computes the image cardinality of each inverse-image operator by applying it to all upsets, checks the exact rank histogram and idempotence count, and explicitly checks implication preservation when the total point count is at most six.

The observed output ended in:

`VERIFY_OK cases= 9 brute_force_candidate_maps= 2523822`

For the nontrivial vector `(2, 3, 2)`, the verified image-rank histogram was `[(2, 2), (5, 6), (12, 24), (14, 24)]` and the idempotent count was eight.

The script checks total idempotent counts, not the separate coefficients of the retraction polynomial. The rank-resolved proof in RESULT.md uses fixation of the dual image to classify all retractions, and the finite checker supplies supporting tests of the quantities entering that proof. Its all-endomorphism histogram is background and is not used as a certificate for the arbitrary-height retraction census.
