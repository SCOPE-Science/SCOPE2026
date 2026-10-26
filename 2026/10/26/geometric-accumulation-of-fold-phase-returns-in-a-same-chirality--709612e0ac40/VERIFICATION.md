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

## Analytic checks

1. Differentiate \(\theta_\lambda(x)=x-K\log h_\lambda(x)\); the fold equation is \(h_\lambda-Kh_\lambda'=0\).
2. Divide the fold equation by \(\lambda\) and use the \(C^2\) expansion to obtain \(g-Kg'+O_{C^1}(\lambda)=0\).
3. Apply the implicit function theorem at the simple root \(x_*\) to get \(x_f(\lambda)=x_*+O(\lambda)\).
4. Expand the positive logarithm at the fold to obtain \(\theta_f(\lambda)=K\log(1/\lambda)+C+O(\lambda)\).
5. The derivative \(-K/\lambda+O(1)\) is negative for sufficiently small positive \(\lambda\), so the phase-locked sequence is uniquely defined for all sufficiently large indices.
6. Exponentiating the phase equation gives the geometric ratio \(e^{-2\pi/K}\).

## Limits of verification

These checks establish the local-model theorem under its stated assumptions. They do not verify those assumptions for every symmetry-breaking family, nor do they establish a universal ratio for actual heteroclinic tangencies. A full-flow use requires checking the higher-order transition terms and the relation between the fold phase and the tangency phase. Independent audit and independent validation have not been performed.
