---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility

Run `python3 verify_link_wedges.py` with Python 3.9 or later and the standard library. The program reconstructs all twelve links, verifies acyclicity of the staged matchings on the complete nonempty-face Hasse diagrams, independently sums the signed gradient paths defining the integral attaching degrees, and checks the CW-cell and wedge counts. The expected terminal line is `ALL_12_FRUCHT_LINK_WEDGES_OK`. The accompanying mathematical argument turns these degrees into homotopy types. No mod-two homology or suspension alone is used for that conclusion.
