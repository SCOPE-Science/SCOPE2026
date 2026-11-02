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

# Reproducible checks

Run `python3 verify_catalan.py` with Python 3.10 or later. It uses only the Python standard library and integer modular arithmetic. The observed output is:

```text
VERIFY_OK exact_integer_cases= 36 horizontal_cases= 144 vertical_cases= 132 levels=3..12
distinct_residues_by_k= [2, 4, 7, 13, 21, 33, 46, 63, 81, 102]
quadratic_lower_and_upper=True
```

The verifier independently computes 36 Catalan values from integral binomial coefficients, checks every required sampled adjacent valuation at 16-bit precision, and enumerates the complete finite cutoff grid for each displayed modulus. The proof of arbitrary exponents is in `RESULT.md`; neither the code nor these finite cases proves infinity on its own. The congruence-reduction theorem of Xin and Xu is prior published work, not re-certified here. Independent mathematical audit has not been performed.
