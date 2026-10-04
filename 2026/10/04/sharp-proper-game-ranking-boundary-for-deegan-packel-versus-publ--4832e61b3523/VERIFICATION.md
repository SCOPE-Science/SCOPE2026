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
The embedded `verify_dp_pgi_proper_boundary.py` uses only the Python standard library and exact rational arithmetic.

It represents each simple game by its antichain of minimal winning coalitions and independently reconstructs the full antichain set in two ways: recursive incomparability pruning and brute-force family testing.

The verifier confirms:
- simple-game counts \(1,4,18,166\) for \(n=1,2,3,4\);
- proper-game counts \(1,3,11,80\);
- zero proper weak-order disagreements through three players;
- exactly \(30\) proper four-player disagreements;
- exactly three four-player isomorphism classes with orbit sizes \(12,12,6\);
- canonical minimal-winning families
\[
\{\{1,2\},\{1,3,4\}\},
\quad
\{\{1,2\},\{1,3\},\{2,3,4\}\},
\quad
\{\{1,2\},\{1,3,4\},\{2,3,4\}\};
\]
- their weighted representations
\[
[5;3,2,1,1],\quad[5;3,2,2,1],\quad[4;2,2,1,1];
\]
- exactly three labeled unrestricted three-player disagreements, all improper and all relabelings of
\[
\{\{1\},\{2,3\}\}.
\]

Run:

`python3 verify_dp_pgi_proper_boundary.py`

The first output line must be:

`VERIFY_OK`

The computation proves the stated finite cutoff only and does not infer larger-\(n\) frequencies.
