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

# Reproducibility and limits

Run `python3 verify_cliques.py` with Python 3 standard library. It directly enumerates every rank-one square-zero matrix and independently tests both matrix products for each pair. It computes graph maximal cliques using Bron–Kerbosch with adjacency bitmasks, then enumerates their subsets and checks *every coefficient* of the exact double Gaussian–Möbius polynomial. It checks maximal-clique multiplicities and image-span dimensions. No source network access or external packages are needed.

Successful completed checks:

```
PASS n=2 q=2 vertices=3 maximal=3 cliques=4 sizes={1: 3}
PASS n=3 q=2 vertices=21 maximal=14 cliques=78 sizes={3: 14}
PASS n=4 q=2 vertices=105 maximal=65 cliques=20436 sizes={7: 30, 9: 35}
PASS n=2 q=3 vertices=8 maximal=4 cliques=13 sizes={2: 4}
PASS n=3 q=3 vertices=104 maximal=26 cliques=6475 sizes={8: 26}
PASS n=2 q=5 vertices=24 maximal=6 cliques=91 sizes={4: 6}
VERIFY_OK_MAXIMAL_ZERO_PRODUCT_CLIQUES
```

The verifier implements prime-field arithmetic only (\(q=2,3,5\)); the proof uses linear algebra over arbitrary finite fields, including nonprime prime powers. Exhaustive small-field evidence does not constitute an infinite proof. The scientific review is not an independent audit.
