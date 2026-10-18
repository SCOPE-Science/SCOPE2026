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

Analytic proof steps: decompose ordered pairs of perimeter points by their supporting edges; integrate the same-edge triangular region exactly; change variables at each corner by a linear map with Jacobian \(\sin\theta\) and cone angle \(\pi-\theta\); choose a positive polygon-specific truncation/separation threshold; divide by squared perimeter. The resulting formula is exact for all sufficiently short distances.

For the inequality use the Euler sine product and its positive even-power reciprocal expansion. It implies \(h''(x)>1/3\) for \(0<x<\pi\), while \(h''(x)\to1/3\) as \(x\to0\). Strict Jensen and the angle-sum identity give the coefficient and equality classification. The repeated exterior-gap tangential polygon construction shows the uniform \(1/6\) constant cannot be improved.

Reproduce: run `python3 checker.py`. Executed python3 checker.py from the complete package: four independent corner-sector midpoint integrations; 250,000 boundary-pair trials on each of three convex polygons; 1,800 stability inequality vectors; five explicit high-side-count sharpness ratios. All checks passed and the final line was CHECKS_PASSED. The Monte Carlo checks have finite sampling error and are not used as universal proofs.

Limits: the finite checker does not establish the universal theorems; no full-distance CDF, fixed-count best stability constant, or smooth-curve version was verified. Independent mathematical audit: not performed.
