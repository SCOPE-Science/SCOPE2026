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

## Mathematical checks

- At a geodesic sphere, \(\kappa_i=\coth R\), so \(\widetilde K^{\alpha/n}=(\coth R-1)^\alpha\) is constant and the sphere is stationary.
- The variation of the shape operator is \(\delta\mathcal W=-\nabla^2u-u(\mathcal W^2-I)\); its trace gives the stated \(\delta H\).
- The derivative of the area average equals the average derivative at a constant reference speed; this is the source of the projection \(u-\bar u\).
- The eigenvalues use \(\Delta_{S_R}Y_\ell=-\ell(\ell+n-1)\sinh^{-2}R\,Y_\ell\).
- The exact gap expression follows from \(\coth R-1=2e^{-2R}/(1-e^{-2R})\) and \(\operatorname{csch}^2R=4e^{-2R}/(1-e^{-2R})^2\).
- The volume asymptotic follows from \(\operatorname{Vol}(B_R)=\omega_n\int_0^R\sinh^n s\,ds\sim\omega_n e^{nR}/(n2^n)\).

## Scope of verification

The proof is analytic and covers every stated \(n,R,\alpha\). No code, finite enumeration, or numerical sampling is needed. The result is about the linearization only; nonlinear global rate constants and independent audit remain unperformed.
