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

# Reproducibility and verification

Run `python verify.py` with NumPy and SciPy installed. The script constructs the full normalized Walsh transform, decomposes the images of all first-shell absorbing basis states inside each distinct hypercube energy eigenspace, and forms the orthogonal bright projector. It checks the formula and the rank in dimensions \(2\) through \(8\), and then independently propagates the non-Hermitian effective Hamiltonian with **unequal** positive sink rates in dimensions \(2,3,4\). The program also checks idempotence of the numerical bright projector.

Observed execution: 557 passed assertions, with maximum absolute error smaller than \(3.5\times10^{-12}\); predicted ranks for dimensions \(2\) through \(8\) were \(3,8,13,22,31,44,57\). Explicit finite-dimensional numerics are regression evidence, **not** a proof of the all-dimension statement. The proof uses exact invariance, radial eigenvectors, cyclic generation, and spectral decomposition, independently of these numerical checks.

Strictly positive absorption rates, positive uniform coherent hopping, finite hypercube size, and the asymptotic \(t\to\infty\) limit are essential assumptions. The program's finite-time propagation does not establish finite-time accuracy uniformly over parameter values. No independent audit has been performed.
