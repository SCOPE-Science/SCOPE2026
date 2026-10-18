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

The analytic argument is given in `RESULT.md`. It derives the integer lower bound from the quadratic dual certificate \((1-u)(u+1/2)\), proves the internal-radius bracketing lemma for all orders, and constructs nonnegative endpoint-supported weights by interpolation of the first three cosine moments, then compresses to at most five nodes by an affine nullspace step (Carathéodory convexity).

Reproduce the supplementary numerical tests with `python verify.py` (requires `mpmath`). A completed run reported:

`VERIFY_OK 796 high-precision moment-zero comparisons, N=3..400; strict dual-aperture checks and endpoint checks`

The test program computes weights to 80 decimal places, confirms both complex moment residuals below \(10^{-49}\) for each order, and checks normalization, endpoint occupation, and the six-frequency ceiling for the explicit precursor; the five-node reduction is analytic. Finite tests cannot prove existence or minimality for untested orders. The rigorous proof does not rely on these computations.

Independent scientific validation has not been performed.
