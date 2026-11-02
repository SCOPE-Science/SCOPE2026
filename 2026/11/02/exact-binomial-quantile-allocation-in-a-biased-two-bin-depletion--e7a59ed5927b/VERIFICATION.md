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

# Verification of the two-bin quantile theorem

The reproducible finite checks require only Python's standard library:

```sh
python verify.py
```

They compare a rational dynamic program for the two-bin removal process to an independently evaluated \(\operatorname{Bin}(n,p)\) loss formula, all forward differences, and the predicted minimizing integer allocations. The script tests eight exact rational values of \(p\), totals \(2\le n\le27\), and both endpoint allocations. It reports `PASS: 7074 exact-rational assertions` when every check succeeds. It separately checks the unequal-selection example \((n,p)=(6,5/6)\).

The infinite-domain proof is the stopped-independent-sequence identity, exact discrete convexity, and a standard central-limit/Berry–Esseen argument. Finite computation is not a substitute for those steps. The theorem makes no assertion for more than two bins or for a varying \(p\) regime. Independent validation has not been performed.
