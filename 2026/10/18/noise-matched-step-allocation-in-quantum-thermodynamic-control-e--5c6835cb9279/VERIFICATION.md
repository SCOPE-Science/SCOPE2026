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

The analytical argument proves the continuous square-completion identity, existence and uniqueness of the matched schedule, the strict metric-speed comparison, and the integer-grid asymptotic bounds. All domains, quantifiers, and finite-noise qualifications are given in RESULT.md.

To reproduce the numerical checks, run `python3 checker.py` with a Python 3 standard-library installation. The checker evaluates independent hyperbolic-function and binary-Gibbs-curvature formulas, integrations for variable local noise, numerical comparisons of monotone ramps, exact discrete objective identities, and small-noise upper bounds. Expected output: `PASS: 236 numerical assertions; all checks are finite tests, not an infinite proof.` The complete executable checker is included alongside this document.

Numerical testing is limited to the sampled parameters in the executable. No exact physical quantum-work simulation beyond the quadratic expansion is claimed, no finite tests certify continuum quantifiers, and no independent audit has been performed.
