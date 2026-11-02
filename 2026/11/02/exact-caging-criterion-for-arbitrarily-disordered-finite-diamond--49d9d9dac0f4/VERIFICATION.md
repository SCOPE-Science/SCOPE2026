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

# Reproduction and exact checks

Use `python diamond_cage_checker.py` with NumPy and SciPy. The checker constructs the full complex Hermitian matrix for independent disordered chain lengths, then separately constructs the local orthonormal cage basis. It checks the change of basis is unitary, that the transformed Hamiltonian has no inter-cage entries, that the block eigenvalue multiset equals that of the original full matrix, and that selected matrix exponentials have vanishing off-diagonal hub-to-hub entries. It independently perturbs one arm potential or one hopping amplitude and verifies the theoretically predicted lowest nonzero matrix moment.

On the distributed checker, the numerical tests cover \(N=2\) through \(N=12\), nine random parameter realizations each, giving 2,970 passed assertions and worst structural/spectral discrepancy \(2.52\times10^{-14}\). Re-run directly from the packaged file to validate the distributed code.

The general iff conclusion is an exact proof by adjacent-hub matrix moments and local invariant subspaces; floating-point agreement is corroboration only. The nonzero-edge hypothesis is essential to force equality of arm on-site energies from the third moment, and the absence of bypass edges is essential to identify the two- and three-step paths.
