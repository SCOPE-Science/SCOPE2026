---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The numerator of t_S is ka(x²+kappa y²)+a(1+kappa)xy sum_epsilon_i, where iid epsilon_i are fair row-products. Negativity is equivalent to cross-sign and |B|/k>(x²+kappa y²)/((1+kappa)|xy|). AM-GM sharply minimizes the right-hand threshold at chi=2sqrt(kappa)/(1+kappa), attained for |x/y|=sqrt(kappa), and binomial signs enumerate B=2J-k. With sketch-null direction denominator zero, numerator zero and minnorm t=0, so no negative event. For kappa=1 numerator=||Sb||². Negative t strictly raises true Euclidean residual since b^T A b>0. Independent exact sign enumeration of all row-product configurations k=1..7 and four square ratios reproduced the sharp tails and endpoints. The infinite k/real kappa theorem comes from AM-GM, not sampling.

## originality

PASS

Best-of-knowledge novelty of the precise final theorem survives comparison with relevant antecedents and currently indexed mathematical literature, but not exhaustive historical priority. An equivalent sketch-and-solve formulation uses sign products B, but no accessed matching full distribution/threshold theorem was found.

## value

PASS

The first sketched Krylov step is a natural minimal failure mode: a discrete sign ensemble has a nonvanishing adversarial wrong-step probability even for SPD matrices arbitrarily close to the identity. The precise binomial staircase and discontinuity identify a useful algorithmic boundary, not merely a generic observation that sketches can err.

The dated certificate retains the supplied scientific assessment, sources and limitations.
