---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The graph is the 12 ordered pairs (i,j), i != j, with triangle and reversal edges; the degree-two bounded-degree complex includes the empty face. Independent exhaustive reconstruction gave 69,075 faces including empty and the exact 12-term f-vector, 34,533 augmented toggle pairs (34,532 nonempty pairs after basepoint transfer), one ordinary critical vertex plus seven 8-cells and two 9-cells. The full nonempty Hasse DAG with 485,070 arrows is acyclic; the independent signed Morse matrix has rows (0,0),(0,1),(0,0),(0,1),(1,0),(-1,0),(0,1), a primitive rank-two image with unit 2x2 minor. Since the 8-skeleton is a wedge of seven S8 and pi8 equals H8, this cancels two attachments, yielding five S8 without torsion. Enumerating all 24 S4 vertex permutations and every invariant face recovers class traces identity 5, transposition -1, double transposition 1, three-cycle 2, four-cycle 1 and 1+sgn+(sgn tensor Std4). No integral S4 lattice or equivariant wedge asserted.

## originality

PASS

Vega establishes general degree-two matching methods and named claw/wheel/leaf cases; Singh studies forests and complete(-bipartite) graph families. The truncated tetrahedron has no leaves, contains triangles and is not complete/bipartite. Resultary 2026 truncated tetrahedron M1 wedge22 S3 is a different cutoff, with no automatic implication of M2 or its S4 action.

## value

PASS

The regular truncated tetrahedron is a natural vertex-transitive Archimedean cubic graph; its degree-two matching complex is the nontrivial bounded-degree stage between the already-calculated ordinary matching stage M1(T) and the degree-three full simplex. The exact eight-dimensional sphere rank and full S4 action answer a natural cutoff-specific homotopy question, not a change of graph labels or an arbitrary filter; torsion-freeness and symmetry require genuine integer attaching and signed trace calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
