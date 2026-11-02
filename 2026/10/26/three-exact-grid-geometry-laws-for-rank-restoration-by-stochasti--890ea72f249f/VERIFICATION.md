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

Each rounded row belongs to one of four vectors (L,L),(U,L),(L,U),(U,U) with respective independent probabilities a_i,b_i,c_i,d_i. Exact real rank drops below two precisely when all nonzero row vectors occupy one one-dimensional line. If L=0, the three line events (diagonal and two coordinate axes) overlap only at all-zero rows, yielding P(rank2)=1-product(a+b)-product(a+c)-product(a+d)+2product(a). If U=0, complement endpoint probabilities. For L=-U !=0 the four row types occupy two distinct lines so P=1-product(a+d)-product(b+c); for nonzero nonopposite levels three distinct lines yield P=1-product(a+d)-product b-product c. This partitions all L<U, even degenerate p_i,q_i. For p_i=q_i=alpha/N, binomial/exponential limits give (1-exp(-alpha))^2 at zero lower endpoint and 1-exp(-2alpha) at opposite/generic levels, despite equal spacing and per-entry variance. Independently exhaustively enumerated N=2 row pairs with p=q=1/4, yielding exact 15/128, 15/32, 69/128 in the three cases; proof covers arbitrary N by line-event geometry. Dependence boundary: common random bit per row can force identical columns.

## originality

PASS

Ma–Yu–Drineas 2026 and Dexter et al 2024/25 study smallest singular values and probabilistic rank restoration, not the target-specific exact real-rank probabilities for four-point rectangular row support. The earlier fair binary-matrix case is subsumed and explicitly not claimed original. The three grid-location regimes and exact rare-rounding contrast, though derived with elementary inclusion-exclusion, are not found in the inspected prior work. Full Ma–Yu–Drineas article inaccessible beyond abstract; material risk of exact two-column example.

## value

PASS

Stochastic rounding is used to restore rank in numerically rank-deficient inputs; exact rank-two probability is a directly motivated natural finite-sample statistic. The striking difference between zero-level and shifted-level critical windows at identical Bernoulli variance exhibits a genuine geometric boundary beyond generic variance-based statements. It is limited to two columns, not a broad singular-value theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
