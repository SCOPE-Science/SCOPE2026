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

# Reproduction

From the extracted file directory, run `python3 verify_double_swap.py`. This uses Python 3 standard-library code only. Successful termination emits `VERIFY_OK integral_morse=zero acyclic=all raw_orbits=all mod2=all`.

For cube dimensions 4, 5, 6 and 7, respectively, the verified nonempty face vectors are `(8,16,8)`, `(16,52,48,8)`, `(32,152,208,84,16)`, `(64,416,768,512,192,32)`; the critical-cell vectors are `(1,1)`, `(1,1,4)`, `(1,1,20)`, `(1,1,68,4)`; and matching-pair counts are `15`, `59`, `235`, `955`.

The checker exhaustively builds all eligible orbits directly from the involution and the Hamming metric; checks a second independent prefix/tail-distance predicate; enumerates all maximal cliques, all simplicial faces and all Hasse incidences; performs a full acyclicity topological sort; and computes all signed **integral** Morse differentials by explicit elimination of unit incidence pairs, verifying that each is zero. A separately implemented Gaussian elimination over the two-element field recovers the same homology dimensions directly from the original simplicial chain matrices.

The infinite-dimensional continuation follows from a symbolic 1-Lipschitz equivariant projection with an equivariant zero-padding section, not from finite tests. Numerical checks alone are not interpreted as proofs for dimensions beyond seven. The one-dimensional fundamental group at seven and lack of a claimed seven-dimensional sphere wedge distinguish algebraic homology from potential higher attaching maps. Independent audit was not performed.
