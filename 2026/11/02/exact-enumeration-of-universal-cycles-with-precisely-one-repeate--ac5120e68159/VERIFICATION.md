---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For q>=2, overlap directed graph on q² ordered pairs has one directed edge for every triple with exactly two equal letters (3q(q−1) edges). Diagonal vertices have in/out q−1, off-diagonal in/out 2; diagonal-to-diagonal two-step routes and transitions show strong connectivity. An Eulerian circuit corresponds bijectively to a cyclic universal word; anchoring the unique 001 edge selects one rotation with no extra divisor. Directed BEST counts anchored tours as rooted in-arborescence tau times ((q−2)!)^q. The outgoing Laplacian off-diagonal block is 2I−R with determinant 3^binom(q,2) and inverse (2I+R)/3; Schur complement of diagonal block is (2/3)(qI−J), rooted cofactor q^(q−2). Thus tau=2^(q−1)3^((q−1)(q−2)/2)q^(q−2), giving U=tau((q−2)!)^q. Each symbol is in first position of 3(q−1) triples, hence occurs that often. Independently computed exact rooted cofactors q=2..5 (tau=2,36,3456,1458000) and small count consistency. All-q proof is determinant identity, not finite tests.

## originality

PASS

The evaluated exact all-q closed product for the natural language of length-three words with exactly two equal letters. Classical BEST and matrix-tree theorems provide counting method but not this specific evaluated Schur complement and closed count; prior restricted-universal-cycle papers often establish existence or other constraints. Historical hidden table may exist.

## value

PASS

Universal cycles give minimal cyclic listings of a natural local equality-pattern language excluding constant and all-distinct triples. Exact enumeration and prescribed symbol balance are motivated combinatorial invariants of these universal cycles, with a nontrivial q²-state matrix-tree reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
