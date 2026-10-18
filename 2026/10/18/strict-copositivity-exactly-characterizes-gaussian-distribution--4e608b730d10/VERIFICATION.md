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

The universal claim follows analytically from four steps: convex projection of the Gaussian factor rows, positivity of conditional monotone covariances, conditional Gaussian Hermite contraction, and a nonnegative covariance-kernel witness for necessity. This argument does not require the full covariance to be invertible.

Run `python verify.py` from this directory. The standalone script uses exact rational and integer arithmetic. It checks the displayed rank-two, four-coordinate Gaussian example and its covariance-simplex certificate; constructs a separate boundary example with a nonnegative null vector; and checks 50 exact Hermite contraction and 54 exact monotone-covariance instances. These finite checks are auxiliary evidence and do not replace the proof for arbitrary dimension or measurable monotone transformations.

The source's original nonlinear copositivity definition is used with the nondecreasing extension justified in its Lemma 15. The stronger conjecture of exact equality between the nonlinear copositivity constant and the linear copositivity modulus is not asserted. Independent validation has not been performed.
