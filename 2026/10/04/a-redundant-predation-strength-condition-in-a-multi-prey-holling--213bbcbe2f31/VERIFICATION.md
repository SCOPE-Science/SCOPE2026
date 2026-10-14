---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For D=1+sum b_j x_j and c_j<=b_j, y_dot/y=(sum c_j x_j)/D-1 <= -1/D. Positive-prey logistic upper comparison gives 0<x_i(t)<=M_i=max(1,x_i(0)), hence D<=1+sum b_i M_i=Dmax. Integrate y_dot<= -y/Dmax to obtain exponential y(t)<=y(0)e^{-t/Dmax}, including y(0)=0. Since q_i(t)=p_i y/D tends to zero, upper and eventual lower logistic comparisons force x_i(t)->1 for every initially strictly positive prey. The source local R0=(sum c_i)/(1+sum b_i)<1 automatically. No condition p_i^2<4a_i is used. Boundary x_i(0)=0 is invariant and explicitly excluded; this is an all-time analytic argument, not a numerical inference.

## originality

PASS

The source Theorem 4 asserts global stability only with strict c_i<b_i plus p_i^2<4a_i. The direct predator-decay comparison allows equality c_i=b_i and arbitrary positive p_i, changing the actual sufficient-parameter region for exactly that n-prey model. The primary source theorem does not imply the removal of its own assumptions. The later related predator-prey examples use different dynamics; although simple once noticed, no equivalent model-specific strengthening was identified in accessible comparisons. A generic logistic comparison lemma is proof technique, not a previously stated n-prey extinction criterion.

## value

PASS

Removing every p_i/a_i restriction from a published extinction/stability theorem and allowing equality c_i=b_i changes the biological admissible parameter region qualitatively, for arbitrarily strong predation, while supplying an explicit uniform decay rate. This is a motivated strengthening of the paper’s principal n-prey global-stability result, not an arbitrary toy invariant; it avoids the article’s cumbersome sufficient Lyapunov inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
