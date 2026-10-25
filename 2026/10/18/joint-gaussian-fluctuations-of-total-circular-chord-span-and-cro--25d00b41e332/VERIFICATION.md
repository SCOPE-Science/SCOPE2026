---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For a uniform perfect matching on 2n cyclic labels, candidate edge indicators have inclusion probabilities 1/(2n−1) and 1/[(2n−1)(2n−3)] for disjoint pairs, giving finite span means/variances. Conditioning the chord at vertex 0 on its shorter-arc span k gives crossing-partner expectation k(2n−2−k)/(2n−3), hence mixed covariance n³(n−1)²/[6(2n−3)(2n−1)]; crossing variance n(n−1)(n+3)/45 is properly credited to Flajolet–Noy. Rank iid uniform random endpoint pairs to represent a uniform matching. A pairwise sum L* of short-arc endpoint occupancies exceeds actual L by mean n(n−1)/[2(2n−1)] = O(n), so its centered n^(−3/2) error vanishes in probability. Crossings are exactly another iid-pair U-statistic. Hoeffding first projections ψ_L(q)=2q−1/2 and ψ_X(q)=2q(1−q)−1/3 for q uniform (0,1/2), yielding covariance [[1/12,1/24],[1/24,1/45]], degenerate remainder O(n²), multivariate iid CLT, determinant 1/8640 and residual variance 1/720. Independent complete matching enumeration n=2..5 (3,15,105,945 cases) verified all 5 finite moment formulas; source checker runs n≤7. Finite checks are not CLT proof.

## originality

PASS

Best-of-knowledge original relative to the named same-object, general-method and neighboring-formulation publications inspected. Exact statement/implication comparisons do not establish prior coverage; limitations on partially read related records remain recorded explicitly. The definition agrees with single-chord length studied previously. Neither marginal crossing law nor chordwise conditional crossing degree states covariance of total lengths with total crossings. Generic methods provide a proof mechanism but not the specific joint statistic, rank-to-occupancy error estimate and explicit covariance and regression constants; no inspected stronger evaluated result covers them.

## value

PASS

Joint fluctuation and 15/16 explained-variance law reveal a nontrivial dependence between two natural global chord-diagram observables. It supplies an explicit residual Gaussian statistic beyond known marginal crossing asymptotics, with a rigorous U-statistic approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
