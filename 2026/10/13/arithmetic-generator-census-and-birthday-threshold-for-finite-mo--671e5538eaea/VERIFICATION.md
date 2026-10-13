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

The standalone standard-library Python script `verify.py` was executed from the accompanying package. It independently constructs the full closure of sample generating tuples under coordinatewise MV negation and truncated addition and the global minimum/maximum quantifiers, rather than merely testing the proposed structural criterion. It checks every ordered tuple across 25 finite parameter combinations, compares the gcd-and-word criterion with actual algebra generation, and compares the totals with the Möbius formula.

Observed output:

```
VERIFY_OK direct_mv_generation_tuples 5968 direct_parameter_cases 25 independent_signature_censuses 53
samples (6, 480, 228, 528, 2)
PEAK_TERMS_OK 14 BIRTHDAY_SAMPLES [(8, 81, 0.60905), (10, 243, 0.60736), (12, 729, 0.60681)] limit 0.60653
```

The `PEAK_TERMS_OK` tests separately construct unary term-function closures and find the Boolean peaks at every truth-chain value up to a five-element chain. The birthday calculations illustrate convergence for the three-valued chain. They are finite checks and do not prove the general interpolation or asymptotic theorems. The general proof is given in `RESULT.md`, citing the classical McNaughton theorem for unary term interpolation.

Reproduce with `python3 verify.py`. The script imports only Python standard-library modules, does not use network resources, and reports an assertion failure on any discrepancy.
