---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Subtracting and averaging the monomer equations gives independent noise drivers of variances 4D and D in q and R, respectively. The q diffusion has potential V=a|q|²/2+b(|q|−ℓ)²/2 and diffusivity 2D, so its stationary reversible path law depends only on the stiffness sum. For ℓ>0 the bounded directional perturbation of the linear drift is locally bounded including at zero; localization and absolute continuity to planar Brownian motion make zero polar from the stationary initial law. On a finite interval away from that point the Stratonovich chain rule applies. Transforming the work in velocity units gives exact energy differentials plus 2δ F(q)·dR, with zero cross variation. Multiplication by γ/(kBT)=1/D yields σ=(2δ/D) E[F·(δF−aR)]. The stable causal center filter gives E[F·R]=δ〈F,(a−Lq)⁻¹F〉; the center noise convolution is independent of q. The remaining quadratic form has multiplier λ/(a+λ), strictly positive for the nonzero mean-zero F in L²(π), with constants the sole zero modes. At ℓ=0, each q component has variance 2D/(a+b) and cov(R_i,q_i)=δ cov(q_i,q_i)/(2a+b), giving σ=8δ²/(2a+b) as claimed. All identities use the fixed equal-bath, equal-friction model and the physical heat normalization.

## originality

PASS

The same-model predecessor solves the zero-length Gaussian case and simulates the nonlinear case; autonomous bond reduction and hidden dissipation as a general phenomenon are not credited as new. The supported contribution is the parameter-sharp combination of identical stationary bond path laws and an exact, strictly positive all-rest-length heat coefficient for this particular trapped nonlinear model. The closest ring formula eliminates the center lag and the linear-network formula assumes Gaussian dynamics; neither inspected result evaluates this resolvent coefficient or supplies its full nonlinear claim as a corollary.

## value

PASS

The constraint is observational rather than just a thermal-density identity: all equilibrium bond path statistics persist under asymmetry, while the heat changes by a positive computable coefficient times asymmetry squared. The result gives a route to that coefficient from a reversible bond generator without having to solve the nonlinear four-dimensional stationary density, filling a precise gap in the positive-rest-length model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
