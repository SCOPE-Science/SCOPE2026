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

# Verification of the singular XX-battery relaxation theorem

The proof uses the exact four-state invariant population system and its explicit solution. The Lindblad damping matrix is positive semidefinite for all \(0\le\alpha\le1\), with eigenmodes \(\sigma_1^-\pm\sigma_2^-\). Their decay rates are \(q_s=\gamma(1+\alpha)\) and \(q_a=\gamma(1-\alpha)\). The Gibbs initial state commutes with the Hamiltonian, and each jump retains diagonal density matrices in the energy eigenbasis. Hence this reduction is exact, not a secular or perturbative approximation.

Execute `python CHECK.py` with NumPy and SciPy. The standalone code explicitly constructs the full Hamiltonian and complete 16-dimensional Liouvillian, evolves a density matrix by matrix exponentiation, and compares it against independently evaluated scalar population formulas. It checks the energy spectrum, positivity, trace one, ergotropy, and convergence of the finite-collectivity slow-time expression to the proved limiting work profile. The local run returned `PASS: 580 density-matrix and slow-limit checks`.

The universal slow-time theorem and strict noncommutation rest on the algebraic population formulas plus the trace-norm ergotropy bound. Computed examples test some finite parameter values only. The asymptotic work plateau is a limit; exact passivity at every finite time or a microscopic implementation beyond the stated generator is **not** claimed. No independent external validation has been performed.
