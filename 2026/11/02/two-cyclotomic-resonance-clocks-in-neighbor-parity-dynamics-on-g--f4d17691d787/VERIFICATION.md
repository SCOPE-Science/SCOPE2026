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

The two Python programs and the fixed-point loop included with this package use standard-library integer bit operations only. Run `python artifacts/verify.py`, `python artifacts/verify_fixed.py`, and `python artifacts/verify_fixed_points.py` from the package root. Outputs of these exact commands are recorded in `artifacts/verification_output.txt`.

Matrix-kernel comparisons test finite sizes and prescribed times; they are not a certificate for the infinite family. The proof uses the characteristic-two Laurent polynomial symbol, factorization into the irreducible \(\Phi_3\) and \(\Phi_5\) components, and separate local-primary Jordan arguments. A polynomial Smith-form calculation supplies a second formulation of periodic-point counts, checked against matrices over a finite parameter grid. Independent mathematical verification has not been performed.
