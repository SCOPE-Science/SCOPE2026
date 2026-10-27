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

Run `python3 verify.py` in the same directory. The script uses only the Python standard library and reconstructs Gram similarities over the finite fields with two and four elements (using the polynomial \(t^2+t+1\) for the latter). For all \((q,n)=(2,1),(2,2),(2,3),(2,4),(4,1),(4,2),(4,3)\), it counts matrices with \(A^TA=cI\), compares isometry and similitude counts to the closed formulas and restores the additive shear factor. It separately checks the linearized Jacobian ranks over characteristics \(2,3,5,7\), in 44 parameter cases, for the dimensions claimed. Actual terminal check: `VERIFY_OK finite_field_count_cases=7 tangent_cases=44 total_cases= 51`.

The symbolic group-scheme argument and finite-dimensional orthogonal geometry prove statements for all dimensions and fields. A finite computation cannot certify this infinite statement or its originality. Independent mathematical audit has not been performed.
