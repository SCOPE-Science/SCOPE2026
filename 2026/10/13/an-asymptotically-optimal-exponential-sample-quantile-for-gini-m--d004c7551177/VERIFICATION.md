---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Independent Exp spacings Y_j=X_(j)−X_(j−1) have rate λ(n−j+1). Exact G_n=2/[n(n−1)] Σ_(j=2)^n (j−1)(n−j+1)Y_j and X_(k)=Σ_(j≤k)Y_j; covariance termwise gives 2B/[n(n−1)λ²], Var G_n=2(2n−1)/[3n(n−1)λ²], Var order stat=V/λ², rank-one covariance zero. Harmonic-sum asymptotics yield ρ. The sign of ρ′ equals sign(2p²−g(p)), g=−p−log(1−p), and g(p)/p² increases strictly from 1/2 to ∞, proving a unique interior optimum. Uniform interior asymptotics plus explicit endpoint bounds (small ranks O((k/n)^(3/2)); upper tail O(sqrt(h/n)(1+log(n/h))) for h=n−k+1) forbid boundary-maximizing subsequences and give convergence for ALL finite maximizers. Fresh independent rational finite covariance identities n2..29 and numerical root/ρ match; finite tests not used for asymptotic proof.

## originality

PASS

Classical exponential spacings and L-statistic linear order-statistic identities supply necessary ingredients, but the inspected sources do not provide the precise mixed Gini mean-difference/order-statistic correlation curve, unique maximizer ≈93%, or all-ranks finite maximizer convergence. Gail–Gastwirth consider a normalized scale-free Gini statistic (not the unnormalized GMD). Hosking L-moments full article inaccessible through authorized access, retained as substantive residual priority risk rather than automatic O failure.

## value

PASS

Selects a natural optimal single sample quantile for Pearson dependence with unnormalized sample Gini mean difference in a classical exponential model, with exact finite profile and rigorous large-n all-ranks optimum. Could guide choice of order statistic for scale dispersion summaries; does not claim causal prediction or normalized Gini coefficient optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
