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
The embedded `verify_five_candidate_three_voter_tournaments.py` performs two exhaustive profile counts and a separate tournament-isomorphism quotient.

Route A evaluates all \(120^3=1{,}728{,}000\) ordered triples of strict rankings.

Route B evaluates all \(inom{122}{3}=295{,}240\) multisets of three rankings and restores ordered-profile multiplicities with exact weights \(1\), \(3\), and \(6\).

The two 12-entry class-count vectors must agree exactly. Independently, all 1024 labeled tournaments are canonically quotiented under all 120 candidate relabelings; this must produce 12 classes. The verifier also checks the stated exact class table, orbit-stabilizer divisibility, and that the displayed degree/triangle-incidence signatures distinguish the classes.

Replay command:

`python3 verify_five_candidate_three_voter_tournaments.py`

Expected leading output:

`VERIFY_OK`

The census is finite and exhaustive; no probabilistic sampling or extrapolation is used.
