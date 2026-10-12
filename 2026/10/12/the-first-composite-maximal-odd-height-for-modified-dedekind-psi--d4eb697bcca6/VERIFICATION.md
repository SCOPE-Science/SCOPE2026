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

# Verification of the finite classification

The theorem reduces the infinite search at each height through 23 to a provably sufficient finite universe. Execute `python3 verify_defant_B23.py` using the Python standard library. The program constructs an exact smallest-prime-factor sieve and the completely additive recurrence, determines all record odd elements for 22 heights, and independently evaluates the defining arithmetic iterate on selected records and all possible larger competitors for the rank-23 maximum.

Actual executed output begins:

```
EXACT_CERTIFICATE_OK first_composite_class=23 B23=8193151 prime_max_23=8126431 suffix_checked=97728
```

The full printed table of maxima can be regenerated from the source file. The package contains no separate third-party proof assistant or independent audit. The identity between additive recurrence and original iteration is proved in `RESULT.md` and is not inferred from numerical coincidence.
