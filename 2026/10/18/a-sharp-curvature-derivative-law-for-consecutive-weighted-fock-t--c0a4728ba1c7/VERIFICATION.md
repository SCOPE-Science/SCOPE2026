---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The unnormalized moment density for the written e^(−2Φ) norm is r^(2k+1)e^(−2Φ(r)). Its strictly concave log has unique mode r_k with r_k²γ(log r_k)=k+1/2 and −h_k''(r_k)/2=A_k=2γ+γ′ there. The exact normalized adjacent likelihood ratio is R²/m_k with m_k=E_k R², so the optimizer changes sign at √m_k, not generally at r_k, and the optimum is the L¹ distance (twice probability TV). For |x|≤r_k^(1/8), the log density of x=R−r_k differs from −A_k x² up to a constant by O(|x|³/r_k). The bound on γ″ controls this remainder; h_k''≤−3/2 controls the complement and normalization is uniformly bounded below by a fixed-size interval at the mode. Integrating the weighted Gaussian difference yields E x=O(r_k^−1), E x²=O(1), and E|x|=1/√(πA_k)+O(r_k^−1). Thus m_k=r_k²+O(1) and E|R²−m_k|=2r_k/√(πA_k)+O(1). Dividing by m_k and using the mode relation proves the claimed scaled error O(k^−1/2). For the globally Gaussian weight, R² is Gamma(k+1,1), giving Δ_k=2e^−(k+1)(k+1)^(k+1)/(k+1)! and the same leading constant by Stirling. In the periodic tail D_g′≥7/4, τ(u+2L)=τ(u)+L, and rounding exp(u+2Lm) gives integer subsequences for each phase. Q_g constant forces g′/g constant and hence zero by periodicity. This verifies the full cluster interval and the factor two in the adjacent square-root-metric slope. The numerical checker was inspected, not executed; its finite sinusoidal examples do not prove uniformity over weights or symbols.

## originality

PASS

The radial eigenvalue representation is established, and the exact total-variation/threshold identity follows directly from it. The supported distinct contribution is the sharp moving-saddle coefficient for arbitrary admissible γ and the quantitative log-periodic phase and full cluster set. Neither fixed-symbol Weyl results (including a distinct same-day record with the same saddle) nor prior metric continuity for each symbol give this optimized adjacent law. The later power-log total-variation theorem treats a different curvature regime. This is a bounded statement-level comparison, not a priority certificate.

## value

PASS

The natural optimization asked by the square-root spectral metric is the exact unit-ball sensitivity of a pair of consecutive coordinate functionals. The sharp law shows that a variable radial geometry changes this sensitivity through a derivative term, and the complete cluster interval detects oscillation and its size, even under uniform convexity. Index-dependent optimizers and local leading coefficients give information unavailable from fixed-symbol regularity. The result does not claim the global modulus or a common optimal symbol.

The dated certificate retains the supplied scientific assessment, sources and limitations.
