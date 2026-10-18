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

# Mathematical and computational verification

The analytic certificate reduces each pairwise score bound to a quadratic scalar inequality. A sum of positive-semidefinite edge blocks bounds both extreme eigenvalues on every principal submatrix; interlacing handles the entire ordered spectrum. The complete-bipartite construction proves that no smaller universal degree coefficient can work. The companion `verify.py` performs deterministic numerical checks on 5,693 random/support-family instances, checks exact pairwise score saturation in the extremal family and checks the spectral ratio approaching the optimal constant. Floating-point checks are used only as consistency tests, not as substitutes for the proof.

**Unproved extensions:** stability under roundoff, computational speedup, eigenvector approximation, relative eigenvalue error, and sparsity preservation by a sequence of rotations. No independent audit has been performed.
