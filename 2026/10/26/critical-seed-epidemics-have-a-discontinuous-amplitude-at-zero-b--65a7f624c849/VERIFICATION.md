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

The normalized Allen–Heller–Pons MB equations were independently differentiated and summed to obtain the four-variable reduction recorded in RESULT.md. Substituting \(d=S_1-\rho(S_1+S_2)\), \(\delta=\beta_1-\beta_2\), and \(\kappa=\rho\beta_1+(1-\rho)\beta_2\) reproduces every displayed term including \(-\rho(1-\rho)\delta SI\) in \(\dot d\). Integrating \(dI/dR\) gives the stated exact identity with the correct signs.

Analytic sign checks: \(d(0)=0\), \(\dot d|_{d=0}\leq0\), and \(0<I(t)\leq\varepsilon e^{-\kappa\varepsilon t}\). Positive-turnover variation of constants bounds \(-d\) by \(\rho(1-\rho)\delta\varepsilon/a\). The resulting balance bounds force the \(\sqrt2\) coefficient for every fixed \(a>0\). At \(a=0\), the differentiable strictly increasing root equation has \(F_0''(0)=M_2>1\) and \(F_0'(0)=0\), yielding \(\sqrt{2/M_2}\). Uniform late-time decay for each fixed positive \(\varepsilon\) justifies continuity in \(a\); it does not justify interchanging the two singular limits.

For the exact rational example, \(\kappa=7/16\) and \(M_2=76/49\). A numerical ODE integration using scipy.integrate.solve_ivp with method DOP853, relative tolerance \(2\times10^{-9}\), absolute tolerance \(10^{-13}\), and termination near \(I=10^{-11}\) produced ratios: \(a=0,\varepsilon=10^{-3}\): \(1.1290062\); \(a=0,\varepsilon=10^{-4}\): \(1.1334484\); \(a=0.05,\varepsilon=10^{-3}\): \(1.3186719\); \(a=0.05,\varepsilon=10^{-4}\): \(1.3784199\). The zero-turnover ratios independently match a scalar root solver at the shown precision. These finite checks do not establish the asymptotic theorem, which is proved symbolically.

Limitations: critical threshold only; non-equilibrium behavioral initial proportions and jointly scaled turnover are not covered. Independent mathematical audit and independent validation have not been performed.
