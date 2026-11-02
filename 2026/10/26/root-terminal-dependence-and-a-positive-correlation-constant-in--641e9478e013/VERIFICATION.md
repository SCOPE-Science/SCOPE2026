---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: Independently reconstructed the actual stationary Moran-forest representation: U_j independent uniform among the n−1 other labels, and edge U_j→j only if U_j<j, with an irrelevant final relabeling. For fixed other H indicators, flipping H_j from attachment to root removes one edge, so no terminal vertex is lost. For i<j, Cov(H_j,A_i)=(n−j)/(n−1)^2 q_n^(n−i−1); summing the independent-parent covariance gives the stated positive finite-n sum. E[A_iA_j]=q_n^(j−i) r_n^(n−j), r_n=(n−3)/(n−1), implying nonpositive off-diagonal terminal covariances because r_n<=q_n². A Riemann-sum limit gives covariance/n=1−5/(2e), and expansion of the exact terminal variance yields 1/e−2/e²; combining with the published root variance limit 1/6 yields the claimed correlation. Independently enumerated every parent configuration for n=3..7, checking exact rational means, variances, cross covariances and conditional influences against formulas. These bounded checks corroborate, rather than prove, all-n statements.

## originality

PASS

PASS (qualified): The full primary Moran forest paper supplies the independent-parent distribution and variance of the number of roots, as well as single-vertex degree laws. It does not state the cross covariance with outdegree-zero terminals, conditional edge-deletion stochastic order, ordered influences or limiting Pearson correlation. General uniform random recursive forests are a different distribution; related Resultary work concerns root degree versus leaves in a single uniform recursive tree, rather than total components versus terminals in the Moran law. The accepted contribution is this exact joint-dependence classification using antecedent construction, not the construction itself.

## value

PASS

PASS: In a stationary reproduction/ancestry forest, number of components and terminal progenitors are two canonical statistics. An explicit strictly positive macroscale root–terminal covariance and nonzero asymptotic correlation, despite pairwise negative terminal correlations, reveal a non-obvious global dependence. The pointwise conditional stochastic order and its arrival-index gradient provide more than a routine single expectation and are biologically/combatorially motivated by birth-time attachment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
