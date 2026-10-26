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
# Mathematical verification

Run `python3 verify.py` from the same directory as this file. The script uses Python's standard-library exact rational arithmetic, not a floating-point root search.

It independently recomputes the equality
\[
\sum_{j=1}^{6}\frac{3}{2^{j+1}+3}-1=\frac{807979}{64203755}>0,
\]
checks a separate ten-term alternating-series upper bound for \(S(-3/2)\), and verifies the first four inverse Taylor coefficients listed by Tóth. The script must print `CERTIFICATE_OK` and exit successfully.

The infinite deductions are supplied in `RESULT.md`: absolute convergence permits the Lambert rearrangement on \(|z|<2\); positivity of derivatives ensures a unique simple negative zero; and the reciprocal's pole bounds its Taylor radius, refuting the conjectured coefficient decay. Numerical tests are not used to claim uniqueness, absence of other complex roots, or a sharp asymptotic constant.
