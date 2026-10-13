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

The standalone `verify.py` artifact was read from its actual packaged path before replay. It checks exact Boolean quotient determinants through rank five, all at-most-one-white type profiles through rank four, complete graph-level forcing polynomials in representative nonfield cases, exact rational adjacency ranks, and subset-product reconstruction with repeated local counts.

```text
B_2: types=2, determinant=-1
B_3: types=6, determinant=-1
B_4: types=14, determinant=-1
B_5: types=30, determinant=-1
B_2: all 4 at-most-one-white profiles force
B_3: all 64 at-most-one-white profiles force
B_4: all 16384 at-most-one-white profiles force
lambda=(2, 2): N=4, Z=2, minimum_sets=4
lambda=(2, 3): N=5, Z=3, minimum_sets=6
lambda=(2, 2, 2): N=18, Z=12, minimum_sets=512
lambda=(2, 3): adjacency_rank=2
lambda=(2, 2, 2): adjacency_rank=6
lambda=(2, 2, 2, 2): adjacency_rank=14
recovery (2, 2) -> (2, 2)
recovery (2, 5) -> (2, 5)
recovery (2, 2, 2) -> (2, 2, 2)
recovery (2, 3, 4) -> (2, 3, 4)
recovery (2, 2, 3, 5) -> (2, 2, 3, 5)
recovery (2, 3, 3, 4, 7) -> (2, 3, 3, 4, 7)
VERIFY_OK
```

The finite checks are corroborative. The arbitrary-r theorem is proved symbolically in `RESULT.md`.
