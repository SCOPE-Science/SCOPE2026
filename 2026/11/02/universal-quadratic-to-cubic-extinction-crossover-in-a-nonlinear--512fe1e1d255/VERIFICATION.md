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
# Verification and limits

The attached `verification/check.py` independently differentiates the exact coordinate reduction using SymPy and checks the cubic coefficient. Numerical integrations for a strictly admissible parameter slice compare shrinking-\(\sigma\) trajectories to the analytically defined inverse profile. These are finite corroborations; the analytical invariant-tube and dominated-convergence argument in RESULT.md proves the infinite-time and zero-parameter limits. Independent validation and independent audit have not been performed.
