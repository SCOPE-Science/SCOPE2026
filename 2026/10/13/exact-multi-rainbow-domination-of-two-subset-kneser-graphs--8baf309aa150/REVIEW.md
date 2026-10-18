# Independent mathematical audit

## correctness

PASS

The graph vertices are 2-subsets of [n] adjacent when disjoint. For four chosen ground elements, split the six edges into the three perfect matchings of K4; put a disjoint nonempty block of the k colors on both edges of each matching. Each empty-labeled vertex is disjoint from at least one edge in each matching, so weight=2k suffices. If weight≤2k−1 and some color absent, no vertex can be empty, costing at least binom(n,2)≥2k. Otherwise one color has a unique bearer e={a,b}; all 2n−3 graph vertices meeting e must be labeled. For n≥k+2 this already exceeds 2k−1. At n=k+1 all incidences must be singleton labels and all nonempty vertices form the two-star about a,b. Every other color has exactly two spokes; any pair of spokes is jointly intersected by a zero-labeled 2-subset of X=[n]\{a,b}, contradicting coverage. Covers |X|=k−1≥2. Independent brute force checked all 12,616 and 174,437 incidence subsets of weight<6 on KG(4,2), KG(5,2) with palette3, no counterexample. All-parameter proof is combinatorial, not extrapolation.

## originality

PASS

Best-of-knowledge novelty assessment compares identical mathematical statements and implications, not titles or a lack of search hits. Colored set-valued rainbow functions differ mathematically from known k-tuple/Roman Kneser domination, and the Cartesian-product equivalence alone gives no exact formula. Comparison risks remain explicitly recorded; noncoverage is not asserted from abstracts of unread whole papers.

## value

PASS

Exact optimization for unbounded k and n of a natural domination invariant on standard Kneser graphs, with a weight-2k construction independent of graph order and an essential sharp boundary obstruction. It improves the naive full-palette labeling of a three-vertex dominating set (weight 3k), a substantive structural gain and natural graph-theoretic fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
