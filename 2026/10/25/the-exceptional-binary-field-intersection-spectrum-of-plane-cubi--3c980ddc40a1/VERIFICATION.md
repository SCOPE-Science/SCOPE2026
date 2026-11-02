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

For all distinct nonzero ternary cubics F,G over F2, exhaustive projective point evaluation on the seven normalized vectors computes distinct rational intersections, while common geometric components are exactly those admitting a common F2 factor of degree one or two. The descent claim follows because the full Frobenius orbit of a geometric common irreducible factor divides both forms, and distinct degree-three F2 forms cannot share a degree-three factor. Independent direct enumeration over all 522753 unordered pairs of the 1023 nonzero forms and the complete seven linear/63 quadratic divisor-incidence table reproduces the unordered coprime histogram (69972,163191,162918,85554,23604,3339,210,0), hence the stated doubled ordered spectrum and maximum six. The source's separately inspected exhaustive PGL3(F2) substitution program enumerates all 168 matrices and obtains five nonoverlapping extremal orbits with sizes 84,28,28,28,42 and representatives (10,180),(10,660),(10,670),(16,446),(57,407). The independent count was complete; independent orbit enumeration was not separately rerun, so the orbit check rests on reconstructed exhaustive code and the total-size partition, not on a fresh second implementation.

## originality

PASS

The claimed object is the q=2 all-cubic coprime rational-intersection frequency distribution and classification of coordinate-fixed extremal pair orbits, not general cubic intersection counts over arbitrary q. Kaplan–Matei's primary theorem expressly restricts the analogous family to q>2; the exceptional q=2 endpoint is not a theorem instance. Asgarli–Ghioca's pencil smoothness question is not a count of all (including singular) coprime pairs. Semantic Resultary comparisons returned no prior exact F2 table or five orbit types; this negative search is supporting context only, not a novelty proof. Residual overlap with unindexed small-field tables remains.

## value

PASS

The smallest field excluded by a closely related general counting theorem is a mathematically motivated boundary: finite-field cubic pair incidence can change sharply at q=2. The exact all-pair histogram, sharp six-point extremum instead of seven, and five extremal projective classes are natural finite-geometric invariants that can be reused as reference counts. They are not a random finite slice or a merely repeated already-published table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
