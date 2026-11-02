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

# Verification of two-point discriminant fibres

The standalone standard-library script `verify.py` enumerates polynomials over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), and \(\mathbb F_9\), using a separately implemented finite-field multiplication for the extension field. It evaluates the discriminant by the resultant of each polynomial and its derivative using exact finite-field Gaussian elimination, compares the resulting squareclass counts with the complete two-point Jacobi-series formulas, and checks the \(q=3\) exact bias and the bounds for \(q\ge5\).

Reproduce with `python3 verify.py`. The checked maximum degrees are \(7\) for \(q=3\), \(5\) for \(q=5\), and \(4\) for both \(q=7\) and \(q=9\). A successful replay prints:

`VERIFY_OK fields=4 degree_value_fibres=388 direct_polynomials=11828 exceptional_q3_and_bounds=PASS`

All output counts are finite checks and cannot alone establish the theorem for unbounded degree or other fields. The universal conclusion rests on the complete formal Euler-product and finite Fourier arguments in `RESULT.md`. No independently performed mathematical audit is claimed.
