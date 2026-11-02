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
Run `python3 verify.py`. No package installation or external data is necessary. The executable conducts 132 exact arithmetic and constant checks for dimensions one through four, comparing determinant polynomial coefficients with the trace-based expansion and checking the reconstructed determinant by independent Fraction Gaussian elimination. In each of dimensions two, three and four, it also samples 50,000 configurations from a thickened near-vertex region, then estimates the conditional event using the exact matrix determinant and a seeded random stream. Each numerical estimate fell within the coded finite-check tolerance of the two-term approximation. The analytical argument in `RESULT.md`, not any finite testing, supplies the quantifiers, universal coefficients, and conditional distribution limits.

The probability formula uses the ratio of the daughter's volume to the parent's volume and is therefore affine invariant; for numerical checks the parent was normalized to a standard simplex. Residual verification limits: no exhaustive numerical enumeration, no computation for all \(d\), and no independently performed audit. Historical priority of the previously inaccessible full articles is not proven by this verification.
