---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The Cayley adjacency on A=(Z/4)^2 was reconstructed, and every 16-bit mask independently tested for independence. There are exactly 16 vertices, 72 edges, 96 triangles and 16 tetrahedra, with no larger faces. All maximal tetrahedra are cosets of three cyclic order-four subgroups and one Klein four subgroup. The existing exact acyclic matching leaves one vertex and 23 degree-two cells, so rational H_2 is the only reduced homology. Direct oriented fixed-simplex Lefschetz for all sixteen translations yields identity 23, all three nontrivial involutions -1, six special order-four elements +3 and remaining six -1. Exact Fourier over fourth roots gives the 4x4 multiplicity matrix with trivial multiplicity 2 and total dimension 23; the claimed rational Q[A] + 1 + three conjugate-pair modules follows. A separate independently written 200-face enumerator checked every trace and Fourier coefficient; no dependence on a verifier success log.

## originality

PASS

The published same-graph Shrikhande/rook result already establishes Ind(S)≃∨^{23}S², but it does not compute the action of all 16 translations. Classical S_4×S_4 chessboard representation methods compute the rook graph, whose independence complex is not isomorphic to the Shrikhande complex. The new rational A-character distinguishes four order-four translation directions and gives a two-dimensional invariant subspace, data not implied by the earlier nonequivariant homotopy type. Resultary and targeted primary-source searches found no dominating same-graph A-module theorem. Best-of-knowledge acceptance with finite-character-table priority risk.

## value

PASS

The Shrikhande graph is a canonical strongly regular Cayley graph paired with the 4×4 rook graph. The exact 23-dimensional homology representation of its natural 16-element translation group is a motivated finite equivariant invariant: unlike a Betti rank it records which translation symmetries preserve/reverse classes and the two invariant classes, useful for comparison of strongly regular graph topology. It requires the complete signed action and Fourier decomposition, not a trivial renaming of known rank 23.

The dated certificate retains the supplied scientific assessment, sources and limitations.
