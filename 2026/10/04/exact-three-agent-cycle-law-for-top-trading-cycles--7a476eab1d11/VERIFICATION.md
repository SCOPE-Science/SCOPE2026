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
The embedded `verify_ttc3_cycle_chronology.py` is a standard-library-only exact replay.

It enumerates all \(216\) strict three-agent preference profiles. TTC is implemented in two independent ways:
1. a functional graph from each remaining agent to the current owner of her favorite remaining house;
2. an explicit bipartite directed graph with distinct agent and house nodes.

Both implementations execute all current cycles simultaneously and are required to agree on the final allocation and the full cycle-size chronology for every profile.

The verifier also checks that the \(27\) first-choice maps each have exactly \(8\) full-ranking refinements and reproduces the six first-round graph-type counts. It separately verifies the star/chain split inside the one-self-loop/no-two-cycle family.

The exact replay requires the chronology histogram
\[
8,24,16,48,48,6,30,36
\]
for the eight stated traces; the mover histogram
\[
98,102,16
\]
for \(0,2,3\) movers; and the round histogram
\[
48,132,36
\]
for \(1,2,3\) rounds.

It then checks the exact fractions \(49/108\), \(17/36\), \(2/27\), \(59/108\), \(7/6\), and \(35/18\).

Run:

`python3 verify_ttc3_cycle_chronology.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite three-agent result under the parallel cycle convention.
