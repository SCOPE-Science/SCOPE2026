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
# Verification

The executable `verify.py`, included in the same package, depends only on the Python standard library. It was run on the extracted package contents, producing the marker `VERIFY_OK`. It enumerates vertices, edges, triangles, four-cliques and all simple four-cycles, checks the six-cycle vertex links, computes the integer lattice displacements of every cycle, checks the three 13-cycle systolic families, and matches all 39 null-homologous loops to rhombi paired with edges. It separately verifies the shortest nonzero lattice vectors, a determinant-13 basis, the multiplier's homology matrix, and a single orbit under 78 affine maps.

The proof of the covering and the lattice-geodesic norm appears in `RESULT.md`; the finite verifier corroborates these steps but should not be mistaken for a general theorem about all cyclic tori. The original 2004 construction and 2023 Paley-map example have been used as background, not as certificates of the new systole statement. External independent audit has not been performed.
