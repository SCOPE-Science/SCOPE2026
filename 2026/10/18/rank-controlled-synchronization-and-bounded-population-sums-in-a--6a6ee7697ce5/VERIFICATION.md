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

The analytic proof relies on the actual full scalar semiconjugacy in Gaivão–Pires, Lemma 6, and verifies separately the activation normalization in Pires, Eq. (6)–(8). Exact branch equalities give the network-wide coboundary. The image-dimension upper and lower bounds follow from finite affine branch cells and the nonempty near-zero active cell, not sampling.

The standalone checker `check.py` ran with the system Python standard library and passed 275 certified branch steps for five rational initial conditions, with 200-digit binary rational enclosure for the Fibonacci parameter and exact integer comparisons. It checks finite itinerary consistency; its output does not prove irrational semiconjugacy or infinite omega-limit statements. Those conclusions use the cited primary mathematical theorem.

The claim is conditional on strictly positive weights with row sums in \((3/4,1)\). One-step global synchronization, unique invariant probability, and the bounded population sums apply only when \(\operatorname{rank}W=1\); the dimensional equality holds for all such matrices. The constant \(2\) is proven but not claimed optimal. Independent mathematical validation has not been performed.
