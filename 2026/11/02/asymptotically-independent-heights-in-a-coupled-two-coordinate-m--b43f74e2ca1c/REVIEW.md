# Independent mathematical audit

## correctness

PASS

Writing ell_i=h_i-1, a coordinate reset at t followed by ell_i nonresets gives exactly one qualifying marker, with t from 1 to n-ell_i and probability (1-q)q^ell_i. Starting from zero, the only additional way to reach h_i is the initial run of h_i successes, of probability q^h_i=O(1/n) in the window. Each indicator depends on its closed update interval and is independent jointly of all indicators on disjoint intervals. Same-type overlapping distinct markers and distinct types started at the same time are impossible. For an X reset and a later Y reset at lag 1≤k≤ell_X, the later reset also serves as one forced X success; L=min(ell_X-k,ell_Y) simultaneous successes have mass a=2q-1 instead of q^2. The resulting joint mass is (1-q)^2 q^(ell_X+ell_Y-1)(a/q^2)^L. Independently enumerated unequal-length examples at q=3/4 with integer weights 1,1,2, including ell_X=4, ell_Y=1, k=1 (18/1024) and k=4 (81/4096), agree. The window bounds the difference of lengths and a/q^2<1 gives an O(1) geometric sum in each direction, so the distinct-neighbor joint term is O(1/n). The product term including self pairs is O(log n/n), from O(n log n) pairs each O(n^-2); the term for dependence on the outside is zero. The standard local-dependence Poisson process bound at individual indices, followed by contraction under summing the two disjoint color classes, gives the claimed vector TV estimate and independent Poisson means. Simultaneous absence plus the initial-run error and the O(log n/n) mean adjustments yield exactly the uniform height formulas. The lattice limits are interpreted along subsequences with convergent intensities, not as a continuously centered weak limit. The frozen checker was read, not executed; its marker-pair loop uses equal lengths, while the independent check above and, decisively, the product argument cover unequal thresholds.

## originality

PASS

Credit the model, its terminal laws, scalar lattice-height laws and the general Poisson approximation method as prior. The distinct supported result is the uniform, quantitative joint rare-run law for two overlapping survival predicates, including the O(log n/n) total-variation estimate, whence the joint independent lattice profile. The overlapping-prefix calculation is not covered by the disjoint-letter run census or by the same-model terminal PGFs. Secondary literature dating of the Kong comparator should cite the earlier journal version; this does not change that scope comparison.

## value

PASS

The two heights interact through the same update symbols, so independent marginal laws and expected intensities are insufficient. The quantitative joint theorem shows that dependence does not persist in the critical window despite intersecting success predicates. It also gives control of counts, not just the maximum distribution, along with the correct discrete phase; this is a meaningful strengthening over terminal-altitude or one-coordinate analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
