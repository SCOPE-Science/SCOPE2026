# Scientific review

## Correctness — PASS

The claim uses the all-vertex shortest-path metric of a complete bipartite graph with one distinguished cross distance in \([1,3]\). On the zero-sum coefficient subspace, the powered-distance quadratic form splits exactly into positive scalar fluctuation spaces and a symmetric \(3\times3\) block. The determinant of this block is \(-\mathcal F/((m-1)(n-1))\), and for \(0<p\le1\) its lower principal \(2\times2\) block is positive definite. Consequently the sign of \(\mathcal F\) is both necessary and sufficient for negative type. Endpoint evaluations and strictness inheritance prove a unique critical root for every \(m+n\ge5\); the four-vertex case is treated separately. The sign-reversal trichotomy is an exact factorization at the previously known intact-biclique exponent, and the inverse-size and inverse-cubic laws follow from explicit expansions. The critical embedding ranks follow from the centered Schoenberg Gram matrix. Exact rational identities, full-matrix eigenvalue checks and high-precision asymptotic tests were run from the packaged verification program.

## Originality — PASS, with priority qualification

Li–Weston supplies the strictness inheritance principle, Sánchez the intact complete-bipartite exponent and a general matrix criterion, and Robertson the related Hilbert distortion formulas **on uniform bicliques**. Sun–Wan analyzes deletion under distance energy, which is not the conditional negative-type invariant. Prior related claims on full matching stretches, resistance metrics, and full matching deletions do not imply this one-edge shortest-path classification. Targeted published-source and mathematical-record queries did not disclose a source giving the exact one-edge criterion, its opposite-direction effect for unbalanced parts, or the two asymptotic scales. The searches are not an exhaustive novelty proof; an unindexed general distance-matrix result or differently stated graph-metric computation may exist.

## Mathematical value — PASS

Generalized roundness is an intrinsic Hilbert snowflake-embedding threshold; a local change of a graph metric is a natural stability question for that threshold. The result identifies the surprising opposite sign of a local perturbation on balanced and unbalanced bicliques, a sharp crossover length and two distinct quantitative scaling regimes, not merely a special-case determinant. It also gives a complete critical Euclidean-dimension classification. The parameter ranges are natural, include all admissible positive single-edge stretches up to the metric's alternate-path limit, and form an infinite family.

## Reproducibility and risks

Run `python verify_one_edge_biclique.py` with dependencies from `requirements.txt`. The checker prints exact-form, determinant, endpoint, spectral, arithmetic-reversal and asymptotic tests. These finite checks support rather than certify the general theorem. The principal residual risk is unindexed or differently worded published coverage; no independent mathematical review has been performed.

Self-review: passed. Independent audit: not yet performed.
