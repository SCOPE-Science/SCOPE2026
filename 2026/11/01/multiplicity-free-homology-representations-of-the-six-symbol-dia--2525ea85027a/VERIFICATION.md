---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

The faces are nonattacking rook placements on the 6×6 board omitting all six diagonal squares. Every face is reconstructed by injection of distinct row and column labels; f-vector (30,315,1420,2715,1854,265). Direct sparse modular reductions of ∂4 at primes 1009 and 65521 reproduce rank1557 and all 22 S6×C2 homology character values; the source additionally performs rational Fraction elimination, and lower and upper boundary ranks (29,286,1134,1557,265) yield reduced rational ranks H3=24, H4=32, nothing else. For each diagonal permutation cycle type and side swap, oriented simplex-fixed-face traces and the induced ∂4 image action give independent H3 and H4 characters via Hopf trace. Reproduced character projections have nonnegative integer multiplicities: H3 partitions (4,2) sign-under-swap, (3,1,1,1) even, (2,2,2) odd, dimensions 9+10+5=24; H4 (6) even, (4,1,1) odd, (3,2,1) odd, (2,1,1,1,1) even, dimensions 1+10+16+5=32. This is rational homology, not integral torsion or homotopy.

## originality

PASS

The named prior literature determines chessboard homology and group representations for full, capacity-bounded boards. It does not, on comparison of actual underlying edge sets and action groups, imply the diagonal-deleted 6-symbol complex or its S6×C2 irreducible characters. Best-of-knowledge PASS with unindexed equivariant matching literature retained as a risk.

## value

PASS

The forbidden perfect matching breaks the separate row/column symmetry to a natural diagonal S6 and transpose involution. Computing both nonzero degrees and their multiplicity-free rational characters resolves a genuine equivariant invariant of a natural classical chessboard subcomplex, not a routine renamed table entry. The transposition parities distinguish summands invisible in ordinary Betti ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
