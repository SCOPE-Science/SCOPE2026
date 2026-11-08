---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The solid is the one-third truncated regular tetrahedron with 12 integer vertices b_ij=2v_i+v_j of common squared norm 11. Away from great-circle zero sets, each strict sign vector corresponds to one open spherical convex cone. All possible cone extreme rays occur among signed primitive cross products of pairs of vertices, so exhaustive 2^12 sign enumeration is complete, not a sample. I independently constructed all 132 candidate rays, checked 4096 strict sign cells, found exactly 134 nonempty chambers grouped (J,H) as (0,4):6,(1,3):24,(1,4):48,(2,3):24,(2,4):24,(3,3):8. Spherical polygon interior angles pi-arccos(q/11) and Girard give the stated exact four-angle probability expressions; chamber-area normalization is 4*pi, with all types positive. Separate 400,000 normal-direction Monte Carlo supports the six probabilities within 0.001, but exact integer enumeration and the spherical geometry are the proof. The side-count classes are 4,5,6, with J+H verified against crossed polyhedron edges.

## originality

PASS

Queries on truncated-tetrahedron central plane sections, face-orbit incidence and stereology returned related random central sections of different solids, but no identical six-class joint law. The prominent truncated-tetrahedron geometry source names the face orbits without probability; published packing research is unrelated. An older exact stereology table remains a real priority risk.

## value

PASS

The regular truncated tetrahedron is a canonical Archimedean solid with two distinct face orbits, so the joint (triangle,hexagon) counts are intrinsic and more informative than polygon side count alone. The complete six-class distribution and exact arccosine constants solve a natural finite stochastic-geometric classification, not an arbitrary numerical subsample; the 134 spherical chamber decomposition is independently usable for related section statistics. No new general stereology theorem is required for this motivated exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
