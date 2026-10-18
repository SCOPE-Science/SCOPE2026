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

# Reproducibility and verification limits

Run `python3 verify.py` with a Python standard-library interpreter. In the scientific verification session the script completed with

```
PASS: 660 exact rational identities; 825 numerical checks
Thresholds: [(2, 1.38629436112), (3, 1.586982565894), (4, 1.686646511539), (5, 1.747037807507), (10, 1.870577951733), (100, 1.986710551422), (1000, 1.998667110548)]
n=2..5 at lambda=1.5: [1.553739679703, 1.582900341777, 1.573877361149, 1.563553606045]
```

The rational checks use `fractions.Fraction` to prove the finite computed instances of the majorization partial-sum identity and the factorization identity with rational test points. Other checks use floating-point evaluations of the exact formulas and high-precision bisection in bounded finite ranges. Numerical comparisons use explicitly stated tolerances, and the infinite theorem does **not** follow from these checks. The general proof is analytical in `RESULT.md`, including the strict convexity/majorization argument and the uniform asymptotic remainder bound. This package contains no formal proof-assistant certificate or independent external audit.
