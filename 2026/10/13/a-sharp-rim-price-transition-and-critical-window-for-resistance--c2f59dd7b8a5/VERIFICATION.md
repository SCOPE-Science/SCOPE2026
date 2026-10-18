---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For any connected wheel, K=(n+1)tr[(L|1-perp)^{-1}] is strictly convex under distinct edge-conductance changes, and compactness with blowup at disconnected boundaries gives a unique global optimum. Rotational invariance forces equal spokes a and equal rim edges b even against nonsymmetric allocations. The Fourier eigenvalues 0,(n+1)a,a+b mu_k lead to K=n(n+1)F_n(u;t), u=nb, a=(1-tu)/n. Differentiating gives F_n′(0)=n^2*t/(n+1)-2*n, hence rim exclusion iff t>=2(n+1)/n; then K=n^3. The cycle sums mu=2n, mu^2=6n and convex derivative show the critical scaling t=2+s/n, n^2*b* -> (2-s)+/4 and (n^3-K*)/n -> (2-s)+^2/8. The Fourier Riemann sum gives large-n min sqrt[t(4-t)]/2 below price2, star value1 above. Independent dense Laplacian eigensum checks for n=3..10 and direct scalar finite-n optimizer scans (n=200,600) corroborate, but do not replace general convex/Riemann arguments.

## originality

PASS

PASS best of knowledge. Ghosh–Boyd–Saberi 2008 §5.2 expressly derives same wheel spectral reduced objective for *uniform unit-cost* budget, and covers t=1 as prior. It does not state the entire all-price rim exclusion boundary, large-wheel price-phase law, or width-1/n critical window. Classical weighted-wheel Kirchhoff-index evaluations give K(a,b), not a price-constrained all-edge optimization and its asymptotic bifurcation. The very closely titled Li–Yang–Zhang 2008 weighted wheel paper could not be read in full despite lawful OA attempts; no whole-document noncoverage is claimed.

## value

PASS

The optimization answers a natural network-design allocation: exactly when the added cycle edges are too expensive to justify against hub spokes. The dimension-dependent threshold, all-price optimizer, large-size budget shares, and quantified critical window constitute a structurally motivated infinite family of exact facts. It is not just recomputing equal-cost wheel Kirchhoff values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
