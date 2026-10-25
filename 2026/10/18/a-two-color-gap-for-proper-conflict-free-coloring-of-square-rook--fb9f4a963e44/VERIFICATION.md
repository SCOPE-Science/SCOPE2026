---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For proper cell colouring of R_{m,n}=K_m □ K_n, a neighbour colour has multiplicity 1 precisely when in row palette A_i symmetric-difference column palette B_j; all multiplicities are 0,1,2, making the proper odd condition equivalent. Rectangular m<n has optimal n-colour cyclic Latin rectangle since row palette size n differs from column size m. For square n×n with ≤n+1 colours, each row/column misses exactly one of n+1 palette colours; counting occurrences of each colour by rows and columns forces identical multisets of missing colours, hence some A_i=B_j, disproving valid χ<=n+1. Explicit 4-colour 2×2 and 6-colour 4×4 matrices realize exceptions. For other n≥3, k=n+2 and c_ij=i+qj mod k with q unit distinct from ±1 gives row missing 2-sets with differences ±q and column missing differences ±1, so palettes differ; piecewise q existence is algebraic for all sizes. A fresh checker of actual open-neighborhood colour multiplicities (not using the palette criterion) verified all 2<=m,n<=12 and squares n=13..80 (189 instances). This finite check corroborates, but the modular construction and omission-multiset counting prove all integer n,m>=2.

## originality

PASS

Best-of-knowledge originality after comparing exact statements/implications, relevant published corpus findings and available primary material. Classical ingredients are credited; no located stronger theorem or exact table entails the claimed new conclusion. Residual access and priority limits are recorded.

## value

PASS

Proper conflict-free and odd neighbourhood colouring of rook/Hamming dimension-two graphs is a natural exact chromatic invariant. A uniform, sharp two-colour penalty precisely for square aspect ratios, together with explicit optimal Latin-type matrices, is a motivated structural classification rather than a routine recalculation of ordinary rook chromatic number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
