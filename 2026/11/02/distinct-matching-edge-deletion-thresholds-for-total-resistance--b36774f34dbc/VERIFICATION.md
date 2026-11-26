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

The reduced Laplacian H on the mean-zero subspace affinely and injectively encodes every individual conductance, since the full Laplacian is zero on constants and its off-diagonals recover the weights. Trace-inverse is strictly convex there (in an eigenbasis its directional Hessian is a positive sum of squares), and logdet strictly concave. The price simplex is compact, has a connected feasible point, and approaching a singular H sends the resistance sum to infinity and the tree enumerator to zero. Thus each optimum exists with connected support and is unique in the full variables. The pair symmetries then force its two weights, with b>0 by connectivity. On pair-constant mean-zero and pair-antisymmetric spaces the respective eigenvalues are x=2mb and y=2b(m−1+t), of multiplicities m−1 and m. These give the stated trace-inverse times 2m and determinant divided by 2m; the price constraint yields b=B/[m(Pt+2(m−1)Q)]. Independently, the benefit gradient along a matching edge has squared incidence norm 2 entirely in the y-space, while a nonmatching edge has squared norm 1 in each space. Thus the matching versus nonmatching marginal-benefit ratios are 2x²/(x²+y²) for A and 2x/(x+y) for D. They strictly decrease with t≥0; the positive optimum sets its ratio equal to r, and deletion is optimal precisely when r is at least the ratio at t=0. The gradient test is sufficient by the full-space curvature; equality at a threshold still gives a unique boundary optimum. This yields both exact roots, the ordered gap 2m(m−1)/[(2m−1)(2m²−2m+1)], and the interval including its D endpoint but not its A endpoint. For fixed γ the two unclipped roots at r=1+γ/m expand as 1−γ+O(1/m) and 1−2γ+O(1/m), and clipping at zero gives the limits including γ=1 and 1/2. No computation is needed for the all-m result. The supplied rational checks and their limits were inspected but not executed.

## originality

PASS

Pass for the exact A-versus-D comparison on the complete graph: the D-optimal price response, the strict disagreement interval with its endpoints, and its critical scaling. The A-optimal conductances and threshold in isolation are exactly covered by an earlier indexed result and receive no originality credit. The matching spectrum and generic convex-design methods are background. The strongest similar A/D theorem uses a complete bipartite graph and does not imply the determinant response or support interval for K_{2m}. No historical priority beyond the inspected evidence is claimed.

## value

PASS

The determinant threshold is useful precisely because comparing it with the known resistance threshold predicts a change of support in one unrestricted optimal design but not the other, despite identical prices and topology. The full ratios and distinct first-order surcharges quantify that discrepancy near uniform prices, rather than merely asserting that A- and D-optimal weights may differ. The known resistance calculation is supporting context, not independent value credit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
