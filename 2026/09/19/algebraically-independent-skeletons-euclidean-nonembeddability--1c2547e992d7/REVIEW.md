# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. For each finite list of edges in the fixed countable skeleton and each nonzero rational polynomial, polynomial nonvanishing is open. Density follows by first moving the induced finite metric into the open strict-metric cone, avoiding one polynomial hypersurface there, and then invoking the exact closed-subset metric interpolation theorem. Countability of the skeleton and of rational polynomials reduces the desired algebraic independence to a countable intersection of open dense sets; the Baire property of the full compatible-metric space then gives density.

The Euclidean-stratum statement was checked separately. Euclidean embeddability in fixed dimension is closed under uniform convergence because the associated Gram kernels remain positive semidefinite with rank at most the target dimension. Empty interior follows by perturbing an arbitrary finite set of \(m+2\) points so that its Cayley--Menger determinant becomes nonzero and extending that finite perturbation globally. The rigidity-matroid corollary uses squared-distance coordinates: a nonzero polynomial relation among squared lengths would remain a nonzero polynomial after substituting \(X_e=T_e^2\), contradicting algebraic independence of the raw distances.

## Originality

PASS, to the best of our knowledge. Ishiki's current 2026 preprint proves density of metrics with algebraic independence of all positive distances under strong zero-dimensionality, and a \(G_\delta\) statement for the full property on sigma-compact spaces. Full-text inspection and searches for countable subsets/skeletons, restrictions, Euclidean embedding, Cayley--Menger, and rigidity-matroid formulations did not locate the fixed-countable-skeleton theorem or its distance-geometry consequences.

The proof is intentionally built from prior machinery rather than presented as a new interpolation technique. Ishiki's 2026 revision of the interpolation paper already gives exact extension of prescribed metrics on closed subsets and a broad transmissible-property framework for generic violations of finite metric inequalities. In particular, weaker generic non-Euclidean consequences can already be extracted in several non-discrete/local settings. Rouyer's generic compact metric space in Gromov--Hausdorff moduli also has strong non-Hilbert behavior. Malić--Streinu provide the Cayley--Menger algebraic rigidity framework. Those ingredients are treated as prior art.

The originality claim is therefore narrow: generic algebraic independence on an arbitrary preassigned countable skeleton without any dimension restriction on \(X\); the fixed-\(X\) closed-nowhere-dense finite-dimensional Euclidean strata in this generality; and the explicit rigidity-matroid transfer/local exact-Euclidean obstruction from the skeleton. Because the motivating preprint is very recent and the interpolation framework is broad, an unindexed or differently phrased corollary remains a real residual risk.

## Value

PASS. The result isolates exactly what survives from full algebraic independence when the ambient topology is not zero-dimensional. Connected manifolds and other positive-dimensional metrizable spaces can generically carry a dense countable skeleton with no rational polynomial relation among its distinct distances. This immediately supplies a clean bridge to distance geometry: every finitely realizable edge set on that skeleton must be algebraically independent in the Euclidean rigidity matroid, and every infinite open set of a separable example fails exact finite-dimensional Euclidean embeddability. The closed-nowhere-dense stratum theorem also gives a topology-independent global category statement for arbitrary infinite metrizable spaces.

## Limitations

The result controls only a chosen countable skeleton, not all pairwise distances on a positive-dimensional space. All Euclidean conclusions concern exact isometric embedding, not approximate or coarse embedding. Rigidity-matroid independence is necessary but not sufficient for realizability. No quantitative probability, perturbation radius, or distortion estimate is provided. The recent source and the generality of the older interpolation framework leave residual originality risk. Independent audit has not been performed.
