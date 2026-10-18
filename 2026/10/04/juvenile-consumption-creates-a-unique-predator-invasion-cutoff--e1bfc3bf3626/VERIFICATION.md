---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

At the predator-free equilibrium xbar=r/a, u=0, prey perturbations have stable eigenvalue -r and predator linearization is autonomous because derivatives of its x-dependent coefficients are multiplied by equilibrium u=0. Along characteristics its renewal eigenmodes give F(lambda,g)=∫ Bbar(τ) exp(-∫_0^τ m0(s)ds -g*xbar*A(τ)-lambda*τ)dτ=1. The real positive mode exists iff R_P(g)=F(0,g)>1; for R_P(g)<1 a complex root with Re lambda≥0 contradicts |F|≤R_P(g). For the source's smooth positive juvenile indicator A(τ)>0 at all positive ages, so R_P is strictly decreasing and tends to 0 by dominated convergence, provided R_P(0)<∞ and positive-age births. It follows that one positive g_c exists iff R_P(0)>1. The displayed derivative lambda'(g)<0 follows from implicit differentiation if the age moment exists. Source finite-lifespan simulation avoids indefinite-tail spectral subtleties. These are local invasion claims, not global nonlinear extinction or general semigroup stability without tails.

## originality

PASS

The complete accessible Suarez et al. primary model gives numerical predator-free regime classification and identifies g as influential, but does not display this source-specific Euler--Lotka reproduction integral or unique monotone threshold. Related net-reproductive threshold work treats age-structured prey or different Lotka--Volterra interactions; generic Euler--Lotka is standard. The contribution is specifically the model's hazard-dependent complete-monotonicity and one-parameter uniqueness, not discovery of renewal theory.

## value

PASS

The source's numerical phase diagrams single out juvenile consumption as a main extinction parameter. An exact one-crossing law for that parameter provides a scalar analytically justified local invasion threshold, separates persistence from global dynamics, and can replace repeated local-stability simulations for fixed maturation age.

The dated certificate retains the supplied scientific assessment, sources and limitations.
