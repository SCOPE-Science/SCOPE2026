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

# Reproducible checks and limits

Run `python3 verify_grassmann_strong.py` with Python 3 standard library. This file builds line-subspaces of finite vector spaces, constructs actual Grassmann adjacency, enumerates maximal pairwise-intersecting families directly by graph-clique search, and independently counts the coefficient distribution by explicit subset generation for the three small instances below.

```
VERIFY_OK q=2 d=4 points=15 lines=35 stars=15 tops=15 cliques=3216
VERIFY_POLYNOMIAL_OK q=2 d=4 coefficients=1,35,315,945,1050,630,210,30
VERIFY_OK q=3 d=4 points=40 lines=130 stars=40 tops=40 cliques=648651
VERIFY_POLYNOMIAL_OK q=3 d=4 coefficients=1,130,3120,20800,56680,102960,137280,137280,102960,57200,22880,6240,1040,80
VERIFY_OK q=2 d=5 points=31 lines=155 stars=31 tops=155 cliques=1029728
VERIFY_POLYNOMIAL_OK q=2 d=5 coefficients=1,155,3255,18445,47740,96348,156240,199640,199485,155155,93093,42315,14105,3255,465,31
VERIFY_FINISHED all finite checks passed
```

The algorithm explicitly constructs finite field points only for prime \(q=2,3\), even though the mathematical theorem holds over every finite field of prime-power order. Finite instances are not infinite proofs; the complete proof is in `RESULT.md`. The maximal-clique structural theorem and general strong metric concepts are credited to prior literature, and mathematical priority is not independently certified.
