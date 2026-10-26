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
# Verification and limits

The supplied `verify.py` uses only Python standard library, builds the GeCo2 map independently from the componentwise published stages, and compares it with the scalar reduction. It checks numerical solutions of \(z(1+e^{-z})=4\), values of \(b_c\) and \(1/b_c\), existence and fidelity of the predicted two-cycle at several supercritical steps, finite-difference local Floquet multiplier, and representative positive mass-conserving updates. It reports its deterministic check count upon execution.

Finite floating-point checks cannot establish uniqueness on an interval, infinite-time convergence, or the analytic critical coefficient. Those conclusions are established by the endpoint inequalities, monotonicity of \(\varphi\), the reciprocal telescoping proof, an exact derivative identity and the implicit-function argument in `RESULT.md`. They assume exact arithmetic, two components, symmetric exchange and strictly positive starts. The independent audit channel has not been performed.
