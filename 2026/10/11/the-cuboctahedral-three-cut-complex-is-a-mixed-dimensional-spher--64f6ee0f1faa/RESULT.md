# The cuboctahedral three-cut complex is a mixed-dimensional sphere wedge

## Finding

Let \(Q_3\) be the cube graph, let \(C=L(Q_3)\) be its line graph (the cuboctahedral graph), and let \(\Delta_3(C)\) be its ordinary three-cut complex. Then
\[
\Delta_3(C)\simeq S^7\vee\bigvee^{6}S^8.
\]
Consequently its integral reduced homology is \(\mathbb Z\) in dimension \(7\), \(\mathbb Z^6\) in dimension \(8\), and zero elsewhere. The complex is pure of dimension \(8\), and hence its nonzero lower-dimensional homology rules out shellability.

The exact face vector, in dimensions \(0,\dots,8\), is
\[
(12,66,220,495,792,924,792,489,164).
\]
In particular, \(\Delta_3(C)\) contains all \(7\)-vertex subsets as faces but is missing six \(8\)-vertex subsets. Its \(7\)-skeleton is therefore not complete, so the full-skeleton hypothesis in Theorem 6.1 of Bayer et al. does not apply; nevertheless the integral homology is torsion-free and occurs in two adjacent dimensions.

## Assumptions and scope

All graphs are finite, undirected, and simple. Represent vertices of \(Q_3\) by the integers \(0,\ldots,7\) with binary representations of length three. Two cube vertices are adjacent exactly when they differ in one bit. Order its twelve edges lexicographically, identify these edges with the vertices \(0,\ldots,11\) of \(C\), and join two vertices of \(C\) when the corresponding cube edges share an endpoint.

For a graph \(G\) with vertex set \(V\), the ordinary three-cut complex \(\Delta_3(G)\) has facets \(V\setminus T\) for every three-element subset \(T\) whose induced graph \(G[T]\) is disconnected. This is not the total three-cut complex, which instead uses independent triples. For a three-element set, disconnectedness means that its induced graph has at most one edge.

## Proof

The twelve edges of the binary cube yield a simple four-regular, twenty-four-edge line graph. Enumerating its \(\binom{12}{3}=220\) vertex triples by the disconnectedness criterion finds exactly \(164\) disconnected triples and hence \(164\) distinct nine-vertex facets. Enumerating all nonempty subsets of those facets produces the face vector above and \(3954\) nonempty simplices, with \(23208\) covering relations in the face poset.

For each vertex \(v=0,\ldots,11\) in order, on the faces not matched at earlier stages, pair every currently available face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both are present. This is a partial matching on the nonempty face poset. Its \(1968\) pairs leave exactly eighteen critical faces: one in dimension \(0\), six in dimension \(7\), and eleven in dimension \(8\). To certify acyclicity rather than infer it from counts, direct every matched Hasse edge upward and every other Hasse edge downward. Topological sorting visits all \(3954\) vertices of this directed graph. Thus the discrete-Morse matching is acyclic and yields a CW model with precisely these critical cells.

Using the indicated vertex order to orient simplices, eliminate every matched lower face by the signed boundary of its paired upper face. Exact recursive substitution along the acyclic matching gives the following integral boundary matrix from the eleven critical \(8\)-cells to the six critical \(7\)-cells, with each row and column ordered lexicographically by its vertex tuple:
\[
\begin{pmatrix}
0&-1&0&0&0&1&1&0&0&0&0\\
0&1&0&1&0&0&0&0&0&0&0\\
0&0&0&0&0&1&0&0&1&0&0\\
0&0&0&1&0&0&0&0&-1&0&1\\
0&0&0&0&0&0&-1&0&0&0&0\\
0&0&0&0&0&0&0&0&0&0&1
\end{pmatrix}.
\]
It has rank \(5\) over \(\mathbb Q\). Its \(5\)-by-\(5\) minor using zero-indexed rows \((0,1,2,3,4)\) and columns \((1,3,5,6,10)\) has determinant \(-1\), so every nonzero integral Smith factor is a unit. Therefore the Morse chain complex has integral homology \(H_7\cong\mathbb Z\) and \(H_8\cong\mathbb Z^6\), without torsion; no other positive-degree homology occurs.

The Morse CW model has one vertex and no cells in dimensions \(1\) through \(6\). Its \(7\)-skeleton is a wedge of six copies of \(S^7\). The homotopy classes of attaching maps of its \(8\)-cells lie in \(\pi_7(\bigvee^6 S^7)\cong\mathbb Z^6\), where they are completely determined by their degree vectors. Integral changes of basis in the \(7\)- and \(8\)-cells reduce the primitive rank-five degree matrix to five identity entries and zeros. The corresponding unit-degree cell pairs cancel, leaving one \(7\)-sphere and six \(8\)-spheres. This proves the asserted homotopy equivalence, not merely a homology calculation.

A pure shellable \(8\)-complex has reduced homology concentrated in degree \(8\). Since \(H_7\ne0\), this complex is not shellable.

## Verification

Run `python3 verify.py` with a standard Python 3.10-or-newer installation. The checker reconstructs the cube, cuboctahedral graph, facets and full face poset from their definitions; verifies all Hasse-cover orientations and acyclicity; constructs the full integral Morse boundary by signed elimination; verifies rank \(5\) and the unit minor; and independently computes all simplicial boundary ranks over \(\mathbb F_2\).

The eight mod-two boundary ranks in dimensions \(1\) through \(8\) are \((11,55,165,330,462,462,330,158)\), giving positive-degree Betti ranks \((0,0,0,0,0,0,1,6)\). This is a secondary check on the integral computation, not a replacement for it.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue introduced the ordinary cut complex and studied homotopy types for trees, cycles, complete multipartite graphs, squared cycles, and prisms over cliques [1]. Their Theorem 6.1 gives torsion-freeness and a two-degree homology constraint under a complete next-to-top skeleton hypothesis. The cuboctahedral complex here has only \(489\) of the \(495\) possible \(7\)-faces, so it does not satisfy that hypothesis. The theorem does not provide the two Betti ranks or a homotopy equivalence for this graph.

Chandrakar, Hazra, Rout, and Singh treated total cut complexes and ordinary cut complexes of rectangular grid graphs [2]. The cuboctahedral graph has degree four at all twelve vertices and is not a rectangular grid, so their grid theorems do not apply. The cube graph and its line graph are different graphs, and cut-complex homology is not preserved by taking a line graph.

## Limitations

The assertion concerns exactly the twelve-vertex cuboctahedral graph and the ordinary three-cut construction. No generalization to line graphs of larger hypercubes is proved, and no equivariant homology representation is asserted. The arithmetic and acyclic matching are finite and exhaustively checked by the included reproducible code. Independent review has not been performed.

## References

[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public 2023-04-26), https://arxiv.org/abs/2304.13675.

[2] H. Chandrakar, N. R. Hazra, D. Rout, and A. Singh, *Topology of total cut and cut complexes of grid graphs*, arXiv:2408.07646 (first public 2024-08-14), https://arxiv.org/abs/2408.07646.
