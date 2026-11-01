---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Exact projection of a solid tube around a circle is radius-r planar tube around ellipse of axes R,Rc (c=|u_z|), outer offset minus inner erosion. Its inradius b=Rc determines hole threshold c=s=r/R; curvature rolling radius min b²/a determines no-normal-overlap threshold c=√s. Steiner/coarea and monotone perimeter give strict area loss below 2rP for c<√s; Haar c uniform on [0,1] gives three regime probabilities and unique overlap maximum 1/4. Inward ellipse offset near minor-axis incenter gives H(c)~R²(8/3)sqrt(2(1−s²)/s)(c−s)^(3/2), hence hole distribution onset 2/3. Independently buffered 12k-vertex ellipse polygons for three ratios and checked finite-δ asymptotic; analysis is general, polygon buffering is not.

## originality

PASS

Best-of-knowledge priority comparison against primary full/partial texts, published Resultary and target-domain queries found no mathematical implication of the final asserted new portion. Specifically: Outer area and ray crossing information alone do not imply the inner erosion area behavior, the two distinct c=s and c=√s thresholds, or the local 3/2 hole collapse. Earlier ingredients and special cases are credited; search absence alone is not proof.

## value

PASS

Three exact orientation regimes of nonconvex torus shadows and a sharp critical hole-size law are motivated geometric-visibility invariants. The two distinct topological/focal thresholds and continuous 2/3 onset give more information than classic offset formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
