# Independent mathematical audit

## correctness

PASS

With hub fibers each of size h=min(k,n), each degree-two neighbor has a two-choice fiber and the hubs are nonadjacent. Ordinary lists: equal hub color if lists intersect; otherwise each leaf list forbids <=1 ordered pair. A complete h-by-h grid needs h² leaves. DP matching: two leaf choices fail only if separately blocked by different hub choices, forbidding <=2 coordinate-disjoint ordered pairs; concatenated cyclic perfect matchings partition the grid into ceil(h²/2) such admissible blocks. Explicit local cover gadgets exclude each block and establish necessity. h=n satisfies both inequalities for n>=3; boundary K2,2 twisted DP C4 cover and K2,1 forced-color obstruction are valid. Independent script constructed 510 sample block cases for h=2..14 and confirmed exactly two coordinate-disjoint forbidden hub pairs.

## originality

PASS

Same-claim comparison: The already-known ordinary obstruction contributes no originality. Two-pair DP correspondence behavior differs because matchings at a leaf exclude two disjoint grid pairs rather than one ordinary pair. Class-wide square-root bounds and uniform-fold color numbers do not force the exact hub-vs-leaf two-cover threshold for every n. Existing stated theorems do not imply the simultaneous exact ordinary and DP thresholds; recognizes already covered obstruction. Historical-priority risks are retained.

## value

PASS

A sharp separation by factor sqrt(2) of two natural degree-truncated coloring invariants for a canonical bipartite family is informative, with a substantive DP-cover gadget classification, not merely the previously known list obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
