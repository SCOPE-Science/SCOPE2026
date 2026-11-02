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

# Exact computational checks

Execute `python3 proof_checker.py`. The code uses exact integers and rational fractions only; it constructs the polynomial certificate, verifies that every expansion coefficient matches the independent rational expression, and checks all 65 Bernstein coefficients. It also recomputes the explicit example from the four probability formulas and checks \(b_*(1/10)=462/551\) and \(E_2-1=19650205/6450554528\).

Observed output:

```
PASS: 65 nonnegative exact Bernstein coefficients establish R(h,t)>=0.
PASS: exact polynomial identity D(h,t)[1-E(b_star)]=h*t^2*R(h,t).
PASS: independent rational example E-1= 19650205/6450554528
```

These are checks of actual embedded checker code and exact algebra. They do not establish independent audit, the scientific applicability of the assumptions, or priority over uninspected literature. Strict inequalities on the continuum additionally require the positive-denominator and Bernstein-basis arguments in `RESULT.md`.
