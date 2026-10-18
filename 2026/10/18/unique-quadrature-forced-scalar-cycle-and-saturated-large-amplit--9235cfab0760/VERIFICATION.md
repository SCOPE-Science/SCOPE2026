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

`python3 verify.py` was executed against the packaged script. It printed `CHECK_OK`, with representative coefficients 0.1, 1, 4, 12 and 40 and numerically evaluated phase roots and multipliers. The proof's crossing monotonicity, global uniqueness, invariant sign arcs, return-map basin classification, and endpoint Laplace asymptotics are analytical; the script tests particular evaluations only. No independent audit has been performed. The external evidence is literature comparison, not independent certification.
