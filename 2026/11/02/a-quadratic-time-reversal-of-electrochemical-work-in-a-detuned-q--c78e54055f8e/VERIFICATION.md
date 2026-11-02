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

## Reproducible numerical checks

`python verify.py` passed 265 finite-dimensional assertions on the complete, directly constructed Hamiltonian and load Markov generator, using detunings 40, 60, 80, 100, 150, 200, 300, and 500 in the normalization \(\Omega=T=1\), \(\Gamma=0.1\), \(c=4.5\). Tests include probability normalization, exact Gibbs detailed balance, work positivity in the finite interval, negativity of the infinite-time accumulated output, both low-level spectral overlap limits, uniformly small quadratic-time profile errors, convergence of the work-zero estimates, and monotone reduction in the observed root errors.

The exact mathematics relies on the finite-state semigroup perturbation and detailed-balance proof in `RESULT.md`. The finite checks do not establish uniform error bounds outside their tested parameters, exclude all other work zeros, or constitute independent validation. The only external dependencies for the verifier are NumPy and SciPy.
