# Self-review

## Correctness — PASS

The claim concerns a finite two-block metric with the explicitly sufficient and necessary triangle constraints. The polarization/centroid variance identity is valid in every real Hilbert space. Applying lower intrablock and upper cross-pair Lipschitz bounds yields \(D^2v^2\ge\Sigma\). Two mutually orthogonal centered regular simplices, separated by a perpendicular centroid displacement of squared length \(\max\{0,v^2-\Sigma\}\), attain the bound for every admissible parameter. Equality forces all within-block pairs tight, all cross pairs at the common upper length, and coincident centroids in the strict-distortion regime. Double-centering enforces orthogonality, uniqueness of the Euclidean distance matrix, and the stated affine ranks. In the isometric regime the centroid separation has the stated exact length. The complete split-graph substitution has \(\Sigma\ge5/4>1\) for \(a,b\ge2\). The standalone checker replayed 2,448 rational Gram-matrix constructions, 448 independent centroid identities, and 244,464 exact assertions. Its finite tests are not substituted for the general proof.

## Originality — PASS, with historical-priority qualification

The closest primary comparison is Robertson, *Negative Type and Bi-lipschitz Embeddings Into Hilbert Space* (2023), arXiv:2309.16070, §4.1, Lemma 4.2 and Theorem 4.3. It already proves the sharp metric Hilbert distortion of complete bipartite graph metrics and their common snowflakes, and those **equal-intrablock** cases are not claimed as new. Its general distorted-negative-type characterization covers all finite metrics variationally but does not state an evaluation for **independent** block distances or classify the equality structures. The present new statement evaluates that independent family, including nonregular complete split graphs, and establishes all-optimal-realization rigidity and the three precise affine-dimension regimes. Vallentin's distance-regular framework (arXiv:math/0509716) and Cioabă et al.'s distance-regular framework (arXiv:2109.09708) are not directly applicable to unequal two-block metric symmetry. Published mathematical-result searches on the exact formula, cluster aliases, and related invariants found no covering statement; this is not a uniqueness proof and older two-distance Euclidean distance-matrix literature remains a priority risk. The extension uses the related centroid-method framework and should not be presented as independent invention of that method.

## Mathematical value — PASS

This is a complete sharp distortion-and-rigidity classification for the natural family of two equilateral clusters with unequal internal scales, not a single arbitrary finite test or a recomputation of the equal-scale case. It supplies a sharp isometric/distorted boundary, the exact optimizer Gram geometry in every regime, and the least affine Hilbert dimension, including a dimension jump across the threshold. Its graph specialization gives a concrete new two-parameter distortion invariant and every optimal configuration for the standard complete split graphs, which are nonregular and do not follow by graph-isomorphism or a common snowflake from the prior complete-bipartite case. The numerical formula is closely related to the published balanced-centroid obstruction; its added structural classification is the motivation. Potential historical equivalents remain a bibliographic limitation.

## Sources and limitations

- Gavin Robertson, arXiv:2309.16070, first posted 2023-09-27, primary full HTML text, especially the exact equal-intrablock theorem §4.1.
- Sebastian M. Cioabă, Himanshu Gupta, Ferdinand Ihringer, Hirotake Kurihara, arXiv:2109.09708, first posted 2021-09-20, abstract/introduction and distance-regular scope.
- Frank Vallentin, arXiv:math/0509716, first posted 2005-09-30, abstract and distance-regular scope.

No claim is made about unequal individual within-block distances, more than two clusters, or non-Hilbert targets. No independent audit or complete historical-priority certification was performed.

Self-review: passed. Independent audit: not yet performed.
