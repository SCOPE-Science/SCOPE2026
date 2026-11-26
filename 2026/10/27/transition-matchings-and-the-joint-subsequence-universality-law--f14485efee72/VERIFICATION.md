---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Reproducibility and limits

Run `python3 verify.py` (standard library only). The program computes path matching numbers by a dynamic recurrence, verifies conditional means for every transition budget through eleven edge positions, and checks the single-swap inequality for all swaps through eight positions. It does not prove the all-length result, the coupling inequality for the martingale, the deviation bound, or the density limit; those arguments are in `RESULT.md`.
