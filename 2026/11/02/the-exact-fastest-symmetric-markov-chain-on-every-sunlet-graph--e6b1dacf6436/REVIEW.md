# Scientific assessment of the sunlet fastest-mixing formula

## Correctness — PASS

The proof explicitly defines the admissible symmetric stochastic matrix class with holding probabilities and the spectral-norm objective. Group averaging establishes reduction from **all** edge-probability assignments to the dihedrally invariant two-parameter family, without claiming uniqueness of the original matrix. The two-dimensional Fourier blocks are computed exactly. A nontrivial eigenvalue gives a universal lower bound, which becomes the **exact** SLEM on the capacity boundary; all other positive, negative, and constant-mode eigenvalues are explicitly bounded. The remaining scalar function has a unique interior stationary point by strict convexity; direct radical substitution yields the optimum and the asymptotic series. Numerical checks from the accompanying artifacts corroborate, but do not replace, these algebraic steps.

## Originality — PASS, subject to the risks below

The original convex fastest-mixing formulation [1] gives a general SDP, not the claimed graph-family closed form. The symmetry treatment [2] proves the general averaging reduction and treats cycles, wheels, and other graph families. Its wheel is a hub attached to every rim vertex, not the claimed collection of distinct pendant leaves. The closest later clique-lift and subgraph study [3] covers different constructions; its inspected topology taxonomy contains no cycle with a pendant at every vertex. Literal searches for sunlet, cycle-corona, pendant-cycle mixing, and equivalent spectral-transition formulations disclosed no exact comparison that implies this formula. Database-search nearest matches concern distinct graphs or objectives. The possibility of unindexed or implicitly specialized prior coverage is explicitly retained.

## Mathematical value — PASS

The result provides a closed-form global optimum for a natural infinite family of non-edge-transitive unicyclic networks where the general fastest-mixing problem ordinarily requires semidefinite optimization. Its rigorous saturation principle, unique invariant allocation, order-\(m^{-1}\) spoke probabilities, and two-term spectral-gap expansion explain how a growing rim should share probability with dangling states. These are graph-specific structural conclusions, not merely a routine numerical SDP recomputation.

## Limitations and residual risks

The claim applies to symmetric transition matrices and the uniform stationary measure, with one leaf per rim vertex. It leaves uniqueness of arbitrary spatially asymmetric optimizers unresolved. A full field-wide priority proof is unavailable, especially for less-indexed formulations with alternative names for the sunlet. Numerical verification is finite and floating-point. No outside mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
