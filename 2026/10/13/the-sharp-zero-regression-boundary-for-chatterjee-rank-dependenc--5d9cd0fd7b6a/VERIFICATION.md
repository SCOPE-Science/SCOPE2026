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

The conditional-i.i.d. identities, normalization of Chatterjee's coefficient, and the \(\eta\) regression-variance formula were independently matched to Equation (43) in Ansari and Rockel, arXiv:2608.20176v1. The proof explicitly conditions on both the predictor and the first response, so the Jensen normalization is \(\mathbb E|V-1/2|=1/4\), not a numerical estimate.

The equality condition was checked on one-, two-, and three-support-point probability laws by the sign-affinity criterion for absolute value. Three or more support points yield a positive-measure region with random differences of both signs, forcing strict Jensen inequality. Absolutely continuous conditional laws cannot satisfy the criterion.

`checker.py` operates solely on rational numbers and verifies 128 paired-partition examples, each normalization and the expression \(\xi=1/4-1/(4m)\), including explicit checks at \(m=1,2,4,128\). Run with `python checker.py`. These computations verify the family only, not the unrestricted theorem. The unrestricted result is the conditional Jensen argument in the proof.

Unproved limits: positive copula correlation ratio, finite-sample inference, and priority relative to unavailable full texts. Independent audit has not been performed.
