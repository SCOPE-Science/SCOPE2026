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
Run `python verify.py` after installing Python 3.13 and `sympy==1.14.0` (or another compatible SymPy release). The included script symbolically checks \(\dot C=0\), \(\dot H=0\), \(F=\nabla H\times\nabla C\), \(\nabla\cdot F=0\), the invariant-plane reduction, potential critical-point factorization, the exact energy gap, and the displayed homoclinic trajectory. The script prints a PASS line only after all assertions succeed; that output is evidence for those identities but is not itself a proof of the orbit census or uniqueness.

The full bounded-complete trajectory classification follows from the scalar Hamiltonian energy-level topology and convexity. Periods follow by exact quadrature of a factored cubic and the substitution described in the proof; the \(\delta\downarrow0\) singular asymptotic is obtained from explicit double-root expansions and the classical elliptic-integral endpoint expansion. These infinite statements are proved in `RESULT.md`, not inferred from sampled trajectories. The stationary measure statement additionally uses Poincaré recurrence and ergodic decomposition on compact invariant supports. No independent external mathematical audit has been performed.
