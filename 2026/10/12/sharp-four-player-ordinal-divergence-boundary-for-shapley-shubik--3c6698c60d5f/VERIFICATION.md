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
The embedded `verify_shapley_nucleolus_proper_simple_games.py` performs an exact finite replay using only the Python standard library.

It represents a simple game by the antichain of its minimal winning coalitions and exhausts every such game on one through four players, filtering exactly for properness.

The verifier computes Shapley–Shubik values from the pivotal-coalition formula with exact rational arithmetic.

For the nucleolus, it uses exact core and least-core certificates:
- veto-player games are reduced by core constraints and symmetry;
- no-veto games use exact rational vertex enumeration of the first least-core linear program;
- singleton least cores directly give the nucleolus;
- the sole non-singleton first least core in the four-player canonical list is resolved by its player symmetry.

It confirms:
- \(1,3,11,80\) labeled proper simple games for one through four players;
- \(1,2,5,14\) isomorphism classes;
- no weak-ranking divergence through three players;
- exactly \(36\) divergent labeled four-player games;
- exactly three divergent isomorphism classes, each of size \(12\);
- canonical minimal-winning families \(\{AB,AC\}\), \(\{AB,AC,BCD\}\), and \(\{AB,ACD\}\);
- the displayed exact Shapley–Shubik vectors and nucleoli;
- \(50\) proper four-player games with no dummy;
- exactly \(24\) nondummy divergences in two isomorphism classes.

Run:

`python3 verify_shapley_nucleolus_proper_simple_games.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite boundary through four players.
