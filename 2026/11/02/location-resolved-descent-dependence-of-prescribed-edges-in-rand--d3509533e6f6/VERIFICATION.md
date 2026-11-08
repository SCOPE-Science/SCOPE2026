---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For a uniformly random perfect matching of even N≥6 and its fixed-point-free involution π, condition on X_ab=1 and use a uniform residual matching of N-2 labels. Nonincident adjacent positions have descent probability p0=(N-2)/(2(N-3)); four (or three for adjacent endpoints) incident positions have the stated partner-count probabilities. Summing them yields six exhaustive cases of H_ab=(N-1)Cov(X_ab,D), including H_1N=1, corner zeros, interior short-chord (N-2)/(2(N-3)) and nonadjacent interior -1/(N-3). Exact sum over short chords yields Cov(S,D)=(N-2)/(2(N-1)), ES=1, Var(S)=(N-2)/(N-1). An independently written exhaustive perfect-matching generator checked every prescribed chord for N=6,8,10,12 (15,105,945,10395 matchings), matching conditional averages exactly. Combinatorial conditional proof covers all even N; finite search alone is not the proof.

## originality

PASS

Targeted Resultary search plus comparison of the closest published primary statements and hypotheses identifies no prior implication of the complete final claim; originality is best-of-knowledge and subject to explicitly named residual risks.

## value

PASS

A complete location-sensitive joint covariance map between a specified chord and ordinary permutation descents is a naturally motivated refinement of classical matching descent and short-chord marginals. It reveals an exact interior sign dichotomy, nontrivial affine boundary effects, and a finite positive limiting short-chord/descents covariance, useful for studying local dependencies in random matchings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
