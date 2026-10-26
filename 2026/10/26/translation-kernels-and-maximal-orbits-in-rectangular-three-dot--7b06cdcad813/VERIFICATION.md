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

# Reproducibility and verification

The analytic argument is in `RESULT.md`. Run `python3 verify.py` in a Python 3 standard-library environment. Expected terminal output:

```text
VERIFY_OK polynomial_cases=196 physical_rank_cases=94 kernel_cases=40 full_orbit_witness_cases=35 additional_rank_cases=7
```

Checks compare polynomial gcd degree with the predicted value in 196 parameter cases; finite-array equation rank with the quotient dimension in 94; both shift orders and full joint kernel in 40; and the predicted full-orbit witness in 35. A further seven independent finite-array ranks are included. These finite tests neither determine the behavior for all parameters nor establish historical novelty; the unrestricted proof is algebraic.
