# Independent mathematical audit

## correctness

PASS

For n>=3 the crown distance table is exact: same-part distinct pairs distance 2, matching nonedges distance 3, other cross pairs distance 1. Same-part difference profiles force every doubly resolving set to omit at most one matched pair P_i, yielding |S|>=n-1. For a single omitted P_i, its matched endpoints require landmarks on both sides. An adjacent cross pair a_i,b_j (i!=j) has just two +/-1 difference levels, each a matched-pair transversal. A set of n-1 vertices is one-hole transversal, and avoids every level exactly if >=3 vertices are chosen from each side. This is feasible precisely for n>=7. For 3<=n<=6 any optimum n-set either has one omitted and another doubled pair (automatically defeats all transversals) or is a full transversal excluding B-side weights 2 and n-2. Counting gives all exact stated coefficients. Independent verifier enumerates all subsets through the claimed optimum for n=3..9, with 142924 subset checks, zero classification mismatches, and bases n3..9 = 14,58,172,514,140,560,1638. The infinite theorem is proved by the distance-level case analysis, not bounded experiments.

## originality

PASS

Originality is a best-of-knowledge judgment for the all-n crown vertex-doubly-resolving phase transition, exact minimum-set structure and enumerations. Foundational theory and general bounds do not imply it; related same-invariant complete multipartite and chain graph theorems exclude the matching-deleted crown; the crown edge-metric theorem is a distinct statistic. Finite cases that follow from classical cycle or hypercube results are not claimed as novel. Searches are not proof of absence and residual unindexed priority risks remain.

## value

PASS

Crown graphs are canonical distance-three matching-deleted complete bipartite graphs. The exact vertex doubly-resolving invariant is mathematically motivated by landmark localization and the classical relation to Cartesian-product metric dimension. The theorem does not just recompute a known scalar: it gives a sharp parameter transition at n=7, complete structure of every minimum set and exact counts, with a nontrivial three-per-side constraint distinguishing doubly resolving from edge resolving. Such detailed bases are reusable as witnesses/counterexamples and for design of landmark sets. The classification is naturally an infinite-parameter family rather than an arbitrary tiny slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
