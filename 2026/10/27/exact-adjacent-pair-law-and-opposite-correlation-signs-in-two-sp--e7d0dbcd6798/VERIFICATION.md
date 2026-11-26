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

A backwards dependency path must have strictly decreasing clocks; reaching arbitrarily far on either half-line has probability zero by the factorial bound. Condition on the attempt time at the central site: its exterior half-lines are independent until that attempt. Conditioning instead on the first neighbor's clock yields h_A=1−q∫h_B and h_B=1−p∫h_A, with the stated solutions and one-site acceptance probabilities. Conditional on the two prescribed labels being A, the edge can be deleted without changing either endpoint's acceptance: each endpoint blocks only B, not A, and before each endpoint attempts its exterior cannot depend on its own state. The resulting half-line acceptance events have disjoint clocks and labels, giving a² and likewise b². Accepted unlike species cannot neighbor. Reflection, marginals and R_A+R_B=a+b−ab (by differentiation from t=0) then give all remaining entries. For 0<t≤1, h_A≥1−qu>0 and h_B≥1−pu>0, and each is strictly less than one for u>0; thus R_A<a and R_B<b. The total-occupancy covariance factors as −ab[2(1−a)(1−b)−ab], strictly negative because a<p and b<q. At t=0 or at degenerate label biases sites have zero covariance. Independent numerical evaluation of the exact symmetric jammed expressions gives P(AA)=0.154818121746, P(XX)=0.045395125835, cov_A=0.054924021523, cov_H=−0.089940157401.

## originality

PASS

The original one-shot paper already gives the single-site densities, and adjacent unlike acceptance is forbidden directly by the rules. The supported distinct content is the nonzero adjacent entries and full ordered-pair law, with strict but opposite signs for equal-species and total occupancy across the same edge.

## value

PASS

Nearest-neighbor dependence is the natural first statistic beyond the known one-site densities. The complete A/B/vacancy edge law exposes a substantive distinction: collapsing A and B to occupied changes the sign, uniformly in positive observation time and all nondegenerate biases, not just at a chosen numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
