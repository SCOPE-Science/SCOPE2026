---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The recurrence puts total weight δ^{d(i,j)}/(n−1) in row i for each target j≠i, distributed over its allowed first hops. The cycle has identical row sums by distance counts, with two vertices at each distance below n/2 and one antipode for even n. The common row sum is both an eigenvalue and the nonnegative matrix row-norm bound. On the star the center averages the leaves with total weight δ, and each leaf updates solely from the center with coefficient [δ+(n−2)δ²]/(n−1). Reduction to the center coordinate and common leaf coordinate gives the two nonzero eigenvalues ±ρ_S as claimed. Independently, let F=(n−1)ρ_C/δ, and P=(n−1)(1+(n−2)δ)−F², with the sign of ρ_S²−ρ_C². For n=3 and 4 this is 2δ−2 and −(1−δ)² respectively. For every n≥5, F is a polynomial with nonnegative coefficients, F(0)=2, F′>0 on [0,1], and F(1)=n−1. Thus (F²)″=2(F′)²+2FF″>0, so P is strictly concave, P(0)=n−5≥0 and P(1)=0. This gives P>0 on the whole open interval, including n=5. The verification notes are consistent; the comparison is spectral, not an ordering of finite-time paths, and eigenvalues of opposite sign on bipartite graphs cause no problem for the spectral radius.

## originality

PASS

Fatas et al. establish the recurrence and four-player examples, not the sharp all-group-size, all-decay-parameter crossover. The closest inspected indexed star–cycle ranking reversal uses adjacency and degree for SIS dynamics, not this updating matrix. The decision credits only the uniform size classification and its formulas where not already covered, not the model or the four-player analysis.

## value

PASS

This gives a precise answer about whether hub concentration or a cyclic arrangement better preserves contributions under an established inference model. The ranking reverses at a small, sharp size and stays reversed for every larger size without a restriction on the interior decay parameter. The uniform result identifies a limit of extrapolating the four-player model comparisons, rather than just evaluating a few more instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
