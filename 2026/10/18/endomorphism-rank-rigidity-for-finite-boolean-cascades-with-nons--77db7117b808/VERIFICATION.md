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

# Reproducibility and scope

Run `python3 verify.py` with Python 3 standard library, from the directory containing the script. The verifier enumerates nine finite level-size vectors, reconstructs the poset and upper cones, brute-forces the condition `f(up(x)) == up(f(x))`, independently constructs all predicted normal-form maps, and asserts equality of the resulting sets. It then computes the image cardinality of each inverse-image operator by applying it to all upsets, checks the exact rank histogram and idempotence count, and explicitly checks implication preservation when the total point count is at most six.

The observed output ended in:

`VERIFY_OK cases= 9 brute_force_candidate_maps= 2523822`

For the nontrivial vector `(2, 3, 2)`, the verified image-rank histogram was `[(2, 2), (5, 6), (12, 24), (14, 24)]` and the idempotent count was eight.

The script supplies bounded empirical corroboration and implementation-independent checks against the formulas; it cannot prove the arbitrary-height theorem. The mathematical proof is given in RESULT.md. No external certification, independent audit, or novelty guarantee is claimed.
