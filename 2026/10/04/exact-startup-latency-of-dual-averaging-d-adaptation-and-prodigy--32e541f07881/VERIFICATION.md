---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Under the stated one-dimensional objective and \(D>d_0\sqrt8\), all gradients entering the cutoff computations equal \(-G\). For dual-averaging D-Adaptation, assuming the estimate has not yet moved gives \(s_n=-nd_0G\), \(\gamma_n=(G\sqrt n)^{-1}\), and the published proposal reduces to \(R_n=(n^{3/2}-1-\sum_{i=1}^{n-1}i^{-1/2})/(2n)\). Exact radical enclosures give \(R_1,\ldots,R_7<1<R_8\). For dual-averaging Prodigy with \(\lambda_k=d_k^2\), the analogous proposal is \(P_n=n^{-1}\sum_{i=1}^{n-1}i/\sqrt{i+1}\), with \(P_1,\ldots,P_4<1<P_5\). The assigned verifier replays the published recurrences and certifies the cutoff signs with rational square-root bounds.

## originality

PASS

The defining D-Adaptation and Prodigy papers contain the exact recurrences used here and motivate Prodigy as faster adapting, but the inspected full texts do not state the constant-subgradient startup cutoffs eight and five. The result is not merely a numerical replay: the cutoff follows from exact symbolic recurrences plus certified radical inequalities. Resultary searches for startup latency, first distance-estimate growth, and constant-subgradient dynamics returned no implication-equivalent prior theorem.

## value

PASS

Startup adaptation is the central advertised distinction between these learning-rate-free methods. The constant-subgradient objective isolates the estimator dynamics without confounding curvature or noise, and exact first-growth cutoffs are a meaningful finite boundary rather than an arbitrary iteration census. The eight-versus-five comparison gives a reproducible structural benchmark for the claimed acceleration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
