# The complete vertex-nonincreasing bistellar neighborhood of Barnette's eight-vertex sphere
## Finding
Let \(B\) be Barnette's eight-vertex triangulated \(3\)-sphere with tetrahedra
\[
1245,2356,1346,1237,4567,1247,2457,2357,3567,1367,1467,1238,4568,1258,1458,2368,2568,1348,3468.
\]
Among bistellar moves that do not add a vertex, \(B\) has exactly two \(2\)-to-\(3\) moves, exactly six \(3\)-to-\(2\) moves, and no \(4\)-to-\(1\) move.

The two \(2\)-to-\(3\) moves are centered at \(123\) and \(456\), both inserting the missing edge \(78\). Both targets are isomorphic to the Brückner--Grünbaum eight-vertex sphere with \(20\) tetrahedra.

The six \(3\)-to-\(2\) moves remove the edges
\[
15,\ 16,\ 24,\ 26,\ 34,\ 35.
\]
Their opposite missing triangles are respectively
\[
248,\ 347,\ 157,\ 358,\ 168,\ 267.
\]
All six targets are mutually isomorphic and have face vector \((8,26,36,18)\).

Barnette's simplicial automorphism group has order \(12\); it acts transitively on the two \(2\)-to-\(3\) moves and transitively on the six \(3\)-to-\(2\) moves. Thus the complete vertex-nonincreasing local Pachner neighborhood has exactly two nontrivial move orbits.

The \(18\)-tetrahedron target is polytopal. A bistellar move preserves PL type, so it is an eight-vertex triangulated \(3\)-sphere. The classical classification has exactly two nonpolytopal eight-vertex \(3\)-spheres: Barnette's \(19\)-tetrahedron sphere and the neighborly Brückner--Grünbaum \(20\)-tetrahedron sphere. The computed target is neither.

## Assumptions and scope
A \(2\)-to-\(3\) move replaces two tetrahedra sharing a triangle by three tetrahedra around the opposite missing edge. A \(3\)-to-\(2\) move is its inverse. A \(4\)-to-\(1\) move deletes a degree-four vertex whose link is a tetrahedral boundary. These are exactly the three-dimensional bistellar moves that do not increase vertex count.

The statement concerns this fixed eight-vertex combinatorial sphere. It classifies actual legal move centers, not merely neighboring isomorphism classes in a bistellar-poset diagram.

## Proof
Reconstructing every face from the tetrahedron list gives face vector
\[
(8,27,38,19).
\]

For a triangle \(t\), a \(2\)-to-\(3\) move is legal exactly when \(t\) belongs to two tetrahedra obtained by adjoining two distinct opposite vertices and the edge between those opposite vertices is absent. Exhausting all \(38\) triangles leaves exactly \(123\) and \(456\), both with opposite vertex pair \(\{7,8\}\).

For an edge \(e\), a \(3\)-to-\(2\) move is legal exactly when its link is the three-cycle on a missing triangle. Exhausting all \(27\) edges leaves exactly the six edge/opposite-triangle pairs listed above. Checking every vertex star finds no tetrahedral-boundary link, so no \(4\)-to-\(1\) move is legal.

Exhausting all \(8!\) vertex permutations gives exactly \(12\) automorphisms. The orbit of one legal \(2\)-to-\(3\) center has size \(2\), equal to the complete upward move set; the orbit of one legal \(3\)-to-\(2\) center has size \(6\), equal to the complete downward move set.

Finally perform every legal move. Exhaustive relabeling over \(8!\) permutations identifies both \(20\)-tetrahedron targets with the standard Brückner--Grünbaum sphere and identifies all six \(18\)-tetrahedron targets with one another.

## Verification
The standalone `verify.py` uses only the Python standard library. It rebuilds every face, tests every possible vertex-nonincreasing bistellar move, enumerates all \(8!\) relabelings to recover the automorphism group and move orbits, performs every legal move, and checks all target isomorphisms.

A successful replay prints exactly:

`VERIFY_OK f=8,27,38,19 aut=12 move23=2 orbit23=2 target23=BG move32=6 orbit32=6 target32_f=8,26,36,18 target32_classes=1 move41=0`

The finite checker proves the combinatorial parts of the claim. Polytopality of the \(18\)-tetrahedron target is inferred from the published complete classification, not from numerical geometry.

## Relationship to prior work
Barnette's 1973 paper supplies the classical eight-vertex sphere classification and the second exceptional nonpolytopal sphere. Datta and Nilakantan later organize all eight-vertex combinatorial \(3\)-manifolds by proper bistellar moves. Their Hasse diagram records neighboring isomorphism classes, and their proof explicitly lists removable edges for the neighborly layer while summarizing subsequent layers.

That classification is the decisive closest prior result and covers the coarse isomorphism-class adjacency underlying the present calculation. The additional statement here is the complete labeled local move fiber at Barnette's sphere: the exact multiplicities \(2\) and \(6\), the absence of a vertex-deleting move, and the fact that each complete move set is a single automorphism orbit. These data are not determined by a Hasse edge between isomorphism classes.

## Limitations
The result is local to Barnette's sphere and does not determine longer bistellar distances, geometric realization coordinates, or move multiplicities for the other \(38\) eight-vertex spheres. The originality assessment is statement-level; an unindexed historical computation or auxiliary table could contain the same local multiplicities.

## References
1. D. Barnette, *The triangulations of the 3-sphere with up to 8 vertices*, Journal of Combinatorial Theory, Series A 14 (1973), 37--52, DOI `10.1016/0097-3165(73)90062-9`.
2. B. Datta and N. Nilakantan, *Three dimensional pseudomanifolds on eight vertices*, arXiv:`math/0701038v1`, submitted 2007-01-01; DOI `10.1155/2008/254637`.
3. SageMath, `simplicial_complex_examples.py`, standard examples `BarnetteSphere` and `BrucknerGrunbaumSphere`, used as an exact machine-readable labeling cross-check.
