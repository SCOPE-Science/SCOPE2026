---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For each count vector the product of reinforcement factors is ∏x_i!, which cancels the sequence multinomial count and gives the uniform weak-composition law. Given X_j=r, the remaining d−1 parts uniformly compose n−r. Thus the conditional empty probability for i≠j is (d−2)/(n−r+d−2); subtract (d−1)/(n+d−1) and multiply by v_r to get (1). In the histogram covariance the d same-color terms each equal −uv_r, and the d(d−1) other terms equal (1); collecting gives the numerator d(r−1)−2(n−1). The common denominator is positive even at r=n; subtracting the two real cutoffs yields (d−2)(d+n−1)/(d(d−1)). The equality family satisfies n≥r and the three rational examples agree. At n=1, r=1 the aggregate is zero since the histograms are deterministic, while the distinct-color covariance is positive, as predicted. A separately written exact Fraction enumeration confirmed both covariances on 180 triples, d=3,…,7, n=1,…,8, all admissible r. The conditional counting proves all orders rather than extrapolating from the checks.

## originality

PASS

Credit classical uniform-composition and Dirichlet–multinomial laws, as well as antecedent exact unseen–doubleton aggregate coverage at r=2. The all-frequency local statement has strong equivalent overlap in a later indexed general-concentration theorem. The supported distinct result is the simultaneous all-r local/aggregate sign classification and strictly separated thresholds, not every individual ingredient or the doubleton case. No inspected antecedent states this general comparison or a stronger mixed-frequency theorem supplying it.

## value

PASS

The two signs answer different questions about unobserved categories under one natural reinforcement law. The exact separation and discordance (including attainable strict opposite signs and exact zeros) show why an inference from a pairwise indicator association to association between frequency counts fails. The result gives a finite-parameter test for every frequency, not just more numerical examples of the known doubleton effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
