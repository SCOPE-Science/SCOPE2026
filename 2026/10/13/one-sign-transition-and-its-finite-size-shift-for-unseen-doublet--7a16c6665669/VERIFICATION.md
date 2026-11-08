---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Reconstructed the exact Dirichlet–multinomial joint mass function from integrating categorical likelihood against Dirichlet(a,...,a); single empty and doubleton probabilities and the ordered distinct-pair joint event yield Cov(C0,C2)=k²uv(R−1) for N≥2, zero at N≤1. Algebra gives R_{N+1}/R_N=1−a(a+2)/[((k−1)a+N−2)((k−1)a+N)] strictly in (0,1); R_2=(ka+1)/((k−1)a+1)>1. In the positive continuous gamma extension, ψ strict concavity makes log R strictly decreasing by equal-mean two-point comparison with larger spread (a+1 vs 1); strict logconvexity Γ gives limiting R∞<1. Thus unique r>2. Re-derived the endpoint-corrected expansion logR(k,λk+b)=L1(λ)/k+L2(λ,b)/k²+O_a(k^{-3}), with L1=(a−(a+1)λ)/(a+λ), L2=−(a+1)+a(a+2)(a+3/2−b)/(a+λ)²; it yields r=(a/(a+1))k+(a+3)/(2(a+1))+O_a(k^{-1}). Marginal limits yield exact displayed D_a linear critical covariance profile. At a=1, cancellation yields r=(k+2)/2. Independently enumerated 112 complete Dirichlet-multinomial finite compositions with exact rational weights and computed actual C0–C2 covariance; 2805 independent rational successive-ratio checks; high-precision gamma evaluation at k 100, 400, 1600 and a 1/2,1,2,5 confirmed second-order coefficients (not an infinite proof).

## originality

PASS

Best-of-knowledge: classical symmetric Dirichlet-multinomial joint law and first-order occupancy covariance are established prior work. The narrow surviving contribution is the strict single sign transition for Cov(C0,C2) as sample size N varies with fixed k,a; its O(1) shifted crossing and nonzero finite critical-window linear covariance law at fixed a. Targeted published-result and primary-source comparisons did not locate stronger coverage. Plausible 1987 same-family source remains inaccessible: this is an explicit residual priority risk rather than proof of absence.

## value

PASS

The unseen count C0 is the natural coverage statistic and doubletons C2 a frequency-of-frequencies measure in species richness/occupancy inference. Their dependence is a mathematically motivated joint invariant for a standard overdispersed symmetric DM allocation. A complete sign transition as sample size increases is stronger than elementary moment recomputation. The first-order covariance vanishes at λ=a/(a+1), so its explicit constant-order finite-size correction and nondegenerate limiting linear critical-window covariance resolve a genuinely delicate boundary not decided by the standard first-order theory. Fixed-a shape dependence is substantive, not arbitrary cherry-picked parameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
