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

`check_dicyclic_moment.py` was executed on the files accompanying this result. It verified all 78 finite signs for \(n=2,\ldots,79\), both exact boundary values and an exact positive rational tail lower bound at \(n=80\). The recurrence is derived in the proof rather than treated as a black-box formula.

`check_small_dicyclic.c` was compiled with a standard C11 compiler and executed. It exhaustively checked every subset of the five groups with \(2\le n\le6\), including 16,777,216 subsets at \(n=6\), with independent group-table arithmetic and the group associativity/inverse checks. Outputs for the first moment were \(-32,-156,-5376,-47280,-779184\), agreeing with the symbolic formula. For \(n\ge80\), positivity rests on the explicit monotone rational lower bound, not finite enumeration.

Limitations: this verification does not independently establish literature priority and does not address the sign-count majority comparison. Independent audit has not been performed.
