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

# Verification of the grid theorem

Run `python3 check_grid_mu3.py` (Python 3 standard library only). The program enumerates all cliques in the distance-at-most-three auxiliary graph on each test grid, so every feasible selected set is tested without omissions. Every candidate is evaluated from the original definition by explicitly generating monotone shortest coordinate-step orders and testing whether at least one has no selected internal vertices.

The grid test cases are 1×4, 1×6, 2×3, 2×4, 2×7, 3×3, 3×4, 3×5, 4×4, 4×5, 5×5, 6×6, 6×8. These examine 20,675 distinct nonempty diameter-at-most-three subsets. All the reported maxima agree with direct checking; for all tested nondegenerate grids the program compares *sets* of maximizing subsets against all explicitly translated horizontal and vertical templates and checks their exact count. For 3×3 the four five-point maxima are also checked exhaustively. The complete deterministic output is `check_grid_mu3.out`.

This finite computation is supplementary to the infinite proof in `RESULT.md`. It does not establish absence of unindexed published results or provide independent scientific certification.
