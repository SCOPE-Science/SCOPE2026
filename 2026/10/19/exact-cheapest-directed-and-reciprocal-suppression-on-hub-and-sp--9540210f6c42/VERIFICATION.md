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

# Reproduction and verification

Run `python3 verify.py` in a directory containing the corresponding standalone script. It uses only Python's standard library. It enumerates a finite set of rational directed attenuation profiles, checks exact determinant/Schur identities, verifies the three-spoke example and both limits of the sharp factor bound. Any failure exits with a nonzero status, and success prints `VERIFY_OK`.

These checks do not prove the theorem for arbitrary real-valued coefficients, arbitrary population size, or a nonlinear epidemic. The analytical proof handles these quantifiers. There is no external formal proof certificate or independent audit.
