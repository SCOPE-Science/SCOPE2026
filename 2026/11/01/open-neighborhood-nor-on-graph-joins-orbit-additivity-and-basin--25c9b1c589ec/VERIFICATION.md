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

The file `verify_join_nor.py` independently enumerates all binary configurations of each finite test graph and its join, and tests the update-operator identity \(F^3=F\), the two orbit-count identities, the total-domination identity, and the universal two-cycle basin formula. It does not use any claimed formula to compute the observed orbit counts: it applies the NOR rule directly and checks \(F^2(x)=x\).

Observed results, recorded verbatim in `verification_output.txt`: 5,625 ordered labelled-graph pairs with both factor orders between 1 and 4 passed, plus 120 deterministic-seed graph pairs with factor orders up to 7. All positive/negative isolate cases and complete-graph cases are among the tested pairs. The proof, rather than these finite checks, establishes the statement for arbitrary finite graphs.

Replay: `python3 verify_join_nor.py` (standard Python 3, no third-party packages). The output file is a record of the actual replay. General-priority literature equivalence and independent scientific audit have not been certified.
