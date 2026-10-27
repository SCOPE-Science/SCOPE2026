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

# Reproduction

Run `python3 verify.py` using Python 3 standard library only. This code enumerates all qualifying smallest-size sets for prime moduli 7, 11, 13, 17 and 19, confirms \(5A\) is not the whole field for the two-element witness modulo seven, and checks 270 seeded sample subsets over four additional prime powers. Its expected terminal line begins `CERTIFICATE_OK`.

The proof relies on Kneser's sumset theorem, the structure of subgroups of a cyclic prime-power group, and a seven-class enumeration; no computational assertion is used to establish the infinite theorem. All boundaries, including exponent one and the strict-density condition, are mathematical statements proved in RESULT.md.
