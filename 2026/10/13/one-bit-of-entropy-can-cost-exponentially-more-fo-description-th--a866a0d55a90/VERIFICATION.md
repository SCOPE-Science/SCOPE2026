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

The bundled `verify.py` checks the specialization of the published formula-size bounds for \(k=2,\ldots,10\). For each \(k\), it verifies the exact entropy levels of the two uniform type distributions, the leading normalized description-complexity coefficients \(3/2^k\) and \(3/2\), and their quotient \(2^{k-1}\).

It also chooses a large model size divisible by \(2^k\) and checks that the ratio bounds obtained from the finite additive constants squeeze the target limiting ratio. This does not numerically compute minimum FO formulas; correctness of the asymptotic rests on the cited upper and lower theorems plus the algebra in `RESULT.md`.

Run:

```text
python3 verify.py
```

A successful replay ends with `VERIFY_OK 72 exact assertions`.
