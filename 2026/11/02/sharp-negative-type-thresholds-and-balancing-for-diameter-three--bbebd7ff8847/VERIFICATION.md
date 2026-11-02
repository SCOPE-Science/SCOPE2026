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

# Verification and reproducibility

The complete proof in `RESULT.md` is analytical. Its essential independently checkable steps are: (i) expand the full distance-powered quadratic form after decomposing leaf fluctuations, (ii) inspect the exact two-by-two matrix, (iii) prove one monotone crossing, (iv) use the product identity and convexity to prove strict balancing, and (v) apply the implicit-function theorem at the balanced limit.

Execute `python checker.py` with NumPy available. The checker independently constructs shortest-path distances for finite cases and verifies full-space quadratic forms, critical eigenvalue signs, balancing, and balanced asymptotic coefficients. A successful run reports 1845 supplementary assertions and sample critical exponents. The checks are finite numerical corroboration, not exhaustion of all positive integer pairs or a computer-assisted infinite proof.

The exact scope is finite, unweighted, diameter-three trees with real negative-type coefficients, and a distinct four-vertex path endpoint. There is no test or proof of the weighted/diameter-four cases. Independent validation has not been performed.
