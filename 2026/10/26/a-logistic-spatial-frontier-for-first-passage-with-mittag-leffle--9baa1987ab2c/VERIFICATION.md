---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: The rate law is normalized explicitly by E exp(-s lambda)=1/(1+s^alpha). The quoted positive-rate survival integral at x=exp(y/alpha), after r-substitution and dominated convergence, yields P(alpha log lambda>y)->(1+exp(y))^-1. Brownian scaling gives alpha log(H_x/2)->2b for alpha log x->b. For finitely many targets, joint convergence of finite rate prefixes and vanishing probability of near-ties yield exponential separation between all pre-success block integrated rates and the Brownian hitting threshold, and crossing within a vanishing fraction of the first superthreshold block. Tail P(K_b>=L)=u_b^L closes the finite-prefix limit. Transform iid logistic levels to uniforms to derive exact geometric joint tails, the independent-increment waiting-time kernel, and the Poisson-jump generating function exp(sum_d u^d(z^d-1)/d). Monotonic target coupling gives the two outer regimes alpha log x->+/-infty. Independently enumerated quartile uniform-threshold samples (prefix lengths 4 and 6), matching the exact two-level increment law. The proof gives only finite-dimensional distributional convergence, not path-space or moment convergence.

## originality

PASS

PASS, qualified: Levit–Reuveni motivate the heavy-tailed refreshed rate and provide its survival formula but primarily examine lattice-walk first-passage means and fixed-distance/parameter regimes. The current theorem is for the explicitly different continuous Brownian time-change and simultaneous exponential-distance singular limit, including joint target dependence. General stochastic-diffusivity first-passage formulas do not directly give this exact spatial independent-increment field. The closest Levit–Reuveni full text was not accessible during this run and therefore is a material priority risk, not asserted not to cover the claim in full.

## value

PASS

PASS: Multi-target hitting times of a shared continuous diffusion in a strongly singular random environment form a natural coupled stochastic object. The explicit geometric marginals, independent-increment spatial law, jump-rate description, and sharp exponential-distance trichotomy classify a genuine scaling frontier rather than merely computing a geometric distribution. The distinction between joint spatial increments and physical-time increments is mathematically consequential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
