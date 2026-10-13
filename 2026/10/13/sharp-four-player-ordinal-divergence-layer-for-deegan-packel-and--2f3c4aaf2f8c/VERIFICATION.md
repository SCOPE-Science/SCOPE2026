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
The embedded `verify_dp_public_good_proper_first_layer.py` performs an exact finite replay using only the Python standard library.

A simple game is represented by its antichain of minimal winning coalitions. Every such antichain on one through four players is enumerated, and properness is checked directly by testing that no winning coalition has a winning complement.

Deegan–Packel is computed independently by:
1. its defining minimal-coalition sum;
2. averaging the equal-split unit payoff vectors of all minimal winning coalitions.

Public Good is computed independently by:
1. normalized minimal-winning-coalition participation counts;
2. explicit normalization of the player-coalition incidence multiset.

The verifier confirms:
- \(1,3,11,80\) labeled proper simple games for one through four players;
- \(1,2,5,14\) isomorphism classes;
- no weak-ranking divergence through three players in the proper domain;
- exactly \(30\) divergent labeled four-player proper games;
- exactly three divergent isomorphism classes with orbit sizes \(12,12,6\);
- canonical minimal-winning families \(\{AB,ACD\}\), \(\{AB,AC,BCD\}\), and \(\{AB,ACD,BCD\}\);
- the displayed exact Deegan–Packel and Public Good vectors;
- weighted representations `[5;3,2,1,1]`, `[5;3,2,2,1]`, and `[4;2,2,1,1]`;
- exactly three non-proper three-player divergences, all in one isomorphism class.

Run:

`python3 verify_dp_public_good_proper_first_layer.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite boundary through four players.
