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
The embedded `verify_dp_ss_proper_boundary.py` gives an exact finite replay with only the Python standard library.

Simple games are independently generated in two ways: as antichains of minimal winning coalitions and as monotone Boolean truth tables obtained recursively from pairs \((f_0,f_1)\) with \(f_0\le f_1\).

The replay confirms the simple-game counts
\[
1,4,18,166,7579
\]
and the proper-game counts
\[
1,3,11,80,2645
\]
for \(1\) through \(5\) players.

For every proper game, Shapley-Shubik is computed independently by the pivotal-coalition factorial formula and by enumerating all player permutations. Deegan-Packel is computed with exact rational coalition-size weights.

The verifier confirms zero proper weak-order disagreements through \(4\) players and exactly \(460\) at \(5\) players. Every disagreement contains a strict pairwise reversal. Canonicalization under all \(120\) player relabelings gives exactly \(9\) classes with orbit-size multiset
\[
\{120,60,60,60,60,30,30,20,20\}.
\]

All nine canonical classes are reconstructed exactly from the weighted representations listed in `RESULT.md`. The witness \([9;5,4,3,2,1]\) is checked to have the stated minimal winning coalitions and exact power vectors.

Finally, the replay confirms that unrestricted ordinal divergence already occurs in exactly \(16\) labeled four-player simple games, all of which are improper.

Run:

`python3 verify_dp_ss_proper_boundary.py`

The first output line must be:

`VERIFY_OK`

No larger-player frequency claim is inferred from the finite classification.
