---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Independently reconstructed every edge/face from the actual 94 tetrahedra, formed a 188×95 integer face-relations matrix after spanning-tree contraction and computed true Smith normal form (93 invariant factors all 1, two free factors). Checked both integer cocycles on every facial boundary, their surjectivity via two identified triangles, and exhaustive coordinates of all 449 graph triangles; counts exactly 43 null and 86+66+65+1 primitive nonzero. Simplicial graph has no simple cycle shorter than 3, so realized nonzero triangles establish systolic length 3.

## originality

PASS

Best-of-knowledge PASS for the previously unstated class distribution, not for the known homology and f-vector.

## value

PASS

The full minimum combinatorial length homology spectrum in a natural minimal 16-vertex flat-manifold triangulation is a finite but structurally meaningful exact invariant: H1=Z² alone cannot determine the irregular 86,66,65,1 distribution or isolated singleton.

The dated certificate retains the supplied scientific assessment, sources and limitations.
