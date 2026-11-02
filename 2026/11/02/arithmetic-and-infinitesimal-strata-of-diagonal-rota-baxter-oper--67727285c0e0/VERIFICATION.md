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
# Reproducibility checks

Run `python verify.py` in the same directory as this file. The script uses Python's standard library and needs no network access. It independently enumerates every diagonal coefficient tuple for 44 small prime-field pairs of dimension and weight, checks the Rota–Baxter basis equations rather than using the closed classification, enumerates actual cyclic-rotation orbits, and checks Jacobian tangent dimensions for all nonzero-weight prime-field solutions. Three separate binary extension fields are checked using explicitly encoded polynomial-basis arithmetic. Observed output:

```text
VERIFY_OK prime_field_parameter_cases= 44
VERIFY_OK extension_field_cases=3
```

**Limits:** no finite enumeration proves the result for arbitrary dimensions or fields; the cyclotomic scheme lengths and nonreduced claims are proved symbolically in RESULT.md. The independent audit has not been performed.
