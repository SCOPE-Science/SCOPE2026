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

# Computational verification and boundaries

The standalone file `verify.py` uses Python 3.8+ and only the standard library. Execute `python verify.py` in a directory containing that file. It builds the two-layer adjacency matrix from the edges of two complete graphs joined by a matching, applies the actual blue-vertex zero-forcing rule until closure, and exhaustively checks every initial white set for orders \(n=2,3,4,5,6,7,8\). Separately, it checks the defining fort predicate on all subsets for \(n=2,3,4,5,6,7\) and tests each fort against **every proper fort subset** to decide inclusion-minimality. Both checks compare exact labeled sets or entire polynomial coefficient dictionaries, not just scalar parameters.

Actual verifier output:

```
n=2 subsets=16 success=9 minimal_forts=2
n=3 subsets=64 success=36 minimal_forts=9
n=4 subsets=256 success=119 minimal_forts=44
n=5 subsets=1024 success=328 minimal_forts=110
n=6 subsets=4096 success=823 minimal_forts=237
n=7 subsets=16384 success=1956 minimal_forts=455
n=8 subsets=65536 success=4495 minimal_forts=unexamined
VERIFY_OK direct_subsets=87376 complete_polynomial_orders=7 exact_minimal_fort_orders=6
```

The exact full coefficient dictionaries agree at every tested order, and the exact lists of inclusion-minimal forts agree for all six fully enumerated orders. The tests do not establish the formulas beyond their finite ranges. The general theorem relies on the neighborhood-count proof, exhaustive case partition, and binomial enumeration in `RESULT.md`. The independent-audit channel remains not performed.
