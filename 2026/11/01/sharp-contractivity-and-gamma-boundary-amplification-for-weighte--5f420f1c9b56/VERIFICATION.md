---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For alpha>-1 (beta=alpha+1) the complex weighted Poisson kernel has positive Fourier multipliers r^n and negative-frequency multipliers m_k=r^(-k) I_(r²)(k,beta)=r^(-k)Pr(N>=k) for N negative-binomial(beta,r²). Parseval makes the circle L² norm a supremum of these. When beta<=1 negative-binomial convolution with shape 1-beta stochastically bounds S_k by r^(2k), so only constants are norm extremizers. For beta>1, the pmf ratios r²(k+beta)/(k+1) strictly decrease, forcing increasing discrete hazards and a unique or two-adjacent-mode maximizer. The first crossing m1=1 occurs at unique r solving (1-r²)^beta=1-r. Incomplete-beta-to-Gamma scaling for k(1-r)->t, with uniform tail escape bounds, gives F_alpha(t)=e^t Gamma(beta,2t)/Gamma(beta), strictly uniquely maximized at t_alpha since Gamma survival hazard increases 0 to 1. For alpha=1 the exact m_k=r^k(1+k(1-r²)) yields switching radii rho_j and limit 2/sqrt(e). Independent scipy multiplier checks at alpha=-.5,0,.5,1,2 and radii bracketing thresholds agreed; finite samples are not proofs of universal limit.

## originality

PASS

Direct statement-level comparison with relevant original primary research and semantic published-finding records did not identify an equivalent or dominating fully checked result. Known premises are attributed; nontrivial new specific quantitative conclusions assessed at qualified best-of-knowledge level. Inaccessible and incompletely inspected papers remain explicit residual priority risks.

## value

PASS

The radius at which a natural complex weighted Poisson extension ceases to contract L², the actual mode responsible, and the nontrivial boundary Gamma amplification quantify a coherent stability question. The all-real-positive-weight mode classification and unique asymptotic frequency scale are structural new conclusions relative to the known coefficients, with a sharp natural transition at alpha=0; not merely reproducing single-mode formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
