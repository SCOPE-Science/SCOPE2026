---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For D,r>0, 0<a<L, p∈[0,1], fixed hidden target B=±L drawn once and initial and every Poisson-reset launch iid from arbitrary Borel μ on [-a,a], Brownian hitting identity E_x exp(-u τ_b)=exp(-|x-b|√(u/D)) and renewal give mean (e^{cL}[p/M_+(r)+(1-p)/M_-(r)]-1)/r and discounted g_s(f)=(r+s)f/(s+rf). The convex chord of exp(±λx) lies below endpoint interpolation strictly at all interior x. Replacing interior μ by the induced endpoint measure strictly increases both exponential moments; because the mean decreases in them and every g_s increases, no optimal μ charges interior. Endpoint mass θ gives M_+=w+(v-w)θ, M_-=v-(v-w)θ, strict mean convexity and unique clipped θ*=clip((Sh-w)/(v-w)), h=√p/(√p+√(1-p)); thresholds p±=1/(1+e^{±4ca}) with p+=1-p-. The discounted objective is strictly concave in θ, yielding exactly θ_s=clip((((2s+rq(v_s+w_s))h-s)/(rq)-w_s)/(v_s-w_s)), where q=e^{-λL}. At p=1/2, θ_s=1/2 for all s>0; the cosh inequality proves unique worst-target minimax. Boundary p=0,1 and transition equality retain uniqueness. The result concerns Laplace order, not ordinary stochastic dominance. Independent 250 settings tested optimizer against independent bounded scalar optimization and strict endpoint domination; six discounts verified the symmetric identity. This is corroboration; proof is analytic.

## originality

PASS

Evans–Majumdar 2011 already derive arbitrary reset-position renewal mean formulas and variational stationary reset densities, including target prior averaging, so neither renewal nor location dependence is original. The claimed finding specializes to a previously unclassified design problem: a single hidden binary fixed target, same iid randomized launch/reset location under compact support, and global optimization over ALL Borel probability laws. Méndez et al optimize a known single target via rate or prescribed interval widths; Julián-Salgado et al allow two reset points with known target but vary resetting rate; García-Valladares et al optimize spatial reset rates instead of relocation law. These inspected full statements do not imply the sharp mixed-to-pure prior thresholds, universal p=1/2 all-discount law, or unique worst-target mean criterion. Resultary semantic search had no directly covering results. Best-of-knowledge PASS with residual possible convex-design equivalence.

## value

PASS

Optimal reset-location design for a hidden target is a natural infinite-dimensional stochastic-search problem. Exact endpoint support over all measures, unique bias at every prior, two threshold transitions and the much stronger symmetric all-Laplace statement yield actionable analytical design limits, not a trivial fixed-reset-point reparameterization or routine mean-only calculation. Restriction to Brownian fixed Poisson rate and no relocation costs explicitly bounds applications; Laplace order does not imply standard stochastic dominance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
