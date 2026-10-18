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

# Verification and limits

**Theorem-side checks.** The proof isolates the exact possible cardinalities of \(B\cup C\) when \(|B|=i\) and \(|C|=j\), including overlap, then analyzes the infinite-cardinality case separately. Its characteristic formulas have depth bounded by their displayed index and recover every size up to \(2^d\). The size-zero and size-one base predicates are interpreted consistently across every powerset model.

**Independent finite replay.** Extract `check_union_modal.py` from this package and run `python3 check_union_modal.py`. The checker uses Python's standard library, a direct powerset semantics independent from a cardinality abstraction, and structural characteristic-formula construction. Expected output:

```
BINARY_UNION_DEPTH_VERIFY_OK profiles=3,4,6,10,18,34 subset_semantics=35770 characteristic_checks=9709
```

The profile test covers sizes through \(70\) and depths through \(5\); direct subset checks cover ground sets of sizes \(0\) through \(8\) and randomly generated nested modal formulas. No finite enumeration proves infinite correctness. The theoretical argument is a complete induction applying to every finite or infinite ground set. Open questions of historical priority and broader-language extensions remain outside these checks.
