# Independent mathematical audit

## correctness

PASS

For n≥2 no vertex dominates alone. An independent dominating union must use exactly one endpoint of each private pair. The chosen coalition's two supports partition the base indices; the remaining blocks' nonempty supports partition the same indices a second time. If at least three residual blocks remain, none can partner another residual block, yet at most two can have supports complementary to the original two blocks. A sole residual block would have full support and no partner. Thus there are exactly four blocks with two copies of each complementary support, and their 2-by-2 coalition graph without isolates has a perfect matching. Its unions give a proper 2-coloring, and conversely splitting either side of such a coloring into two nonempty blocks gives coalitions. The 2^(c−1)(2^(n−1)−1)² unordered-coloring presentations double-count exactly the partitions for which switching the matching flips colors on a union of components: a crossing base edge would become monochromatic, while without such an edge the switch works. Each of the 2^(c−1)−1 component splits gives 2^(c−2) doubly presented partitions when c≥2; there is no correction when c=1. The K₂ singleton partition is the only n=1 case. The finite recorded checks are consistent with these arguments.

## originality

PASS

Credit is for the exact independent-partition enumerator on arbitrary bases, especially the disconnected presentation correction and coverage beyond trees. An ordinary-coalition upper bound, the broader four-block bipartiteness implication, and the reported connected-tree count are not credited as distinct contributions.

## value

PASS

The partition polynomial distinguishes bipartite from nonbipartite arbitrary bases and reveals an exact edge-independent count within each bipartite (n,c) class, despite independence being edge-sensitive. The correction quantifies exactly when different proper colorings produce the same unlabelled partition; it is needed even for elementary disconnected examples and is not supplied by a maximum-size result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
