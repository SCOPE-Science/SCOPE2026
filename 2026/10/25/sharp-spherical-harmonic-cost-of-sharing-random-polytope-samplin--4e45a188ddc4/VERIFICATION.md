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

# Reproducible checks and scientific limits

The source identity is \(\mathcal I_j=\int\kappa^{1/(d-1)}H_{d-j}\rho^{-2/(d-1)}dS\) and the source's Hölder formula supplies the individually minimizing densities. The new analytic calculations comprise: the radial shape-operator expansion, normalization of \(p_j\), second-order Taylor expansion of the endpoint average and of the explicit common density, and the complete spherical-harmonic spectrum. These steps are written in the proof and do not depend on the numerical verifier.

Run `python verify_spherical_minimax.py` using Python 3 standard library only. It calculates meridional and azimuthal principal curvatures for \(r=1+\varepsilon P_2(\cos\theta)\), numerically integrates three different curvature-weighted optimal densities, bisects the exact two-objective weighted lower-bound stationary equation, computes the all-three-objective geometric-mean-density upper bound, and checks both quadratic coefficients approach \(1/5\). The program printed `CURVATURE_MINIMAX_QUADRATURE_OK` in the preparation check. It uses midpoint quadrature and does not give an exhaustive or interval-arithmetic certificate.

Proof coverage is for all integers \(d\ge3\), all index sets with at least two elements, and each fixed \(C^4\) radial direction, but only in the limit \(\varepsilon\to0\). The expected random-polytope limits hold for fixed positive continuous densities as sample size tends to infinity; no uniform interchange of these limits is assumed. There has been no independent scientific audit or independent numerical certification.
