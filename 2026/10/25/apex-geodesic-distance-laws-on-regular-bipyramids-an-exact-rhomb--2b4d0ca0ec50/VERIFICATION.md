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

## Reproducibility

Run `python CHECK.py` using Python 3 with NumPy and SciPy installed. This evaluates 640 closed-form CDF versus adaptive-quadrature comparisons (eight face-apex angles), uses 320,000 uniform planar samples to check exact moments and selected CDF values, and evaluates three first-contact asymptotic coefficients. The script exits with an error on discrepancies above stated numerical tolerances.

## Analytic checks and limits

The central analytic step is the global one-Lipschitz distance potential on the folded bipyramid: local Euclidean distance to the apex's developed image agrees on every seam, while convexity of each developed rhombus supplies a path that attains this bound. Thus the intrinsic distance is exact, not estimated by triangulation or mesh geodesics. The probability distribution follows a uniform affine coordinate map from the unit square onto the rhombus. Polar integration with the transition angles gives the exact CDF in every feasible angle range. Independently check its endpoint values, continuity at \(t=\sin\alpha\) and \(t=1\), and its small-radius coefficient \(\alpha/(2\sin\alpha)\). The special tangency exponents follow by the local normal form of the radial boundary. Finite computations corroborate but cannot establish the universal quantifiers or literature originality. No external validation is represented.
