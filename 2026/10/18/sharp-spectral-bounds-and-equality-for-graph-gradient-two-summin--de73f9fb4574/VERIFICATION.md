---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The weak-2-summability constraint is exactly sum_j u_j u_j^T <= I. For u_e=(L^dagger)^(1/2)b_e, their covariance frame sum is QLQ=P_(1^perp), proving admissibility and the lower bound from the e-th output coordinate. Since sum_e rho_e=tr(QL)=tr L^(1/2), scalar Cauchy–Schwarz forces baseline S/sqrt(m), with equality iff all rho_e constant. For any edge, spectral Cauchy–Schwarz |b_e^Tu|² <= rho_e u^T L^(1/2)u, then the matrix trace constraint gives pi_2² <= (max rho_e) S. Hence constant rho_e makes both bounds coincide, and converse follows from the lower bound. For strongly regular graphs, Q belongs to the adjacency Bose–Mesner algebra span{I,A,J}, so rho_e is constant even when edge transitivity fails. Independently checked exact matrix identities and numerical eigenvalue bounds for all 38 connected labelled four-vertex graphs, including 30 nonuniform and 8 uniform-rho cases, and reconstructed stated cyclic/complete spectral formulas.

## originality

PASS

Best-of-knowledge distinct final theorem after comparison of equivalent objects, broader implications and exact accessible primary statements; not a historical priority guarantee. The claimed necessity is not merely symmetry averaging: lower witness enforces rho_e uniformity from equality in scalar Cauchy–Schwarz, and sufficient upper bound uses the same covariance frame. The earlier operator-framework references do not supply this iff implication; a prior complete-bipartite formula is strictly narrower.

## value

PASS

A structural if-and-only-if equality boundary relates an intrinsic operator-ideal norm of graph incidence maps to a natural fractional Laplacian edge statistic, yielding explicit norming frames and exact values beyond edge-transitive graphs, including non-edge-transitive strongly regular Chang graphs. The all-graph two-sided quantitative bounds go beyond a known bipartite specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
