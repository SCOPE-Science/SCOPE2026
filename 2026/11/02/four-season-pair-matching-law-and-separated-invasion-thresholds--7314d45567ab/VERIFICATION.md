---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Write M_i=sI+tX_i with X_i off-diagonal. Any odd X-product has zero trace; pair terms at t² are permutation independent. The sole schedule-dependent trace term is t⁴ product(c_i)(r_pi1 r_pi3+r_pi2 r_pi4). Three distinct alternating-position partitions occur eight times each and strictly order by products of positive ratio differences. The determinant of the product is product(s²−t² b_i c_i), independent of schedule. For a strictly positive 2x2 product Perron eigenvalue is strictly increasing in trace at fixed determinant, even if determinant is negative. Each matrix product increases entrywise with t>0, so each Perron root increases continuously from s^4<1 to infinity; distinct classes cross 1 at strictly separated unique t. For <=3 factors no ordering-dependent even X-product of length four exists. Independently reproduced all 24 rational schedule products, trace classes, determinant, and opposite invasion outcomes in the supplied numeric example.

## originality

PASS

Qualified PASS: periodic population matrix products and malaria seasonal threshold models are prior work, and a one-direction special case of four-season pairing is credited. The unrestricted two-direction varying-ratio 3-class ordering plus all-parameter separated crossing theorem is not evidenced in the checked earlier model results. A general positive 2x2 matrix-product rearrangement theorem is a genuine residual priority risk.

## value

PASS

Complete sharp finite-horizon schedule-dependence classification for a natural seasonal two-type linearized infection model. The proof establishes rigorous nonempty intervals with different local invasion verdicts despite identical four seasonal factors, and four is the first possible sensitive horizon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
