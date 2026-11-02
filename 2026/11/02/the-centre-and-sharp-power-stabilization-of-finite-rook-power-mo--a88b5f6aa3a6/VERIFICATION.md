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

# Verification record

The theorem is proved symbolically in `RESULT.md`; the accompanying script uses only the Python standard library. Run from the directory containing `verify.py` with `python verify.py`.

The script independently enumerates partial bijections and computes setwise products for \(n\in\{1,2,3\}\). For \(n=1,2\), it checks every nonempty subset for centrality against every base singleton. For \(n=3\), it checks every predicted central subset and every pair of predicted central products, but does not enumerate all \(2^{34}-1\) nonempty subsets. It also checks rank-support multiplication, idempotence and the power-stabilization identity through \(n=9\) by exact integer arithmetic.

Observed output:

```
n=1: elements=2, central_candidates=3, central_idempotents=3, exponent=1, exhaustive=True, verified
n=2: elements=7, central_candidates=7, central_idempotents=5, exponent=2, exhaustive=True, verified
n=3: elements=34, central_candidates=15, central_idempotents=7, exponent=3, exhaustive=False, verified
rank-index exact arithmetic verified for n=1..9
VERIFY_OK
```

The proof's necessity argument, not the finite search, establishes that no additional central subsets occur when \(n\ge3\). Neither symbolic checks nor finite enumerations are an external independent mathematical audit.
