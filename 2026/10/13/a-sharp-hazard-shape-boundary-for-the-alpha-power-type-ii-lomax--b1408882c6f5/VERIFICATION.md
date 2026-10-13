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

# Mathematical checks and limits

The CDF, density, survival and hazard were algebraically reconstructed from the source's equations (2.4)–(2.7). The numerical-stability form
\[
h(x)=\frac{\theta}{\lambda+x}\frac{\alpha(e^{t(x)}-1)}{e^{\alpha t(x)}-1}
\]
was directly differentiated. The exact derivative identity is
\[
\frac{d\log h(x)}{dx}=\frac{\theta K_\alpha(t(x))-1}{\lambda+x}.
\]
The proof in RESULT.md explicitly checks both \(\alpha\le1\) and \(\alpha>1\), both sides and equality of the critical boundary, \(x\downarrow0\), and \(x\to\infty\). The core universal strict-monotonicity step is proved analytically using the derivative of \(\sinh z/z\), not inferred from a plot.

To reproduce the finite checks, execute `python3 hazard_phase_checker.py`. It requires Python 3.11 or later and only the standard-library `decimal` module. The completed run of the exact packaged script reports:

```
finite derivative identity tests: 360
alpha=2, theta=2: x*/lambda= 0.06788960253492849930452255336622850752459049227671769657967813173898908
alpha=2, theta=2: hazard maximum (lambda=1)= 1.34699989940591358088412858215633954857732887468980836163678348816863365
test status: PASS
```

The checker uses 72-digit decimal precision and tests the logarithmic derivative against centered differences across eight powers, three Lomax shapes, three scales and five positive times. It additionally verifies the rational boundary at \(\alpha=2\), the exact radical peak, sign changes, and several decreasing cases including boundary equality. Finite checks do not certify infinitely many parameter values: the analytic proof does. The listed computation depends on Python decimal behavior and is reproducible without source data.

The literature comparison supports a provisional mathematical originality assessment, not a proof that all publications have been found. Independent audit and external certification have not been performed.
