---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The checker tests every format with
\[
3\le t\le5,
\qquad
2\le m_i\le4.
\]

For each basis coordinate in each factor it assigns a distinct power of two. It enumerates every tensor-coordinate tuple and verifies that the resulting sums are pairwise distinct, exactly as required for the one-parameter subgroup fixed-point argument.

For every dual coordinate functional it also checks that the first two factors have nonzero kernel directions available, which is the only finite-dimensional premise in the explicit tangent-point construction.

The checker records the number of tested formats and coordinate fixed points. These finite checks are regression evidence only. The theorem for arbitrary dimensions follows from binary-expansion uniqueness, the symbolic Segre tangent-space calculation, and Euler localization.
