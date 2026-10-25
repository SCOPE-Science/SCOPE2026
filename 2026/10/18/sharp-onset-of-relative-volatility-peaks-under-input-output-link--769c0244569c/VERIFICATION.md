---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Under nonnegative productive A(t), L=(I-A)^{-1} and w=L^T1 are positive enough that mu^T w>0. For the single-link perturbation t e_i e_j^T, Sherman–Morrison gives w=w0+[ct/(1-t ell)]q; after mean normalization this traverses an affine segment with a strictly increasing scalar. V=w^T Sigma w/(mu^T w)^2 is a convex quadratic in that scalar for every positive-semidefinite covariance Sigma, excluding strict interior maxima even with correlated shocks. For n=2 and any affine nonnegative productive perturbation, adj(I-A(t)) has affine entries and its positive determinant cancels in V, again leaving a convex quadratic on a monotone affine line; n=1 is constant. For n=3 with A=t(E12+E23), nilpotence yields weights 1,(1+t)/10,(1+t+t^2)/10000, and exact risk at t=0,10,100,1000,10000 has alternating high-low-high-low-high values. Continuity plus analyticity yields distinct strict extrema. An independent Fraction check reconstructed the five ratios exactly; it corroborates the witness, whereas the analytic argument covers arbitrary n in (i) and (ii).

## originality

PASS

Best-of-knowledge novelty lies in the exact one-link and two-sector shape restrictions plus sharp three-sector/two-link reversal, not in Sherman–Morrison, Leontief inverse, or input-output exposure variance.

## value

PASS

The mathematical question is motivated by whether network strengthening can reverse relative gross-output shock exposure. Theorem supplies a genuine structural threshold: neither one link (any dimension) nor any affine two-sector technology can exhibit a strict interior normalized-risk peak, yet a minimal acyclic three-sector two-link technology exhibits two strict valleys and an intervening peak. The distinction between variance amplification and squared-mean-normalized volatility is substantive; it is neither a routine citation of inverse formula nor a tiny unmotivated numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
