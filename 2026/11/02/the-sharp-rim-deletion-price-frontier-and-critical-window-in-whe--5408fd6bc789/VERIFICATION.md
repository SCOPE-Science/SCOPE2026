---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For any connected nonnegative conductance vector, Kirchhoff index is (n+1)(tr(L+J)^−1−1). The Hessian along every nonzero edge variation is 2(n+1)tr(A² (L+J)^−1)>0, so unique global minimizer exists and wheel rotations force equal spokes a>0 and equal rims b≥0 without imposing symmetry a priori. Fourier modes yield (n+1)[1/((n+1)a)+sum_{k=1}^{n−1}1/(a+c_k b)], c_k=2−2cos(2pi k/n). Budget saturation n(Pa+Qb)=B yields scalar F=(P+Qz)S(z), z=b/a. S(0)=n²/(n+1), sum c_k=2n and sum c_k²=6n give derivative zero exactly Q/P=2(n+1)/n; strict convexity in budget-affine b gives unique activation and interior root. Second derivative and implicit Taylor yield stated local linear onset and quadratic improvement; Riemann-sum derivative limit gives z→max(0,P/Q−1/2), cost limit and critical window nz→max(0,(1−eta)/2) for Q=2P(1+eta/n). New checks computed independent weighted-Laplacian eigenspectra and derivative signs for n=3,4,7 and three price regimes (9 class parameter combinations). These finite checks do not establish general n/budget.

## originality

PASS

Ghosh–Boyd–Saberi 2008 already proves general strict convexity and explicit wheel spectral reduction at equal edge prices; no novelty for these facts. The additional distinct spoke/rim prices, sharp deletion threshold, finite-size onset coefficients, and critical scaling differ mathematically from the equal-price case. A 2008 weighted-wheel Kirchhoff index paper may compute some overlapping spectral identities; complete optimization coverage remains unverified.

## value

PASS

The exact cost-dependent edge-removal frontier for a natural electrically designed wheel, including strict uniqueness without symmetry assumptions and the singular 1/n price window, gives structurally meaningful topology selection and budget-allocation guidance rather than a routine fixed-price spectral computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
