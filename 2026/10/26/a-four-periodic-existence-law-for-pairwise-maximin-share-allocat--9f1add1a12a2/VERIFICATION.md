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

# Exact verification and limits

Run `python3 verify.py` using a standard Python 3 interpreter. The program depends only on `functools` and built-in `itertools` and represents all weights/counts as integers.

The run enumerates all class-count allocations in the balanced cases \(k=4,\ldots,13\): \(20\) partitions of \(A\), \(56\) of \(B\) and \(56\) of \(C\), or \(62{,}720\) raw labeled multiplicity assignments per \(k\). With capacity constraints and necessary-and-sufficient optimized deficit checks, valid allocation counts are \(28,24,8,0,0,0,0,0,0,0\). In particular, complete counts are zero for each \(k=7,\ldots,13\). These are not merely partial searches.

For every \(p=0,\ldots,14\), the program verifies a displayed allocation, first via derived criteria and then again using complete bipartitions of the actual \(A,B,C,D\) item-count vectors and their integer valuations. It performs the same two checks for explicit higher-size witnesses, including a case where all rare-item subsets are feasible. Analytical stabilization at large bundle size extends these finite checks to infinitely many common-good counts.

The accompanying proof supplies the logical implication from finite enumeration to the exact infinite family, and establishes the cardinality lemma independently of computation. These scientific checks were performed without a separately commissioned independent audit or external formal proof certification. Historical priority and generalization beyond this numerical family are not certified.
