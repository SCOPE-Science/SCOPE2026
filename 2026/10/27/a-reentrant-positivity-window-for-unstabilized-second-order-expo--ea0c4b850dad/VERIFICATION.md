---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With q=e^(-x) and s=1-q, eliminating the stage gives R=q-rho s+rho(1+rho)s(1-s/x), the stated multiplier. For x>0, 0<s<min(x,1), so 1-R=(1+rho)s[1-rho(1-s/x)]>0 and R>-rho(1+rho)>-1 in the claimed contraction range. The derivative divided by q is -(1-rho^2)+rho(1+rho)[(2 sinh(x/2)/x)^2-2s/x]; this increases strictly from -(1+rho) to infinity since s/x decreases and the hyperbolic ratio increases. The unique minimum and positive endpoint limits, with R(2L)<0 by 4rho L<(1-rho^2)^2 for rho<=1/100, give two simple crossings and one bounded negative interval. At (1±eta)L, for 0<eta<1 fixed, the exponential and rho/x balances bracket the lower crossing, and the exponential and rho/x^2 balances bracket the stationary point. Thus both divided by L tend to 1. The respective exact equations yield e^(-x_-)=rho/x_-(1+o(1)) and e^(-x_m)=rho/x_m^2(1+o(1)); logarithms give coefficients 1 and 2 on log L with o(1) errors. For x=k/rho the scaled multiplier tends to 1-1/k, bracketing the upper crossing; there the exponential is superalgebraically small and the exact zero gives x_+=(1+rho)/rho+o(1). At x_m the term -rho/x_m dominates the other terms, giving the stated depth. The inspected checker is a numerical diagnostic, not the basis for these universal conclusions.

## originality

PASS

The supported distinct contribution is the bounded two-simple-zero sign-loss window with its unique minimum and sharp small-ratio locations and depth. The stage method, exact stability function, and unconditional linear stability (in a broader split range) are prior, not claimed as new. The strongest inspected positivity analogues involve different maps or different stabilizations and do not supply this sign theorem.

## value

PASS

Unconditional quadratic contraction masks a structural failure of positivity even for scalar decay. Proving loss and subsequent recovery, and distinguishing the two logarithmic scales from the reciprocal recovery scale, identifies where the failure occurs and how weak but persistent it is as the explicitly treated split vanishes. The value is in this sharp failure mechanism and regime, not a restatement of known stability or a claim for nonlinear or matrix problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
