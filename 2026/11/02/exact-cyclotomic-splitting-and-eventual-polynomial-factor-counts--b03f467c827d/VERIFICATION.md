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
The supplied standalone `verify.py` uses only standard Python 3 and exact integer arithmetic. It enumerates Galois orbits of the roots of \(X^{d^n}-\alpha\) under congruence subgroups fixing a specified cyclotomic or quadratic base field, independently of the arithmetic closed formula. It checks 624 cyclotomic combinations, three levels over \(\mathbb Q(\sqrt5)\), three levels over \(\mathbb Q(\sqrt{-15})\), five alternate primitive targets, and the exact early-level transient identities.

The actual completed run from the supplied file printed:

```
VERIFY_OK independent_cyclotomic_orbits= 624 quadratic_subfield_orbits=6 nonstandard_targets=5 closed_formula=PASS transient_and_eventual_polynomial=PASS
```

Finite computations are consistency checks only. The mathematical proof is the Galois orbit count, exact root-order parametrization, the finite cyclotomic conductor and capped-exponent expansion in `RESULT.md`. The code does not attempt to verify all number fields or prove a universal theorem by enumeration. No independent audit has been performed.
