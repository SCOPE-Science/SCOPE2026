---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS. The claim quantifies over every induced nonattacking-rook matching complex of a subset B of at most 16 positions in the 5-by-5 board, modulo separate row/column permutations; it does not claim arbitrary larger subboards. I independently rebuilt the complete 5-row bitmask canonicalization, enumerated 5130 distinct row/column orbit representatives of cardinality 0..16 (k=0..16 counts 1,1,3,6,16,34,69,130,234,367,527,669,755,755,669,527,367), and reconstructed the matching-complex integral boundary d3. Exactly 1 of 367 size-16 types has a nonunit residual: representative (3,13,28,30,30), 161 triangles,108 tetrahedra, 93 integral unit pivots and a single column with 24 nonzero entries all of absolute value 3. Every other type gives no third-boundary torsion. The original package additionally checks mod3 ranks d2=67,d3=93 for that board, d2=176,d3=423 for the full 5-by-5 board, and nonzero ambient inclusion, with exact boundary witnesses. The independently reconstructed exhaustive finite state space certifies this bounded classification; absence of a smaller board is not inferred from timeouts. The order-three group on the witness and ambient inclusion depend on exact integer boundary and mod3 cycle arguments, not merely on saved VERIFY_OK logs.

## originality

PASS

PASS best-of-knowledge: The known complete-board homology does not imply internal torsion in sparse induced boards. The Section 8 sufficient family and lower connectivity bounds do not cover exhaustive uniqueness among all 5130 symmetry types. The assertion concerns integral torsion of an induced subcomplex itself and ambient inclusion, rather than a small representative of a nontrivial ambient homology class. Searches of equivalent graph matching and chessboard subboard terminology returned no exact classification. A negative search alone is not proof of originality.

## value

PASS

PASS. The 5-by-5 complete chessboard complex is the first natural square chessboard with second-degree 3-torsion. Locating the smallest induced board on which that torsion exists intrinsically (not just as a chain supported in the large board), establishing uniqueness up to its natural S5 × S5 symmetry, and showing that its inclusion detects the global torsion are sharp, motivated boundaries in matching-complex topology. The invariant is not an arbitrary slice, a table recomputation, or a routine consequence of the known full-board homology. Limits: 5-by-5 subboards of cardinality at most 16 and specific degree two; not a classification of all boards or higher homology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
