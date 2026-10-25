---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Gale evenness identifies tetrahedra as unordered pairs of vertex-disjoint cycle edges. A hyperplane sign word has at most four cyclic changes by a degree<=4 polynomial, and every such mixed word is realizable. Counting mixed tetrahedra gives F=pq+rn-r^2-5r+s; compare 2 versus 4 sign changes and control singleton runs. A polar stability argument bounds nongeneric sections. Euler and 2+2 colored tetrahedra determine f-vector and quadrilateral count. Independent own exact Gale-evenness/disjoint-cycle enumeration across n=5..12 gave sharp maxima (5,9,14,20,26,33,...) and matched F. This finite arithmetic checks the proof but is not extrapolated to all n.

## originality

PASS

Known C(n,4) section vertex maximum floor(n^2/4), Gale facet structure, and general algorithms for optimum slice k-face counts are prior. The assessed claim is a distinct exact all-n polygonal facet maximum plus rigidity and triangle/quadrilateral profile; available related sources do not establish the same expression. Priority is best-of-knowledge; oriented-matroid enumeration could contain an equivalent result.

## value

PASS

Cyclic 4-polytopes are canonical extremal polytopes. Maximizing section facets is a natural nontrivial face-number objective different from maximizing vertices; a sharp all-n bound, complete generic equality class, and polygon-type counts are directly useful combinatorial geometry data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
