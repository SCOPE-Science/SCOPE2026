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

The attached `verify_apn.py` implements bit-polynomial arithmetic in five binary finite fields, tests every map for orders two and four and additional seeded maps for larger orders, and cross-checks all exact integer collision counts against the APN criterion. For ten seeded complex vectors at each field order, it compares the weighted two-sum convolution with \(|T|^2+2(S^2-Q)\), the direct two-dimensional Walsh transform's fourth moment with its Parseval form, and the analytic remainder with its pairwise sum-of-squares expression. Three sign-vector equality cases are tested in each field.

Run `python3 verify_apn.py` with Python 3 using only its standard library. The output ends with `TOTAL 50 complex moment + Walsh transform + deficit checks`. Integer equalities and exhaustive small-field enumeration are exact; floating-point checks use explicit tolerances. The universally quantified theorem and all equality cases are established by the proof in `RESULT.md`, not by extrapolating the numerical tests. This record is not an independent audit.
