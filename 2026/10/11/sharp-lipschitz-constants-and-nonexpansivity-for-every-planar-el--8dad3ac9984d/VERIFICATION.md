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

# Reproducible verification

With Python 3.10+, NumPy and SciPy installed, execute `python verify_wedge.py` in this directory. The script compares direct active-face projections against independently optimized nonnegative ray coefficients for 3,675 randomized cases (across seven exponents), tests 3,150 distinct input pairs against the derived constant, and probes 210 boundary regions to witness the sharp local operator norms. A fixed pseudorandom seed makes the cases reproducible.

Observed completion: `VERIFY_OK independent_optimizations=3675 global_pair_checks=3150 boundary_sharpness_checks=210 max_solver_difference=9.36e-07`.

The independent optimization is numerical and subject to floating-point errors, with a recorded absolute matching tolerance. The complete statement for all cones and all exponents is established by the analytic proof rather than by finite sampling. No independent audit has been performed.
