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

The proof is self-contained after the explicitly cited vertex classification for hollow symmetric Monge polytopes and standard Gaussian probability theorems. The relevant mathematical checks are:

1. **Finite geometry:** For each \(n\ge3\), there are \(n(n-1)/2\) normalized corner-block vertices, each supported on two disjoint transposed rectangles. The Frobenius-orthonormal Gaussian coordinate of each off-diagonal pair appears once in the support score and has coefficient \(1/(\sqrt2\,ab)\).
2. **Intrinsic normalization:** The tangent space has dimension \(n(n-1)/2-1\), and removing the all-ones off-diagonal component changes every vertex score by an identical scalar, preserving width and maximizing vertex. The squared Gaussian tangent norm equals the coordinate sum of squares minus the squared coordinate sum divided by the coordinate count.
3. **Infinite limit:** The summable bound \(\sum_{a,b}\exp(-\varepsilon^2ab/2)<\infty\) proves decay of every sufficiently distant Gaussian rectangle average. Positive and negative finite extrema and pairwise nondegenerate score differences ensure unique eventually stable maximizing and minimizing index pairs.
4. **Moments and angles:** The gamma-function chi moment identity and monotone convergence give all positive moments. Conditioning on the single independent \((1,1)\) Gaussian coefficient gives the exact limiting normal-cone probability as an expectation of a normal tail.

`CHECK.py` is an ordinary NumPy test script, not a machine-verified infinite proof. Run `python CHECK.py`. With the included fixed seed it passed 576 direct Frobenius Gaussian support/width comparisons across dimensions 3--10, and performed 4,800 diagnostics with triangular cutoff 95 of the limiting anchored-rectangle field. The finite cutoff diagnostic found mean range 1.473515 and 0.214583 as the fraction of samples exposing the \((1,1)\) maximum. These sample statistics are not claimed as exact mathematical constants or rigorous bounds.

No independent mathematical audit or independent validation has been carried out. Residual risks include incomplete bibliographic coverage of Gaussian-array extrema and the absence of a closed expression for the full limiting law.
