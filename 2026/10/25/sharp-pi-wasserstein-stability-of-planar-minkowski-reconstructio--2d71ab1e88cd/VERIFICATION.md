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

The theorem is established analytically in `RESULT.md`, using the published Green-kernel upper bound, a balanced explicit near-antipodal family, dual and primal transport certificates, exact Green-kernel evaluation, and positive smooth approximation.

Run `python3 verify.py` in the extracted package; no nonstandard dependencies are needed. The script checks signed masses, first moments, the explicit four-point transport potential, kernel evaluation, and numerical approach to the coefficient \(\pi\). The computation is finite supporting evidence only. There is no independent audit and no claim of computer certification of uniqueness or global mathematical priority.
