---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For tree edge e let b_e be its two side sizes multiplied. The tree index is sum b_e/g_e; Cauchy–Schwarz with total expenditure 1 gives g_e^0=sqrt(b_e/c_e)/S and K^0=S², with S=sum sqrt(b_ec_e). Old-edge derivatives are −S²c_e. On the mean-zero subspace the new edge direction is beta beta^T, giving derivative −N times the squared norm of the mean-zero unit-current potential. The potential is the centered version of S sum sqrt(c_i/b_i) 1_(U_i), since only path edges carry current. For i<j the centered indicator inner product is s_i(N−s_j)/N, giving the stated threshold and eliminating S. The feasible directional derivative per unit z from the best tree-only allocation is S²(tau−Theta). Strict convexity of trace-inverse on connected support follows from positivity of its second directional derivative and injectivity of the simple-edge Laplacian map. As support disconnects at least one positive mean-zero eigenvalue tends to zero, giving lower semicontinuity on the compact budget simplex and existence. Hence the threshold includes equality in the unique zero-chord regime, and a negative directional derivative forces purchase. Every positive cross coefficient is less than one and tends to one under symmetric endpoint leaf additions. For two hops, squared correlation is ab/((N−a)(N−b)); it strictly increases in each end size, giving a=b=1 as the unique minimum profile and middle size one at the maximum. With a+b=N−1 it is ab/(ab+N), maximized exactly at the balanced splits. The odd/even formulas and N=6 example follow, and for N=3 the two profiles coincide. Off-path edges are bridges: their contribution is a sum b_e/g_e separate from the cycle block, which is homogeneous of degree −1 in its conductances. Optimizing the block expenditures allocates them in proportion to the square roots of their unit-expenditure objective minima, so changing one off-path price rescales positive cycle conductances without changing the purchase decision.

## originality

PASS

Credit the general trace-inverse optimization framework, optimality inequalities and tree solution to Ghosh–Boyd–Saberi; the weighted derivative test alone is a standard adaptation. There is exact catalog overlap on the entire single-chord cut formula with a later, stronger simultaneous-chord record, not merely a related weighting model, so the threshold is not credited as distinct from that catalog theorem. The independently supported distinct content is the path cut-profile price analysis, most concretely the sharp finite-N two-hop window with complete minimizing and maximizing profiles. The inspected stronger catalog Finding gives the star case and selected path examples but not that classification over all trees at fixed N. Its later date is not taken to establish a priority relationship.

## value

PASS

A planner deciding whether to buy a two-hop shortcut needs to know when purchase is forced or ruled out irrespective of branching elsewhere, for known N and arbitrary positive path prices. The attained endpoints give exactly that robustness window; the equality profiles distinguish leaf-to-leaf stars from balanced branch masses separated by a degree-two middle vertex. This is useful beyond the known generic derivative test and the matched catalog's evaluation of a specified tree; no positive optimizer formula or simultaneous active-set determination is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
