---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In total concentration u and imbalance q, the equations are u̇=a u²q and q̇=−δu(1−q²)/2. Eliminating time gives u=Cδ(1−q²)^(a/δ). The physical-time quadrature diverges at both q endpoints, so it defines a complete nonstationary positive orbit approaching the origin at both ends; strict monotonicity of q yields the unique maximum. With k=a/δ and fixed q₀>0, the normalized quadrature on [0,q₀] has endpoint coefficients 1/(2q₀k) and (1−q₀²)/(4q₀³k²): for f=−log(1−q²), g=(1−q²)⁻¹ one has g/f′=1/(2q), and differentiating gives the second coefficient. A split away from q=0 controls the remainder O(k⁻³). The even quadrature gives exact time reversal with q changing sign, so compact-time dependence before t* also gives the reflected Riccati arc after t*. Substituting q=z/√k makes the centered clock kernel converge locally uniformly to exp(z²); strict monotonicity gives compact-uniform inverse convergence, including balanced data with Cδ=u₀ and diverging width.

## originality

PASS

The fixed-rate homoclinic geometry and first integral at (1,3,1) are explicitly prior; integrability is not the novelty. The supported distinction is the quantified degeneration in physical time: exponential height for fixed positive imbalance, the two-term event clock, the compact-uniform inverse-erfi profile, and the selected, species-swapped post-singularity limit. The inspected matching statements do not already give or mechanically imply this package.

## value

PASS

This natural exchange-rate boundary is where a complete positive flow develops finite-time singular behavior in the limit. The peak scale and correction are needed to locate the increasingly narrow concentration excursion, the balanced regime exhibits an opposite time scaling, and the reflected arc identifies what the positive regularization actually selects after the limiting blow-up. These facts add dynamical information beyond the phase portrait or a conserved quantity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
