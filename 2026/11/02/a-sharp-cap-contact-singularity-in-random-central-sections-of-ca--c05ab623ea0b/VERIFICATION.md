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

# Verification of the exact capsule-section law

`verify.py` uses only the Python standard library. Execute it with `python3 verify.py` in the containing directory. It evaluates the exact closed profile, independently computes areas by Simpson quadrature of the point-to-segment inequality with an endpoint-smoothing substitution, checks monotonicity, and tests the reciprocal CDF branch and two asymptotic coefficients for three positive aspect ratios.

Observed output:

```text
PASS: 18 independently quadrature-evaluated sections; max relative area discrepancy 4.11e-13
PASS: strict sampled monotonicity, reciprocal CDF branch, endpoint asymptotics, 5/2 contact law
```

The analytic proof in `RESULT.md` supplies the infinite-parameter and asymptotic statements. Numerical integration at finitely many parameters neither proves universal quantification nor historical priority. The independent audit remains unperformed.
