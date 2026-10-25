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

Running `python3 verify.py` on the accompanying standalone program returned `PASS: 1343 independent deterministic direct-matrix checks, monotonicity, signs, and weak-coupling limits`. The 1,343 cases comprise 336 grid cases, 1,000 deterministic pseudorandom cases, one exact-form counterexample comparison, and six small-correlation comparisons. Each reconstructs all four Nyström matrices and the objective directly rather than trusting the derived coefficient formula. The proof independently establishes the general two-site claim through the determinant/inverse identities, strict derivative positivity, and Taylor coefficients.

The program relies only on Python's standard library and exact real mathematical formulas represented at floating-point precision. It is *not* a symbolic proof or exhaustive enumeration of real parameters. The logarithmic counterexample sign and the positivity of the universal coefficients are proved analytically in RESULT.md. Independent audit was not performed.
