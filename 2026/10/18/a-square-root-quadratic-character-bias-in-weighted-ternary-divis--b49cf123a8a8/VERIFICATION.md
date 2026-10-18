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

# Reproducible verification

The standalone Python 3 program `verify.py` uses only the standard library and exact rational arithmetic. Execute `python3 verify.py`. Its independent algorithms (prime-exponent formula versus the arithmetic convolution with a square indicator) agreed for every integer \(1\le n\le20{,}000\), producing:

```
EXACT_COEFFICIENT_IDENTITIES 20000
MOD3_DIFFERENCE 211/9
VERIFY_OK
```

The rational value \(211/9\) is the computed difference between the two reduced congruence classes modulo \(3\) through \(20{,}000\). Neither the finite identity check nor this one sampled difference is an asymptotic proof. The proof of the universal claim instead consists of the formal Euler-series identity, exact character hyperbola decomposition, absolutely convergent tail estimates, and positivity of the real quadratic \(L\)-value and Euler product. All assertions about \(x\to\infty\) depend on those explicit analytic steps.

Independent audit has not been performed. No rate optimality or broader modulus uniformity has been verified.
