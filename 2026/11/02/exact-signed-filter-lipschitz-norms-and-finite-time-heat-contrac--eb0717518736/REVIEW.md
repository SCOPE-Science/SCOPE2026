# Scientific assessment: signed Kneser adjacency-filter norms and heat contraction

## Correctness — PASS

The graph is explicitly the two-subset Kneser graph with \(n\ge5\), the norm is the real graph-distance Lipschitz norm modulo constants, and the generator is the unnormalized rate-one combinatorial Laplacian. Edge transitivity reduces the operator norm to one signed edge measure. For \(n\ge6\), a fixed-point-free outsider permutation gives a cost-one matching for every positive/negative coefficient, and a bounded-range Lipschitz potential attains the full absolute coefficient sum. For \(n=5\), averaging reduces the optimization to a two-dimensional polygon; every extremal corner is realized by valid graph-distance potentials. The exact adjacency quadratic identity yields the two nonconstant eigenvalues; their heat multipliers give the asserted formula for all nonnegative times. Differentiating its explicit positive two-exponential form proves the strict rate acceleration. Exact-integer/rational replay and numerical Kantorovich dual checks were executed; no finite enumeration is used as proof for all dimensions.

## Originality — PASS, with stated historical risk

The closest inspected primary work provides (i) a general equivalence of curvature lower bounds and Lipschitz heat estimates (Münch–Wojciechowski, arXiv:1712.00875), (ii) geometric rigidity and Petersen curvature/spectral information (Cushing et al., arXiv:1807.02384), and (iii) formulas for infinitesimal Ollivier curvature on strongly regular graphs including the Petersen zero-curvature case (Bonini et al., arXiv:1907.06733). These compare to the present statement but do not imply a complete unrestricted *signed* two-parameter adjacency-filter norm or its exact positive-time heat coefficient. Semantically related published research records and accessible historical claims were compared against the all-filter and heat formulations, including domination by general transport/curvature theorems; no covering statement was identified. A previously published equivalent computation under a different semigroup, spectral-multiplier or earthmover convention remains a nonzero historical-priority risk. This assessment is not independent novelty certification.

## Mathematical value — PASS

The operator norm is an exact natural invariant for all real two-parameter spectral filters on a prominent infinite family of finite graph Lipschitz spaces; the exceptional Petersen facet and the sharp matching transition at \(n=6\) are structural, not arbitrary parameter selections. Its heat specialization gives a full-time Wasserstein-one coefficient, distinguishes vanishing *initial* curvature from strictly positive later contraction, and proves a strict acceleration law. The result does not seek all graph heat semigroups or the exact norms of arbitrary non-polynomial operators.

## Verification and limitations

The executed standard-library certificate checked 123188 exact adjacency identities, 767 signed-filter witness/matching cases, and 225 rational spectral-heat identities. Finite numerical linear programs tested 75 additional signed-filter and heat cases on orders \(5\) through \(9\). The theorem itself is proved analytically for all stated parameters and times. Generalizations to higher-subset Kneser graphs, non-unit weights, and other Wasserstein exponents are not established. The investigation cannot exclude every older equivalent theorem; independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
