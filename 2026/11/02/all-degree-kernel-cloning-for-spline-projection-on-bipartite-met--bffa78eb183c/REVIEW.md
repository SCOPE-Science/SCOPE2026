# Scientific review: All-degree kernel cloning for spline projection on bipartite metric graphs

## Correctness — PASS

The theorem is reconstructed from the endpoint-minimal polynomial decomposition. The endpoint evaluation Gram follows from Legendre sums, giving \(a_d=1/[d(d+2)]\) and \(b_d=(-1)^{d+1}/[(d+1)d(d+2)]\). The within-part zero-sum and two-dimensional part-constant subspaces invert the complete-bipartite mass matrix, producing precisely the claimed reciprocal-\(q\) row coefficients. Edge multiplicities cancel that factor. The sharp functional norm is the kernel \(L^1\) norm, attained by the sign input. The monotonicity follows from the triangle inequality in the variable \(1/p\), and positivity excursion from reproduction of constants. A pure-Python checker confirmed 4,032 exact rational edge-kernel cases for degrees one through eight and part sizes up to six. The analytic proof does not rely on finite extrapolation.

## Originality — PASS, qualified

Kayumov's 2004 interval-spline orthoprojector thesis and Arioli–Benzi's 2017 metric-graph finite-element work were compared with the exact kernel statement. Their inspected scientific results do not give the all-degree reciprocal-\(q\) clone identity or sharp vertex-reduction formula. Existing fixed-degree graph-spline results are prior special cases, not claimed as novel. The absence of a previously unindexed equivalent algebraic derivation has not been established and is a genuine publication-priority risk.

## Mathematical value — PASS

The degree-uniform identity unexpectedly equates vertex-evaluation robustness on dense \(K_{p,q}\) graphs and sparse \(p\)-leaf stars, despite the differing numbers of edges and cycles. It reduces an infinite two-part family and every polynomial degree to a one-variable exact evaluation formula and yields monotonicity and sharp positivity-loss constants. This is a structural reduction, not a routine next-degree recomputation or finite table entry.

## Scope and limitations

Unit edges, arclength measure, common degree, only value continuity, and original-vertex evaluation. Interior evaluation and full projector norms for degree above one are not classified. Literature-priority risk remains.

Self-review: passed. Independent audit: not yet performed.
