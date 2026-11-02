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
# Reproducibility and verification

The attached `checker.py` requires Python 3 and no third-party packages. Run `python checker.py` from the extracted package directory. It completed 2,991 deterministic checks when executed for this result. The checks independently construct concrete two-by-two rank-one matrices, compute both sides using symmetric Gram eigenvalues, and test the optimized hyperbolic profile. It also checks selected endpoint asymptotics, stationary roots, and a comparison to the conjectural common-output model.

The analytical claims for **all** \(1<p<2\), for arbitrary finite matrix dimension, and for the unique global extremizer are proved in `RESULT.md` by the Gram-product reduction, a strict concavity argument, and strict monotonicity of a hyperbolic ratio. Numeric finite grids are only auxiliary consistency tests, not exhaustive searches over continuous parameters. The result is sharp within the stated equal-singular-value rank-one class; its extension to arbitrary matrix pairs remains unproved. Independent validation and mathematical publication-priority certification have not been performed.
