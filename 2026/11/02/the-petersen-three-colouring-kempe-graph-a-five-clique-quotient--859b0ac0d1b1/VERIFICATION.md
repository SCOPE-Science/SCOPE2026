---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Petersen is KG(5,2). Any independent set of size 4 is a unique complete star; a 3-colouring of 10 vertices must have such a 4-class, and the leftover six vertices induce 3K2, whose 3+3 classes are a three-star (centre t≠c) and the complementary triangle. This yields exactly 5×4×3!=120 named states (c,t;A,B,C), with no missing assignments. Analyzing each pair of colour classes: BC has three isolated two-vertex components (3 moves), AB has a singleton and a connected six-cycle (2 moves), AC connected (1 move), giving six exact neighbor transformations and quotient adjacency. Independent enumeration over all 3^10=59049 color assignments reconstructed the legal Kempe components directly; it found 120 states, 360 edges, all six-regular, shortest-path shells (1,6,25,61,27), radius/diameter 4, and 60 one-site-recoloring edges. The transitive action of permutations of 5 ground labels and named colours transfers the representative distance census to all states. Entire finite case is exhaustively classified rather than extrapolated to all cubic graphs.

## originality

PASS

Best-of-knowledge PASS for full six-move model, exact quotient and metric, and single-vertex contrast. The chromatic counts 120/20 and cubic-graph Kempe connectivity are known prior facts, not novel. No checked literature supplies exact all-state distance shells or five K4 reconfiguration quotient.

## value

PASS

Exact finite structure of Kempe reconfiguration at the chromatic threshold of a canonical cubic graph: five-K4 quotient, diameter four, transitive all-state shell census, and disconnected elementary recoloring contrast. A natural benchmark for differences between two standard reconfiguration moves, not just state-count trivia.

The dated certificate retains the supplied scientific assessment, sources and limitations.
