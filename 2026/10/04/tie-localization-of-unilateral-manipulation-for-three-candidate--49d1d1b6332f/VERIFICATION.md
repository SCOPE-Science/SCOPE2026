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
The embedded `verify_kemeny_singleton_strategy.py` is a standard-library-only finite replay supporting the analytic proof.

It computes Kemeny winner sets independently in two ways.

The margin implementation uses the three pairwise margins
\[
u=M_{AB},\qquad v=M_{BC},\qquad w=M_{CA}
\]
and the exact best-top scores
\[
u-w+|v|,\qquad v-u+|w|,\qquad w-v+|u|.
\]

The direct implementation evaluates all six social rankings by total Kendall-tau distance to the ballots.

For every anonymous strict profile with odd electorate size
\[
1,3,5,\ldots,17,
\]
the replay checks:
- equality of the two Kemeny implementations;
- the transitive-majority/weakest-cycle-edge characterization used in the proof;
- every present sincere voter type;
- every alternative strict report;
- every singleton-to-singleton outcome change;
- zero cases in which the changed singleton winner is strictly preferred by the manipulator to the truthful singleton winner.

The replay also records a small example in which a report touches a multiwinner Kemeny tie, confirming that the theorem is deliberately narrower than full strategyproofness.

Run:

`python3 verify_kemeny_singleton_strategy.py`

The first output line must be:

`VERIFY_OK`

The exhaustive computation is a stress test through seventeen voters. The theorem for arbitrary odd electorates follows from the proof's parity and margin inequalities, not from finite extrapolation.
