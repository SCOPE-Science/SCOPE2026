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
# Verification

The argument was checked at three levels.

1. **Published quotient.** The exact right-hand side of Exner--Spitzkopf equation (3.6) was read from the open full text and transcribed before taking the scaling \(L=x/\tan(\beta/2)\). The source also states \(\epsilon_{\mu_\perp,\rho_\beta}\to\epsilon_{\mu_\perp,\rho}\) and \(\eta_{\rho_\beta}\to\eta_\rho>0\).

2. **Analytic optimization.** After \(y=\eta_\rho^2x\), maximizing the coefficient is equivalent to maximizing \(g(y)=y^2(\Delta-a y)/(1+y)\) on \((0,\Delta/a)\). Its derivative has the sign of \(2\Delta+(\Delta-3a)y-2ay^2\), which has one positive root and one negative root. The positive root is the displayed \(y_\star\), and both endpoint values are zero.

3. **Delta profile.** For two attractive delta interactions at \(\pm\rho\), the even bound state gives \(2\kappa=\alpha(1+e^{-2\kappa\rho})\). Direct integration of its squared norm with central amplitude one gives \(\rho+(e^{2\kappa\rho}+1)/(2\kappa)=\rho+(2\kappa-\alpha)^{-1}\).

The bundled `verify.py` numerically checks the optimizer identity and the delta normalization algebra over representative positive parameters. Numerical checks are not used to infer the infinite-dimensional spectral limit.
