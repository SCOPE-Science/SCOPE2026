---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Cauchy facet projection yields B_d(U)=E_sign|sign·U| with the 2^{d−1}/(d−1)! normalization. Rotational symmetry gives mean √d Γ(d/2)/(√πΓ((d+1)/2)); the normalized inner product of two independent sign vectors is 1−2K/d, K∼Bin(d,1/2). The bivariate Gaussian absolute-product identity produces E B²=(2/π)E f(1−2K/d). Independent exact Rademacher moments through degree six, Taylor coefficients 1/2,1/24,1/80 of f, and gamma Stirling expansion exhibit cancellation at orders d^0,d^{-1},d^{-2} and surviving 1/(3π)d^{-3}. Numerically evaluating the exact formula up to d=512 gives d³ variance 0.106394 versus 0.106103 target. Hoeffding tails justify truncation for the unbounded integer limit; finite numerics do not substitute for it.

## originality

PASS

The full-text Kabluchko–Litvak–Zaporozhets result computes moments of one-dimensional projected width; this problem measures (d−1)-dimensional hyperplane projection volume (brightness) and thus is not implied by those line-width formulas. Horváth–Lángi provide the volume-of-hull translation identity, and Ivanov studies projection extrema rather than the uniform second moment and third-order variance constant. The specific binomial brightness law and 1/(3π) asymptotic remain best-of-knowledge not covered.

## value

PASS

Sharp d^{-3} variance, with two nontrivial cancellations, quantifies concentration of random hyperplane shadows of a canonical high-dimensional polytope. It answers an intrinsic geometric probability question beyond merely evaluating the mean, and the exact binomial expression supports future fluctuation analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
