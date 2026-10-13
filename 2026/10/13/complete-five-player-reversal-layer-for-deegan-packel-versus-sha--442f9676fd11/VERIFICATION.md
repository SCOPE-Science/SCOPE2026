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
The embedded `verify_dp_shapley_proper_first_layer.py` performs an exact finite replay using only the Python standard library.

It represents each simple game by its antichain of minimal winning coalitions and exhausts every such game on one through five players, filtering properness directly.

Deegan–Packel is computed independently by:
1. the defining minimal-winning-coalition sum;
2. explicit averaging of equal-split coalition payoff vectors.

Shapley–Shubik is computed independently by:
1. the exact factorial-weighted swing formula;
2. exhaustive pivotal-player counting over all player permutations.

The verifier confirms:
- \(1,3,11,80,2645\) labeled proper simple games for one through five players;
- \(1,2,5,14,86\) isomorphism classes;
- no weak-ranking divergence through four players;
- exactly \(460\) divergent labeled five-player games, incidence \(92/529\);
- exactly \(9\) divergent isomorphism classes;
- strict-reversal counts \(300,120,40\) for one, two, and three reversed player pairs;
- no tie-only differences in either direction;
- all nine canonical divergent classes are weighted, with the displayed integer representations;
- \(2330\) dummy-free proper five-player games and all \(460\) divergences inside that subdomain;
- the displayed witness and its exact power vectors.

Run:

`python3 verify_dp_shapley_proper_first_layer.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite boundary through five players.
