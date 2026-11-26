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

Independently using the reset-age representation, the stationary angle is an independent reset angle plus circular Brownian motion of independent Exp(λ) age. Its nth Fourier coefficient is the nth reset coefficient times λ/(λ+n²Drot), which gives c₁=aμ and c₂=bη. Coupling at the next reset also shows uniqueness of this stationary law. Conditional on the initial angle, the no-reset contribution to the centered velocity harmonic at lag s decays at k=Drot+λ, while on a reset all dependence on the initial angle is lost. Thus the centered lag covariance is exp(−ks)Σ. In planar coordinates 2Σ=(1−|c₁|²)I+H(c₂−c₁²). Integrating over both times and adding independent translational noise yields the displayed G_k(T) and effective tensor under Cov/(2T). For a circle variable Z of mean μ, |E(Z−μ)²|≤E|Z−μ|²=1−|μ|². Any boundary value is realized by the unique mean-preserving law on the endpoints of the appropriate line through μ; a mixture of opposite boundary phases realizes any interior value, and |μ|=1 forces a single atom. This proves the whole affine tensor disk. Isotropy is its containment of zero in the traceless coordinate, so q_*=b/(b+|b−a²|). At positive extremal drift rotate μ to the positive real axis. Equality forces a perpendicular chord for b−a²>0 and a parallel chord for b−a²<0, giving exactly the stated symmetric and antipodal weights. Since b−a²=t(1−2t)/[(4+t)(1+t)²], the transition has q_*=1 and unique deterministic reset; substitution gives v/3 and D+8v²/(27Drot). The four-atom example gives μ=1/2 and η=5/16, hence v aμ=1/4 and K=D+15/64 in each direction. G_k(T)>0 ensures that isotropy is exactly the same criterion at each positive finite time.

## originality

PASS

The supported distinction is the exact full fixed-drift tensor synthesis with arbitrary complex traceless phase, constructive finite-support laws, and its joint interpretation with the all-time covariance. The angular moment balance and circle moment disk are prior mathematical machinery, and the deterministic isotropic point at λ/Drot=1/2 follows from previous fixed-direction diffusivities. A later catalogue item overlaps the arbitrary-law long-time tensor and its sharp longitudinal-minus-transverse projection, with genuine implications for isotropic feasibility and extremizers; these parts are not credited as distinct against that comparator. Its stated interval is not the full off-diagonal disk. The inspected earlier literature does not give the fixed-drift tensor synthesis.

## value

PASS

The physical design question is to prescribe mean directed transport while controlling covariance in two dimensions, not to maximize one diffusion number in isolation. Complete feasible-tensor geometry and explicit finite-support realizations allow joint control of diagonal and off-diagonal fluctuations. Stationarity makes the same design apply at every observation time. The extremal isotropic transition is a meaningful comparison of reset protocols, while the complete disk is the substantive addition beyond longitudinal anisotropy alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
