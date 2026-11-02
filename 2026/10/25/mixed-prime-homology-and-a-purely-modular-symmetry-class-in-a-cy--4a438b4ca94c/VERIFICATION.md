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

PASS: Each nonempty rook placement has trivial column-shift stabilizer because shifting a selected rook forces a second rook in the same row. Standard chessboard connectivity (5-by-5 simply connected) gives universal C5 covering. Independently enumerated every 1545 original nonempty placement, quotient cell counts (5,40,120,120,24), all integral boundary matrices and verified d²=0; computed exact Smith factors d1=1^4,d2=1^35·5,d3=1^83·3,d4=1^24, independently verified characteristic ranks at 2,3,5,7. Constructed group-cover integral cocycle U, Bockstein lift δU/5, and the signed 24-cell integral 3-cycle z, checked ∂z=0 and <u cup βu,z>=2 mod5. Independently enumerated all 120 S5 row permutations and exact Lefschetz traces [12,-2,0,3,1,0,-3] for seven classes; class-weighted trivial multiplicity zero. Full finite enumeration is exhaustive for exactly this board.

## originality

PASS

PASS best-of-knowledge: Shareshian–Wachs full primary text establishes 3-torsion in unquotiented Δ5,5 and chessboard connectivity; Reiner–Roberts gives rational symmetric-group homology of unquotiented complexes. Those do not determine the free cyclic column quotient integral SNF, nor a mod-5 symmetry-fixed cup/Bockstein class absent in rational invariants. Resultary query did not find matching quotient result. A highly relevant October 2026 preprint on column law/torsion was accessible only as substantial search-indexed excerpts (full page timeout); it remains an explicit priority risk, not asserted noncovering in full.

## value

PASS

PASS: The quotient by a natural board-translation symmetry exhibits adjacent-degree torsion at two distinct primes and a modular-vs-characteristic-zero symmetry distinction. The exact Smith classification plus explicit nontrivial Bockstein product is a natural motivated finite algebraic-topology invariant, not merely known 3-torsion transported without work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
