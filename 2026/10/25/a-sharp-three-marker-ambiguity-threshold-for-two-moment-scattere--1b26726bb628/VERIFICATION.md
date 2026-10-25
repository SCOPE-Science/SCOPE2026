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
# Reproduction and limits

Execute `python3 verification/right_bounded_block_check.py` in the extracted package root. It needs Python 3 standard library only and verifies the exact observation by two independent implementations for every word of length zero to ten; reproduces the complete length-seven ambiguous pair census; enumerates the \(7^r\) norm sector for \(1\le r\le9\); reconstructs words; and checks the common observation for each norm-shell family.

Expected final marker: `RBB_TWO_MOMENT_PASS first_collisions=7 classes=2 growing_three_marker_fibers=1..9`.

This finite computation does not prove claims for all integer \(r\); the paper proof uses the Euclidean Eisenstein-integer ring, its split prime 7, unit sectors, congruences, and exact reconstruction of the binary word. No independent audit has been performed.
