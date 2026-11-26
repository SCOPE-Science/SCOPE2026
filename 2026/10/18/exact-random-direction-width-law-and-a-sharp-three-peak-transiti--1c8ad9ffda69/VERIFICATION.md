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

The four dot products give max(cos θ,a sin θ)+max(cos θ,b sin θ) on the uniform reduced quadrant. The two switches order as p≤q; intersecting the applicable cosine and sine sublevel sets with their respective intervals gives exactly the three CDF terms, including empty intervals and thresholds at branch maxima. The middle sine is concave, so minima lie at switches, and its derivative vanishes strictly inside exactly when 2p<π/2<p+q, equivalent to b>1 and ab<1. The outer endpoints are strict one-sided maxima; at a boundary equality the middle junction itself is not a third maximum. Each inverse branch there or at the interior peak contributes (2/π)/sqrt(M²−t²); multiplicities two, one, and zero give the interior, boundary, and empty-branch coefficients. Integrating each max(cos θ,k sin θ) on the quadrant independently gives sqrt(1+k²), verifying the mean. The example's peak levels round to 1.9171592980, 1.9508234187 and 2, and its minimum to 1.7172502208. The law is in the stated normalized length units: for original horizontal-diagonal half-length L, use F(t/L). The frozen numerical checker was inspected, not executed; the exact argument covers all shapes and the numerical checks do not establish it.

## originality

PASS

The distinct contribution supported by the comparison is the all-shape explicit sublevel law and the strict three-maxima phase with its boundary density multiplicities. Mean width and general pointwise projection representations are not new. A later indexed record substantially overlaps the law and phase; this is disclosed as coverage by a later-dated result, not evidence of earlier priority.

## value

PASS

A complete law and a sharp parameter boundary for the number of local maxima are useful beyond width-moment comparisons. The result explains when and how a new singular contribution appears, including at coinciding numerical peak levels and on the transition boundaries. Its value is the usable family-wide distribution and phase, not the classical mean or a single numerical kite.

The dated certificate retains the supplied scientific assessment, sources and limitations.
