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
Run `python3 revival_proof_check.py` in a Python 3 environment with no third-party dependencies. The script reconstructs the system-plus-environment unitary, applies the exact joint reset channel, traces the environment, and compares the excitation probability against independent iteration of the analytical three-variable matrix at 20 parameter combinations. It also checks the two-collision expression and representative small-exchange revival-count scaling.

The included execution completed 1,432 assertions successfully. The proof's analytic conclusions concern all sufficiently small positive exchange defects at each fixed retention; these cannot be established by a finite test. The source's dynamics and all reference comparisons must be read with that distinction.
