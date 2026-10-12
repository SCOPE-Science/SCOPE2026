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

# Exact finite verification

Execute `python3 verify.py` using Python 3.10 or later with assertions enabled. The checker builds every binary even word at the five specified orders, constructs every permutation, and enumerates every complementary split of its positions. An explicit cyclic family is checked against every word for each upper bound.

For lower bounds through order five, a second representation builds pair-compatibility masks and exhaustively unions every candidate permutation coverage vector. The maximum numbers of words covered by one permutation at orders two and three are \(6\) and \(28\); at orders four and five, the maximum numbers covered by two permutations are \(126\) and \(496\). For order six, the checker uses nine explicitly displayed even words; across all \(720\) permutations their neighborhoods produce \(73\) signatures, none of whose three-fold unions contains all nine word-indices. The superset table contains exactly \(512\) entries and exhausts all possible third permutations.

The checker was executed from its package path and returned:

```
VERIFY_OK m2(2..6)=2,2,3,3,4 upper-even=8,32,128,512,2048 n6_obstructions=9 n6_signatures=73 max_pair_n4=126 max_pair_n5=496
```

All arithmetic and comparisons are exact finite integer/string operations. The finite classification is proved by exhaustive enumeration and does not imply values at higher orders. No independent external audit has been performed.
