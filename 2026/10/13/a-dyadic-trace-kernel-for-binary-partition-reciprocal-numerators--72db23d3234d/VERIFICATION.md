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

The accompanying self-contained `verify.py` compares every coefficient of the exact binary-partition numerator with the independent dyadic-kernel construction for all integers from 2 through 100. It checks the evenness needed for division by two, that the kernel evaluates to one at the characteristic-two point x=1, and the first-coefficient congruence. This is finite corroboration; the proof gives the all-index result. The exact modular root order is deduced algebraically, not from numerical tests.

Observed output:

`PASS: all coefficients and exact modular-root multiplicity, n=2..100`
