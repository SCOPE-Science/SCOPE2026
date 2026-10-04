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
The embedded `verify_rsd_two_type_envy.py` uses exact integer counts over all serial-dictatorship priority orders.

It verifies every strict profile for \(n=1,2,3\). There are no failures for \(n\le2\). For \(n=3\), it verifies exactly \(144\) stochastic-dominance envy-free profiles and \(72\) failures among the \(216\) labeled profiles. Every failure uses three distinct preference orders. Independent canonicalization under all agent and object relabelings yields \(10\) total profile classes and exactly two failing classes, both of orbit size \(36\).

It exactly reconstructs the displayed three-agent witness and its RSD matrix. It also checks every normalized two-preference-type multiplicity profile through \(n=6\), totaling \(4{,}166\) cases, and verifies the top-\(k\) lower bound used in the proof.

Replay command:

`python3 verify_rsd_two_type_envy.py`

The first output line must be:

`VERIFY_OK`

The all-\(n\) theorem is established by the algebraic proof in RESULT.md; the finite replay is a consistency and boundary check only.
