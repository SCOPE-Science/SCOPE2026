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

# Exact reproducibility instructions

Run `python3 verify.py` using Python 3 standard library only. The script rebuilds the graph, the complete face set, and each elementary collapse; no stored face lists, precomputed matrices or imported certificates are assumed. Its independent field-chain check uses the original residual simplicial boundary, not the simplified group presentation. Successful execution ends with `ALL_VERIFY_OK`.

Expected exact counts: 808 original nonempty faces, 256 elementary simplicial collapses, 296 surviving nonempty faces in dimensions zero through two, 104 homotopy-preserving one/two-cell cancellations, one surviving circle, 42 constant two-cell attachments, 14 degree-two attachments. Direct second-boundary ranks are 104 modulo two and 105 modulo three and five. The one degree-two attachment creates a standard projective plane; the other 55 two-cells attach nullhomotopically.

All checks concern the stated finite Clebsch graph; no infinite family, equivariant homotopy classification, independent audit, or absence of unindexed prior work is asserted.
