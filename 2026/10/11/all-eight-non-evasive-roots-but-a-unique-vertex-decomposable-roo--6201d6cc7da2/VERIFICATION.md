---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The exact 19-tetrahedron source sphere minus the seven listed tetrahedra gives the published 12 facets and f=(8,25,30,12). An independently written face-closure/memoized recursion enumerated all non-evasive deletion and link cases and obtained roots 0,1,2,3,4,5,6,7. A distinct pure shedding recursion returned root 5 only. For each other vertex the deletion maximal-face profile contains both triangles and tetrahedra, hence violates purity before recursion. For vertex5, the deletion is pure with nine tetrahedra and both deletion/link branches recursively vertex-decomposable, consistent with the source's explicit valid sequence starting 5,2,4,0,1. These are exhaustive finite decisions on the actual finite complex, not partial searches.

## originality

PASS

The full original primary article proves this ball is vertex-decomposable/non-evasive and exhibits one route. Existence of a route does not determine the full set of eight first non-evasive queries, nor uniqueness of the one pure vertex-decomposition first move. The exact eight-versus-one root spectrum is an additional strict structural computation.

## value

PASS

The minimal non-extendably-collapsible canonical ball is a natural stress test for recursive simplification. Demonstrating maximum first-step robustness under non-evasiveness versus unique first-step rigidity under pure vertex-decomposability is a meaningful complete local classification, not an arbitrary one-vertex check. It illustrates two notions that are often compared only through existence implications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
