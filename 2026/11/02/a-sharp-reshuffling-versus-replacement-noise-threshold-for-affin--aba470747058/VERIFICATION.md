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

The proof derives the random update by inserting the affine component field into both stages of the original same-sample stochastic extragradient formula. Its nonstandard identities are the paired innovation \((M-I)d\) and the modal difference \(t_j^2(1+\kappa^2t_j^2)-(1+r_j^2)=2(\kappa t_j^2-1)\), each explicitly established in `RESULT.md`.

Reproduction command, using only the Python 3 standard library:

`python3 verify.py`

The exact arithmetic checker performs an exhaustive enumeration of all component sign histories for four rational test cases (three planar frequencies and one mixed-frequency two-plane case), through four epochs under each of the two sampling rules. The total is 32 exact expectation comparisons to the analytical formula. It separately tests the sharp equality parameter and the rational stationary example. The observed terminal line was:

`VERIFY_OK 32 exact uniform-history moments; source-ratio threshold; mixed-frequency and rational stationary witness`

No floating-point approximations, hidden local files, external datasets or optional libraries are needed. The proof, rather than the finite checker, establishes arbitrary dimension, real parameters, all positive epoch counts, and stationary limits. A new external independent audit has not been performed.
