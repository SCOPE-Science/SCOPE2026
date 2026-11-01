---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

In H=L(K_{n_1,...,n_r}), each selected code vertex has exactly one selected neighbor, so selected base-graph edges split into disjoint length-two paths with no shared vertices between paths. For a base edge uv, the open signature is T(u)∪T(v), except a selected edge receives its unique partner; these supports imply at most one unused base vertex and, if one, all P3 endpoints lie in its part and centers outside. Conversely every specified P3 factor/near-factor has nonempty distinct signatures. For N=3k, existence is exactly max_i n_i<=2k by the nonmonochromatic triple-partition induction; the labeled set-species formula uses cubic Q=(1/2)sum_{i!=j}x_i^2 x_j+3sum_{i<j<l}x_ix_jx_l and yields prod n_i![x^n]exp Q. At N=3k+1, the unique unused part must have size 2k+1 and code count is (2k+1)!/2^k. N=3k+2 cannot occur. All codes have size 2k. Independent direct enumeration of open-neighborhood signatures across 22 small complete multipartite profiles agreed, but arbitrary N relies on the combinatorial proof.

## originality

PASS

Prior OLD_oind sources introduce the invariant and classify different graph families; a known L(K_{a,b}) rook specialization is admitted as covered. The full r-partite path-factor structure, three-part triple weights, and multivariate census for arbitrary r do not follow from the inspected sources. Best-of-knowledge PASS with alternative terminology priority risk.

## value

PASS

OLD_oind is a distinct natural identifying-code invariant of line graphs. Converting a general signature problem into disjoint P3 factors yields sharp existence for all multipartite part-size profiles and a complete multivariate labeled code census. This extends a recognized two-part (rook graph) subfamily to arbitrarily many parts and covers triangular graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
