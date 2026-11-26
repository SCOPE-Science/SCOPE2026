# Independent mathematical audit

## correctness

PASS

Branch vertices are recognized by degree n−1>2 and determine all automorphisms. Each interior mark forces preservation of its endpoint pair, and an off-midpoint mark fixes both endpoints. Two marked paths sharing an endpoint fix all their endpoints because both distinct pairs must be preserved. This propagates in each nontrivial support component. The only moves left are independent endpoint flips on free-central edges and arbitrary permutations of unused unmarked branches. Refinement at round r recognizes distance ≤r from any original singleton mark, with a distinct out-of-range outcome (induct by a shortest path through a neighbor). By round L−1 the branch signatures distinguish exactly that stabilizer’s branch orbits: a mark identifies a marked branch or an oriented endpoint, and a shared signature of nonempty midpoint supports can only arise from the two endpoints of an isolated free-central edge. The degree test keeps these classes separate from interiors. Another L−1 rounds recognize distances <L from those branch classes. The only branches at distance <L from an interior vertex are its two endpoints; two different endpoint classes give the position relative to either class, and one shared class gives the position up to reflection. Independent block actions have exactly those interior orbits; within a common block the action is transitive on unordered pairs and realizes reversal. Counting gives L−1 orbits per pair of distinct classes, and floor(L/2) per nonsingleton class. For the latter, sizes are twice the number of endpoint pairs except at the midpoint, where they are that number. This also handles S empty, L=2 and u=0 or 1. Since every refinement color is invariant under the stabilizer and its orbit partition is equitable, the partition at the asserted bound is stable.

## originality

PASS

The supported distinction is the uniform subdivision family with simultaneous branch and interior marks, an explicit orbit census, and an n-independent round bound. The general Tinhofer criterion and the Johnson graph proof are prior; neither gives these conclusions for the stated graphs.

## value

PASS

A natural extension of a known Tinhofer family question is whether arbitrary marks still suffice when the graph is replaced by its uniform incidence/path subdivision. The result settles it with a mechanism that isolates all residual symmetry and supplies a uniform convergence bound independent of graph order, as well as exact sizes and counts, rather than just certifying individual cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
