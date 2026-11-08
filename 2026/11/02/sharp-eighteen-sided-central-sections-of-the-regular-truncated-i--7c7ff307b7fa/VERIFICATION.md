---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For generic unoriented central normals, vertex-sign great circles partition the sphere into fixed facet-crossing chambers. Independent construction counted 30 distinct truncated-vertex normal circles plus 3 octant circles: 882 intersection vertices with multiplicities 804 double, 72 triple, 6 quadruple; Euler formula gives 968 octant-refined cells. Independent sampled witnesses identified all 968 sign chambers and precisely ten (P,Q) classes with multiplicities 24,72,120,72,192,72,120,144,120,32 and maximum P+Q=18, P=6,Q=12. The inspected CERTIFY.py uses exact Q(√5) field sign comparisons, checks 20 favorable full hexagonal chambers, and proves alternating spherical boundary-normal dot values (88−√5)/109 and (25−4√5)/109. Girard excess and 20 congruent hexagons give the exact probability 0.03002464079675. Independent float witnesses corroborate combinatorial counts, while exact certificate supplies finite proof.

## originality

PASS

A prior published Resultary record classifies central sections of the regular untruncated icosahedron; the vertex arrangement, facets and Haar law for the regular truncated solid are different and not inferred from the former. General polytope-section and projection-area theory do not determine exact 18-sided probability.

## value

PASS

The sharp generic polygon complexity and its exact spherical-direction probability form a nontrivial natural finite geometric classification, supported by an explicit exhaustive exact algebraic certificate and interpretable symmetry orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
