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

# Mathematical verification

The companion `verify_prism_maximal_matchings.py` is self-contained (Python 3 standard library) and prints

`VERIFY_OK 25_states 53_arcs determinant_degree_8 trace_orders_1..25 brute_orders_3..12 brute_search_nodes=5142377 minimum_coefficients_3..25`

The verifier regenerates the admissible local triples from explicit rung and rail choices; computes the exact complete determinant polynomial \(\det(I-tT(z))\) over \(\mathbb Z[z]\), not evaluations at selected numeric weights; uses an independent matching-subset backtracking routine to compare all coefficients for \(3\le n\le12\); and tests the extremal coefficient formula for \(3\le n\le25\). Its 5,142,377 recursive search nodes are neither a count of distinct matchings nor a proof of the all-order theorem. The general result follows from the local bijection, finite exact determinant, and formal coefficient extraction in `RESULT.md`.

Separately, substituting \(z=1\) into the derived determinant yields the exact characteristic denominator of OEIS A284703 (https://oeis.org/A284703), independently confirming its published total sequence without claiming this known ungraded result as novel.

Independent audit or independent priority validation has **not** been performed. Mathematical applicability excludes \(n<3\), open ladders, twisted ladders and unmatched independent-set enumerations.
