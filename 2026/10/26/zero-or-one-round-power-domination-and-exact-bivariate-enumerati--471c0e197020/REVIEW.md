# Independent mathematical audit

## correctness

PASS

An edge is initially observed in the line graph exactly when it meets the set T of selected endpoints. An observed edge wholly in T has no unobserved neighbor, while an observed boundary edge xy with y outside T has exactly deg(G[V\T],y) unobserved neighbors. Since nonempty S meets at least two parts, every uncovered vertex has an observed boundary edge to a covered vertex in a different part. The induced uncovered complete multipartite graph is either edgeless, a star (every edge can be forced simultaneously at a leaf), or of minimum degree at least two (no force can begin). For fixed uncovered counts, choose the uncovered labels, then apply inclusion–exclusion over missed labels among the remaining vertices; the empty remaining vertex set contributes zero after subtracting the empty selection. This verifies both size and round exponents, with zero measured after initial domination. An independent direct propagation enumeration agreed coefficientwise with the bivariate formula on (1,1,2), (1,2,3), (2,2,2), (1,1,1,3), and separately on the bipartite example (3,3).

## originality

PASS

Pass for the mixed multipartite joint cardinality/propagation enumerator and its structural classification as assessed against the accessible earlier statements. The later general endpoint–forest result covers the feasibility condition and explains its specialization, but does not supply earlier priority or the round-resolved polynomial. The same-day all-singleton result is a boundary analogue and is outside the claim; ordinary rook domination and scalar power domination are not the joint enumerator.

## value

PASS

Two selected sets of the same size can require different propagation effort. The exact joint distribution, valid for arbitrary mixed part sizes, identifies precisely when propagation can start and why it then terminates in one round; it is more informative than the minimum number or ordinary domination polynomial. The residual classification isolates the obstruction from three occupied uncovered parts, absent in the rook case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
