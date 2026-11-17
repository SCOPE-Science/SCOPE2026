---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

Rebuilt the cube's 12 edge-vertices and 24 cuboctahedral adjacencies from bit arithmetic, tested all 792 five-subsets for connectedness (516 disconnected), generated 2,973 nonempty faces with f-vector (12,66,220,495,792,872,516). Independently implemented staged toggling on all faces: 1,418 matched pairs; critical cells in dimensions 0:1,5:15,6:121; verified all 15,576 oriented Hasse covers acyclic. Exact integral gradient boundary is a 15-by-121 matrix of rank 3 with determinant +1 on rows and columns (0,1,6). Thus 12 free degree-five and 118 free degree-six generators, no torsion; the 5-skeleton wedge and degree classification of pi_5 permit unit cancellations and the claimed INTEGRAL homotopy wedge. Fifty-two size-six faces are missing, excluding the high-skeleton shortcut. Pure dimension six with H5 nonzero is nonshellable. This is a complete finite result, not an infinite extrapolation.

## originality

PASS

PASS on best available evidence: the published cuboctahedral three-cut is a different Delta_3 (different facets and sphere degrees); other cut families and cube line-graph matching/independence/Čech complexes have nonidentical face definitions. Primary Bayer et al. high-skeleton theorem is inapplicable at k=5 because 52 six-vertex faces are absent. This is not a claim that failed searching proves novelty; the actual 5-cut homotopy classification was not implied by the inspected primary statements or indexed other published records.

## value

PASS

PASS: the ordinary five-cut complex of the canonical cuboctahedral line graph is a natural exact topological invariant; the unexpected two adjacent sphere dimensions, non-shellability of a pure complex, absence of torsion and failure of a general high-skeleton shortcut are mathematically motivated facts beyond a small arbitrary calculation. Complete finite homotopy classification can serve as a concrete boundary example in cut-complex topology, without needing a family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
