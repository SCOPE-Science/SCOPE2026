---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The theorem is analytic. The accompanying checker uses exact rational arithmetic for the finite identities.

It exhaustively enumerates every graph on four, five, and six labeled vertices for several rational edge probabilities. For each graph it computes every degree-class count together with non-induced counts of edges, triangles, four-cycles, four-cliques, and three-vertex paths.

The edge, triangle, four-cycle, and four-clique cases test regular motif degrees one, two, two, and three. The three-vertex path tests the nonregular formula with degree sequence \((2,1,1)\).

The checker verifies the full covariance identity, the regular specialization, the sign rule, and the triangle formula. A separate high-\(n\) computation checks the stated first-order location of the continuous regular-motif sign boundary.

Finite replay is supplementary. The universal statement is proved by indicator expansion and conditional binomial degree calculation in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK parameter_sets=9 graphs_enumerated_weighted=101568 formula_checks=225 regular_checks=180 sign_checks=180 triangle_checks=45 asymptotic_checks=48`.
