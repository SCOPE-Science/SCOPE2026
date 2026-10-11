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

The bundled `verify.py` reconstructs the coefficient expansion of \(F^4\) from multinomial arithmetic, checks the exact \((A,B,R)\) identity, checks the derivative factorization for \(\Psi\), and checks the resultant polynomial for \(K_8^8\). It then isolates the unique positive root of \(35\tau^3-21\tau-2\) by bisection and reports the corresponding numerical constants.

The global proof does not depend on numerical search: boundary faces are bounded analytically by the two-character value \(35/8\), strict monotonicity in \(R\) forces equal endpoint magnitudes, and the sign pattern of the factored derivative proves uniqueness of the interior maximizer. Deterministic complex-coefficient samples in the checker are only a stress test for transcription or normalization errors.

Scientific limit: the verification establishes exactly the theorem for the continuous circle spectrum \(\{0,1,2\}\) at exponent \(8\); it does not certify a general formula for other supports or exponents.
