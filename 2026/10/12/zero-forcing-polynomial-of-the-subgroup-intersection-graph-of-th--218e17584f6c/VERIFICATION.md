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

The standalone `verify.py` artifact was read from its actual packaged path before replay.

For \(p=3\), it tests all \(131072\) initial blue subsets of the \(17\)-vertex abstract graph. It verifies the accepted-set criterion subset-by-subset and compares the entire coefficient dictionary with the closed product formula.

It independently constructs the exponent-\(p\) Heisenberg group for \(p=3\) and \(p=5\), enumerates all order-\(p\) subgroups and projective-line maximal subgroups, and checks every subgroup-intersection edge against the claimed graph.

Finally it expands the closed formula for \(p=3,5,7,11\) and checks the minimum exponent \(p^2\) and minimum coefficient \((2p+1)p^p\).

Exact replay output:

```text
p=3 full polynomial: {9: 189, 10: 918, 11: 1848, 12: 2005, 13: 1286, 14: 508, 15: 124, 16: 17, 17: 1}
p=3 characterization checked on all 2^17 subsets
Heisenberg p=3: 17 proper nontrivial subgroups, graph pattern OK
Heisenberg p=5: 37 proper nontrivial subgroups, graph pattern OK
p=3: Z=9, min_count=189, polynomial_at_1=6896
p=5: Z=25, min_count=34375, polynomial_at_1=4971968
p=7: Z=49, min_count=12353145, polynomial_at_1=7114145536
p=11: Z=121, min_count=6562168424053, polynomial_at_1=60185692241063936
VERIFY_OK
```

The finite computations are corroborative; the arbitrary-prime theorem is proved by the subgroup-lattice reduction and the necessary-and-sufficient forcing criterion.
