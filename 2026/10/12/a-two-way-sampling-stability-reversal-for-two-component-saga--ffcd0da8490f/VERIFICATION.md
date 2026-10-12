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
# Verification

The accompanying `verify.py` was executed with Python 3 and SymPy. It separately reconstructs the three-dimensional SAGA index maps and six-dimensional quadratic lifts and checks that lifting commutes with map composition. It verifies that two rational symmetric Lyapunov matrices and their exact expected one-step or one-epoch decrements are positive definite using all three leading principal minors.

For both divergent sampling schemes it reconstructs the rational generating function of expected squared position error from the standard gradient-table initialization, verifies exact equality of rational functions, tests denominator signs at zero and one, checks numerator–denominator coprimality, and independently enumerates all possible sample paths through five grouped rounds (six lengths including zero). The scalar normalizations and the signed Bernstein basis check are exact, not estimated from floating-point experiments.

The strict Lyapunov inequalities prove geometric mean-square convergence in the stable schemes for arbitrary deterministic finite states. The pole argument proves exponential growth along an infinite subsequence of expected position errors for the unstable schemes from the specified initial state; it does not prove almost-sure divergence or an exact maximal domain of stability. The verifier is a reproducibility supplement to the analytic reduction in RESULT.md, not an external certification.
