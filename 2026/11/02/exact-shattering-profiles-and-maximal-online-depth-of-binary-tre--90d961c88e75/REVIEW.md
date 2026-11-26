# Independent mathematical audit

## correctness

PASS

The closed neighborhoods have the two exact forms singleton leaf plus ancestor chain, or singleton internal node plus descendant cluster. The pair counts are binom(L,2), hL and sum(d 2^d). Laminarity rules out three leaves, chains rule out three internals, and two internal ancestors of one leaf cannot realize the lower internal alone. For the remaining triple type the all-positive trace fixes the internal vertex above or at the LCA; the double-leaf trace requires the LCA not to be root, and singleton-leaf traces exclude sibling leaves. At depths 1 through h−2 the two child centers, a different joint ancestor, third descendant leaf, and a disjoint branch give all required traces. Counting by LCA gives the claimed cubic coefficient; a four-point set necessarily contains a forbidden triple. The h=1 root is unavoidably positive, and the two leaves are individually but not jointly shattered. For Littlestone rank, 2^(h+1)−1 is a concept-count upper bound, and the 2^h leaf centers realize recursive internal-subtree tests followed by a leaf test on the remaining sibling pair. The deepest internal vertex on any cycle of length at least six forces a chord, and depth-one internals have distance four. Independent bounded enumeration (no frozen code executed) compared all supports to size four at h=2,3,4, and to size three at h=5, with coefficient lists [1,7,16,0,0], [1,15,62,16,0], [1,31,218,112,0], [1,63,754,576]; a memoized online recursion returned 1,2,3,4. Replay method: index tree by heap indices, build ancestors by integer halving, count distinct concept intersections with each support, and compute rank on concept masks by maximizing one plus the smaller child rank over nontrivial membership splits. The bounded checks do not establish the all-height claims, which follow from the structural arguments.

## originality

PASS

The exact profile of the full ground-set closed-neighborhood system together with maximum possible online depth on this chordal-bipartite family is distinct in the checked comparisons. The prefix split construction and concept-count bound are standard and not credited as standalone contributions.

## value

PASS

This is a concrete family inside a restrictive graph class for which the exact count of every static shattered layer is known and the concept-count upper bound on adaptive depth is attained. The conjunction is useful as an exact separation/witness and as benchmark data for graph-neighborhood dimension; the rank proof alone would be a routine prefix example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
