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

Congruence on 1-perp reduces the attacked Laplacian to I minus a rank-one term, with altered eigenvalue 1-delta R_e. Thus the single-edge threshold is a supremum, not strict stability at equality. Candidate edges with zero nominal conductance still have well-defined nonzero incidence vectors and finite resistance. Resistance in a block is unchanged by the outside branches of the block-cut tree, since the endpoint drive has a constant harmonic extension into each such branch. Independently minimizing cost at unit worst resistance gives the full result: equalizing spokes at fixed sum and backup is strict for unequal spokes because the common denominator increases and the maximum numerator cannot increase. For equal spokes a, the least backup b is a(1-a)/(2a-1) on 1/2<a<=2/3, 1-a/2 on 2/3<=a<=2, and zero thereafter. With y=2a-1, the first cost is 1+(1-t/4)y+t/(4y); the minimizing stationary point fits exactly for t<2/5. The middle cost is linear with slope 2-t/2, explaining the whole interval at t=4, and the third cost increases. The verified costs and equality cases are those claimed. By homogeneity each block has its own necessary lower budget at the same resistance cap; equality in the sum requires every block to saturate. Analytic replay: reviews/evidence/cactus_cost.md. The supporting finite tests were inspected, not run, and are not required by the proof. In the frozen sentence about t>4, the combined piecewise objective has its sole minimum at zero; the second branch on its own minimizes at r=1, not at zero. This wording does not affect the global result.

## originality

PASS

The resistance stability criterion and fixed-graph edge-max reweighting objective have prior coverage. No inspected source covers the specific continuous priced triangular-cactus block law, both thresholds and all optimizer faces with zero-conductance candidate edges retained. The strongest indexed robust-resistance analogue uses complete outage and an all-pairs sum on an alternating-price even cycle, so neither its plateau nor its optimal design implies this one. This judgment is limited to the exact priced classification, not the general method or objective.

## value

PASS

This is an exact resource design law for a natural stability diagnostic rather than an example at chosen prices. It resolves when optimal designs delete an edge that is still vulnerable to subtraction, explains a full equal-design interval even under unequal prices, and identifies exactly when the optimum stops being unique. Block locality turns those distinctions into an explicit allocation for arbitrary triangular cacti under the stated budget model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
