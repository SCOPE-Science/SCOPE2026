---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For ≤3 distinct anchored points, equality and ternary collinearity extension types are exhausted by collinear anchors (q-2 unused same-line points; off-line points iff dimension≥2), and noncollinear anchors (q-1 points on each joining side; (q-1)^2 off three sides). All counts hold in every projective plane, including non-Desarguesian, and in higher-dimensional spaces by working inside the generated plane; one moving pebble always has matching extension. The persistent four-pebble game proves unrestricted-depth equivalence. Four-variable formulas for noncollinear triples and four collinear distinct points separate the bits; 5-variable skew-line formula separates dimensions 2 and ≥3. Original source verify.py was inspected but not trusted as proof; independent PG(1,2/3), PG(2,2/3), PG(3,2/3) signatures matched four classes, with 15 and 40 higher-dimensional points.

## originality

PASS

No inspected published statement implies the full point-only, unrestricted-depth four-class theorem or its sharp representative sizes; general pebble characterization and geometric covering results are proper antecedents. This is a qualified originality judgment, not exhaustive historical priority.

## value

PASS

Classifies the expressive power of a natural geometric ternary signature for an infinite family including non-Desarguesian planes. The exact width 2/3/4 spectrum, 13-point bound and width-five dimension witness identify sharp logic/geometry boundaries beyond a routine algorithmic application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
