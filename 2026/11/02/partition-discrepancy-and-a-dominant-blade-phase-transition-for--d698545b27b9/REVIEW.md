# Scientific review

## Correctness — PASS
The nonlinear optimization is reduced to a product of explicit finite Lipschitz polytopes, on which centered variance is strictly convex modulo constants. The complete vertex classification yields the exact integer objective \(NK-S^2\). Filling and sign-flipping arguments force every partially occupied maximizing configuration to have a single positive dominant blade; the integer quadratic then proves both branches and the tie at \(A=3Q+2\). Exact arithmetic checks independently enumerate labelled admissible functions and smaller reduced configurations. The proof is universal; finite checks are not used as an infinite certificate.

## Originality — PASS (subject to residual literature risk)
The closest antecedent, Alon–Boppana–Spencer (1998), introduces the spread and guarantees integral extremizers, but does not compute the heterogeneous clique-bouquet invariant. Addario-Berry–Janson–McDiarmid (2009) studies random graph classes; Yancey (2017) studies general and hair-graph extremizers. Related calculations of clique-bouquet negative type, heat stability, and double-broom spread do not imply the present arithmetic formula. No inspected source gives the same optimization or its dominant-blade classification; differently worded unindexed literature is an unresolved possibility.

## Mathematical value — PASS
The spread is the optimal squared norm of centering from a finite real Lipschitz seminorm to \(L^2\), and is the sharp variance parameter in product-space concentration. The theorem settles every heterogeneous vertex-bouquet of cliques, exposes the precise signed-partition obstruction in the balanced regime, and proves a structural transition and exact squared gain when one clique dominates. This is a natural complete classification rather than an isolated computational value.

## Scope and limitations
Only real one-Lipschitz functions, uniform vertex weights, one shared vertex and simple unweighted clique blocks are considered. The result is not an evaluation of the distinct subgaussian constant. The universal proof rests on the explicit polytope argument, not on numerical testing. Primary literature inspection does not exclude an unknown equivalent formulation.

Self-review: passed. Independent audit: not yet performed.
