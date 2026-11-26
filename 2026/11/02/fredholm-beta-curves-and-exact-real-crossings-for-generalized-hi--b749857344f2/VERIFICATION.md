---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical verification notes

The all-integer crossing classification is analytic. Gamma recurrence gives the exact polar form, and the Euler product for hyperbolic cosine gives strict radial decrease. The phase passes exactly the specified integer multiples of pi. Distinct radii and the real and imaginary parts of the derivative prove the count and transversality. The prior Fredholm boundary and its compact operator model are inputs, not new assertions of priority.

The existing standard-library `CHECK.py` provides finite diagnostics for the symbolic normalization, reflection, modulus and phase, and numerical real-crossing locations up to parameter 15. It also contains checks about the known operator model. No finite test certifies the theorem for all integer parameters.
