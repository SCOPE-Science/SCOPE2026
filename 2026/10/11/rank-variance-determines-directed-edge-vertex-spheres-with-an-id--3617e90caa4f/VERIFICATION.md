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

The rank hyperplane <1,x>=0, <r,x>=-1 has codimension two by connected rank function and Numata dimension theorem. Orthogonal projection of zero is -r/S; |e_v-e_w|²=2 gives R²=2-1/S. All edge vectors are vertices. A common sphere is minimum exactly when its center lies in the vertex convex hull. Nonnegative incidence flow of divergence -r/S has total mass one automatically; network cut constraints on lower ideals give necessity and sufficiency. An explicit graded five-vertex DAG violates the condition with R²=23/14. All N≥3 and rank normalization checked; finite tests are corroborative only.

## originality

PASS

Best-of-knowledge the joint all-ranked-quiver circumsphere formula and exact lower-ideal optimality criterion are not supplied by the materially checked facet/dimension and root-dissection results. The affine rank hyperplane is prior work; the metric center and max-flow/min-cut equivalence are a separate conclusion.

## value

PASS

Gives an exact metric invariant and a natural max-flow certificate/noncertification for optimality for a broad, structurally defined family of directed root polytopes. The ideal criterion distinguishes two geometrically different spheres and is usable beyond a routine renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
