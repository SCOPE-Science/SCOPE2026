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

`verify_impurity_xxx_threshold.py` reconstructs the full three-spin Hamiltonian from Pauli matrices, forms its Gibbs state by spectral decomposition, traces out one spin, and computes Wootters concurrence directly.

The direct result is compared with the analytic impurity-neighbor expression over deterministic antiferromagnetic and ferromagnetic grids.

The script independently solves
\[
e^{6u}=e^{(2+4r)u}+4
\]
by bisection, checks monotonicity of its unique positive root, verifies the exact strong-impurity cubic constant and first correction, and checks convergence of
\[
\frac{T_c/J_1}{6/W(6/(1-r))}
\]
to one as \(r\uparrow1\).

Finite calculations are supplementary; uniqueness, monotonicity, and both asymptotic laws are proved analytically in `RESULT.md`.

No independent audit has been performed.
