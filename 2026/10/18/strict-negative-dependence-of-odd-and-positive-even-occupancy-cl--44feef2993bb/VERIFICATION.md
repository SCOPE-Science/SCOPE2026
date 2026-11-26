---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

# Verification

Run `python3 verify_parity_occupancy.py` with the standard library. The program enumerates weighted allocations for specified unequal box probabilities, checks the ordered-pair covariance formula on these samples, and checks strict signs for qualifying pairs and for the aggregate under the global pair bound. The unrestricted result relies on the analytic proof, not the finite grid.
