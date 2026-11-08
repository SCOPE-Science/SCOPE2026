---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For uniform recursive trees n>=2 with independent later parent choices, P(vertex i is childless at n)=(i-1)/(n-1). Conditional on this event later parents avoid i and are otherwise uniform; distinguished depth retains mean H_(i-1). The total-path-length conditional recursion gives E[T_n|I_i=1]-E T_n=-(H_(n-1)-H_(i-1)), hence the exact covariance product. Summation in the opposite order gives Cov(L_n,T_n)=-(n-2)/4. Adjacent profile differences equal (H_(n-1)-H_(i-1)-1)/(n-1), so unimodality follows; bulk profile -x log x and controlled endpoints give peak i/n and amplitude ->1/e. Independent full enumeration of trees through n=8 confirmed exact rational identities.

## originality

PASS

A leaf indicator is absence of all later attachments to marked i; this is distinct from conditioning a particular j on attachment to the root, and distinct from root degree-leaf covariance in published related Resultary work. The independent future-parent conditioning and harmonic shift directly supply a nontrivial joint statistic absent from the inspected marginal formulas; published root-degree results do not imply its exact leaf-index dependence or the sum -(n-2)/4. Best-of-knowledge priority risk remains explicit; unsuccessful search alone is not claimed as proof of novelty.

## value

PASS

A natural age-resolved dependence statistic in a canonical growth model reveals the nonmonotone 1/e peak and exact global linear anticovariance, information not obtainable from individual marginal moments. The finite-n formula is independently useful in probabilistic tree analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
