# Independent mathematical audit

## correctness

PASS

For incidence graph of PG(2,3), all 13 points and 13 lines labeled. The DET:OLD definition requires each open detector neighborhood size>=2 and for each distinct pair at least one directional neighborhood difference size>=2. Bipartite point/line tests separate independently. A set of selected lines is DET-feasible iff every point selected degree d(p)>=2 and every selected line contains at most one weak point with d(p)=2. The omitted lines form an arc of size <=4 in the dual plane. Four omitted lines force six weak pair-intersections on only nine selected lines (12 incidences), hence fail. Three nonconcurrent omissions work, as their pairwise intersections are joined only by omitted lines. The 0/1/2/3 omitted counts 1,13,78,234 yield side polynomial z^13+13z^12+78z^11+234z^10, squared for full DET; minimum 20 with 234^2=54756 extremizers. RED only needs double cover, allowing 234 4-arcs, hence RED square with extra 234z^9 and minimum 18. Independently enumerated all 8192 side masks with exact incidence over F3 and checked both histograms. Geometry proves all 26-vertex cases, not an unproven infinite extrapolation.

## originality

PASS

Jean and Seo formulate DET and RED neighborhood criteria and study extremal graphs, complexity, infinite grids, cubic graphs, not this Desarguesian plane incidence graph. Classical finite-plane double-blocking/arc counts already imply RED minimum and four-point arc counts. The directed DET restriction rules out four omitted lines and yields the exact new full DET enumerator/extremizer characterization. Risk of a preexisting exact PG(2,3) detector table under different indexing remains.

## value

PASS

The detector sets are a natural information-theoretic, one-fault graph-code invariant on a canonical 4-regular, 26-vertex finite geometry. Exact polynomials separate two closely related error models by two detectors and classify every optimum, potentially useful to a researcher comparing code robustness; finite size does not by itself negate mathematical significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
