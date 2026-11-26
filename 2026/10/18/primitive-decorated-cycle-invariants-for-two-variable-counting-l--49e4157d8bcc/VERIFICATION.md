---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a fixed finite comparison, existence of a backward walk longer than both structures defines cyclicity with two variables. Inductively counting noncyclic predecessors by child tree type recovers the attached tree labels. Distinct periodic forward sequences can be separated by a finite label prefix, and the exact counts of phases recover each long repetition weight. Loop and reciprocal pair tests separate short cycles; sum cyclic counts for their decorated necklace and divide by the tagged length, including the constant-letter two-cycle. Conversely, color the cyclic roots by phase and the noncyclic vertices by root phase and orbit in the corresponding rooted tree. For each color the counts of outgoing-only, incoming-only, mutual, equality and nonedge pairs by target color are fixed by the phase, tree and short/long tag, and the global class sizes match under equality of signatures. This is a balanced equitable coloring for the full atomic pair types, implying C^2 equivalence. Connected reconstruction follows and a nontrivial split of a long repetition weight needs at least two cycles of length at least three, yielding exactly the stated first collision. An independently written enumeration through six confirmed all counts and classified the collision. The phrase 'their sizes ... differ' in the Finding can only mean cycle lengths: the two graphs both have six vertices, as explicitly stated by the theorem.

## originality

PASS

The distinct contribution is the all-structures, phase-weighted normal form for directed total functional relations with separate treatment of loops and reciprocals. Neither the general refinement criterion nor the closely related undirected bracelet theorem supplies this statement. The census of isomorphism types and the six-point witness in isolation are not credited as new.

## value

PASS

The signature gives a usable complete invariant for arbitrary unions of functional components and identifies exactly which global information counting logic loses while retaining tree types, orientation and exceptional short cycles. It also proves the earliest failure of identification in this class without relying on the finite census as a substitute for structure. This value is not attributable to the already-tabulated isomorphism count or to the easy example alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
