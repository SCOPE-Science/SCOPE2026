---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of finite statements and asymptotic reductions

`python3 CHECKER.py` (Python standard library only) returned `exact checks 70`, with exact equality of two independent computations for two-core infection probability and expected peripheral outbreak count. The compared infection-rate values were 1/4, 1/2, 1, 3/2, and 2; peripheral sizes were every integer from 1 through 7. The independent computation is a continuous-time state-recursion with rational transition rates; the displayed formulas are binomial-integral expressions.

Additional deterministic convergence diagnostics at c=0.5, 1, and 2 and n=500, 2000, and 10000 approached the limiting core-infection probabilities c²/(1+c²) and limiting peripheral means c(1+c²/(1+c²)). These finite diagnostics are not an infinite proof. The infinite theorem depends on the conditional multivariate law of small numbers, the vanishing multiple-arc contribution controlled using only E[J]<∞, and the uniform-over-subsets binomial concentration step in RESULT.md.

The full Laplace expression follows by conditioning on the first core duration. For generic nonexponential infectious periods, only the general graph-valued limit is claimed. No independent audit, publication-priority certificate, or external mathematical validation has been obtained.
