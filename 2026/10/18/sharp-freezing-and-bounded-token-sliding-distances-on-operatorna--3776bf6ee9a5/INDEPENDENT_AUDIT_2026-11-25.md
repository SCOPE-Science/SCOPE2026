# Independent mathematical audit

## correctness

PASS

Pairwise-intersecting families of complete-graph edges are stars or the three edges of a triangle; any fourth edge forces a common center. A slide in a star of size at least four must avoid its old center while meeting at least three distinct retained leaves, which is impossible. This proves the isolated-state counts and the absence of states above n−1. One token has diameter two since intersecting edges use three labels, leaving two labels for a common disjoint edge. For two tokens each retained edge yields n−3 replacements with the other endpoint as new center, and label permutations are transitive. Independent exhaustive BFS on the directly generated slides reproduced the entire target-orbit table: 30 and 60 states, degrees 4 and 6, respective base histograms (1,4,10,14,1) and (1,6,21,29,3), all eccentricities four. These cases suffice for the upper bound because any two states use at most six labels and the legal moves on those labels embed into the full graph. Two two-edge stars at the same center with disjoint leaf pairs require four slides: the first cannot add a target edge, the second would reach a state with the common center and only one target edge, and the third would have to change centers. For three tokens, each slide must change type between triangle and star. The two-step graph on triangles is exactly J(n,3) by sharing two labels, so the triangle metric is twice Johnson distance and each star endpoint contributes one more edge via its adjacent triangles. For n=5 all eccentricities are four: triangles can intersect in exactly one point, and stars with the same leaves and different centers have no common neighbor but have neighbors sharing two labels. For n=6 triangle eccentricity is six by disjoint triples, star eccentricity five by a triangle with one common support label; star-star distance is at most four. For n=7 opposite types can have disjoint supports and give seven, while star-star distance is at most six. For n≥8 triangles have eccentricity seven and each star has a disjoint star at distance eight. The edge counts follow from the degree and state counts. The independent finite BFS was necessary for the supplied two-token upper-bound proof; it was not an extrapolation to arbitrary n. The submitted checker was inspected but not executed.

## originality

PASS

The distinct supported claim is the complete occupancy classification with sharp two-token distances and the precise Johnson-based three-token metric and radius/diameter transition on independent sets of KG(n,2). The nearest comparisons concern other moves, other state spaces even on the same host, or the ordinary unpointed incidence relation. The standard star/triangle fact and the Johnson distance formula are ingredients, not asserted novel.

## value

PASS

Kneser graphs are canonical disjointness graphs and this resolves a natural exact reconfiguration invariant across every occupancy: not only where reachability fails but also how far reachable configurations can lie. The pointed-incidence model gives an explicit state-pair distance and explains the small-n radius/diameter changes. The compact finite computation is tied to a proved six-label cutoff, not an arbitrary census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
