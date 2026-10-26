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
The proof independently derives the Pauli norm identity, both finite-group Fourier quadratic multipliers, the frequency upper bound and equality conditions, and the four-state trace-norm certificate. The checker `CHECK.py` is standalone (Python 3 standard library only). Its rational witness check enumerates all 16 group positions and all nine ternary increments and verifies the exact quotient of five. Fifteen numerical pure-qubit Fourier-mode tests cover side lengths 4, 6, 8, 10 and 12, and dimensions one through three. The numerical checks do not certify all parameters. The claimed infinite family is justified by the algebraic Fourier proof; no theorem is asserted about optimal higher-dimensional constants.
