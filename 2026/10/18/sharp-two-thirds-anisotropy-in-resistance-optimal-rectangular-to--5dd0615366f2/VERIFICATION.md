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

# Mathematical verification

The analytical argument establishes unrestricted uniqueness by the strict Hessian of the trace of the inverse mean-pinned Laplacian and the injective edge-to-off-diagonal mapping. Translation/reflection invariance reduces the optimum to two orientation weights. The exact Fourier derivative has a unique positive root; the periodized lattice Green function supplies a fully specified expression and derivative. The fixed-width limit is obtained by rescaling the root by the two-thirds power of the longitudinal circumference and bracketing its sign against the limiting strictly monotone balance. Substitution into the original spectral sum gives the second term of the optimal trace and proves the comparison with uniform edge spending.

Run `python verify.py` with Python 3, NumPy and SciPy from the directory containing the extracted program. The standalone program executed successfully with 1,296 assertions. Its checks construct full Laplacians independently of the Fourier formula, compare all nonzero eigenvalues and resistance traces, test feasible asymmetric examples, verify the finite-period Green identity, and probe representative limits for the optimal ratio and cost coefficient. Such tests corroborate finite computations but cannot replace the proof of the infinite limit.

The mathematical model assumes two simple cycle factors of length at least three, equal linear conductance price on all edges, a positive total budget, and fixed short cycle length in the singular asymptotic. The uniqueness statement is among all nonnegative budget-feasible edge allocations on connected support, and disconnected supports are assigned infinite cost. Independent mathematical audit has not been performed.
