---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Unique John and Löwner ellipsoids must be centered at (s/n)1 and scalar on the irreducible sum-zero permutation representation, so they are genuine unrestricted balls. Coordinate facet distances and positive John contact certificate give r=min(s,n-s)/sqrt(n(n-1)). Vertices with k=floor(s) ones, one remainder u and zeros all have R²=k+u²-s²/n; uniform vertex orbit has centroid s1/n and isotropic covariance, giving exact Löwner contact certificate. Piecewise D²=(n-1)[n-1-2nk/s+nk(k+1)/s²] for s<=n/2; derivative sign 2n(n-1)k(s-k-1)/s³ establishes plateau 0<s<=1 and unique center minimizer, with D²_min=n-1 even n and (n-1)²/n odd n. Taylor expansion near center yields even quadratic coefficient 4(n-1)(n-2)/n² and odd linear cusp coefficient 4(n-1)²/n². Independent exact-rational vertex radii/minimum checks for n3..8 and rational s denominators 2,3,5 passed. Finite checks do not replace permutation/contact proof or the real-s parameter derivative.

## originality

PASS

Classical simplex John radii and a previously published all-capacity thin-slice inradius cover the small-s portion and inner radius; the complete real-level paired unrestricted John/Löwner distortion, sharp center minimizer and parity stability were not in examined stronger publications. Best-of-knowledge, exact prior implication comparisons required.

## value

PASS

A natural one-parameter family of hypersimplex/real box slices has a nontrivial sharp ellipsoidal distortion profile: minimum only at the central slice, with two different parity stability exponents (quadratic versus linear cusp). The unrestricted John and Löwner certificates make the invariant intrinsic and exact, useful for comparing affine sections and extremal approximations even though the individual radii are classical geometric computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
