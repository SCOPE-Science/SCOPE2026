# Exact edge-defect homotopy of \(\mathcal M(P_3\square P_5)\) and \(\mathcal M(P_3\square P_6)\)

## Finding

For every edge \(e\) of \(G_n=P_3\square P_n\), where \(n\in\{5,6\}\), the ordinary matching complex of the one-edge-deleted graph has the exact integral homotopy type
\[
\mathcal M(G_n-e)\simeq\bigvee^{b_n(e)}S^{n-1}.
\]
The complete list of \(49\) ranks \(b_n(e)\) is given below. In particular, deletion location affects the answer: when \(n=6\), all eight ranks \(21,22,23,24,25,26,27,28\) occur.

## Assumptions and scope

The simple graph \(G_n\) has vertices \((r,c)\) for \(0\le r\le2\), \(0\le c<n\). Two vertices are joined when their grid coordinates differ by one in exactly one coordinate. The horizontal edge \(h_{r,c}\) joins \((r,c)\) and \((r,c+1)\), with \(0\le c<n-1\). The vertical edge \(v_{r,c}\) joins \((r,c)\) and \((r+1,c)\), with \(0\le r<2\), \(0\le c<n\). A face of \(\mathcal M(H)\) is any set of pairwise vertex-disjoint graph edges, including the empty face. The values below are exact; the theorem asserts no behavior at widths beyond \(n=6\).

For \(n=5\), horizontal-edge ranks (columns \(c=0,1,2,3\), rows \(r=0,1,2\)) are:

| \(r\) | \(c=0\) | \(c=1\) | \(c=2\) | \(c=3\) |
|---|---:|---:|---:|---:|
|0|12|12|12|12|
|1|14|14|14|14|
|2|12|12|12|12|

Vertical-edge ranks (columns \(c=0,1,2,3,4\), rows \(r=0,1\)) are:

| \(r\) |0|1|2|3|4|
|---|---:|---:|---:|---:|---:|
|0|10|12|12|12|10|
|1|10|12|12|12|10|

For \(n=6\), horizontal-edge ranks (columns \(c=0,1,2,3,4\)) are:

| \(r\) |0|1|2|3|4|
|---|---:|---:|---:|---:|---:|
|0|24|22|28|22|24|
|1|26|28|27|28|26|
|2|24|22|28|22|24|

Vertical-edge ranks (columns \(c=0,1,2,3,4,5\)) are:

| \(r\) |0|1|2|3|4|5|
|---|---:|---:|---:|---:|---:|---:|
|0|21|25|23|23|25|21|
|1|21|25|23|23|25|21|

## Proof

This is an exhaustive finite discrete-Morse proof, with the self-contained executable certificate `verify_grid_edge_defects.py`. Each deleted-edge complex is constructed independently from its graph: the program lists graph edges in a specified fixed order and recursively enumerates all matchings by either excluding the next edge or including it when its endpoints are unused. This generates every augmented face exactly once. Each graph then has its own explicitly provided permutation of remaining graph edges, stored in `ORDERS`.

Given one such permutation, process its edge vertices in order. At step \(i\), for every unmatched face \(\sigma\) not containing the current edge vertex \(x_i\), pair \(\sigma\) with \(\sigma\cup\{x_i\}\) if both faces remain unmatched; remove the pair. The program does not assume this prescription is automatically acyclic: it reconstructs **every** cover relation of the full augmented face poset, directs matched covers upward and all other covers downward, and performs exhaustive Kahn topological sorting. A directed cycle would leave unsorted faces. Each of the \(49\) independent tests sorts every face, establishing acyclicity.

For every deleted edge, exactly \(b_n(e)\) unmatched faces remain, all of dimension \(n-1\). The augmented empty face is matched. Remove only its pair, turning the associated original vertex into one ordinary critical \(0\)-cell; this cannot create a directed cycle because the empty face becomes a sink. Consequently, the geometric realization is homotopy equivalent to a CW complex with one \(0\)-cell, \(b_n(e)\) cells in dimension \(n-1\), and no other cells. Because \(n-1\ge4\), all these attaching maps have zero-dimensional target and are trivial. This proves the asserted wedges, and in particular the **integral**, not only field, homology descriptions.

## Verification

Running `python3 verify_grid_edge_defects.py` checks \(49\) edge-deletion graphs, \(774599\) augmented faces, \(4028730\) face-cover incidences, and \(386842\) distinct Morse pairs. For each case it verifies exact face coverage, the full acyclic orientation, the dimensions and number of critical faces, and the reduced Euler characteristic. As a separate numerical check, a memoized deletion/cover recurrence for the matching polynomial at argument \(-1\) reproduces each reduced Euler characteristic from the graph vertex adjacency structure without enumerating simplicial faces. The script uses Python standard library only and prints `PASS` when all assertions hold.

## Relationship to prior work

Chauhan, Sharma and Shukla (arXiv:2609.27366, first posted 2026-09-23) study connectivity and homology of matching complexes of the **unmodified** three-row Cartesian grids. The older Goyal–Shukla–Singh article (arXiv:2106.09915) also concerns **unmodified** three-row grids. Neither unmodified-graph statement directly determines the homotopy types or edge-position-dependent Betti ranks after deleting a graph edge: the matching complex of the deleted graph is a vertex-deletion subcomplex of the original matching complex and need not have the same homotopy type. Related results on matching complexes of outerplanar graphs give qualitative wedge decompositions only when their outerplanar hypotheses apply, not these complete defect-rank tables.

## Limitations

Only the two specified grid widths and exactly one missing graph edge are classified. The result does not imply a recurrence for arbitrary widths, nor a theorem for multiple simultaneous edge deletions. The primary 2026 paper's complete text was not available during the literature comparison, and equivalent unindexed finite calculations cannot be excluded. The presented reproducible discrete-Morse data establish the finite homotopy claims independently of any literature-based inference. Independent scientific validation has not been performed.

## References

1. P. Chauhan, A. Sharma and S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366 (first posted 2026-09-23).
2. S. Goyal, S. Shukla and A. Singh, *Matching complexes of \(3\times n\) grid graphs*, Electronic Journal of Combinatorics 28(4), P4.16 (2021), arXiv:2106.09915 (see subsequent author withdrawal notice concerning the original proof).
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
