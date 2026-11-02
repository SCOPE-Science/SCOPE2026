---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The centered cube projection is centrally symmetric; hence its minimum enclosing disk is centered at zero and maximization over the eight projected vertices gives R²=3-min_j(v_j·U)² for four antipodal tetrahedral axes. Their tight-frame identity gives support [sqrt(2),sqrt(3)]. Each axis defines a belt of probability t/sqrt(3); conditioning on one latitude gives the stated arcsine integral J(t) for each of six equal belt pairs. Inversion of any three rows gives 1=||U||²=[(q+h)²+(p-h)²+(p-q)²]/4<=3t², excluding positive-area triple intersections for 0<t<=1/sqrt(3); an explicit normal produces triple overlap above. Therefore inclusion-exclusion gives 4t/sqrt(3)-6J(t), exactly on the claimed interval. Taylor expansion of the joint two-axis density and t²=2sqrt(3)epsilon-epsilon² verifies coefficients, including the negative linear epsilon correction. Independent random-sphere 500,000-normal checks at three thresholds agree with analytic quadrature (not proof of continuity). The lower-radius distribution is unproved.

## originality

PASS

Qualified PASS: direct primary and published-mathematical comparisons distinguish projected-cube circumradius (equivalently octahedron-section inradius, twice shadow-diameter) from cube-line directional width, octahedron-section diameter (cube-projection inradius), and octahedron-projection inradius (cube-section circumradius). Finch treats cube shadow area/perimeter. No independently published exact formula for this same high-tail event was found in the inspected source material, without treating search absence as priority proof.

## value

PASS

The radius of the smallest disk enclosing a random planar cube shadow is a canonical geometric-probability functional, distinct from area and perimeter. An exact probability law over the maximal-radius regime, a sharp triple-belt intersection threshold and explicit endpoint correction are useful self-contained projection benchmarks, not a mere renamed first moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
