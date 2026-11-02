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

Run `python3 verify.py` with Python 3 and only its standard library. It enumerates all cyclic binary hosts of optimum length for forbidden runs of 2 and 3 zeros; the resulting necklace counts are 1 and 8. For forbidden-run parameters 2 through 6, it independently builds the augmented directed graph and computes exact Laplacian cofactors with fraction-free Bareiss elimination. The results are 2, 16, 2048, 67108864, 144115188075855872, agreeing with the twice-optimum-necklace formula. It also builds 25 randomized Eulerian tours at each forbidden-run parameter 2 through 10 and verifies each exact window multiset.

Expected terminal line:

```
VERIFY_OK cyclic_exhaustive_r=2,3 matrix_tree_r=2..6 constructed_r=2..10 instances=225
```

Finite enumeration and matrix checks verify the sampled domains only. The proof for arbitrarily large forbidden-run length is the vertex-contraction bijection in RESULT.md. The ordinary de Bruijn enumeration formula is a classical theorem, not certified by this finite script. No independent audit has been performed.
