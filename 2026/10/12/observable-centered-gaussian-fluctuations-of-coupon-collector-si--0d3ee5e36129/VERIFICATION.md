---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Under the independent rate-one Poisson embedding, completion time M_n=max first arrival E_i has n exp(−M_n) -> Exp(1). Conditional on M_n=t and unique last index, its count is exactly 1; all other n−1 counts are independent Poisson(t) conditional on at least one. Thus each nested deficit indicator has p=q_j(t)=Σ_(r=1)^(j−1)t^r/r!/(e^t−1), and exact mean 1+(n−1)q_j, variance (n−1)q_j(1−q_j), covariance (n−1)q_i(1−q_j) for i<j. Since at t=log(n/w), (n−1)q_j~w(log n)^(j−1)/(j−1)! and off-diagonal covariances vanish under coordinatewise square-root scaling, the bounded triangular-array Lindeberg theorem yields independent conditional normals; compact-uniform w and Exp mixing yield the stable joint limit and independent W. The stopped martingale E[(K_n−nM_n)^2]=n E M_n=nH_n and q_j derivative O((log n)^(j−1)/n) imply observable S_n=K_n/n replaces M_n with centered errors o_P(1) even on unstudentized scales. Independent finite truncated-Poisson enumeration verified all stated nested-indicator covariance formulas for t=2,6,12,18 and index pairs (2,3),(2,5),(3,6). All-n CLT is analytical, not finite evidence.

## originality

PASS

The two closest full papers Long 2026 and Ilienko 2026 both give first-order common-Exp limits for scaled sibling deficits, whereas the audited theorem subtracts the random observed completion-time conditional mean and establishes the next-order independent Gaussian vector and exact conditional correlation decay. Long proves conditional Bernoulli noise negligible ONLY at the larger first-order a_n,j scale. Ilienko also establishes independent centered completion TIMES, a different observable. No direct implication was found; priority remains best of knowledge with occupancy-CLT literature risk.

## value

PASS

The first-order sibling deficits share one exponential amplitude and so are perfectly correlated asymptotically. The sharp question what remains after centering by the actually observable completion index is statistically and mathematically natural; the answer exposes independent second-order Gaussian noise, a mixed-normal version and exact finite-size conditional decorrelation powers. This adds a useful fluctuation layer to the established first-order coupon collector theorem rather than recalculating first moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
