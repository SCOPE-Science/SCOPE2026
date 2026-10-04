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

`verify.py` is a standalone Python-standard-library replay for the exact benchmark. It performs four checks:

1. An exact-rational sample verifies the algebraic identity between squared cross-MMD studentization and the scaled pooled-Student statistic.
2. A continued-fraction implementation of the regularized incomplete beta function evaluates Student survival probabilities and reproduces the reported 5 percent null sizes for \(s=5,10,20,50,100\).
3. Bisection of the exact Student survival function verifies that \(\sqrt{s/(s-1)}\,t_{2s-2,1-\alpha}\) gives exact size \(\alpha\).
4. Increasing \(s\) confirms convergence of \(s(\alpha_s-\alpha)\) to \(\phi(z)(z^3+5z)/8\) at the stated numerical tolerance.

A successful replay prints `VERIFY_OK`. The script numerically verifies the closed forms and a concrete algebraic instance; it is not used as a substitute for the analytic proof of the infinite family.
