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

# Verification of the valuation rank census

The accompanying `check_jordan_val.py` uses polynomial convolution modulo \((x^2,y^n)\) to construct the regular multiplication matrices, finite-field Gaussian elimination for every power, and second differences to reconstruct Jordan block multiplicities. It contains independent arithmetic for the extension field \(\mathbb F_4\). It also counts the strong-Lefschetz Jordan stratum directly, without using the valuation count as the tally.

The checker exhausted exactly these cases: \((q,n)=(2,2),(2,3),(2,4),(2,5),(2,6),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2),(5,3)\). In every case it confirmed the predicted rank of every power for every radical element and confirmed the number of elements with partition \((n+1,n-1)\). Its terminal marker was `ALL_TWO_VARIABLE_JORDAN_CHECKS_PASSED`.

These checks are finite and are not a substitute for the invariant-factor proof. The proof of the all-characteristic formula and the valuation fiber counts is in `RESULT.md`. The published-source comparison is bounded; the absence of a located equivalent theorem is not an independent priority certification.
