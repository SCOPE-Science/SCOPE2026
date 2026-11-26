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

Same-uniform rounding preserves the order of the real arguments, giving expected distance equal to their difference by unbiasedness. Applied to the affine arguments, this contracts W1 by at most |a|, and completeness yields one invariant law of finite first moment. To exclude invariant laws outside that space (a small omitted step in the written proof), let R=1/(1-|a|). Pathwise distance from beta is at most |a|^n times the initial distance plus R. Invariance gives pi(|J-beta|>R+eps) at most pi(|J-beta|>eps/|a|^n), tending to zero; a=0 resets in one step. Thus every invariant law is finitely supported. Unbiasedness then gives mean beta. The integer inequality j(j-1)>=0 gives the sharp error bound beta(1-beta), with equality precisely for the Bernoulli law. Both Bernoulli atoms have positive mass, so invariance at the floor is equivalent to both affine images being in [0,1]. For a=-c these are (1+c)beta and beta-c(1-beta), giving exactly the two stated inequalities, inclusive. At beta=1/4, c in (1/3,3/5], the three affine images lie respectively in (0,1], (0,1), (-1,0); the three-site class is closed and communicates. Flow into -1 and the invariant mean give p(-1)=p(1)(3c-1)/4 and p(1)-p(-1)=1/4. The excess variance is 2p(-1). Past c=3/5, the negative site sends positive mass to 2 and a two-site substitute is already impossible. Exact integer balance and variance checks at c=1/3,2/5,1/2,3/5 independently confirmed the endpoints and 65/304 example (node /workspace/branches/independent-checks.js, record 2 block). The frozen verifier was inspected, not executed; global claims follow from the proof, not the test points.

## originality

PASS

The supported distinct result is the sharp precision-floor criterion across the entire scalar contraction range, together with the exact upper endpoint of the quarter-cell three-site phase. Do not credit the contraction argument, the overrelaxed invariant-law existence and rate, or the formulas within the already covered interval as independently new. The closest three-site classification assumes a>=-1/2; a separate same-model Gaussian result covers the full overrelaxation range for other conclusions but does not classify the sharp nonasymptotic floor or phase exit there.

## value

PASS

This identifies when overrelaxation can be used without any increase in stationary squared error, a concrete boundary that unbiasedness or a contraction rate alone does not give. At a quarter-cell, the exact interval of three occupied sites and its distinct exit threshold quantify when a new grid point is necessary. The value is that finite-parameter phase information, not a claim about practical floating-point implementations or the already covered numerical value in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
