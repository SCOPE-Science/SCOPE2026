# Independent mathematical audit

## correctness

PASS

The claim is unchanged in /workspace/repairs/3/RESULT.md. The frozen separator proof called (d−1)(d−3) the number of nonneighbors of all three anchors, omitting the d−3 additional neighbors of the star center. The corrected number outside the triple is d(d−3), with the same zero/positive cutoff. The table itself is correct: its last star row cell counts vertices touching neither the anchors nor their center. Rechecking the proof: diameter two gives a common neighbor for any nonedge, four-cycle exclusion gives uniqueness, and triangle exclusion treats edges. The two-anchor profile with a nonedge splits the no-adjacency cell into d−2 star extensions and (d−1)(d−2) nonstar extensions. For three distinct anchors the profile is determined by incidence to them and their pair-centers. A nonstar independent triple forms an induced hexagon with its centers: only opposite pairs can have an external common neighbor and each does, giving three distinct opposite-pair witnesses; the centers themselves give three singleton profiles. Each hexagon vertex has d−3 further private neighbors and (d−3)²+1 outside vertices touch none. For an edge plus isolated anchor the corresponding pentagon permits only private attachments, d−2 per vertex, and (d−2)(d−3) vertices touch none. In the star case the center gives one witness, with d−3 other center neighbors, d−1 private neighbors per original anchor, and the remainder. For a path the middle anchor is the endpoints' center, so the independent-star bit for the endpoints simply records a new neighbor of the middle. Each set of labeled supports, not just its cardinality, is thus independent of degree for d≥4. Relocating a pebble leaves at most three anchors; the strategy restores every pair and triple invariant on every move, also when several pebbles occupy one vertex. The written separators have ranks three and four, and any rank-q sentence can rename bound variables using at most q names. This proves the rank lower bounds and the conditional 50-vertex representative statement inside the Moore family.

## originality

PASS

The supported distinct claim is unrestricted counting-free FO⁴ equivalence in the higher-degree class. The existing four-round proof, lower-width results, and low-rank separators are expressly credited in the corrected result. Their conclusions do not perpetuate the enhanced invariant. This is a scoped distinctness judgment, not publication priority.

## value

PASS

The stronger fixed-width result closes the nontrivial logical question left by the rank-four comparison. The permanent support invariant explains structurally how the known 50-vertex graph represents the conditional higher-degree theory without the use of transitivity or cardinality information. This matters at every depth, not just in a checked tuple enumeration; the scope clarification preserves that motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
