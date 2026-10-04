# The cube is a minimal forbidden graph for \(3\)-cut-complex shellability
## Finding
For the three-dimensional cube graph \(Q_3=P_2\mathbin{\square}P_2\mathbin{\square}P_2\), let \(\Delta_3(Q_3)\) be the simplicial complex whose facets are the complements of disconnected induced three-vertex subgraphs. Then
\[
\Delta_3(Q_3)\simeq S^3\vee\bigvee^{4}S^4.
\]
In particular, \(\Delta_3(Q_3)\) is not shellable. Moreover every proper induced subgraph \(H\subsetneq Q_3\) has shellable \(\Delta_3(H)\). Hence \(Q_3\) is an induced-subgraph-minimal forbidden graph for \(3\)-cut-complex shellability.

## Assumptions and scope
The graph \(Q_3\) has vertex set \({0,1}^3\), with an edge exactly when two binary triples differ in one coordinate. The \(3\)-cut complex uses the Bayer--Denker--Jelić Milutinović--Rowlands--Sundaram--Xue convention: a facet is \(V(Q_3)\setminus S\) for a three-element set \(S\) whose induced subgraph is disconnected. The statement concerns this single graph and ordinary cut complexes, not total cut complexes and not higher-dimensional hypercubes.

For induced subgraphs with fewer than three vertices, and for induced subgraphs having no disconnected three-set, the corresponding void or empty-face-only complexes are taken to be shellable, matching the conventions in the defining cut-complex literature.

## Proof
The bundled verifier reconstructs \(\Delta_3(Q_3)\) directly from the cube adjacency relation. It obtains 32 facets and 188 nonempty faces with face vector
\[
(8,28,56,64,32).
\]
It then performs the sequential element matching in the vertex order \(0,1,2,3,4,5,6,7\). There are 91 matched face pairs. The oriented Hasse diagram has 640 cover relations and is acyclic after reversing exactly the matched covers. The unmatched faces consist of one vertex, one three-dimensional face, and four four-dimensional faces. Forman's discrete Morse theorem therefore gives a CW complex homotopy equivalent to \(\Delta_3(Q_3)\) with one \(0\)-cell, one \(3\)-cell, and four \(4\)-cells.

An exact rational simplicial-chain computation gives boundary ranks
\[
\operatorname{rank}(\partial_1,\partial_2,\partial_3,\partial_4)=(7,21,35,28),
\]
so the Betti vector is \((1,0,0,1,4)\). In the Morse CW complex the cellular boundary from the four \(4\)-cells to the single \(3\)-cell must therefore have rank zero over \(\mathbb Q\), hence it is the zero integral homomorphism. The attaching map of each \(4\)-cell is a map \(S^3\to S^3\); its cellular degree is zero, so it is null-homotopic because degree classifies \(\pi_3(S^3)\cong\mathbb Z\). This proves
\[
\Delta_3(Q_3)\simeq S^3\vee\bigvee^{4}S^4.
\]

The complex is pure of dimension \(4\). A pure shellable \(4\)-complex is homotopy equivalent to a wedge of \(4\)-spheres, whereas the displayed homotopy type has nonzero third homology, so \(\Delta_3(Q_3)\) is not shellable.

For minimality there are two checks. First, the defining paper proves that a \(3\)-connected graph in which every vertex has a neighbor of degree \(3\) is a minimal forbidden graph for \(3\)-cut shellability whenever its \(3\)-cut complex is nonshellable. The cube is \(3\)-connected and \(3\)-regular. Second, independently of that criterion, the verifier enumerates all 255 proper vertex subsets of \(Q_3\), constructs the corresponding cut complexes, finds a shelling order in every case, and rechecks each order against the shelling definition.

## Verification
Run `python3 verify_cube_cut.py`. The program uses only the Python standard library. It regenerates the graph, all disconnected three-sets, all simplices, the complete Hasse diagram, the element matching, exact rational boundary ranks, vertex-connectivity checks, and shellings for every proper induced subgraph. A successful replay ends with `VERIFY_OK`.

The critical-cell counts are one in dimension \(0\), one in dimension \(3\), and four in dimension \(4\). The rational Betti vector is \((1,0,0,1,4)\). The verification is exhaustive for the stated eight-vertex graph; it is not an extrapolation from random samples.

## Relationship to prior work
Bayer et al. introduced \(k\)-cut complexes, proved that pure shellable complexes are wedges of top-dimensional spheres, and explicitly framed the classification of induced-minimal nonshellable cut complexes as a natural problem. Their Corollary 5.5 supplies the structural minimality criterion used above, and their listed families include prisms over cliques, but their paper contains no cube-graph case or the displayed mixed-dimensional homotopy type.

A later paper on grid graphs treats rectangular \(2\times n\) and \(3\times n\) grids. Those are two-dimensional rectangular grids and do not include the three-dimensional product \(P_2\mathbin{\square}P_2\mathbin{\square}P_2\). The defining paper's general face-lattice theorem also does not force the present result: \(\Delta_3(Q_3)\) does not contain the complete codimension-one skeleton, since it has 64 three-faces rather than \(\binom{8}{4}=70\).

## Limitations
The result is only for the cube graph \(Q_3\). It does not classify all minimal forbidden graphs for \(3\)-cut shellability, does not assert a formula for higher hypercubes, and does not determine integral cup products or simple-homotopy type. Originality is assessed against the inspected primary papers and indexed searches; an unindexed computation under different terminology remains a residual literature risk.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675; DOI 10.1137/23M1569034.
2. H. Chandrakar, N. R. Hazra, D. Rout, A. Singh, *Topology of total cut and cut complexes of grid graphs*, arXiv:2408.07646.
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90--145.
