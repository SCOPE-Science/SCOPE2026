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

# Verification of the explicit two-token phase boundaries

The program `verify.py` was executed using the embedded source, and its stdout was compared byte-for-byte with `verification_output.txt`. It directly evaluates the full nonlinear softmax update and central-difference Jacobians, rather than inserting the claimed Jacobian as a test input. It tests all three named canonical families for multiple positive parameters, exercises fifty-seven resonance-circle parameter/angle cases, and uses exact fractions for an explicit coexistence example.

The infinite-parameter assertion is established by the algebraic proof, not by the finite test suite. The numerical tests use floating arithmetic and a tolerance of \(3\times10^{-6}\); they do not constitute interval or machine-checked formal certificates. Nonhyperbolic boundaries are identified algebraically, without a claim of asymptotic attraction there. Tests cover only neighborhoods where the normalized map is defined.
