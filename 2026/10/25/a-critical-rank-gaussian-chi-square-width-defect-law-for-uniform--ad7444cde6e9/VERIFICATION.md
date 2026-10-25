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

# Scientific verification

The self-contained `verify.py` uses Python's standard library only. Running `python3 verify.py` from its package directory performed 1,400 comparisons of optimized support functions against exhaustive Boolean-vertex enumeration in dimensions 2 through 8, checked the exact cube/capped-cube Gaussian width-loss identity and the exact zero-loss sign criterion, and completed 1,080 independent seeded Gaussian diagnostics for dimensions 256, 1,024 and 4,096 at the three rank offsets 0, +0.75 and −0.75. The run ended with `CHECKER_PASS`. No external dependency or network access is required.

At dimension 4,096 the observed mean absolute approximation errors of the scaled loss by its conditional quadratic sign-count expression were 0.037916, 0.001440 and 0.186640 for the three offsets, respectively. The program also checked the numerical constants for cube fluctuation variance 0.045070341449 and the balanced loss-limit mean 0.313328534329.

The unrestricted infinite-dimensional statement depends on analytic arguments in RESULT.md: exact support-function optimization, the uniformly controlled half-normal small-order-statistic lemma, the binomial central limit theorem, Gaussian radial normalization, and the delta-method variance calculation. Finite simulations cannot prove convergence in law or originality. The Gaussian cube-width central limit theorem is an earlier result; its inclusion here serves the joint independent two-scale comparison. No independently audited certificate is asserted.
