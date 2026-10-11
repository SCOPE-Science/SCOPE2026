---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The all-signed-poset proof is given in `RESULT.md`.

Critical checks:
- the irredundant facets are exactly the minimal roots and the signed-maximal box facets;
- a unit root has Euclidean normal length \(1\), while a two-coordinate type-B root has length \(\sqrt2\);
- every root facet is represented by two antipodally paired arcs with the same physical clearance;
- positive and negative signed maxima are exactly nonzero literal sinks;
- the doubled graph is acyclic because its arcs are generating relations of the Fischer representation;
- every source-to-sink path gives \(rW\le2-2r\);
- longest-source-path potentials satisfy all arc and endpoint inequalities at \(r=2/(2+H)\);
- antipodal averaging produces a genuine point of \(\mathbb R^n\) without weakening feasibility;
- every maximum path has zero total slack and therefore forces all of its physical facets to be tangent.

`verify.py` constructs the doubled graph for deterministic minimal signed-root systems and independently solves the complete Chebyshev linear program by generic active-set enumeration. It compares the LP optimum with the longest-path formula and checks the canonical center. Finite computation is corroborative only and does not assess originality.
