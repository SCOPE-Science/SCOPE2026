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

# Verification record

Run `python verify.py` with Python 3 and SymPy. The checker independently confirms the two exact resonant output identities, the leading Laurent coefficients in the full Jacobian determinant, and 200 direct floating-point evaluations at both signs of resonance, and 12 directly evaluated nonzero fixed-point witnesses. It prints `VERIFICATION_OK` when all tests pass.

The universal rank classification additionally relies on the analytic zero-set theorem and explicit sign symmetries; the singular invariant-probability conclusion follows from the one-step image inclusion; fixed-point infinitude follows from two intermediate-value arguments. No finite numerical test certifies these infinite claims. The equation is not defined when any input coordinate vanishes. Independent mathematical audit has not been performed.
