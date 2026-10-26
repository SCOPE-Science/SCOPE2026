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

# Verification of exact quantifier-rank profiles

The symbolic correctness argument establishes the theorem for all positive sizes and quantifier ranks, using the Ehrenfeucht–Fraïssé game and graph-language separating formulas. The key checks are (1) round-by-round coordinate equality patterns under matching truncated factor sizes, (2) completeness iff a rook factor equals \(1\), (3) every clique of size at least three lies in one row or column, and (4) the number of common neighbors of an edge is one factor size minus two. These facts imply both directions of the equivalence law.

Run `python3 check_rook_ef.py` using the bundled standard-library Python source. It independently checks all unordered pairs of canonical rectangles with factor maximum three at ranks one and two, all pairs with factor maximum four at rank three, and selected comparisons at rank four. Compare stdout with `checker_output.txt`. Exhaustive *finite* tests are not proofs of uniform claims; the complete proof is in `RESULT.md`. The package does not claim machine formalization or independent validation.
