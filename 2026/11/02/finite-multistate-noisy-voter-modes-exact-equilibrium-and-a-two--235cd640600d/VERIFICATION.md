---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The probability for a specified voter changing a→b is p/(sN)[1+t n_b(n_b-1)] where t=s(1-p)/(p(N-1)(N-2)); after reversal the corresponding factor uses n_a-1, so the proposed microscopic weight product h_t(n_i) satisfies detailed balance. Multinomial configuration aggregation gives the labeled-count invariant probability proportional to prod_i h_t(n_i)/n_i!, not orbit-aggregated probabilities. The adjacent ratio R_t(k)=[1+t(k-1)(k-2)]/k has difference t-(1+2t)/(k(k+1)), which changes sign at most once. Concentrating increasing-tail coordinates and balancing decreasing-tail coordinates yields one-leader balanced-remainder canonical maximizers. Convexity of g_t(k)=∂_t log w_t(k) in k and majorization of λ_L over λ_K give monotonic largest canonical leader. For N=6,s=3, exact weights W2=1/8,W3=(1+2t)/12,W4=(1+2t)(1+6t)/24,W5=(1+2t)(1+6t)(1+12t)/120,W6=(1+2t)(1+6t)(1+12t)(1+20t)/720; W3 and W5 never maximize, W2/W4 and W4/W6 cross exactly at (sqrt(10)-2)/6 and (sqrt(451)-4)/60. Independent exact-rational scans for 35 (N,s,t) combinations corroborate maximality and no leader reentrance; unrestricted conclusions follow from proof, not scans.

## originality

PASS

The identical annealed multi-opinion unanimity-panel rule is established by Nowak–Stoń–Sznajd-Weron (2020/2021); this model is not new. That primary work treats deterministic mean-field concentration equations and phase diagrams, not the finite detailed-balance joint count law or labeled-count mode staircase. Herrerías-Azcué–Galla (2019) study a linear copying multi-opinion process and exact one-color marginals; their transition generator is linear in another count, not quadratic unanimity-two. Peralta et al. (2018) and Mobilia (2015) are binary nonlinear or zealot systems, not the full s≥3 finite joint state. Classical reversibility and majorization are acknowledged methods. No stronger theorem covering the finite one-leader/no-reentrance and N6 thresholds was established by inspected sources.

## value

PASS

Finite stochastic modes differ from deterministic mean-field equilibria and from per-color marginals; this is particularly meaningful at N=6 where exact count noise dominates. A general mode-reduction theorem compresses a multivariate search to balanced-remainder leader profiles and precludes leader-size reentrance. The sharp two-jump six-voter transition with skipped shapes is a mathematically motivated, exact finite-population phenomenon tied to an established social dynamics model, rather than an arbitrary chosen numeric table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
