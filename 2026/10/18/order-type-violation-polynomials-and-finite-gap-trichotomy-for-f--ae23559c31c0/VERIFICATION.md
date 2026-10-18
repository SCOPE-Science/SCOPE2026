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

# Reproducibility and checks

Run `python verify.py` with Python 3's standard library. The program generates canonical boundary-marked weak order types in the \(k+2\)-element chain, counts violating types, predicts counts on chains of sizes \(2\) through \(9\), and separately exhausts all tuples to compare. It tests 201 equations over one through three variables, 153624 tuple evaluations, 4259 per-equation canonical-pattern visits, and 16 products of two finite Gödel chains.

Observed output:
```
VERIFY_OK equations=201 tuple_assignments=153624 canonical_patterns=4259 product_pairs=16
double-negation-top [1, 0]
double-negation-elimination [0, 1]
material-implication [0, 1, 1]
reflexivity [0, 0]
excluded-middle [0, 1]
comparison [2, 4, 2]
```

The exact infinite-chain-size claim follows from the order-embedding lemma and the binomial count, not from tested bounds. The finite-product gap follows from coordinatewise equation satisfaction. This is self-review with reproducible computational sanity tests, **not** independent mathematical validation.
