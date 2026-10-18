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

## Reproducible checks

Run `python3 artifacts/verify.py` after installing the sole Python requirement in `requirements.txt`. All graph edges, independent simplices, signed boundaries and octahedral fundamental cycles are reconstructed from the given Cayley difference set. The code verifies the complete sixteen-vertex face vector, the integer Smith invariant factors of the third boundary and augmented matrices, and the orbit of all 32 minimum sphere supports under 192 affine automorphisms.

It also enumerates every six- and seven-vertex induced restriction using independently constructed binary boundaries, and confirms the exact seven-vertex second-homology profile of 11,120 zero cases and 320 one-dimensional cases, each positive case containing exactly one shortest octahedron. The eight-vertex witness is tested by two explicit free-face collapses, all vertex links, the signed fundamental-cycle boundary, and the unit Smith sequence after adjoining its class.

The checks establish an exact theorem for the enumerated finite graph. They do not infer an infinite-family result, verify publication priority, or substitute for an independent scientific audit.
