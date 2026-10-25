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

# Verification details

Run `python3 verify.py` with Python 3 standard library in the same folder as `RESULT.md`.

Observed result: `VERIFY_OK support_cases= 40 quadratures=3 spherical_cases=3 asymptotic_ratios=3 edge_cdf=3`.

The program exhaustively compares zonotope segment-sign supports against sum-of-absolute-differences supports on forty small deterministic cases, integrates the Gaussian contractions in the analytical proof, checks Monte Carlo spherical width means/second moments against a previously published formula, checks three aspect-ratio asymptotic variance predictions against exact finite-size moments, and numerically verifies the sharp left-edge coefficient for the one-vertex part case. The proof of limits is analytical; neither enumeration nor simulation establishes them in general. The source identifiers refer to public literature; no external independent validation was performed.
