---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For nonempty input, a value-two integral min-cost flow on the sorted endpoint DAG decomposes into two paths, and exactly encodes feasible schedules, including meetings at half-open endpoints and parallel job arcs. Empty input is trivial. In a selected optimum, order the equal-length jobs by start time (ties arbitrary). An overlapping pair with another start between them would place all three jobs at the later start, contradicting depth at most two. Hence conflict edges occur only between consecutive vertices and components are paths. Deleting a minimum-weight index class modulo three in each component costs at most one third and leaves only edges and singletons. Orient a component against the signed load difference D: if the old heavier side remains heavier, its witness item is still present and the gap decreases or stays fixed; if the side changes or the old gap was zero, the new heavier side gets the larger edge item or the singleton, whose weight is at least the increment and thus the new gap. A zero gap is EF1. This proves the ordinary EF1 inequalities for common nonnegative values. The three-job construction forces both outer jobs onto one machine if all are scheduled; the middle weight is less than either outer weight, and the fair optimum is exactly two. The factor is approached as epsilon tends to zero. Sorting, flow, and the remaining steps are polynomial for rational data. The bundled finite script was inspected, not executed or used as a universal certificate.

## originality

PASS

The distinguishable contribution is the uniform weighted upper bound for two machines. The exact lower-bound construction and the prior unweighted guarantee are credited, not judged novel. The strongest retrieved results do not supply the claimed guarantee for arbitrary common weights.

## value

PASS

Closes the gap between the explicit weighted obstruction and a weight-class-dependent bound for the natural two-machine case. The optimal approximation factor is independent of the weight spread and number of distinct values, and the construction is algorithmic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
