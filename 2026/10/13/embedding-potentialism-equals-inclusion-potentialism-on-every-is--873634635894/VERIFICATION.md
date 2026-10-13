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
# Verification

The general proof is structural. Given an embedding on the embedding-potentialist side, replace its target by an isomorphic copy whose underlying set contains the source literally, and pull the target structure back along the chosen bijection. Isomorphism-closure guarantees that this renamed target is still an allowed world. The reverse direction is immediate by composing a literal inclusion with the inverse of the isomorphism relating the current worlds.

Run `python3 artifacts/verify_replete_bisimulation.py`. The script exhaustively replays both constructions for every simple graph of source size one through three and every target size through four, across all source isomorphisms and all relevant embeddings. It checks literal induced-subgraph inclusion, target isomorphism, and the commuting equations on the old source.

Expected output:

`VERIFY_OK 149691 exact assertions`

The exhaustive finite computation is a sanity check of the transport construction. The theorem for arbitrary structures and cardinalities follows from the explicit pullback-of-structure proof and is not inferred from the finite cases.
