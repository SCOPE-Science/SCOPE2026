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
# Verification details

Run `python3 verify_moran_geary.py` using the Python standard library. The script uses exact `fractions.Fraction` arithmetic. It separately calculates both indices from their defining edge sums on the path with input vectors \((1,1,4,2)\) and \((1,2,1,4)\), checks means and squared norms, and verifies the strict simultaneous increase of both statistics.

It enumerates all labeled connected simple graphs for orders \(2,3,4,5,6\), totaling \(1+4+38+728+26704=27475\) graphs. In each it compares the degree-pattern test (regular or star) against an independently assembled centered bilinear-form span condition for adjacency and degree matrices over rational arithmetic. The counts classified as satisfying the affine centered-form criterion are respectively \(1,4,8,18,152\). It also evaluates the exact regular-graph and star affine laws on cycle and star graphs for orders \(3\) through \(9\).

Actual execution returned:

`VERIFY_OK witness_P4=2 equal_mean_variance=1 connected_graph_census=[(2, 1, 1), (3, 4, 4), (4, 38, 8), (5, 728, 18), (6, 26704, 152)] star_cycle_identities=14`

The finite cases corroborate but do not prove the theorem for arbitrary graph order; the all-orders proof is in `RESULT.md`. Proof of the quadratic-form order lemma is analytic. The algorithm does not analyze row-normalized/directed graphs or significance testing. No independent external validation has been performed.
