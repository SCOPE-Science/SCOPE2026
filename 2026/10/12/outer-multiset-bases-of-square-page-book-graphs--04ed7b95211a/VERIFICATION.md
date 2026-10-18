---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

A nonlandmark a_i is distinguished from another nonlandmark a_j only by whether its mate b_i is a landmark, forcing <=2 omitted a and similarly <=2 omitted b. Six omissions then require both spine endpoints omitted and equal a,b landmark counts, making their distance multisets coincide. The explicit five-omission witness has five distinct m_1,m_2,m_3 signatures for each r>=3. Exhausting size-five cases forces two listed types; their signatures are distinct except the type-two r=3 collision. Combinatorial multiplicities give 12 and 2r(r−1)^2. Independently enumerated ALL vertex subsets for r=3,4,5,6 using BFS distances: max five omissions and counts 12,72,160,300. Finite checks corroborate structural proof.

## originality

PASS

The studied invariant is explicitly the outer multiset metric dimension (distance MULTISETS of vertices outside landmarks), not ordinary metric dimension, local multiset dimension or dual general position. Gil-Pons et al introduce the invariant and solve other families. Klavžar–Kuziak–Yero cover regular diameter-two extremals, low-dimensional cases, grids and products but the available results do not imply the nonregular, diameter-three B_r classification. Published Resultary broom-tree or complete multipartite exact formulas do not imply this square-book theorem.

## value

PASS

Square-page books are a standard generalized-theta graph family. The theorem determines an infinite high-codimension regime and every minimum resolving set, including a new exact extremal count and the exceptional three-page boundary, all natural quantities for the invariant rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
