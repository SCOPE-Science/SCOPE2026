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

# Reproduction and limits

Run `python3 verify.py` using the Python standard library. The program computes each gcd-reduced binomial-row sum directly through index 320, verifies fifteen source sequence values, and constructs the binomial probability masses as exact fractions. For every test index it checks the exact decomposition, a rational upper bound on the replacement mass, the primitive-binomial versus totient bound, and the resulting pointwise estimate. It also checks all 1,901 modular-discrepancy cases with \(d\mid n\) for these indices.

Recorded successful output:

```
VERIFY_OK: 320 exact reduced-binomial rows; 1901 residue-class inequalities; 15 OEIS initial values; mean through 320 = 0.386319266652; proposed exact limit = 0.392072898146
```

The independent finite calculation verifies instances and the implementation of the finite formulas. It does not certify the infinite theorem, which requires the full summation-by-parts, Möbius and averaging arguments in `RESULT.md`. There has been no independent mathematical audit.
