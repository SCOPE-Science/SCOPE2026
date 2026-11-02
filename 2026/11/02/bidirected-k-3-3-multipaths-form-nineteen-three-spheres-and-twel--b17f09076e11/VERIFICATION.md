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

# Reproducibility

The complete standalone `multipath_k33_certificate.py` is supplied with this record; Python 3 standard library alone suffices. Execute `python3 multipath_k33_certificate.py`.

The implementation constructs the eighteen lexicographically ordered cross-part directed arcs and all 715 augmented faces, independently compares their membership with a complete subset enumeration and topological sort, generates the deterministic 341-pair nonaugmented discrete-Morse matching, verifies acyclicity across 2,394 Hasse incidences, and applies integral unit-pivot chain cancellation. After reduction the only boundary is the augmentation of the critical zero-cell, and reduced Morse degrees three and four have ranks nineteen and twelve. The checker independently computes the full original mod-two boundary ranks \((1,17,91,173,60)\); this is corroboration, not a substitute for the exact integral proof.

Expected terminal marker: `BIDIRECTED_K33_MULTIPATH_INTEGRAL_19S3_12S4_VERIFIED`.

# Limits

The checker establishes only the stated finite complex. An integral chain cancellation alone would not prove a wedge for arbitrary degrees, but here the absence of cells in dimensions one and two and the Hurewicz isomorphism for a wedge of three-spheres identify the remaining four-cell attaching maps. The assessment is not an independent audit.
