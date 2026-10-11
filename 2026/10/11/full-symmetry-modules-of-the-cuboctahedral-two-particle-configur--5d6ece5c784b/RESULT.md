# Full symmetry modules of the cuboctahedral two-particle configuration space

## Finding
Let \(C=L(Q_3)\) be the cuboctahedral graph and \(X=\operatorname{UConf}_2(C)\). The integral homology is
\[
H_0(X;\mathbb Z)\cong\mathbb Z,\qquad H_1(X;\mathbb Z)\cong\mathbb Z^{14},\qquad H_2(X;\mathbb Z)\cong\mathbb Z^{43},
\]
and \(H_i(X;\mathbb Z)=0\) for \(i>2\).

Write \(\operatorname{Aut}(C)\cong S_4\times C_2\), with \(S_4\) acting on the four body diagonals of the cube and the central \(C_2\) distinguishing rotations from orientation-reversing cube symmetries. Let \(V\) be the standard \(3\)-dimensional \(S_4\)-module, \(V'=V\otimes\operatorname{sgn}\), and \(W\) the \(2\)-dimensional irreducible of type \((2,2)\). Superscripts \(+\) and \(-\) denote the trivial and sign characters of the central \(C_2\). Then
\[
H_1(X;\mathbb Q)\cong \operatorname{sgn}^{+}\oplus2(V')^{+}\oplus2\mathbf1^{-}\oplus V^{-}\oplus W^{-},
\]
and
\[
H_2(X;\mathbb Q)\cong \mathbf1^{+}\oplus3V^{+}\oplus2(V')^{+}\oplus W^{+}\oplus2\operatorname{sgn}^{-}\oplus2V^{-}\oplus5(V')^{-}\oplus W^{-}.
\]

## Assumptions and scope
The graph \(C\) is the simple \(12\)-vertex, \(24\)-edge line graph of the cube. For two particles, the standard sufficient-subdivision criterion for Abrams' discrete configuration model requires at least one edge between distinct essential vertices and at least three edges in every non-nullhomotopic loop. Both conditions hold for this simple graph, whose shortest cycles have length \(3\). Thus the discrete unordered configuration cube complex computes the topology of \(X\).

The representation statement concerns the full graph automorphism group. The \(48\) cube symmetries induce \(48\) automorphisms of \(L(Q_3)\); the cuboctahedral graph has automorphism group of order \(48\), so these exhaust \(\operatorname{Aut}(C)\).

## Proof
The unordered discrete two-particle model has one \(0\)-cell for every unordered pair of distinct vertices, one \(1\)-cell for every pair consisting of a graph edge and a nonincident vertex, and one \(2\)-cell for every unordered pair of disjoint graph edges. Hence its cell counts are
\[
(c_0,c_1,c_2)=(66,240,204).
\]

Orient every graph edge by increasing vertex label. The cellular boundary of a \(1\)-cell is the difference of its endpoint configurations, while the boundary of a \(2\)-cell is the signed product boundary. The verifier checks \(\partial_1\partial_2=0\) on all \(204\) two-cells.

The configuration \(1\)-skeleton is connected, so \(\operatorname{rank}\partial_1=65\) and its integral cycle lattice has rank \(240-65=175\). A spanning tree identifies this cycle lattice integrally with the coordinates on the \(175\) non-tree edges. In these coordinates the certificate gives a \(161\times161\) minor of \(\partial_2\) with determinant \(1\). It also gives \(43\) integral vectors in \(\ker\partial_2\) whose selected \(43\times43\) coordinate block is unimodular. Therefore \(\operatorname{rank}\partial_2=161\). The unit maximal minor shows that \(\operatorname{im}\partial_2\) is primitive in the cycle lattice, so
\[
H_1(X;\mathbb Z)\cong\mathbb Z^{175-161}=\mathbb Z^{14}.
\]
Since \(C_3=0\), \(\ker\partial_2\) is free of rank \(204-161=43\), giving \(H_2(X;\mathbb Z)\cong\mathbb Z^{43}\).

For equivariance, enumerate the cube automorphisms as signed coordinate permutations \(C_2^3\rtimes S_3\). Their induced signed permutation actions on \(C_1\) and \(C_2\) commute with the boundary maps. The action on the four cube body diagonals gives the \(S_4\)-factor, and the determinant of the signed permutation gives the central \(C_2\)-character. The certificate's integral kernel basis has a unimodular \(43\times43\) coordinate block, so every automorphism acts on \(H_2\) by an exactly reconstructed integer matrix. The \(H_1\)-trace is then obtained from the cellular Lefschetz identity.

For \(S_4\)-cycle types \(1^4,(2,1,1),(2,2),(3,1),(4)\), the traces on \(H_1\) for central signs \(+,-\) are respectively
\[
(14,0),\ (0,-6),\ (2,-4),\ (2,0),\ (2,0),
\]
and the traces on \(H_2\) are
\[
(43,-7),\ (-3,7),\ (-5,1),\ (1,-1),\ (1,-1).
\]
Taking inner products with the ordinary \(S_4\) character table separately in the central \(+\) and \(-\) sectors gives exactly the two decompositions stated above.

## Verification
Run `python3 verify.py` beside `certificate.json`. The verifier reconstructs the cuboctahedral graph as \(L(Q_3)\), rebuilds all cells and signed boundary maps, checks the chain condition, verifies the determinant-\(1\) maximal minor and the \(43\)-vector kernel certificate, enumerates all \(48\) cube symmetries, checks every homology character value, independently recovers the \(H_2\) character from the \(43\) disjoint planar face pairs, and recomputes the irreducible multiplicities. Its terminal success line is `VERIFY_OK cells=66,240,204 H=(1,14,43) Aut=48 characters_decomposition_facecheck=OK`.

## Relationship to prior work
Agarwal–Banks–Gadish–Miyata define unordered graph configuration spaces and emphasize naturality with respect to graph embeddings and automorphisms; their paper has primary MSC \(55R80\) and was first public on 2020-05-27. Their general functorial results ensure that the symmetry action considered here is mathematically natural, but they do not give the cuboctahedral character calculation.

An–Drummond-Cole–Knudsen develop cellular chain models for graph configuration spaces and functoriality. Barnett–Farber give a general description of rational cohomology for ordered two-particle configuration spaces of planar graphs; this substantially explains why the nonequivariant Betti numbers of a planar example are accessible. Neither inspected source states the full \(\operatorname{Aut}(C)\cong S_4\times C_2\) decomposition above. Exact-object, line-graph, character, and representation searches likewise found no cuboctahedral two-particle homology-module result.

## Limitations
This is an exact calculation for two unordered particles on one graph. It does not classify the corresponding modules for all Archimedean graphs, does not compute the integral representation lattice beyond the free abelian homology groups, and does not determine the cohomology ring. The literature search cannot prove absolute novelty; a specialized unindexed computation could still exist.

## References
1. S. Agarwal, M. Banks, N. Gadish, D. Miyata, *Deletion and contraction in configuration spaces of graphs*, arXiv:2005.13666.
2. B. H. An, G. C. Drummond-Cole, B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351.
3. K. Barnett, M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180.
4. P. Prue, T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511.
