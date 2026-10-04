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
The embedded `verify_da_pareto_boundary.py` is an exact finite replay using only the Python standard library.

It exhausts all \(16\) complete strict \(2\times2\) profiles and all \(46656\) complete strict \(3\times3\) profiles.

For each profile it independently checks:
- deferred acceptance by a sequential free-student queue;
- deferred acceptance by simultaneous proposal rounds;
- stability of every perfect assignment;
- student-optimality of the deferred-acceptance assignment among all stable assignments;
- Pareto improvements by direct comparison with every perfect assignment;
- equivalence of Pareto inefficiency with a directed trading cycle in the assignment envy graph.

For \(3\times3\), the replay confirms:
\[
1296
\]
Pareto-inefficient profiles out of \(46656\), exactly one Pareto improvement at each bad profile, exactly two strict beneficiaries, and rank-multiset counts
\[
(2,2,2):648,
\qquad
(2,2,3):648.
\]

It also independently classifies all \(216\) priority structures with the unit-capacity Ergin cycle condition and confirms
\[
0:42,
\quad4:36,
\quad8:126,
\quad12:12
\]
for the number of bad preference profiles, with exactly \(42\) acyclic and \(174\) cyclic priority structures.

Run:

`python3 verify_da_pareto_boundary.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite classification.
