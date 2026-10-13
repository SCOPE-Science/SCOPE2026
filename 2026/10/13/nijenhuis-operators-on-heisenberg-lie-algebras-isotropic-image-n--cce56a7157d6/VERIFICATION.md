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

# Reproducibility and verification

Execute `python3 verify.py` with Python 3.9 or later; no external packages are needed. The script performs complete direct Nijenhuis-equation checking over the two small fields for three-dimensional operators; complete symplectic-isotropic matrix rank counts over several small cases, including dimension four in characteristic two; and deterministic randomly selected larger matrices. Successful execution prints `VERIFY_OK`.

The defining operator equation is checked directly against the normal-form characterization on every enumerated case. The general proof is symbolic and field-independent; finite checks do not establish universal correctness or exclude inaccessible prior results. No external independent validation or audit is asserted.
