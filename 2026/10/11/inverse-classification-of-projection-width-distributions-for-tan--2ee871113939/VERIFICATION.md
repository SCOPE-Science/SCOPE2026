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

For a tangential centrally symmetric 2m-gon, adjacent tangent normals separated by 2delta determine vertex v=r*sec(delta)*u(midpoint). The vertex maximizes support on exactly that angular normal cone, giving width/(2r)=sec(delta)*cos(phi-midpoint). Integration over the m half-turn intervals gives Pr[T>t]=(2/pi)sum_{t<sec(delta_j)}acos(t*cos(delta_j)) for t>=1; no atoms. Differentiation gives density (2/pi)sum cos(delta)/sqrt(1-t^2 cos^2(delta)) with positive square-root singularities precisely at tau=sec(delta), coefficient k*sqrt(2cos(delta))/pi for multiplicity k. Therefore exact law recovers all gaps with repetition, and unnormalized essential minimum 2r recovers scale. The cyclic gap word classifies congruences modulo the dihedral action. For m<=3 this is the full permutation action; for pairwise distinct m>=4, m!/(2m) classes. The given m=4 two words are not dihedrally equivalent. Side tangent lengths give perimeter 4r sum tan(delta) and area half r times perimeter. Checked boundaries m=2,3, repeated gaps, 0<delta<pi/2; positive singularities cannot cancel. Finite grid checks in repository do not certify this analytic inverse theorem.

## originality

PASS

In the natural exact uniform-direction projection-width inverse problem, full primary Kim-Yaskin-Zvavitch 2015 establishes broad nonuniqueness among general symmetric convex bodies, but does not determine the full normal-gap multiset within centrally symmetric tangential polygons or its sharp eight-side ambiguity and finite dihedral orbit count. Random normal measurements and chord-length distributions observe different data, not consequences of the same law. Earlier tangential-polygon gap permutation observations may exist and are a real residual risk, not ruled out by negative searches.

## value

PASS

Distribution of random projection widths is a natural direction-unlabelled tomography datum. The result exactly reconstructs all unordered tangent-normal gaps in a class of arbitrary even side count, pinpoints the only loss (cyclic order), and classifies congruence fibers with a first nonuniqueness at eight sides. The m-fold family classification and area/perimeter recovery are meaningful complete inverse data, not arbitrary finite examples or re-tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
