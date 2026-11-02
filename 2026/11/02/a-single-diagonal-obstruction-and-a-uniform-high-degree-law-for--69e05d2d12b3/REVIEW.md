# Scientific review

## Correctness: PASS

The precise claim is an exact necessary and sufficient positivity interval for the three-stage Gauss–Legendre endpoint update on a uniformly weighted \(K_{p,q}\), including the \(K_{1,1}\) exception and a uniform high-degree limit. The proof follows from four orthogonal Laplacian eigenspaces; it gives every entry of the rational endpoint matrix. The two derivative polynomials are strictly sign-definite on the nonnegative half-line. The divided decrement is strictly decreasing, forcing positivity of *all* off-diagonals; spectral ordering puts the first zero on the smaller class. The smaller-class diagonal decreases from one to \(2/(p+q)-1\), so there is exactly one crossing. A uniform bound on the difference from the scalar rational function proves the maximum-degree asymptotic. The accompanying verification script checks exact rational identities, full-matrix comparisons and boundary samples. The proof is not dependent on any finite enumeration.

## Originality: PASS, subject to stated uncertainty

The most relevant accessible primary full texts are Zappavigna et al. (2010), *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, and Zappavigna et al. (2012), *Essentially Negative News About Positive Systems*. Their general matrix-based sufficient step conditions, examples and Padé-method warnings do not present the claimed complete-bipartite \([3/3]\) entry formulas, sharp single interval, diagonal-only failure or uniform maximum-degree law. The inspected fourth-order diffusion results likewise apply to a different Padé stability function and do not imply the sixth-order theorem. Searching variants using sixth-order Gauss, third diagonal Padé, complete bipartite, graph Laplacian and positivity did not identify stronger equivalent coverage. The full text of the closely relevant 2004 Wade Padé-smoothing paper was not available from the inspected sources, although its abstract concerns a different composite smoothing scheme. The self-review conclusion is an originality judgment under this residual coverage risk, not proof of absolute priority.

## Mathematical value: PASS

The endpoint update is sixth-order and stable but can produce negative transition probabilities. This result gives a complete, sharp timestep safety rule across every complete bipartite network, isolates the only possible source of failure (the diagonal of the smaller class), and proves a uniform constant in the maximum-exit-rate scaling even across highly unbalanced topologies. It improves over generic matrix-entry sufficient conditions and supplies a motivated structural relationship between local exit rates and global numerical positivity. The result is specific, but complete and independently useful as a benchmark for structure-preserving time integration.

## Closest literature and limitations

Primary sources and access: Zappavigna et al. (2010), repository full PDF, particularly sections II–III and Theorem 3; Zappavigna et al. (2012), repository full PDF, particularly sections 2, 4 and Theorem 3. Wade (2004), full-text inspection unavailable; title and abstract inspected. Relevant previous research records on \([2/2]\) Padé and Crank–Nicolson were compared by statements, not titles alone. Assumptions exclude nonuniform edges, general graphs, directed generators, and internal stage positivity. Exact formulas and proofs are provided only for the stated graph family and method; no independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
