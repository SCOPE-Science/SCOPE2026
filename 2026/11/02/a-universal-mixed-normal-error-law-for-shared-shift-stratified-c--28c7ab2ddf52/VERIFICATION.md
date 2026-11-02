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

# Reproducibility and scope

Execute `python verify.py` after installing packages in `requirements.txt`. The script symbolically computes the affine-interpolation error and the polynomial variance \(V(t)=1/180+(t-1/2)^2/12\), its first and second shift moments, and the exact limiting standardized fourth moment \(101/27\). It checks direct interpolation residues on polynomial examples, the pair-difference variance identity, consistency for a cubic integrand, a numeric 95% coverage integral, and simulation as sanity evidence.

The archived script prints `PASS: 137 exact and numerical assertions`, followed by the exact moments and estimated limiting Gaussian-interval coverage `0.9446368057`. These tests do not prove the infinite-dimensional quantifier over nonaffine \(C^2\) functions. That is supplied in RESULT.md by uniform interpolation remainder, conditional Lindeberg, the joint conditional limit, fourth-moment control and consistency of the paired-residual variance estimator.

The construction uses a fresh collection of uniform residual evaluations for each cell and two residual draws per cell, with a single shared uniform interpolation shift across all cells. This common shift is *not* resampled by the exact-moment calculations. The independent-shift comparator changes only the coupling of interpolation phases. Gaussian confidence limits are asymptotic, not finite-sample bounds.
