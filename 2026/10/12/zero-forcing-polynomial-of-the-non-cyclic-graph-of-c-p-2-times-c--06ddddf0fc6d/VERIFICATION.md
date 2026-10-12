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

The standalone `verify.py` artifact was read from its packaged path before replay.

For \(p=2,3,5\), it constructs every element of
\[
C_{p^2}\times C_p,
\]
forms every cyclic subgroup directly, and builds the non-cyclic graph without using the claimed quotient structure. It then reconstructs the \(P,A_i,B_j\) classes from element coordinates and checks their sizes, every interclass adjacency, and the false-twin property.

For each tested prime, every admissible white-class subset is replayed on the full vertex graph and weighted by the exact number of representative choices. The resulting complete polynomial is compared with the closed formula. For \(p=2\), all \(2^7\) vertex subsets are also exhaustively tested independently.

Finally, the closed profile criterion and coefficient identities are checked for \(p=3,5,7,11\).

Exact replay output:

```text
p=2: N=7, class_sizes=P:1, A:2x2, B:1x2, polynomial={7: 1, 6: 7, 5: 18, 4: 20}
p=3: N=26, class_sizes=P:2, A:6x3, B:2x3, polynomial={26: 1, 25: 26, 24: 276, 23: 1080, 22: 1296}
p=5: N=124, class_sizes=P:4, A:20x5, B:4x5, polynomial={124: 1, 123: 124, 122: 6640, 121: 104000, 120: 320000}
p=2 exhaustive_all_subsets={4: 20, 5: 18, 6: 7, 7: 1}
p=3: profile_formula_OK min_omitted=4 min_sets=1296
p=5: profile_formula_OK min_omitted=4 min_sets=320000
p=7: profile_formula_OK min_omitted=4 min_sets=9335088
p=11: profile_formula_OK min_omitted=4 min_sets=732050000
VERIFY_OK
```

The finite checks corroborate the proof but do not replace it. The arbitrary-prime result is proved by the subgroup partition, the false-twin obstruction, and the necessary-and-sufficient class-peeling criterion in `RESULT.md`.
