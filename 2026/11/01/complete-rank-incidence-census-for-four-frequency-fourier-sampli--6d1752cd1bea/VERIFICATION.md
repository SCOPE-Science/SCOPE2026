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

Exact integer cyclotomic rank computation has been completed for every representative row orbit and every four-element column subset. Run `python3 verify_fourier15.py`; successful output ends with `EXACT_CERTIFICATE_OK` and the expected exact rank totals. The script uses no external files or numerical approximations. It checks affine-orbit exhaustiveness, every orbit-by-orbit rank count and transposition reciprocity. The calculation is finite and exhaustive; no assertion is made about other matrix sizes, higher minors, or numerical conditioning.

The evaluation is an internal self-review only. No independent audit or independent validation has been performed.
