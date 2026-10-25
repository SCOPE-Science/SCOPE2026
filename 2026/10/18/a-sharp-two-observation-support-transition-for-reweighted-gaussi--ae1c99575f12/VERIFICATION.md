---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For weighted observations ±a, likelihood strict concavity in the two fitted kernel means gives uniqueness when the dual equality support is ≤2. Reconstructed sensitivity D_delta(z+t)=exp(-t²/2)[q exp(-2a(1-q)t)+(1-q)exp(2aqt)] with z=a(1-2q); published Schlemm sharp Kearns–Saul Bernoulli moment inequality, including its nonzero equality case, yields singleton iff a≤a_c(q). The derivative-stationarity equation for a positive Gaussian mixture has at most two local maxima, bounding any optimum support by two; linear independence of the two fitted kernel vectors proves unique measure. For unequal q, critical second dual contact at -z and negative curvature up to a_loc justify discontinuous-support onset with vanishing mass; q=1/2 contacts coalesce. Exact Gamma normalization gives Q~Beta(α,α), and a_c monotonic in |1−2q| yields 1−2I_{(1−x_a)/2}(α,α), with artanh(x_a)=a²x_a; x_a~sqrt(3(a²−1)). Independent numerical sensitivity and Beta checks confirm sample values but do not replace the global Kearns–Saul proof.

## originality

PASS

Best-of-knowledge comparison of the exact mathematical claim against published Resultary records and named primary literature finds no stronger statement implying its new sharp result. Distinguishes known general ingredients and specific overlapping endpoints; access limitations and unindexed priority risks retained rather than treated as absence proof.

## value

PASS

A closed-form support-count threshold, local-vs-global transition separation, and exact finite-sample random-reweighting probability for a natural Gaussian-mixture estimator provide a motivated small-sample structural classification not supplied by general high-probability sparsity bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
