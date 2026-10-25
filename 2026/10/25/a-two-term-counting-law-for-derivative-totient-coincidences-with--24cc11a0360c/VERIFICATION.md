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

# Reproduction and limitations

Run `python3 verify.py` using Python 3.8+ and its standard library. The script checks 220 independent Diophantine enumerations for small prime pairs, verifies all qualifying two-prime integers up to 180000 by direct factorization and integer arithmetic, and checks 15 high integer cutoffs by two distinct exact constructions.

Observed result:

```
VERIFY_OK: 220 independent two-prime Diophantine enumerations; 3 direct semiprime-support equality cases through 180000; 15 exact high-cutoff counting comparisons.
Caution: asymptotic expansion is proved analytically, not by these finite tests.
```

The standalone code requires no external data, imports, URLs or hidden artifacts. Critical infinite ingredients are the exact Diophantine reduction, the \(O_p(1)\) Lambert cutoff control, the prime number theorem for fixed reduced residue classes, and the two-term logarithmic-integral expansion. The code does not simulate the limiting regime or certify originality.
