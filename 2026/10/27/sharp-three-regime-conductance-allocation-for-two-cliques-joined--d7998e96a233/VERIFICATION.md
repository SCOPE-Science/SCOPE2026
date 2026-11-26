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

For the repaired theorem with the original full budget/allocation quantifiers, concavity on the full edge simplex justifies averaging, and the invariant-space spectrum accounts for all 2(k+m) dimensions. The smaller odd orbit-constant eigenvalue is strictly below t=kc by its nonzero off-diagonal entry; hence the normalized constraint implies t>1. The Schur complement of t−1 yields exactly the bridge lower bound, and the even matched-gateway transverse eigenvalue ka+mc yields the only other possibly active inequality. The nonsymmetric support result follows from uniqueness of the averaged optimum and nonnegative orbit weights, including the empty m=1 edge class. Substitution into the budget gives a strictly convex scalar objective with derivative zeros 3/2 and s_k on the appropriate smooth branches; the kink gives t=r, and the costs and rates agree at the common endpoints. As a separate bounded replay, for t=t_* use z equal to ±1/2 on gateways and ±t/[2(t−1)] on nongateways, with opposite signs across layers, and P the projector onto identical across-layer zero-sum gateway patterns. The positive semidefinite matrix X=zzᵀ+wP with w=2k/(k−1)·(1−1/[4(t−1)^2]) annihilates constants and has dual edge lengths squared 1 on bridges and gateway–nongateway edges, w on intracluster gateway edges, and 0 on the remaining edges. Here 0≤w≤1 and w=1 if a_*>0. At the proposed optimum Lz=z, and LP=P whenever w>0, so tr X=tr(XL) equals its cost. For any unit-gap feasible L, tr X≤tr(XL)≤ its cost, giving the same lower bound. An edgewise computation for (2,2), (3,2), (8,5), (2,1), (3,1), (13,8), (20,21), (26,15) found trace-cost agreement within 2×10^−12 and active-space residual below 10^−14 (finite numerical corroboration only). The frozen VERIFICATION.md and verify_spectral.py were inspected, not executed; the script's finite numerical checks remain applicable. The new prior-implication paragraph was checked by preserving the bridge degree and testing the matching transverse constraint. Complete corrected file: repairs/5/RESULT.md.

## originality

PASS

The repaired finding credits the earlier biclique-gateway result for the low-ratio branch via the subgraph bound and feasible redistribution, and removes the frozen miscitation to a Witt-algebra paper. The complete matching-specific classification, including both higher-ratio regimes and the support activation boundary, does not follow from the examined biclique theorem or the row-stochastic same-graph result. This verdict is for the corrected attribution and surviving full classification.

## value

PASS

A partial gateway matching is a natural constrained model of exchange between dense communities. The matching transverse constraint is invisible to a two-orbit mixing surrogate yet governs a distinct intermediate regime and the point beyond which some intracluster gateway weight is unavoidable for every optimum. The exact costs, thresholds and universal support restrictions provide more than a numerical optimizer or reiteration of the inherited low-ratio branch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
