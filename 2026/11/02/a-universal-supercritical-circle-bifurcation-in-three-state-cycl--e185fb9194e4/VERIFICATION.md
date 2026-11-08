---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

In Fourier coordinate z=x0+omega x1+omega^2 x2, the exact third-order analytic jet is lambda[(beta/3)z+(beta^2/18)bar(z)^2-(beta^3/54)z|z|^2]+O(|z|^4), lambda=1-epsilon+epsilon omega, |lambda|=r_epsilon. Hence tangent eigen modulus beta r/3 crosses 1 transversally at beta_c=3/r. The quadratic conjugate term is nonresonant for interior epsilon, with cubic normal form Re(bar(a)d)=-3/(4r^2) <0; excluding epsilon=2/3 removes strong 1:4 resonance. Standard Neimark–Sacker theorem gives locally normally attracting invariant Jordan curve of radius (2/3)r^(3/2)*sqrt(beta-beta_c)+O(beta-beta_c). At criticality inverse-square radius grows by 3/(2r^2)+o(1), hence |z_n|~r sqrt(2/(3n)) for nearby nonfixed trajectories. Epsilon=1/2 specializes beta_c=6 and cubic -3; not a global basin or rotation number claim. Independently checked exact normal form algebra at rational epsilon and numerical local behavior.

## originality

PASS

General discrete logit rock–paper–scissors models already have attracting invariant circles (Umezuki 2018) and softmax contraction (Wang 2026) while tied embedding feedback has known Lyapunov descent (Jones 2026). These results do NOT establish the exact cyclic mixing family threshold, universal radial coefficient, critical decay and radius law in inspected material. Umezuki is a serious plausible stronger source because the same cyclic map may be recast in payoff coordinates; complete source inaccessible (authorized VPN disconnected), so priority is qualified and a different parameterization could cover it, but no decisive coverage has been verified.

## value

PASS

Calculates a full motivated local phase transition for a natural minimal three-state feedback system, including rate and amplitude, beyond the known qualitative phenomenon that logit maps can exhibit circles. Universality of strict cubic sign over continuous mixing parameters is a substantive bifurcation classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
