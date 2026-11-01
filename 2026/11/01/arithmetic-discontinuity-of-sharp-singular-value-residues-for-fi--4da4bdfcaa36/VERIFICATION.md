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

# Verification record

The analytic proof computes the exact orthogonal monomial diagonal, verifies Haar positivity using distinct rotations, derives the two-scale counting law by character equidistribution and a product-measure continuity argument, and inverts the counting function to get the singular-value leading term. The two-rotation trigonometric means and norm-Lipschitz inequality are verified symbolically in the proof.

The standalone `checker.py` runs 3,209 finite diagnostic assertions. It uses only the Python standard library. Results at finite cutoffs are not interpreted as a proof of an infinite limit; the analytic argument is the evidentiary basis. Independent mathematical audit: not performed.
