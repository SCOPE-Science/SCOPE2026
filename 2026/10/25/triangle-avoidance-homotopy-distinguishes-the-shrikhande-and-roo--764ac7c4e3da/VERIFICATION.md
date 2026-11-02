---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The definition is the K3-devoid complex, not ordinary independence. Both graph adjacencies were reconstructed from their explicit Z4^2 step sets; each has 16 vertices of degree six, 48 edges, 32 triangles, and common-neighbor count two. Every one of the 65536 vertex subsets was independently tested for forbidden triangles, yielding 8951 faces including empty for Sh and 7343 for rook. The specified staged greedy Morse matching leaves nine critical six-faces after 4471 pairs (Sh) and fifteen critical five-faces after 3664 pairs (rook), with augmented empty face paired in each. An independently implemented complete directed Hasse topological sort visits all 8951 faces/48288 incidences and all 7343 faces/37744 incidences without cycles. Removing the empty pair leaves one critical vertex and cells only in a single higher dimension: Forman then gives wedges of nine six-spheres and fifteen five-spheres integrally. Modular boundary computations are corroborative, not the source of the homotopy claim.

## originality

PASS

The rook graph result is logically IDENTICAL to the published two-matching complex M2(K4,4) and explicitly excluded from novelty; it is retained only as comparator. The new natural Shrikhande K3-devoid complex and dimension-separated comparison survive. Prior Shrikhande independence-complex results use edge-avoidance instead of triangle-avoidance and do not imply this homotopy classification.

## value

PASS

This exact integral homotopy invariant separates the canonical nonisomorphic strongly regular pair with identical (16,6,2,2) parameters and even identical triangle count. The strong dimension change (S6 versus S5) demonstrates structural information invisible to low graph parameters and supplies a test object for K3-devoid complexes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
