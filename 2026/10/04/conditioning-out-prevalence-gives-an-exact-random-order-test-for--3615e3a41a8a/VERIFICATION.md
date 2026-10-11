---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Conditional on \(M_k=m\), every binary relevance vector has probability \(p^m(1-p)^{k-m}\), hence the conditional law is exactly uniform and independent of \(p\). Independent enumeration for all \(k\le8\) verified the submitted closed conditional-mean formula exactly. The source paper's online variance formula has leading term \(5p^3(1-p)/k\). Independently expanding the linear Hoeffding projection gives coefficients \(c_{i,k}=p+(1-p)/i+p(H_k-H_i)\); their normalized squared sum tends to 5. Differentiating the centering baseline contributes the projection on the total count, and the squared residual coefficients tend to 1, yielding the stated adjusted variance and the \(4+1\) split. Standard triangular-array Lindeberg plus negligibility of the degenerate quadratic remainder gives the two CLTs.

## originality

PASS

Manzhos--Ianevych--Melnyk provide exact offline and online expectation/variance formulas and explicitly leave statistical testing for future work. Their offline model makes the fixed-count uniform ordering visible, but the exact online conditional randomization test, the conditional baseline in the online normalization, and especially the plug-in CLT with variance reduction from 5 to 1 are not stated there. Resultary searches found no equivalent AP@k conditional-test or variance-split theorem.

## value

PASS

The result converts an existing random-ranking benchmark into an exact finite-sample, prevalence-free test and quantifies precisely how much asymptotic fluctuation is attributable to estimating/conditioning out prevalence. That addresses the source paper's explicit testing gap and supplies a practically interpretable variance decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
