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

Run `python verify.py` in the directory containing the standalone checker. It enumerates all vertex tetrahedra for each polygon order from 3 through 13 at five periodic twist values and two radius/height choices; its expected terminal line reports 110 passed enumerations and six exact-formula specializations.

The checker uses only Python's standard library. Numerical determinants are compared at explicit tolerances; the checks are finite regressions and do not establish universal quantifiers. For the infinite proof, verify the difference-body identification, equation (5), and the strict triangle comparison in equations (6)--(7) directly in RESULT.md. No external validation or independent certification is asserted.
