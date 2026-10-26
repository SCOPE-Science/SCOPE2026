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

The exact proof is in RESULT.md. The standalone `verify.py` uses exact rational coefficients for 45 matrix-pencil discriminants and characteristic expansions, 1,200 reproducibly seeded floating-point bound checks, and nine sharp witness checks, for 1,254 checks in total; it prints `VERIFY_OK 1254`. It does not serve as a proof for all dimensions, all inputs, or all sketching parameters. A full independent scientific audit has not been performed.
