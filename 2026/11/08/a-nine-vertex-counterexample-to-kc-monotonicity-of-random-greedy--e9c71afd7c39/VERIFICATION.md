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

# Reproducible verification

Run `python3 verify.py` under Python 3.10 or newer. No external packages or data files are required.

The script reconstructs each finite tree on at most eight vertices from every possible Prüfer word, uses a complete rooted-tree encoding to retain one representative per unlabeled tree, and checks every proper bare-path KC transformation with exact `fractions.Fraction` recursion for the greedy expectation. The checked orders have \(1,1,1,2,3,6,11,23\) tree types and respectively \(0,0,0,1,4,13,35,93\) proper paths, for \(146\) nontrivial comparisons; every exact difference is positive, with minimum \(1/480\) among the 93 order-eight comparisons.

Independently, the script enumerates all \(9!=362880\) uniform vertex permutations of each exhibited tree. For \(T\), the numbers of orders producing sets of cardinalities \(3,4,5,6\) are respectively \(25984,139776,53760,143360\). For \(U\), they are \(35200,127680,53760,146240\). All counts sum to \(9!\); the exact means are \(73/15\) and \(34/7\) respectively.

The `VERIFY_OK` terminal line indicates that the rational recurrences, path coverage and independent permutation checks passed. Exhaustiveness is justified by the Prüfer bijection and completeness of the recursive tree encoding, not by the mere fact that a program terminated. The computation establishes a finite cutoff, not an assertion about trees on ten or more vertices. Independent external audit remains not performed.
