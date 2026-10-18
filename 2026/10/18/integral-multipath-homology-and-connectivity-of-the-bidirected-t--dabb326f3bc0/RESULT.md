# Integral multipath homology and connectivity of the bidirected three-cube

## Finding
Let \(Q_3\) be the three-dimensional binary cube and let \(X=\mathcal X(\overleftrightarrow{Q_3})\) be the multipath simplicial complex of its fully bidirected graph. Then
\[
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{6}&j=3,\\
\mathbb Z^{45}&j=4,\\
\mathbb Z^{36}&j=5,\\
\mathbb Z^{12}&j=6,\\
0&\text{otherwise}.
\end{cases}
\]
In particular, no integral homology torsion occurs. The space \(X\) is 2-connected and \(\pi_3(X)\cong\mathbb Z^6\).

## Assumptions and scope
The vertices of \(Q_3\) are all binary strings of length three, encoded by integers from \(0\) to \(7\). Two vertices are adjacent exactly when their binary representations differ in one coordinate. Both orientations of every undirected edge are included, yielding 24 arcs. A simplex of \(X\) is a subset of those arcs such that every vertex has at most one selected incoming and one selected outgoing arc and the selected directed graph contains no directed cycle. Equivalently, each selected component containing an arc is a directed simple path; isolated graph vertices are allowed. The empty simplex is included in the augmented simplicial chain complex. All stated homology groups use integer coefficients.

The undirected graph \(Q_3\) is also the four-by-four crown graph \(K_{4,4}\) with a perfect matching removed: its two bipartition classes are the even-parity and odd-parity binary strings. This is an equivalent description of the *graph*, not an equivalence with the ordinary graph matching complex.

## Proof
A deterministic finite proof is provided by the standalone Python 3 program `verify_cube.py`, using only the standard library. First, enumeration by all \(4^8\) outgoing-arc choices and a separate backtracking enumeration with indegree and directed-cycle pruning produce the identical augmented face set. Its cardinality is 6,497 and its face counts by number of arcs (including the empty face) are
\[
(1,24,216,928,2016,2160,1008,144).
\]
The lexicographically sorted faces, each stored as a three-byte little-endian 24-bit mask, have SHA-256 digest `9115bf451a1470e640cb1d07f243f5c9f16cf7e1276d1c5a9034acc5e9a6a102`.

On the augmented face poset, take arcs indexed in lexicographic order \((a,b)\), and successively toggle each index in the following order, pairing a remaining face not containing that arc to its remaining upper face containing it:
```
1,5,16,10,14,15,12,0,4,2,22,11,19,18,8,21,3,17,13,7,20,23,6,9
```
The program explicitly constructs all 29,160 codimension-one incidences and reverses every matched incidence. A topological sort visits all 6,497 vertices of this directed incidence graph. Thus the matching is acyclic. It contains 3,199 pairs and exactly 99 critical augmented faces, with critical dimensions and multiplicities \((3,6),(4,45),(5,36),(6,12)\).

Every signed simplicial boundary coefficient is computed over \(\mathbb Z\) from increasing arc-index orientations. Integer Morse projection recursively cancels each matched lower-upper pair using the incidence coefficient \(\pm1\). Acyclicity guarantees recursion terminates. All 99 critical-cell boundary calculations have zero signed coefficients, so the *integral* reduced Morse differential vanishes identically. Hence the displayed homology groups hold over \(\mathbb Z\) with no torsion, not just modulo any finite collection of primes.

The empty face belongs to one matched pair. Dropping just that pair from the ordinary nonaugmented face-poset matching leaves a single critical vertex, no critical one- or two-dimensional cells, and the same high-dimensional critical cells. The resulting CW Morse model has one zero-cell and no one-/two-cells, hence is 2-connected. By the Hurewicz theorem its first nonzero homotopy group is \(\pi_3(X)\cong H_3(X;\mathbb Z)\cong\mathbb Z^6\).

## Verification
Run `python3 verify_cube.py` from any directory. It independently generates and compares the faces in two ways; validates the full directed incidence graph acyclicity; evaluates all integral Morse boundary coefficients; and computes the augmented simplicial boundary ranks directly over \(\mathbb F_2\). The latter ranks for dimensions zero through six are \((1,23,193,735,1275,840,132)\), independently giving reduced Betti numbers \((6,45,36,12)\) in dimensions three through six. The program prints `VERIFIED_Q3_BIDIRECTED_MULTIPATH_INTEGRAL_HOMOLOGY` only after every check succeeds.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith introduce multipath complexes and calculate homotopy types for directed paths, polygons, several small directed grids and transitive tournaments [1]. Their results provide the natural framework but do not include this fully bidirected three-cube calculation in the inspected relevant sections. Caputi, Collari and Ramos analyze categorical graph-minor properties, torsion bounds and a blow-up-to-matching-complex comparison for digraphs *without* oriented cycles [2]. The bidirected cube has opposite-arc directed two-cycles, so that theorem does not apply. Later work on bidirectional polygonal digraphs [3] concerns degree-two cycle and path graphs rather than this degree-three graph. Published calculations of ordinary matching and ordinary discrete-Morse complexes of the cube have different simplex definitions and homology; those assertions do not imply the present result. The four-crown, binary Hamming cube and cycle-free restricted-chessboard descriptions were also included in the overlap searches.

## Limitations
Only this eight-vertex bidirected graph is classified; no generalization to higher-dimensional cubes is proved. Torsion-freeness and 2-connectivity do not imply a wedge decomposition, and no such homotopy classification or complete persistence statement is claimed. Verification is an exhaustive reproducible finite calculation and a mathematical deduction from an acyclic Morse matching; no independent mathematical audit has been carried out. Unindexed equivalent earlier work remains a possible priority risk.

## References
[1] L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first publicly submitted 2022-08-09, https://arxiv.org/abs/2208.04656.

[2] L. Caputi, C. Collari and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248, https://arxiv.org/abs/2401.01248.

[3] L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, https://arxiv.org/abs/2601.05670.
