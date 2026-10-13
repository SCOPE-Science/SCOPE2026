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
# Reproducibility and checks

Run `python3 verify.py` with Python \(\ge3.8\); only standard-library modules are imported. The checker symbolically forms the two piecewise-linear Watson-centered bridge kernels with exact rational polynomial arithmetic and compares **all coefficients** of
\[
\int_0^1\bigl(\min(s,t)-st-s(1-s)/2\bigr)^2dt=s^2(1-s)^2/12.
\]
It exactly verifies \(\int_0^1s(1-s)/12\,ds=1/72\) and the independent-pair Watson moment \(\mathbb Eh(V_1,V_2)^2=1/720\); it tests positivity and strict correlation monotonicity numerically over \(2\le n\le200\). A separate seeded Monte Carlo simulation evaluates Watson and Anderson–Darling **from the order-statistic formulas**, at \(n=1,2,4,9,20\). It uses \(60{,}000\) independent samples at each of the first four sizes and \(40{,}000\) at the last. The run produced:

```
EXACT_ALGEBRA_OK centered_bridge_polynomial= ('0', '0', '1/12', '-1/6', '1/12', '0') independent_watson_kernel_second_moment= 1/720
SIMULATION_OK [(1, 60000, 0.0, 0.0), (2, 60000, 0.0139976, 0.0138889), (4, 60000, 0.0209547, 0.0208333), (9, 60000, 0.024895, 0.0246914), (20, 40000, 0.0261595, 0.0263889)]
VERIFY_OK
```

The simulation is not an infinite-sample or all-size proof. The beta logarithm moments and the triangular Anderson–Darling kernel integral are analytically evaluated in the main proof; no claim of formal-machine or external independent certification is made. All source-dependent statements are accompanied by bibliographic references in the result and audit. The formulas do not apply to fitted composite nulls. Correlation is undefined at \(n=1\) because the Watson statistic is constant.
