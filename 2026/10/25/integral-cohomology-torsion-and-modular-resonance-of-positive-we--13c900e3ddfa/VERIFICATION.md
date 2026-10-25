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

# Reproducibility and limits

Execute `python verify.py` with a Python environment containing SymPy. The checker builds the differential from bracket evaluations, tests `d*d=0`, verifies integer Smith normal forms, and checks modular cohomology dimensions independently by elimination over five prime fields for seven weight lists. Successful execution prints `VERIFY_OK`. No finite computation proves the unrestricted formula: the proof is the two-term integral cochain decomposition. The checker covers the specified cases only.
