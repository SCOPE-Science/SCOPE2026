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

Reconstructed the uniform root-split law: with M right-subtree nodes, R_n=1+R_M and L_n=L_M+L_(n−1−M) for n≥2, with singleton leaf exception. H_M and leaf expectation (m+1)/3 outside m=0,1 yield covariance forcing a_n=(n−2)/(3n(n−1)) from only four boundary splits. Recurrence c_n=(sum_(m<n)c_m)/n+a_n gives ((n−2)(n+1))/(12n(n−1)). Independent exact enumeration of n=2..7 gives covariances 0,1/18,5/72,3/40,7/90,5/63. H_n−H_n^(2) right-record variance and known leaf variance give correlation sqrt(5/32)/(sqrt(n log n)); finite enumeration is not asymptotic proof.

## originality

PASS

Existing primary fringe-tree papers contain exact occupied-leaf moments and covariances between fringe counts, and extreme-key path papers contain depth marginals. Those separate ingredients do not explicitly give the exact covariance between the global rightmost search path and occupied leaf count; a new root-boundary cancellation gives the stated rational identity. No claim to exclusive priority against unknown mixed-function recurrences.

## value

PASS

The dependency between successful extreme-key search cost and occupied leaf count is a motivated algorithmic/tree statistic. Its exact positive covariance, 1/12 limit, vanishing correlation, and cancellation to four root-split boundary cases supply structural information absent from marginal means/variances. This is an independently useful exact mixed invariant, not a renaming of leaf moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
