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
The embedded `verify_public_good_dominance_first_layer.py` performs an exact finite replay using only the Python standard library.

A simple game is represented by its antichain of minimal winning coalitions. Every nonempty antichain on one through five players is generated and tested directly for properness.

The normalized Public Good index is computed independently from:
1. direct minimal-winning-coalition incidence counts;
2. an explicitly constructed player-coalition incidence multiset.

Dominance is computed independently from:
1. the defining implication over all coalitions excluding the compared players;
2. a replacement test over all winning coalitions containing the dominated player but not the dominating player.

Both pairs of implementations agree on every enumerated game.

The verifier confirms:
- \(1,3,11,80,2645\) labeled proper simple games on one through five players;
- \(1,2,5,14,86\) corresponding isomorphism classes;
- no Public-Good dominance violation through four players;
- exactly \(460\) labeled five-player violations;
- exact incidence \(92/529\);
- exactly nine violating isomorphism classes;
- the labeled distribution \(300,120,40\) for one, two, or three violating dominance comparisons;
- all nine displayed integer weighted representations;
- strict voting-weight reversal for every violating pair in each displayed representative;
- the compact witness with minimal winning coalitions \(\{AB,ACD,ACE\}\), representation \([8;5,3,2,1,1]\), and Public Good vector \((3/8,1/8,1/4,1/8,1/8)\).

Run:

`python3 verify_public_good_dominance_first_layer.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite boundary through five players.
