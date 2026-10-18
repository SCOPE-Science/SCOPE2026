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

# Verification of the scalar sampled-feedback classification

Run `python verify.py` using Python 3.10+, SymPy and mpmath. The program checks the exact differentiation identity and exponential factorial-coefficient pattern, the undiscounted scalar gain, the exact discounted rational-in-exponential witness, direct numerical integrations and minimizer conditions on a reproducible parameter grid, the unique positive threshold root and the two example discount crossings. It prints the critical constants and exits successfully when checks pass.

The analytic sign-change argument for all derivative coefficients is established in the accompanying proof, not inferred from finitely many coefficients or experimental sampling. Likewise neither the finite numerical tests nor decimal root evaluations constitute validated floating-point interval certificates. The two prior theoretical settings compared are exact discounted ZOH running-cost discretization and discounted finite-horizon discrete-time stability; they do not by themselves establish the claimed necessary-and-sufficient result. No independent scientific audit has been performed.
