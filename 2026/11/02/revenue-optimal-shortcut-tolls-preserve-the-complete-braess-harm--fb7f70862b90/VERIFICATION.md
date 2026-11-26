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

This assessment is for the complete corrected RESULT.md under /workspace/repairs/4/. The frozen wording 'absolute harm'/'sharp absolute maximum' permits the mathematically false reading |L_*−L_0|: for Q=B/10 the magnitude is 0.85B, already larger than B(1−√3/2). The repaired claim explicitly separates the signed maximum and the absolute supremum, and states identity latency on the two congestion arcs rather than an unexplained f. For the repaired statement, symmetry and Wardrop complementarity force equal direct flows and z=clip_[0,Q](2(B−τ)−Q). Revenue is zero for B≤0 or Q≥2B and otherwise has the increasing all-shortcut segment (if nonempty), the strictly concave partial-use segment and a zero tail. The quadratic vertex reaches the kink at Q=2B/3, giving the exact unique maximizers on the positive-revenue regime, including equality at the kink. Aggregating physical link costs gives L−L_0=z(2Q−2B+z)/(2Q). Substitution gives both signed harm intervals; z_0>z_* and the derivative in z is already positive at z_* within the common open harm interval, giving strict reduction. On that interval the signed increment has derivative −3/8+B²/(2Q²) and negative second derivative; it vanishes at the interval ends and is nonpositive outside, so its global maximum is uniquely B(1−√3/2) at 2B/√3. The absolute difference tends to B from below as Q→0, never attaining B for Q>0. Minimizing the convex delay quadratic over 0≤z≤Q gives the clipping of B−Q, with the exact claimed overuse and efficient control cases. A separate rational Beckmann-potential calculation (python3 /workspace/review_evidence/reproduce.py 4) checked 432 parameter pairs including no-usage cases; discrete tests corroborate but do not replace the all-real comparisons.

## originality

PASS

The final claim is the exact joint toll, flow and physical-delay phase diagram for fixed demand with only the added physical crosslink priced by its private owner, including the complete shared positive-harm interval and signed peak. Indexed and published comparisons establish relevant Braess networks, link-pricing games or socially designed tolls, but no inspected result gives or directly implies this restricted profit optimum and the unchanged interval. The absolute-difference supremum is a clarification of the signed result, not a separate novelty claim. The judgment is bounded by the inspected sources and does not assert priority over all edge-specific pricing work.

## value

PASS

The repaired result compares two natural but different pricing regimes on a canonical congestion externality. It quantifies the full open demand interval in which the sole shortcut owner's individually optimal pricing fails to cure the paradox, its strict mitigation, and the difference from the implementable social use. The exact signed peak and thresholds are a useful policy-design benchmark even without general-network or empirical claims. The absolute-magnitude statement is correctly separated and is not needed for that value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
