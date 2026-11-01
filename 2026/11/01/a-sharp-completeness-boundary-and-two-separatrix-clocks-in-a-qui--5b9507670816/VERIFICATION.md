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

The accompanying `verify.py` was executed from the same complete package. It checks the exact first-integral identity, the fifth-order time-preserving normal form, the Gaussian ceiling, and finite-amplitude quadrature comparisons for three parameter values and four amplitudes each. Its last line is `CHECK_OK` when all checks pass.

The mathematical proof is contained in RESULT.md steps 1–5. In particular, the asymptotic period theorem uses a uniform ratio of tail integrals away from the turning point and an explicit integrable strip estimate at that point. No finite quadrature sample is used as proof of either infinite-amplitude limit. The finite-time escape rate follows from a separate one-sided Laplace-tail identity.

The program requires Python 3, SymPy and SciPy. The checked region is not a computational enumeration of all possible parameters; all-parameter claims follow from the analytic inequalities. Verification is self-review only; independent audit is not performed.
