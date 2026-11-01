# Integral face-torus basis and full tetrahedral symmetry of a two-particle graph configuration space

## Finding
Let \(T\) be the truncated-tetrahedral graph, and let \(X=\operatorname{UConf}_2(|T|)\) be the space of unordered configurations of two distinct particles on its geometric realization. Then
\[
H_k(X;\mathbb Z)\cong\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z^8,&k=1,\\
\mathbb Z^{10},&k=2,\\
0,&k\ge3.
\end{cases}
\]
The ten geometrically embedded product tori from the disjoint pairs of faces of \(T\) form an **integral basis** for \(H_2(X;\mathbb Z)\). These are the six pairs of distinct triangular faces and the four pairs consisting of a triangle and the opposite hexagonal face.

All graph automorphisms arise from permuting the four triangular faces, so \(\operatorname{Aut}(T)\cong S_4\). Let \(V\) be the three-dimensional standard rational representation of \(S_4\), and let \(V'=V\otimes\operatorname{sgn}\). The complete rational symmetry representations are
\[
H_1(X;\mathbb Q)\cong 2\operatorname{sgn}\oplus2V',
\qquad
H_2(X;\mathbb Q)\cong\mathbf1\oplus2V\oplus V'.
\]
On conjugacy classes of cycle type \(1^4,(2,1,1),(2,2),(3,1),(4)\), respectively, the character traces are \((8,-4,0,2,0)\) in degree one and \((10,2,-2,1,0)\) in degree two. In particular the rational Betti vectors of the two natural symmetry quotients are
\[
(\beta_0,\beta_1,\beta_2)(X/S_4)=(1,0,1),
\qquad
(\beta_0,\beta_1,\beta_2)(X/A_4)=(1,2,1).
\]
No statement about their homotopy types or cohomology rings is inferred from these vectors.

## Assumptions and scope
The graph \(T\) has vertex set \(\{(i,j):i,j\in\{0,1,2,3\},\ i\ne j\}\). Two vertices are adjacent exactly when they have the same first coordinate, or they are the reversed pair \((i,j),(j,i)\). Consequently it has 12 vertices and 18 edges. Its four triangular faces are the sets of vertices with fixed first coordinate. Its four hexagonal faces are indexed by the excluded label: for the three remaining labels \(a,b,c\), a boundary orientation follows \((a,b),(b,a),(b,c),(c,b),(c,a),(a,c)\).

The graph is simple, every essential vertex pair is separated by at least one edge, and its shortest noncontractible cycle has three edges. The two-particle sufficient-subdivision theorem therefore identifies the standard finite unordered configuration cubical complex with \(X\), up to homotopy, in a graph-automorphism-compatible way. The finite complex has a 0-cell for each unordered pair of distinct vertices, a 1-cell for each pair consisting of an edge and a nonincident vertex, and a 2-cell for each pair of vertex-disjoint edges.

The claims are about ordinary singular homology, the induced full graph-automorphism representation over \(\mathbb Q\), and the ten specific integral geometric generators. They do not address more particles, Borel–Moore homology or local coefficients.

## Proof
**1. Exact cubical chains.** The three cellular chain groups have ranks \((66,180,117)\). Orient each graph edge from its smaller to larger indexed vertex; orient each square as the product of its two graph edges in ascending edge-index order. The signs in the cellular boundary follow \(\partial(e\times f)=\partial e\times f-e\times\partial f\). The standalone verifier reconstructs all nonzero entries and checks exactly that \(\partial_1\partial_2=0\). The configuration 1-skeleton is connected, giving \(\operatorname{rank}\partial_1=65\), so the integral 1-cycle lattice has rank 115.

**2. Ten embedded face-pair tori.** A triangular or hexagonal facial boundary is an oriented graph cycle. If two faces have disjoint vertex sets, their geometric product lies in the unordered collision-free configuration space and is an embedded two-torus (the two factors are separated by their supporting faces). There are exactly ten such pairs: all six triangle–triangle pairs and exactly four triangle–hexagon pairs, with the hexagon opposite the triangle. Using oriented products of their graph edges, the verifier constructs a \(117\times10\) signed integer matrix \(Z\) whose columns are the ten torus 2-cycles. Direct multiplication gives \(\partial_2Z=0\). Its full Smith diagonal consists of ten units, hence the cycles span a primitive rank-ten sublattice of \(C_2\).

**3. All integral homology.** Independent exact elimination over \(\mathbb F_2\) gives \(\operatorname{rank}_{\mathbb F_2}\partial_2=107\), which is a lower bound for its rational rank. The ten independent integral kernel columns force the rational rank to be at most \(117-10=107\). Thus the exact rational rank is 107 and \(\ker\partial_2\) has rank ten. Since the ten cycles form a primitive sublattice of \(C_2\) contained in the rank-ten kernel, they equal the complete integral kernel: the face tori form an integral basis of \(H_2\), because no 3-cells occur.

Choose a spanning tree in the connected configuration 1-skeleton and use the 115 non-tree edge coordinates as an integral basis for its cycle lattice \(\ker\partial_1\). The matrix of \(\partial_2\) in these coordinates is \(115\times117\). Its exact integer Smith form has 107 nonzero diagonal entries, **all equal to one**. Therefore the quotient \(\ker\partial_1/\operatorname{im}\partial_2\) is free of rank \(115-107=8\), proving the displayed integral homology without a field-to-integers inference.

**4. Full symmetry characters.** Every graph automorphism permutes the four triangles; a vertex in the triangle indexed by \(i\) is distinguished by the index \(j\) of the triangle containing its external neighbor. Thus every automorphism is a simultaneous permutation of both labels, yielding exactly \(S_4\). The verifier enumerates all 24 permutations, checks their signed actions commute with both cellular differentials, and checks that each of the ten face-torus cycles is sent to the signed cycle of the corresponding disjoint-face pair. This gives the degree-two character directly in its integral basis. The cellular Lefschetz identity
\[
1-\operatorname{tr}(g\mid H_1)+\operatorname{tr}(g\mid H_2)
=\operatorname{tr}(g\mid C_0)-\operatorname{tr}(g\mid C_1)+\operatorname{tr}(g\mid C_2)
\]
then computes the degree-one character. For class sizes \((1,6,3,8,6)\), the resulting characters are \((8,-4,0,2,0)\) and \((10,2,-2,1,0)\). Taking exact inner products with the five irreducible rational characters of \(S_4\) gives the stated decompositions. The trivial representation occurs zero times in degree one and once in degree two; for the alternating subgroup it occurs twice in degree one and once in degree two. For a finite group acting cellularly, rational homology of the topological quotient is the invariant rational homology after equivariant subdivision; this yields the two quotient Betti vectors.

## Verification
The standalone `verify.py` requires Python 3 and SymPy and runs with `python3 verify.py`. It constructs the graph, all three cubical cell sets and signed boundaries, checks \(\partial_1\partial_2=0\), enumerates all ten facial product 2-cycles, independently checks their Smith invariant factors and the mod-two boundary rank, computes the integral Smith invariants of the one-cycle boundary image, and tests all 24 graph symmetries on chains and cycles. The exact recorded standard output is in `verifier_output.txt`; its first line is `VERIFY_OK cells=66,180,117 boundaries=(65,107) top_face_tori=10 HZ=(1,8,10) Aut=S4`. In the package, all required computations are reconstructed from the graph specification, rather than relying on previously generated matrices.

## Relationship to prior work
Barnett and Farber's 2009 work develops the intersection theory of **ordered** two-particle graph configurations, including planar graphs; Farber and Hanbury continue that ordered theory. Prue and Scrimshaw provide the sufficient-subdivision result validating the finite cubical model. These foundations make the two-point construction natural, but the inspected statements do not specify the ten integral generators or full \(S_4\)-module for the unordered truncated-tetrahedral graph.

A published calculation of the cuboctahedral two-particle configuration gives a different automorphism group action and different integral ranks for a different graph, while an analogous dodecahedral two-point calculation concerns a different graph and \(A_5\times C_2\) modules. A general exchange-sign Borel–Moore calculation addresses a different homology theory. Results on the truncated-tetrahedral matching, cut, Rips and Čech complexes do not imply ordinary two-particle configuration homology. Equivalent graph descriptions, general results, exact-object publications and the closest mathematical research records were checked; no directly covering statement was identified. The literature comparison cannot certify absolute novelty.

## Limitations
The result is specific to two unordered particles on the truncated-tetrahedral graph. No integral decomposition into representation lattices, quotient homotopy equivalence, cohomology-ring presentation or general classification across Archimedean graphs is asserted. Some broader results on planar two-point configuration homology may imply nonequivariant ranks without providing the explicit integral geometric basis or symmetry character. An unindexed equivalent published character calculation remains a residual priority risk. The finite code proves the stated finite-rank and character calculations but does not independently certify publication priority.

## References
1. Kathryn Barnett and Michael Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180v1 (first public March 12, 2009), https://arxiv.org/abs/0903.2180.
2. Paul Prue and Travis Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511v1 (September 30, 2009), https://arxiv.org/abs/0909.5511.
3. Michael Farber and Elizabeth Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300v1 (first public May 13, 2010), https://arxiv.org/abs/1005.2300.
4. Adam Sawicki and Tomasz Maciążek, *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics (2019), DOI:10.1007/s00220-019-03583-5.
