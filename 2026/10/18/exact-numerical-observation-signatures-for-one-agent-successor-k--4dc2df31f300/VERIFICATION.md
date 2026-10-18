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

Run `python check_signature.py` using Python 3. The self-contained checker depends only on the standard library. It implements the original S5 possible-world truth clauses of ordinary knowledge and conditional knowing value separately from the proposed support-signature recursion.

It tests all nonempty subsets of values \(\{0,\ldots,k+2\}\), all pointed support values, 80 pseudorandom formulas per parameter with modal nesting up to depth four, and additional worlds with repeated numeric values, for each \(k=0,1,2,3\). The fixed seed is recorded directly in code.

Observed output:

```text
k=0: signatures=2 optimal_max_worlds=2
k=1: signatures=7 optimal_max_worlds=3
k=2: signatures=20 optimal_max_worlds=4
k=3: signatures=52 optimal_max_worlds=5
KNOWING_VALUE_SIGNATURE_VERIFY_OK 82880
```

The checker explicitly verifies the proposed canonical representative signature and size on each of these finite cases. The unrestricted theorem is proved by induction and finite combinatorial counting in `RESULT.md`. The checks do not enumerate all formulas, all sizes, or infinite structures, and no independent audit has been performed.
