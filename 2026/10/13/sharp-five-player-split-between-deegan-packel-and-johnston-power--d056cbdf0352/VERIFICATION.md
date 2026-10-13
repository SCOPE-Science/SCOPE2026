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
The embedded `verify_dp_johnston_proper_first_layer.py` performs an exact finite replay using only the Python standard library.

It enumerates every nonempty minimal-winning antichain through five players and filters exactly for properness.

Deegan–Packel is computed independently by:
1. the defining average of reciprocal minimal-winning-coalition sizes;
2. averaging explicit equal-split coalition payoff vectors.

Johnston is computed independently by:
1. scanning every winning coalition, finding its critical-player set, and splitting that coalition's unit score among those players;
2. reconstructing the same critical-coalition score player by player.

All arithmetic is exact rational arithmetic.

The verifier confirms:
- \(1,3,11,80,2645\) labeled proper simple games for one through five players;
- \(1,2,5,14,86\) isomorphism classes;
- identical weak rankings under Deegan–Packel and Johnston for every proper game through four players;
- exactly \(940\) divergent labeled five-player games, incidence \(188/529\);
- exactly \(18\) divergent isomorphism classes;
- exactly \(480\) pure Johnston tie-refinement games in \(9\) classes;
- exactly \(460\) strict-reversal games in \(9\) classes;
- exact signature counts \(420,60,300,120,40\);
- no Deegan–Packel refinement of a Johnston tie and no mixed first-layer signature;
- all \(940\) divergences are dummy-free;
- the exact vectors and rankings of the two displayed witness games.

Run:

`python3 verify_dp_johnston_proper_first_layer.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite boundary through five players.
