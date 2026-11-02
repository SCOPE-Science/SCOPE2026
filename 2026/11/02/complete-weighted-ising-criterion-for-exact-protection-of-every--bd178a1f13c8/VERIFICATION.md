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

# Verification of complete weighted-Ising singlet protection

The analytical proof in RESULT.md is the support for the universal statement over every even number of qubits. This file records finite independent cross-checks and explicitly limits their evidentiary reach.

Run \(\texttt{python verify.py}\) with Python 3 and \(\texttt{numpy>=1.24}\). The standalone program builds the computational-basis Hamiltonian, constructs the total-spin raising matrix in the zero-magnetization sector and forms the singlet projector from its nullspace without assuming the dimer-space calculation. It tests \(N=2,4,6,8\), dimension \(C_{N/2}\), heterogeneous additive couplings and sparse stars, arbitrary nonadditive edge and field samples, the energy-variance formula for perfect matchings, and nonzero projector leakage of controlled violating Hamiltonians.

Observed output: \(\texttt{PASS 435 finite independent checks}\). Numerical tolerances are declared in the verifier. The checks do not exhaust all interaction coefficients, all matrix sizes, or numerical precision. In particular, an energy variance is not automatically the squared norm of leakage outside the whole singlet subspace.

No independent audit has been performed.
