---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For x>0 on a positive first-return leg, d(log x)/dt=(x-alpha)(1-x)-lambda y/(x+y). The prey jump sets log x(T-)-log x(0)=L=-log(1-p). Concavity of g(x) yields sup_{0<x<h} g(x)=rho piecewise with vertex (1+alpha)/2. ydot/y=lambda1 x/(x+y)-beta > -beta for x,y>0; the predator jump has y(0)=(1-q)y(T-)+tau>tau. Hence y(t)>tau exp(-beta t); first return yields x(t)<h. The predation fraction is increasing in y and decreasing in x, so y/(x+y)>tau exp(-beta t)/(h+tau exp(-beta t)). Its exact time integral is beta^-1 log((h+tau)/(h+tau exp(-beta T))). Thus L<F(T)<rho T for T>0, and T>L/rho. Fprime(T)=rho-lambda tau exp(-beta T)/(h+tau exp(-beta T)); the displayed sufficient condition makes Fprime>0 for all T>0, F(0)=0 and F→infinity, giving unique T_*>0 and T>T_*. The strictness, endpoint sup, positivity, and conditional quantifier were verified. Independent 55-digit mpmath computations reproduced both numerical root and frequency bounds to >25 digits. Finite numerical checks verify only the particular evaluations, not the all-parameter inequality.

## originality

PASS

Qualified best-of-knowledge: the model and elementary logarithmic device are prior, but the checked primary sources do not assert or dominate the release-corrected parameter-only necessary period inequality and its evaluated control-frequency ceilings. The same-result Resultary hit cannot be counted as earlier independent coverage. The derivation is short and plausible as an unindexed observation, so historical priority is not certified.

## value

PASS

A minimum permissible intervention interval is a natural control quantity in the originating 2019 paper because its economic objective is cost per period. The necessary release-dependent floor uses physical stocking tau and predator decay beta and requires no trajectory integration or cycle stability proof. The first example increases the lower bound from 1.5541271350 to 2.3686218445 (about 52%); the reported optimum increases it from 0.4727161250 to 0.6782308510 (about 43%). This quantitatively excludes overly frequent interventions for any existing positive order-one cycle, and is mathematically more informative than a mere normalization or sign check. Limits: the derivation is elementary and gives a possibly nonsharp necessary condition, not existence or feasibility at parameters without positive cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
