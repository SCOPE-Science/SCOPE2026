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

# Verification

Execute `python3 verify.py` under Python 3. The test file is standalone and uses only the standard library. It enumerates all matrices over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) in the indicated small dimensions, selects idempotents, computes each actual product-rank quadruple, and compares every possible stratum with the exact formula. The implementation of \(\mathbb F_4\) uses binary polynomials modulo \(x^2+x+1\), not integer arithmetic modulo four. Separate arithmetic checks confirm the two-idempotent rank margins and reversal symmetry through dimension five and several field orders.

Actual successful run output:

```
PASS exhaustive 2 2 idempotents 8 pairs 64 nonempty strata 12
PASS exhaustive 3 2 idempotents 14 pairs 196 nonempty strata 12
PASS exhaustive 4 2 idempotents 22 pairs 484 nonempty strata 12
PASS exhaustive 2 3 idempotents 58 pairs 3364 nonempty strata 28
PASS exhaustive 3 3 idempotents 236 pairs 55696 nonempty strata 28
PASS exhaustive 2 4 idempotents 802 pairs 643204 nonempty strata 57
PASS totals/swap 2 5
PASS totals/swap 3 5
PASS totals/swap 4 5
PASS totals/swap 5 5
PASS totals/swap 7 5
PASS totals/swap 8 5
VERIFY_OK
```

The symbolic proof, rather than the finite test scope, establishes all dimensions and prime powers. Published exact equivalence/novelty remains subject to independent literature review. Independent audit has not been performed.
