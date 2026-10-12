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

# Reproducibility of the ordered-damping threshold

Run `python verify.py` in a Python 3 environment with SymPy and NumPy installed. This script constructs four Kraus operators from scratch for two unequal amplitude-damping channels separated by a real rotation, computes the normalized Choi partial transpose, proves the symbolic determinant identity after imposing rotation normalization, and checks the trace-preservation identity. A separate floating-point Kronecker calculation checks eight sampled positive, negative and boundary cases, including reversed damping order. The expected success line is `VERIFY_OK symbolic_Choi_determinant=passed Kraus_trace=passed numerical_cases=8 order_boundary=passed`.

These checks reproduce the critical algebraic identity from the definitions. The all-unitary reduction uses diagonal-phase covariance. The analytic fact that two-qubit partial transposes have at most one strictly negative eigenvalue is proved in `RESULT.md` using product vectors in two-dimensional complex subspaces; numerical sampling cannot substitute for that proof. Equality follows by continuity, not a tolerance test. The result is not verified for other local dimensions, nonunitary controls, generalized thermal damping or more than two damping stages.
