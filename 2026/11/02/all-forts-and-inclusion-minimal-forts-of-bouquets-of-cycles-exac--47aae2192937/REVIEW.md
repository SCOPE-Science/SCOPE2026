# Scientific review

## Correctness

PASS. Every fort is classified by whether it contains the articulation vertex. In the hub-present case, missing peripheral vertices form independent sets of paths. In the hub-absent case, active petals must select both hub-adjacent vertices and omit an independent subset of the remaining interior path. This exhaustive dichotomy proves the all-fort product formula. To obtain inclusion-minimality, maximal independence is required on each relevant path, and hub-present forts additionally need at least one unselected hub-adjacent endpoint per petal. The extremal formula uses the exact independent-set bound on a path and counts odd/even effective-length ties correctly. A direct all-subsets verifier and a separate standard zero forcing implementation corroborate the equations. The proof, not the finite tests, establishes unbounded parameters.

## Originality

PASS, subject to publication-priority uncertainty. Becker et al., arXiv:2404.05963 (2024-04-09), supply general vertex-sum minimal-fort constructions and the already-known all-triangle (friendship) count. Proposition 27 can be specialized to recover a structural component of the hub-containing minimal-fort description, so that mechanism itself is not claimed as new. Their inspected Section 5 does not give the complete all-fort cardinality polynomial for arbitrary cycle bouquets, the complementary maximal-independent-set boundary enumerator, or the joint mixed-length exact formulas. Their triangle windmill count \(2^k+k\) is explicitly credited as prior work. Brimkov and Carlson, arXiv:2204.01887, concern minimal zero forcing sets, not the two fort polynomials here. Searches for one-point unions of cycles, generalized friendship graphs, graph-amalgamation fort polynomials and alternative zero-forcing terminology found no covering formula. Mathematical-record searches yielded nearby but noncovering results on friendship-graph zero forcing and minimal forts of complete multipartite graphs. Other available published comparisons found no covering bouquet polynomial. A failed search alone does not certify publication priority, and explicit bouquet formulas in less indexed venues remain a residual risk.

## Mathematical value

PASS. The general cycle-bouquet family is a natural cactus-graph class with arbitrarily many petals and unrestricted lengths. The pair of full size-distribution formulas resolves both all-fort and inclusion-minimal-fort enumeration on this family, rather than just a known scalar minimum. The hub-dependent product structure, endpoint-restricted maximal independence filter, Fibonacci total count and exact count of extremal failed zero forcing initial sets offer reusable structure, including a nontrivial parity-tie correction. The all-triangle specialization is known and not asserted as an independent discovery.

## Scientific limits and nearest literature

The 2024 vertex-sum result is the strongest inspected nearby coverage and implies part, but not the displayed all-fort polynomial, of the result. Relevant unindexed enumeration literature remains a risk. No claim is made for arbitrary cactus graphs, graph automorphism quotients, or full enumeration of all failed zero forcing starts. Finite verification covers only bounded small graphs. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
