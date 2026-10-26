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

# Reproducible checks

Run `python3 verify.py` using Python 3 and only its standard library. The program enumerates all candidate-unlabeled multiset profiles for exactly four candidates and labeled voter universes of sizes one through six; it includes empty and duplicate approval-supporter sets. The run passed 823,086 four-candidate instances and returned precisely 120 exceptions at six voters, all with coverage profile \((0,3,4,6,6)\) and the three-pair-plus-transversal form. Candidate labeling yields 2880 profiles. It separately checks all six single-voter deletions of the witness for voter-interval realizability, and checks that the undeleted instance does not admit a voter-interval order.

This finite program cannot prove concavity for an unbounded number of candidates, which is established by the inequalities in the main proof. Numerical or finite computations are not used to claim broader uniqueness beyond the stated scope. No independent audit has been performed.
