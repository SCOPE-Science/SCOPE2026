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

# Verification
The analytic proof identifies the exact domain of the covariance operator, its trace-class property, the eigenvalue product and its convergence, the CP-divisibility equivalence for invertible qubit phase-damping maps, and a stationary finite-correlation Gaussian counterexample for each sign-changing modulation. These are mathematical deductions and not numerical extrapolations.

The standalone Python 3/NumPy file `verify_quadratic_dephasing.py` was executed with environment `OPENBLAS_NUM_THREADS=1`. It reported 480 fixed-sign monotonicity comparisons on 40 independently seeded random continuous-covariance-inspired discretizations, 18 echo and static-limit comparisons (including five strictly positive Ornstein–Uhlenbeck relaxation rates and three couplings), and 20 complex-determinant cross-checks, a total of 518 successful finite checks. Its tests use positive-semidefinite, possibly oscillatory kernels. The finite tests do not establish the infinite-dimensional all-baths theorem; that theorem rests on the proof.

The physical model assumes classical centered real Gaussian quadratic noise, a bounded deterministic control, and a finite observation interval. Each stationary Ornstein–Uhlenbeck process used for necessity has finite positive relaxation rate. An independent audit has not been performed.
