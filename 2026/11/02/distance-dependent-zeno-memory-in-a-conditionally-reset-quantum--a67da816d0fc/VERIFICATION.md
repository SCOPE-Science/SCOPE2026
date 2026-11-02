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
# Reproducibility and scope

The attached `verify_quantum_relaxation.py` is standalone apart from Python, NumPy and SciPy. Run `OPENBLAS_NUM_THREADS=1 python verify_quantum_relaxation.py`; the observed successful execution reports 85 finite consistency checks. It compares the finite Bessel identity against direct amplitude sums; computes and orders the positive Laplace roots; compares the large-rate formula numerically; compares two numerical renewal discretizations with the analytically predicted time asymptotic; and independently evolves a finite-site density-matrix generator at a common finite observation time. Numerical quadrature occasionally warns about requested precision; passing tests use explicit finite error tolerances. The mathematical bounds, unique root, strict distance ordering, and asymptotic constants rely on the written analytic proof, not on finite samples or generator truncations. This file provides no independent scientific certification.
