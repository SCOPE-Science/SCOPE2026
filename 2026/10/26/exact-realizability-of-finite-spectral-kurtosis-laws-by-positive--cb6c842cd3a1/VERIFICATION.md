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

The theorem is established analytically by four explicit steps in `RESULT.md`: conditional Gaussian fourth moments; the covariance integral identity; positive spectral decomposition of an irreducible reversible finite-state generator; and a positivity-preserving independent-two-state-chain construction. Uniqueness of the active exponential spectrum follows from the linear independence of distinct real exponentials. Boundary cases: an empty mixture means constant diffusivity; no bound on the maximum diffusivity is imposed; all positive rates and weights are finite.

The reproducibility artifact `verification/verify.py` uses only the Python standard library and exact fractions for stationary weights, generator construction, detailed balance, eigenrelations, covariance weights, positivity and prescribed mean. Execute `python3 verification/verify.py`; three cases with 2, 4, and 8 states return `EXACT_VERIFY_OK` if all assertions hold. A floating-point covariance comparison at three times in each case tests a separate semigroup evaluation. These finite examples are checks, not exhaustive proof of the theorem for all parameters.

The literature comparison uses accessible article text where available. The inaccessible full texts of two relevant comparison publications are explicitly named and remain priority risks. This record is not an independent audit or third-party certification.
