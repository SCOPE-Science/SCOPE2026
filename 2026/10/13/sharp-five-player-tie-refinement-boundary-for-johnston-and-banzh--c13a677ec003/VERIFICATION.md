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
The embedded `verify_johnston_banzhaf_proper_first_layer.py` performs an exact finite replay using only the Python standard library.

It enumerates every simple game through five players from its antichain of minimal winning coalitions and directly checks properness.

Banzhaf power is computed independently by:
1. adding a player to losing coalitions and counting losing-to-winning swings;
2. removing a player from winning coalitions and counting winning-to-losing swings.

Johnston power is computed independently by:
1. coalition-centered equal division among all critical players of each winning coalition;
2. player-centered recomputation of critical-player counts for every coalition.

All arithmetic is exact rational arithmetic.

The verifier confirms:
- simple-game counts \(1,4,18,166,7579\);
- proper-game counts \(1,3,11,80,2645\);
- proper-game isomorphism counts \(1,2,5,14,86\);
- no weak-ranking divergence through four players;
- exactly \(480\) divergent proper five-player games;
- exact incidence \(96/529\);
- exactly nine divergent player-relabeling classes;
- orbit sizes seven times \(60\) and twice \(30\);
- no strict pairwise rank reversal in any divergent game;
- \(420\) games refining exactly \(2\) unordered player comparisons and \(60\) refining exactly \(4\);
- every displayed canonical family and vector.

Run:

`python3 verify_johnston_banzhaf_proper_first_layer.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite boundary through five players.
