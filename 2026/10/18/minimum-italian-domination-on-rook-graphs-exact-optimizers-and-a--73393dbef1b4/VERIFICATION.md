---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For 1<=m<=n, at a zero entry f_ij the Italian defense inequality is precisely row_sum_i+column_sum_j>=2. If a row has weight zero, all columns have >=2; if a row has weight one, all columns are positive; if every row has weight >=2, total >=2m. This proves weight >=min(n,2m); a surjection assigning one 1 to each column with each row occupied attains n, and arbitrary weight-two rows attain 2m. Equality excludes zero rows and yields either the one-1-per-column onto family or independent weight-two rows. Counts are m!S(n,m), [n+binom(n,2)]^m, and at n=2m inclusion–exclusion subtracts n!/(2!)^m. Degenerate R_1,1 is correctly a single 1. Independent literal-rook-neighborhood enumeration of all 3^(mn) labelings at sizes (1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3) reproduced gamma and counts including (2,4)=(4,108).

## originality

PASS

Best-of-knowledge distinct contribution after direct comparison with relevant same-invariant primary results, strong alternatives, indexed tables and a Resultary semantic search (Italian domination rook graph Cartesian product complete graphs minimum function count). Known minimum values, feasibility reductions, algorithms and finite tables are credited, while the claimed additional structural enumeration is assessed separately. Unread high-relevance literature and alternative indexing are retained as residual risks, not silently treated as absence.

## value

PASS

Rook graphs are a canonical product family; the sharp change of optimizer geometry at n=2m, a complete equality-case classification and exact multiplicities refine the natural minimum Italian domination value. The two visibly different configuration families and their boundary overlap make a motivated enumerative result, not a parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
