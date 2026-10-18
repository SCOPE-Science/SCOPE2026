---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: Verified index normalization Y_i=(X_i+X_{i+1})/2, sign(Y_{i+1}-Y_i)=sign(X_{i+2}-X_i). The r prescribed signs split into two independent monotone rankings on parity coordinate chains; either alternating orientation has probability q_r=1/[(floor(r/2)+1)!(ceil(r/2)+1)!], so event probability p_r=2q_r. For overlap displacement d<r, two alternating windows agree only if their shared sign is consistent; their union is a single r+d alternation of probability p_(r+d). For r<=d<=r+1, the windows share at most s<=2 original innovations, and conditioning on them multiplies any complete rank-order probability by at most (m)_s<=m², bounding joint event by m²p_r². Disjoint windows at d>r+1 are independent. The 1989 Arratia--Goldstein--Gordon local-dependence theorem with neighborhoods |d|<=r+1 and b3=0 gives a conservative TV bound of the displayed b1+b2 form. For λ_n=(n-r)p_r bounded and r=o(sqrt n), both (n-r)m²p_r² and (n-r)q_(r+1) decay because q_(r+1)/q_r ~1/r; p_r->0. Union bound and floor((n+1)/(r+2)) disjoint event blocks give finite tail sandwich. With Stirling, r≈(1±epsilon)log n/loglog n gives summable dyadic upper/lower failure bounds; monotonicity fills intermediate n for a.s. scale. Independently enumerated full innovation-rank permutations for r<=5 and verified p_r=1,1/2,1/6,1/18,1/72. No finite test is treated as infinite proof.

## originality

PASS

PASS (qualified): Bandt--Shiha (2007) Section 6 Proposition 7 explicitly establishes distribution-free probabilities for ALL fixed descent sign patterns of equal-weight moving averages, so the parity-factorial single-window probability is covered. Their inspected full public text contains no longest-run Poisson law, growing-r Chen--Stein error, or a.s. extreme-length law. Arratia--Goldstein--Gordon (1989) is a general dependency-neighborhood theorem, which does not imply this model-specific quantitative error without nontrivial overlap calculations. Indexed nearly-periodic permutation patterns and subsequence problems concern different underlying events and cannot supply this theorem by title or marginal probabilities alone. Potential historical rare-pattern or oscillation extrema remain real originality risks.

## value

PASS

PASS: Quantifying sustained alternating oscillation of a smoothed series is a natural extreme-value statistic; it is unexpectedly only log n/loglog n rather than an independent-sign logarithmic scale. Finite-sample Poisson error and exact overlap classifications make this nontrivial information usable without knowing the continuous innovation law. The theorem is narrow to equal two-point smoothing but genuinely explains a structural dependence effect beyond known fixed-pattern counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
