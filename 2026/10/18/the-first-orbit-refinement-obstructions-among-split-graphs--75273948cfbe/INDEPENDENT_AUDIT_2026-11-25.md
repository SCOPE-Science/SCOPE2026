# Independent mathematical audit

## correctness

PASS

The mask-multiset search covers every split representation up to independent labels, including disconnected graphs and empty parts, and the original pinned automorphism algorithm tests adjacency and nonadjacency exactly. I separately enumerated the mask multisets through ten, retaining clique degrees in sorted order and restoring presentation counts by the multinomial number of row-degree arrangements. I refined the full uncolored graph into equitable classes and computed within-part orbits by enumerating clique permutations preserving the multiset, with free permutations of identical columns. This restriction is exact: cross-part equal-degree vertices are twins (degree k−1 or k, for clique size k). Also, the image of the clique under any automorphism differs in at most one vertex, and the exchanged pair has equal degree and hence is a twin pair. The twin switch can undo that one swap without affecting a designated same-part target, which lies in the intersection of the old and new parts. The run matches all presentation counts, no failures through nine and 71 at ten, and the four exact canonical lists with counts 6,10,10,45. Degree separation makes the two parts intrinsic for the exceptions and the stated biregular degrees make them equitable; every column is nonempty. For k=4 the masks are an alternating doubled/single 4-cycle, giving a transitive size-four clique orbit and independent orbits of sizes four and two, with automorphism order 4·2²=16. The k=6 incidence is its transpose up to labels. For k=5 the size-two columns are a double edge and a disjoint triangle, giving 2+3 in each part and order (2!·3!)·2=24; the size-three column case is its incidence complement. These give the exact reported profiles.

## originality

PASS

The standard refinability definition is prior work. The closest split-graph theorem inspected concerns distinguishing two different graphs, not recovery of automorphism orbits inside one graph. Related outerplanar obstructions and general colour-refinement rules do not give the exact split-graph census or imply its lower bound.

## value

PASS

This gives the sharp threshold for a standard graph-symmetry test in a natural hereditary graph class. The four explicit minimal patterns and their orbit profiles distinguish the first forms of failure, not just the existence of an example. This is also a useful boundary distinct from the earlier between-graph distinguishability failure; regularity of the two stable cells alone is not enough for within-graph orbit recovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
