# Scientific review: sorting in finite-star graph Sobolev norms

## Correctness — PASS

The proof reduces a globally continuous piecewise-permutation map to the maximum of all local permutation operator norms, including an explicit argument giving actual attaining input pairs. The star's leaf automorphisms reduce this to one hub/leaf swap. The difference of star Laplacians has rank two; their positive-definite forms have equal determinant, and an exact inverse provides the trace defect \(\gamma^2(n^2-1)/[(1+\gamma)(1+(n+1)\gamma)]\). These two constraints determine the nontrivial generalized eigenvalues and hence the sharp norm. The \(n=1\) case and homogeneous limit are handled separately. An independently formulated executable checker passed 2704 exact-rational and numerical tests. Residual risk: the analytic proof is not independently audited.

## Originality — PASS, with residual risk

The mathematical comparison distinguishes (i) norm contraction of decreasing rearrangement in permutation-invariant \(L^p\) spaces, (ii) one-input graph Pólya–Szegő energy inequalities, and (iii) norm-preserving GroupSort activations from the **two-input** norm in a graph-Sobolev geometry. Direct published-finding corpus queries over sorting, graph energy, finite stars, Sobolev Lipschitz moduli, coordinate permutations, and analogous metric projections returned no matching claim. The closest records concern single-input fractional-gradient rigidity, finite-star Lipschitz-free geometry, and isotonic regression rather than the map and metric here. An equivalent calculation may exist in unindexed operator-norm or graph signal processing literature.

## Mathematical value — PASS

Sorting is a canonical rearrangement that contracts all permutation-symmetric coordinate norms but fails to preserve a graph derivative. This finding quantifies the exact price of that failure on the simplest nontrivial branching graph, identifies all worst local chambers, and separates fixed from dimension-rescaled coupling. The \(\sqrt n\) growth and the homogeneous golden-ratio three-vertex case show that perturbation stability cannot be inferred from energy monotonicity of a single rearrangement. The complete parameter law is useful as a benchmark for stability of graph-based sorting operators and regularized graph signals.

## Comparison and limitations

Chernozhukov–Fernández-Val–Galichon (arXiv:0704.3686) studies ordinary rearrangement of monotone estimation; Steinerberger (arXiv:2209.06765) proves one-input gradient rearrangement inequalities; Anil–Lucas–Grosse (arXiv:1811.05381) addresses GroupSort in coordinate norms. None of the inspected statements establishes the same graph-Sobolev two-input operator modulus. Arbitrarily weighted stars and general finite graphs are not addressed. Unindexed historical overlap and the lack of independent proof checking remain.

Self-review: passed. Independent audit: not yet performed.
