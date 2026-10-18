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

# Verification and reproducibility

Run `python verify.py` with the standard library. The program constructs each real weighted combinatorial Laplacian and tests the Kalman reachability matrix with modular Gaussian elimination using primes 1000003 and 1000033, as well as exact rational elimination for selected small cases. It prints `VERIFY_OK 1100 controllability-rank checks over finite fields and exact rationals`. Assertions exercise every individual leader in both layers on sample networks for \(3\le n\le12\); the uniform symmetry obstruction; the predicted forbidden indices; sampled nonuniform eligible indices; and an explicit five-cycle exceptional defect weight.

For \(n=5\), unit cycle and regular pendant conductances, and defect conductance \(1/2\), deleting core vertex \(u_1\) from \(L-zI\) leaves a characteristic polynomial sharing the exact factor \(z^2-3z+1\) with the full determinant. The corresponding single-input control matrix is rank-deficient. The dimension-ten system with the same baseline parameters and defect conductance \(2\) has full Kalman rank for \(u_1\).

The proof in `RESULT.md` covers infinitely many orders and all positive real weights. The program does not enumerate all algebraic exceptional weights and its finite tests cannot replace the analytic spectral, rank-one, and rational-function arguments. Independent audit is not performed.
