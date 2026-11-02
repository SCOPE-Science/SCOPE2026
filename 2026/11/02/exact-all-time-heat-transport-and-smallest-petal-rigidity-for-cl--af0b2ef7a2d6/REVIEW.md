# Self-review

## Correctness — PASS

The claim is quantified over every positive integer clique profile and every real nonnegative time, with an unweighted shortest-path metric and combinatorial (not normalized) heat generator. Applying the Laplacian to the four explicitly described orthogonal spectral families gives eigenvalues \(0\), \(k+1\), \(1\), and \(d_i+1\), with the indicated multiplicities summing to the number of vertices. Every pairwise heat-row difference has an explicit decomposition. Positivity and negativity are established for all times by monotonicity of \((1-e^{-xt})/x\), not inferred from numerical sampling. Direct couplings and dual one-Lipschitz witnesses yield matching exact Wasserstein costs; finite-metric duality and the edge-orbit comparison give the sharp norm and an attaining function. Differentiation proves the peak and contractivity classification; singleton blades, a single clique, and zero time are included. The executable rational checker verified 255 profiles, 510 exact spectral heat matrices, and 14,846 independently optimized pairwise dual costs. Those checks corroborate, but do not replace, the unrestricted analytic proof.

## Originality — PASS, qualified

The closest transport framework is Ollivier (arXiv:math/0701886), with subsequent general graph heat-flow curvature equivalence in Münch–Wojciechowski (arXiv:1712.00875). The first defines Wasserstein contraction and the second relates curvature lower bounds to exponential heat-Lipschitz estimates; neither inspected statement gives the exact two-exponential norm and all three pairwise transport laws for arbitrary clique bouquets. Jost–Liu (arXiv:1103.4037) uses a degree-normalized neighbor walk and graph clustering inequalities, not this generator and full time profile. Jost–Mulas–Zhang (DOI 10.1002/jgt.22999) treats normalized-Laplacian spectral gaps on homogeneous petal graphs, not transport.

Previously available results include the **infinitesimal edge-total-variation threshold on the same clique-bouquet family**, and a sharp heat-Lipschitz profile for complete bipartite stars. These are explicitly excluded from the novelty claim. Their statements do not imply the exact non-star pairwise heat transports, nor the equality of the full sharp norm for all repartitions preserving the minimum clique size. Targeted published-record and mathematical-database searches returned no covering theorem; this is evidence of noncoverage within the inspected set, not proof that unindexed prior calculations cannot exist.

## Mathematical value — PASS

These are natural finite block graphs: one cut vertex joins arbitrarily many cliques of unequal sizes, and their heat dynamics exhibit competing within-clique and between-clique decay modes. A complete, all-time pairwise transport classification is a useful quantitative benchmark beyond the existing contraction threshold. The smallest-blade rigidity has direct mathematical content: a graph may acquire many new edges and different nonzero spectral modes, yet its **entire sharp heat-Lipschitz profile remains identical** to the star's whenever a singleton blade remains. More generally the exact improvement caused by making the smallest blade larger is \(2(s-1)(e^{-t}-e^{-(k+1)t})/k\). The invariant is natural and its full-time value is not a known-table recomputation or a degree-only exercise.

## Limitations and risks

This does not handle arbitrary block graphs, weighted conductances, degree-normalized random walks, or transport exponents other than one. The existing infinitesimal variation theorem and star formulas are not claimed anew. An unindexed equivalent family calculation could affect publication priority; independent audit has not yet been performed.

Self-review: passed. Independent audit: not yet performed.
