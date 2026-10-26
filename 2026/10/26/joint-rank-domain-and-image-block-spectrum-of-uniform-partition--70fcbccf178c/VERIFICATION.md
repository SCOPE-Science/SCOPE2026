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
# Computational verification

Execute the embedded script using `python3 verify_uniform_partition_idempotents.py` with Python 3 and the standard library. The script first constructs the exact trivariate generating polynomial via the independent component-recurrence implementation. It then directly enumerates actual partial maps, explicitly tests equivalence-relation preservation and idempotence, and compares every coefficient for the six parameter pairs \((1,1),(1,4),(4,1),(2,2),(3,2),(2,3)\). For four further pairs \((3,3),(4,2),(5,2),(2,5)\), it checks rank-one, next-to-maximal-rank and full-domain specializations; the latter are independently computed from the classical full-map rooted-block decomposition.

Selected directly checked totals are 76 partial idempotents at \((m,n)=(2,2)\), 1236 at \((3,2)\), and 1291 at \((2,3)\). The script terminates with `VERIFY_OK_UNIFORM_PARTITION_PARTIAL_IDEMPOTENT_TRIVARIATE` if all assertions hold. Finite enumeration does not establish the infinite-parameter formula by itself. The reversible star decomposition in the proof is the mathematical justification for the full scope. This is not an independent mathematical audit.
