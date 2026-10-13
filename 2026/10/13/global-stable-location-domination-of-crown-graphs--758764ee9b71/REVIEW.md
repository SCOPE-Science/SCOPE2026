# Review of Global stable location-domination of crown graphs

## Correctness
PASS. The proof uses the literal stability definition, including the removed selected vertex as a newly outside vertex after each sensor deletion. If two vertices are omitted from one side, any shared omitted matching index either makes two original outside traces equal or makes them equal after deleting the other vertex’s matched sensor; hence the omitted-index sets must be disjoint. Robust domination then forces the selected opposite side to contain at least three vertices whenever there is an omitted vertex, while an entirely selected side needs at least two vertices on the opposite side. The exceptional common-singleton omission is checked separately. Conversely, the crown and complement trace formulas show that these conditions survive every sensor deletion. Exhaustive direct verification agrees with the complete classification for every subset through order sixteen and with the minimum theorem at order eighteen.

## Originality
PASS. The 2023 introducing paper gives the same invariant, but its inspected results concern general existence and graph operations rather than crown graphs; targeted full-text searches found no crown or complete-multipartite specialization. The 2021 stable locating-domination predecessor lacks the complement requirement and likewise has no crown or bipartite specialization in the inspected text. Earlier bipartite/complement work is for ordinary locating-domination, not one-deletion stability. Closest stored crown results concern solid/self locating-domination, distance-based locating-domination, or unrelated domination variants; their statements do not imply the simultaneous deletion-stability conditions in both a graph and its complement.

## Value
PASS. Crown graphs are a canonical matching-deleted biclique family, and the invariant was introduced specifically to model location systems that must remain functional after one monitoring device fails, simultaneously in a graph and its complement. The result gives more than a scalar optimum: it classifies every feasible sensor set, gives the complete size enumerator, exposes the small-order phase transition, and identifies all minimum fault-tolerant configurations for every order.

Self-review: passed. Independent audit: not yet performed.
