---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For every bounded centered rank-one copula density c=1+q(u)p(v), the essential extrema alpha<0<beta of q give a valid binary latent J with pi=-alpha/(beta-alpha), w=(q-alpha)/(beta-alpha), and conditional V densities 1+alpha p,1+beta p. Thus U->J->V is Markov, establishing 0<=I(U;V)<=H(J)<=log 2. Equality forces pi=1/2 and deterministic common J measurable from each coordinate; both margins are uniform and conditional independence gives exactly two equal-measure matching rectangles with density 2. Covariance through binary J bounds |rho_S|<=3/4; integration by parts for C=uv+g(u)h(v) proves tau=(2/3)rho_S. For t=1/4-r/3, A_t=[0,t] union [t+1/2,1], B=[1/2,1] have half measure, yield I=log 2, rho_S=3/4-3t=r and all r in [-3/4,3/4], including endpoints and zero. Independently recomputed exact sign first moments and rho for r=-3/4,-1/4,0,1/3,3/4; checked the analytical equality and boundary arguments. Does not extend beyond one separable bounded perturbation.

## originality

PASS

The sharp rank range and latent Bernoulli representation already occur in Blier-Wong; their accessible complete Sections 2 and 5 and appendices do not present mutual-information max at every fixed rank or the complete equality construction. Classical data processing supplies the log2 cap, not the flat conditional envelope and rank-prescribed maximizers. The 2014 Ebrahimi et al. mutual-information dependence paper could contain an equivalent model-specific comparison; only its abstract was available, so full-text noncoverage is NOT asserted. Best-of-knowledge priority qualified.

## value

PASS

The maximization of mutual information at fixed Spearman/Kendall rank in the natural rank-one Sarmanov family is motivated by interpreting correlation versus dependence strength. A uniform sharp information envelope with all extremizers, including zero-correlation maximum-information examples and endpoint attainable range, is a concrete structural classification potentially useful in copula modeling; not merely data-processing alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
