# Independent mathematical audit

## correctness

PASS

For every r>=2, the friendship graph F_r has hub h and r outer edges. A capped dominating set with size≤r+1 is exactly H_X={h}∪X, |X|≤r, a transversal L_T choosing one vertex each edge, or an upper U with one doubled edge and singletons elsewhere. Edges are all allowed outer toggles inside H-ball, H_T↔L_T, and L_T↔U where T is a floor of U. This supplies explicit sharp routes: hub-hub Hamming; hub-lower 1+Hamming; hub-upper 2+min floor-Hamming; lower-lower Hamming; lower-upper 1+min floor-Hamming; upper-upper Hamming unless their same doubled blade forces two extra operations (U≠V). The crucial hub-upper lower bound uses the last hub deletion; same-doubled upper pairs must first delete and later readd a currently common blade vertex. Maximizing these distances gives stated eccentricity by singleton/double counts a,b, radius r+2, diameter 2r+1, center r+1, periphery (r+2)2^r. Counting the three vertex classes and allowed toggles gives claimed vertex/edge formulas. At cap r each transversal is isolated; cap r+1 is connected via hub states. Independent subset-domination/BFS for r=2,3,4,5 obtained (states,edges,radius,diameter,centers,periphery) equal respectively (19,28,4,5,3,16), (62,128,5,7,4,40), (211,592,6,9,5,96), (750,2752,7,11,6,224), as symbolic formulas predict. The all-r proof is the route/lower-bound argument; finite BFS corroborates.

## originality

PASS

PASS for complete all-pairs TAR reconfiguration metric and eccentricities of friendship graphs at cap Γ+1, not for the definition, upper domination number or threshold connectivity. Haas–Seyffarth’s 2013 chordal theorem already gives connected D_{Γ+1}, and general Suzuki–Mouawad–Nishimura bounds do not supply precise F_r distances; ordinary domination polynomial counts alone cannot establish shortest paths. This new exact metric is a structurally motivated classification of a natural family at its first connected size cap, though an unindexed graph-specific metric calculation remains possible.

## value

PASS

At the first connected dominating-set size cap, determining actual shortest change sequences is a natural reconfiguration metric problem, and known chordal connectivity does not answer it. All-pairs formulas, eccentricities, unique center types, periphery counts and the sharp disconnected-to-connected threshold give a complete infinite-family classification valuable for graph reconfiguration comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
