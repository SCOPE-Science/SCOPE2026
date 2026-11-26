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

The budget simplex is compact and a positive surviving tree count is feasible for m≥2, so allocations with any singular outage cofactor cannot maximize the objective. On the positive domain log of the worst tree count is the minimum of concave log determinants of affine reduced Laplacians and is therefore concave. Averaging over page permutations and hub interchange preserves budget and does not decrease it. For symmetric weights, direct tree counting gives the intact count 2^(m−1)a^m(ma+2b): a tree uses the hub edge and one spoke per page, or omits the hub edge and uses exactly one double-spoke connector page. Removing the hub sets b=0; removing one spoke instead forces its page to use the other spoke, giving 2^(m−2)a^m((m−1)a+2b). These outage counts tie at r=(m+1)/2. The budget substitutes a=B/(2m+tr). To the right of the tie the objective strictly decreases; on its left the derivative sign is that of 4m−(m²−1)t−2mtr. Its zero reaches the tie and zero precisely at the stated t1 and t2. This verifies the optimizer, optimum, active failures and both equality cases. For unrestricted uniqueness, the average of the spoke-outage log determinants is strictly concave on its positive domain: a zero log-det curvature direction would vanish on every undeleted-edge dyad sum; in a simple graph those dyads are independent by inspecting off-diagonals and then diagonals, so the different deletions admit no common nonzero null direction. If an optimal allocation were nonsymmetric, group averaging would strictly increase this spoke average. But the average is at least the worst-outage log determinant at the original allocation and equals it at the symmetric optimum, since spoke outage is active there in every regime. That is a contradiction, including at b=0 or either threshold. The intact scalar derivative has sign 4m−m(m+1)t−2mtr, giving the nominal threshold 4/(m+1) by the same concavity and symmetry reasoning. It is strictly below t2; the displayed limits follow directly.

## originality

PASS

The distinct result is the unrestricted maximin spanning-tree optimizer, its two exact thresholds and equality cases. The strongest exact-topology overlap optimizes the surviving spectral gap, not the product of nonzero eigenvalues. The indexed nominal determinant result covers the intact benchmark, not the worst-outage criterion. General determinant-design and edge-deletion identities do not give the classified optimum without additional analysis. The assessment is bounded by the inspected statements.

## value

PASS

Worst single-outage tree connectivity is a natural robust analogue of an established continuous network-design measure. On an infinite graph family the theorem distinguishes equalized failure scenarios, an interior spoke-limited design and complete abandonment of the hub edge. Its exact price comparison isolates when backup remains worthwhile under the robust criterion but not without outages; proof of unrestricted uniqueness makes that interpretation independent of any symmetric-design restriction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
