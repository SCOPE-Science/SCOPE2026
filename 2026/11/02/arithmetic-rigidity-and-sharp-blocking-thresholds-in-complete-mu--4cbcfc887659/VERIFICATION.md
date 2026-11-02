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

# Verification method and limits

Run `python3 verify_multipartite.py` with Python 3 (standard library only). The checker independently enumerates all set partitions of labeled agents for \(2\le t\le 4\), each type size \(1\), \(2\), or \(3\), total size at most \(9\). It tests both same-type enemies and same-type neutrals, calculates actual Nash stability by testing every unilateral move, and compares with the exact all-type balanced characterization and divisor-sum count. For total population size at most \(7\), it also tests all nonempty deviating coalitions and compares minimum fully-strict and weak-with-one-strict blocker sizes.

Expected exact output:

```
PASS 102 type-size profiles; 948546 set partitions; 316 Nash instances; 300 blocking minima
Examples: [2,2,2] -> 5 ; [3,3,3] -> 37 ; [2,2,2,2] -> 9
```

The finite test is an error detector rather than an exhaustive check of arbitrary populations. The proof in RESULT.md establishes all-size statements by exact inequalities, elementary cardinality algebra, and explicit constructions. The manuscript does not claim computer-assisted proof, independent auditing, a literature novelty certificate, or applicability outside the specified lexicographic model.
