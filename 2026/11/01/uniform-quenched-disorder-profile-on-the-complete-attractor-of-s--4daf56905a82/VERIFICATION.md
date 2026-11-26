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

The voltage update gives x_i >= k_min after one step and at every bilateral time. The stable recovery recursion, iterated into the past on a bounded orbit, gives y_i <= Y=c/(1-a). Forward iteration first into y_i <= Y+delta, then into x_i <= X_delta, then into the stated lower recovery bound proves absorption of bounded sets. The displayed box is invariant, including when a=0. Compactness and continuity give complete prehistories through the nested-image intersection, and bounded complete orbits lie in it by uniform absorption of their bounded ranges. The two extrema for |(2x-x^2)e^(-x)| are attained at 2±sqrt(2); the ratio of the larger-x lobe to the smaller-x lobe is (1+sqrt(2))^2 exp(-2sqrt(2)) < 1. The y derivative is bounded by its x=2 value. Orthogonal centering cancels the mean-field term; subtracting F at the spatial means, the mean-value bound gives ||PF|| <= L_x||xi||+L_y||eta|| on the convex half-strip. The bounded past implies eta_t=-b sum_{j>=0} a^j xi_{t-1-j}. Thus S_x <= q||Pk||+qLS_x, and substituting the resulting S_x bound into the centered voltage equation and then into the recovery series gives both advertised remainders. All constants are independent of N and of the orbit. The q=0 and identical-input cases give zero deviation; for small q the norm bounds with relative error qL/(1-qL) give the variance result after squaring and dividing by N.

## originality

PASS

The exact network model and generic mismatch-forcing mechanisms are known. The distinct content supported by the checked sources is the nonlinear all-bounded-complete-trajectories estimate, including its explicit first-order disorder profile, second-order error, and size-independent constants. The inspected precedents do not give this package under the stated hypotheses.

## value

PASS

Quantifies the spatial imprint of heterogeneous inputs in the exact network used to study coherence. Its fixed direction and leading variance, with error proportional to the disorder and uniform over population sizes and all complete trajectories, allow one to separate residual disorder from longitudinal dynamics without classifying periodic or chaotic attractors. The elementary projection estimate supports a useful structural conclusion rather than a threshold or simulation specific to one trajectory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
