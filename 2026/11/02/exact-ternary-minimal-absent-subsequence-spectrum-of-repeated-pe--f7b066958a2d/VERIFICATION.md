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

The mathematical identity is checked without external packages by `verify_ternary_periodic_mas.py` using `ternary_mas_algebra_certificate.json`. The certificate has nine polynomial entries and verifies \((I-M)p=Dw\) and \(vp=N\) coefficient-by-coefficient in the integral polynomial ring. This is an exact algebraic check of the generating function for every repetition index and length.

Independent direct occurrence tests covered 143,310 literal target words over 12 small hosts, identifying 740 minimal absent strings and agreeing with the local criterion. A separate transfer recurrence agreed with the bivariate rational coefficient identity in 1,035 positions for bounded indices. The results were `VERIFY_OK direct_parameter_cases=12 literal_targets=143310 tested_MAS=740 rational_coefficients=1035 ternary_prefix=6,16,46,127,349,960,2640,7264` and `ALGEBRA_CERT_OK states=9 polynomial_terms=47`.

Limits: the finite exhaustive tests are bounded. The all-parameter theorem relies instead on the paper proof and finite exact polynomial certificate. No external independent assessment or formal proof-assistant certification was performed.
