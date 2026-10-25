---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For Hamming words of length d>=2 over alphabet q>=3, two distinct radius-one balls intersect in a full coordinate line of q words if their centers differ in one coordinate, exactly two common words at distance two, and none at distance >=3. Any hypothetical five-scale has every pair of distinct attribute balls contain at least three common objects, forcing those attribute centers to lie on a line and then all five objects on a line, impossible because a radius-one ball meets a line in either all q members or at most one. In four-scale, fixing an attribute and its three incident objects, the cases one object=attribute, three different changed coordinates, and two shared changed coordinates exhaust possibilities: respectively a rectangle, parity tetrahedron in a binary three-face, or two rows of two points each in a two-coordinate face. The attributes are uniquely forced in all cases. Inclusion-exclusion for two-line row vs column presentation subtracts q-grid rectangles: for c=C(q,2), 2c^3-c^2=c²(2c-1). Parity count is 2C(d,3)q^(d-3)c³, yielding the claimed N_{d,q}=C(d,2)q^(d-2)c²(2c-1)+2C(d,3)q^(d-3)c³. Independent direct incidence enumeration counted four-scales in (q,d)=(2,2):1,(2,3):8,(3,2):45,(3,3):459,(4,2):396, with unique witnesses and expected geometry; a complete search over C(27,5)=80730 five-object subsets found none at (q,d)=(3,3). These finite instances support but do not prove the full parameter theorem.

## originality

PASS

Best-of-knowledge PASS for sharp dimension cap, full geometry and exact q,d formula. Published formal-concept work connects contranominal contexts with Boolean lattice suborders and develops generic scale/induced-matching algorithms, but no inspected result specializes to closed Hamming radius-one incidence and states this two-line/parity classification or counting polynomial. Published generic algorithms could enumerate instances but do not by themselves imply the all-parameter closed formula.

## value

PASS

Maximal contranominal scales determine the size of Boolean suborder patterns in concept lattices; Hamming radius-one incidence is a natural symmetric q-ary test bed. Sharp constant extremal size independent of growing parameters plus a complete two-family geometry, unique matching and exact polynomial count is a reusable structural theorem, not an arbitrary tiny-instance enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
