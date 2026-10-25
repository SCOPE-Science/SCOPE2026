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

# Verification notes

The analytic proof is in `RESULT.md`. The critical steps are: (i) contractive existence/uniqueness for the stationary law; (ii) generator identities on three moments; (iii) explicit positive determinant; (iv) torque polynomial identity; (v) strictly positive threshold derivative. The proof does not rely on a numerical approximation or symbolic assertion.

Run `python3 verify.py` from this package. It requires Python 3 and no external modules, and prints `PASS: 347 exact rational parameter checks; stall and sign examples verified.` The checker independently computes the three unknown stationary moments from Cramer's rule and compares them with the displayed denominator and potential torque identity. It also checks the sign criterion and exact stall samples. These finite tests corroborate only the algebra: universal stationarity, positivity and monotonicity are proved analytically.

Exact scope is \(a,b,D_x,D_y>0\), \(c\ne0\), \(ab>c^2\), \(0\le\theta<1\), with \(r>0\) and an explicit continuous \(r=0\) endpoint. No claim is made about finite-temperature discontinuities, joint singular limits, jump work, or local current topology. Priority may depend on specialized literature not located in the stated comparisons.
