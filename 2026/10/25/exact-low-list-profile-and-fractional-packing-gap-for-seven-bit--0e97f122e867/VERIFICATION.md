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

Run `python3 verify.py` with `seven_list_certificates.json` in the same directory. This independently reconstructs all incidence entries and verifies six explicit codebooks and six rational upper-bound certificates using exact integer arithmetic. At list budget two it additionally checks a rational feasible primal vector proving the fractional optimum. A completed run prints `VERIFY_OK`. No numerical optimizer is required to replay the proof; no claim is made for longer blocks or other list budgets.
