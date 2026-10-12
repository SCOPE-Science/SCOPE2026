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
The embedded `verify_ss_banzhaf_six_player_layer.c` performs an exact exhaustive replay using only the C standard library and integer arithmetic.

It enumerates every nonempty antichain of nonempty coalitions for \(n=1,\ldots,6\), using the antichain as the minimal-winning family of a unique nontrivial simple game.

For every player it computes:
- raw Banzhaf swings by exact coalition enumeration;
- Shapley–Shubik comparison numerators using the integer swing weight \(k!\,(n-k-1)!\).

Every pair of players is classified as agreeing, strictly reversed, a Banzhaf tie split by Shapley–Shubik, or a Shapley–Shubik tie split by Banzhaf.

Properness is independently checked by:
1. testing that no winning coalition has a winning complement;
2. testing that no two minimal winning coalitions are disjoint.

The verifier confirms:
- total simple-game counts \(1,4,18,166,7579,7{,}828{,}352\);
- zero ordinal divergence through five players;
- exactly \(2{,}540{,}340\) six-player divergences;
- zero strict reversals;
- zero Banzhaf-only splits;
- every divergence contains a Shapley–Shubik split of a Banzhaf tie;
- every divergent six-player game is dummy-free;
- \(1{,}422{,}563\) proper six-player games and \(573{,}960\) proper divergences;
- the displayed witness, its swing-size spectra, raw Banzhaf vector, and exact Shapley–Shubik numerators.

Compile and run:

`gcc -O3 -std=c11 verify_ss_banzhaf_six_player_layer.c -o verify_ss_banzhaf && ./verify_ss_banzhaf`

A successful run contains the line:

`VERIFY_OK`

The computation proves only the stated finite boundary through six players.
