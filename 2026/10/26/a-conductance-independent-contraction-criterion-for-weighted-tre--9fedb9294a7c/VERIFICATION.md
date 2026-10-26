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

# Reproducibility and verification

The proof is contained in `RESULT.md`; no external compiler, proof assistant, or inaccessible data is needed. Run `python check.py` with Python 3's standard library. The executed output is:

```
PASS: exactly 18248 labeled-tree classifications;
PASS: 150 weighted rational generator identities and small-time tests.
Finite checks are diagnostics, not a proof of the universal theorem.
```

The Prüfer enumeration is exhaustive only for labeled trees on at most seven vertices. It checks the theorem's uniform-mass topology consequence over that **finite** range. Separate independent rational calculations check all off-diagonal edge-generator entries, exact absolute-column sums, and 150 small-time numerical comparisons with the matrix exponential. The all-tree statement instead depends on the incidence-surjectivity, logarithmic-matrix-norm, Perron–Frobenius and vertex-degree proofs in `RESULT.md`. This document reports finite diagnostics and their limitations; no independent audit is claimed.
