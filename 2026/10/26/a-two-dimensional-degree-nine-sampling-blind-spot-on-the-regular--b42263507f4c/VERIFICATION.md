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

Run `python3 checker.py` using the Python standard library. Actual replay output:

```
Exact Q(sqrt(2)) degree-nine rank-upper-bound checks: PASS
Modular exact ranks, degrees 0..115: PASS
Degrees 0..5: [1, 3, 5, 7, 9, 11] ; degrees 6..8: [12, 12, 12] ; degree 9: 10 ; all degrees 10..115: {12}
Global high-degree diagonal-dominance constants: PASS
Parameter-deformation degree-nine rank at a=2: PASS
ALL CHECKS PASSED
```

The quadratic-field checks are exact rational fraction operations. The finite-prime rank checks are exact modular elimination and use the certified prime 998244353 with a verified square root of 2; a nonzero minor after good reduction guarantees a nonzero minor in characteristic zero. The two explicitly supported null vectors prove the degree-nine upper bound. The computer checks stop at degree 115; the bound for the unbounded tail is proved analytically by Bernstein's Legendre inequality and diagonal dominance. No numerical tests are treated as a proof of an infinite statement.

The source comparison is bounded and does not amount to independent validation or a guarantee of publication priority. Independent audit and validation have not been performed.
