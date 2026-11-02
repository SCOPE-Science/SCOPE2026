# Review of the weighted-wheel endpoint projection result

## Correctness — PASS
The statement concerns one precisely defined real finite-dimensional projection, with conductance-rescaled coordinates and all positive spoke weights. Grounded Laplacian inversion gives a strictly positive symmetric Green sequence. Monotonicity and its discrete convexity determine, without sign assumptions left unchecked, the absolute row sums of both edge orbits. The central recurrence reduces the rim expression to a closed formula. Strict positivity of the derivative of the spoke diagonal leverage establishes a unique transition and its monotonicity in graph size. The zero-conductance and infinite-size limits follow from an explicit constant-mode/mean-zero decomposition and geometric decay. The independent rational-matrix program establishes all asserted sampled rows and checks projection identities, but does not substitute for the all-parameter proof.

## Originality — PASS (qualified)
Bapat–Gupta's fully readable original wheel resistance-distance paper has an exact Green kernel; this premise is appropriately credited. Its Theorem 5 and Corollary 6 concern effective resistance and do not state the absolute transfer-current row sums or classify the maximizing edge orbit. Kelner–Maymounkov provides general routing operators, not the exact wheel amplification. A separately examined full wheel Löwner-ellipsoid result is an ellipsoid optimization, not a fixed-conductance endpoint projection. The closest previously recorded projection results concern internally disjoint paths, multipartite graphs, Cartesian products, or a complete graph with one exceptional edge; none includes a general wheel with its correlated cycles and two weighted edge orbits. Equivalent formulas in older circuit-theory literature remain possible, and independently confirming mathematical priority is recommended.

## Mathematical value — PASS
Electrical gradient projections quantify worst-case edge-coordinate amplification under bounded perturbations. A wheel is a basic nontrivial series-parallel-looking planar network with overlapping cycles, and weighting its hub spokes models a natural connectivity parameter. Complete sharp formulas separate two qualitatively distinct edge sensitivities, prove the unique conductance transition and its exact limiting location, and expose the noncommutation of network-size and low-conductance limits. These are structural results about an infinite family rather than recomputation of isolated graphs.

## Scientific limitations
All edges in an orbit share conductance, and all signals use symmetric \(\sqrt c\) edge scaling. No assertion is made for arbitrary weights, general routing competitive ratios, or physical-current scaling. The kernel itself is known, and an equivalent historical electrical-flow norm formula might exist.

Self-review: passed. Independent audit: not yet performed.
