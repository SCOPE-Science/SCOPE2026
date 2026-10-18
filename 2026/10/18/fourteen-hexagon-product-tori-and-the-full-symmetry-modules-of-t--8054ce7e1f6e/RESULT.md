# Fourteen hexagon-product tori and the full symmetry modules of the Heawood two-particle configuration space

## Finding
Let \(H\) be the point–line incidence graph of the Fano plane, and let \(X=\operatorname{UConf}_2(|H|)\) denote its collision-free space of **unordered** pairs of points, including points in edge interiors. Then \(H_2(X;\mathbb Z)\) has an explicit integral basis consisting of the fundamental classes of **fourteen embedded product tori** \(C\times C'\), where \(C,C'\) are vertex-disjoint hexagons of \(H\). The full group \(G=\operatorname{Aut}(H)\), of order \(336\), acts on rational positive-dimensional homology by
\[
H_1(X;\mathbb Q)\cong U_8,\qquad H_2(X;\mathbb Q)\cong U_8\oplus W_6,
\]
where \(U_8\cong H_1(H;\mathbb Q)\) and \(W_6\) are distinct absolutely irreducible rational \(G\)-representations of dimensions eight and six. These are determined by the complete character table given below. The integral groups are
\[
H_0(X;\mathbb Z)\cong\mathbb Z,\qquad H_1(X;\mathbb Z)\cong\mathbb Z^8\oplus\mathbb Z/2,\qquad H_2(X;\mathbb Z)\cong\mathbb Z^{14},
\]
and higher homology vanishes. The first-homology group and the ranks alone also follow from general published graph-braid results and Euler characteristic; **the contribution here is the complete integral geometric basis and the full symmetry decomposition**.

The columns below give \((\mathrm{ord}(g),\text{point–line exchange},\#g,\chi_{U_8}(g),\chi_{H_2}(g),\chi_{W_6}(g))\):

| Order | Exchanges points and lines | Number | \(U_8\) | \(H_2\) | \(W_6\) |
|---:|:---:|---:|---:|---:|---:|
| 1 | no | 1 | 8 | 14 | 6 |
| 2 | no | 21 | 0 | -2 | -2 |
| 2 | yes | 28 | -2 | -2 | 0 |
| 3 | no | 56 | -1 | -1 | 0 |
| 4 | no | 42 | 0 | 2 | 2 |
| 6 | yes | 56 | 1 | 1 | 0 |
| 7 | no | 48 | 1 | 0 | -1 |
| 8 | yes | 84 | 0 | 0 | 0 |

## Assumptions and scope
All chain groups are over \(\mathbb Z\) unless coefficients are explicitly specified. Label the seven points by \(0,\ldots,6\) and the seven lines by \(7+j\), \(0\le j<7\); put an edge between point \(p\) and line \(7+j\) exactly when \((p-j)\bmod7\in\{0,1,3\}\). The graph has fourteen vertices, twenty-one edges, and girth six. Give each edge the orientation from its smaller to its larger endpoint. Fix the lexicographic orders of edges and cells described in `verify.py`. All finite calculations are for this one canonical graph, not a family of arbitrary incidence graphs.

The unordered cubical deleted-product model \(D(H,2)/\mathfrak S_2\) is homotopy equivalent to \(X\). Its cells are unordered pairs of distinct vertices; an edge with a nonincident vertex; and unordered pairs of disjoint edges. They give \((91,252,168)\) cells in dimensions \((0,1,2)\), respectively. This equivalence follows from the equivariant strong deformation retract in Barnett–Farber, Lemma 1.1 [1], followed by the free particle-swap quotient; the inclusion is invariant under graph automorphisms. Thus the computed cellular character is the geometric \(G\)-character.

## Proof
**Integral homology and the torus basis.** Write \(e_i=(a,b)\) and \(e_j=(c,d)\) for increasing endpoints and \(i<j\). With \([e_i,w]\) denoting the oriented cell with one point on \(e_i\) and the other at \(w\), the integral cellular differentials are
\[
\partial_1[e_i,w]=[b,w]-[a,w],\qquad
\partial_2[e_i,e_j]=[e_j,b]-[e_j,a]-[e_i,d]+[e_i,c].
\]
The one-skeleton is connected. Choose the deterministic spanning tree obtained by processing the \(252\) one-cells in lexicographic order and joining previously disconnected zero-cell components. This selects \(90\) tree edges. Projection onto the \(162\) non-tree one-cell coordinates gives an integral basis for \(\ker\partial_1\). The resulting integral matrix \(B\), representing \(\partial_2\) in this basis, has size \(162\times168\) and \(430\) nonzero entries.

`CERTIFICATE.json` gives a specified \(154\times154\) minor of \(B\) with determinant \(+2\). Hence \(\operatorname{rank}_{\mathbb Q}B\ge154\) and the product of its nonzero Smith invariant factors divides two. Exact binary Gaussian elimination gives \(\operatorname{rank}_{\mathbb F_2}B=153\). The fourteen oriented disjoint-hexagon products described next lie in \(\ker B\) and have an integral \(14\times14\) coordinate minor with determinant \(+1\). Thus they are independent, so \(\operatorname{rank}_{\mathbb Q}B\le168-14=154\). Consequently \(\operatorname{rank}_{\mathbb Q}B=154\), and the Smith invariants are exactly \(153\) units and one factor of two. As the complex is two-dimensional, \(H_2=\ker\partial_2\) is free of rank fourteen; the first homology has free rank \(162-154=8\) and one element of order two.

For the geometric basis, an ordered six-cycle \(C=(v_0,\ldots,v_5)\) determines the oriented integral one-cycle formed by successive graph edges. If \(C\) and \(C'\) are vertex-disjoint, their product defines an embedded torus in \(X\), with two-chain the signed cross product of their edge cycles. The fourteen specific cycle pairs are enumerated as `torus_cycles` in `CERTIFICATE.json`. The verifier checks adjacency, vertex disjointness, \(\partial_2 z=0\) for every product, and a \(+1\) determinant for the selected fourteen rows of their coefficient matrix. Because \(\ker\partial_2\) has rank fourteen, this unit minor proves that **every integral two-cycle** is a unique integral combination of these fourteen torus classes: subtract the integral combination with the same selected coordinates, and the remainder must vanish by injectivity of the selected-coordinate map on the rational kernel. The basis is therefore complete and primitive, not merely rationally independent.

**Homology representations.** The map from the unordered configuration to the symmetric square of the graph induces the sum-of-particle-locations chain map. It sends \([e,w]\) to the edge \(e\) and sends \([e_i,e_j]\) to zero, while \([u,v]\) maps to \(u+v\). Every elementary oriented hexagon of \(H\) can be traced in \(X\) while parking the other point outside that hexagon; eight hexagons span the rank-eight graph cycle space. Thus the induced map \(H_1(X;\mathbb Q)\to H_1(H;\mathbb Q)\) is onto and, by equal dimensions, is an equivariant isomorphism. For any automorphism \(g\), its degree-one character is therefore
\[
\chi_1(g)=\operatorname{tr}(g\mid C_1(H;\mathbb Q))-\operatorname{tr}(g\mid C_0(H;\mathbb Q))+1.
\]
Here edge traces include orientation signs. The Lefschetz formula for the two-dimensional unordered deleted-product complex gives
\[
\chi_2(g)=\operatorname{tr}(g\mid C_0(X))
-\operatorname{tr}(g\mid C_1(X))
+\operatorname{tr}(g\mid C_2(X))-1+\chi_1(g).
\]
All fixed-cell traces are signed: exchanging the two edges of a two-cell reverses its product orientation. This yields the displayed character table.

All \(336\) automorphisms are generated without an external group table: enumerate the \(168\) permutations of the Fano points preserving the seven line triples, extending each uniquely to the seven lines, and compose each with the point–line polarity \(p\mapsto7+(-p\bmod7)\), \(7+j\mapsto(-j\bmod7)\). The graph's connected bipartition ensures every automorphism is in one of these two sets. For \(\chi_8=\chi_1\) and \(\chi_6=\chi_2-\chi_1\), direct character sums give
\[
\sum_{g\in G}\chi_8(g)^2=336,\quad
\sum_{g\in G}\chi_6(g)^2=336,\quad
\sum_{g\in G}\chi_8(g)\chi_6(g)=0.
\]
Thus \(U_8\) is absolutely irreducible. Semisimplicity and the displayed orthogonality show that the six-dimensional complementary constituent \(W_6\) of \(H_2\) is also absolutely irreducible. Neither positive-dimensional rational homology group has a nonzero \(G\)-fixed vector.

## Verification
Run `python verify.py` alongside `CERTIFICATE.json` with Python 3, NumPy and SymPy. The verifier reconstructs the entire graph and the \((91,252,168)\) boundary matrices; checks \(\partial_1\partial_2=0\); constructs the canonical spanning tree; checks the exact \(+2\) boundary determinant, mod-two rank \(153\), fourteen product cycles and their determinant \(+1\); and recomputes signed characters for every one of the \(336\) automorphisms. The expected eight character rows are embedded in the certificate and are compared exhaustively. The exact determinant, rank, torus, and character assertions were reproduced from these files. The three integral ranks are established by the exact certificate, not by finite sampling of a conjectured infinite family.

## Relationship to prior work
Barnett–Farber [1] provides the ordered deleted-product model and equivariant deformation retract and develops intersection methods, principally for planar graphs. Ko–Park [2], Theorem 3.16, already gives the first-homology structure for the triconnected nonplanar graph; its theorem plus Euler characteristic also implies the present Betti ranks. These **are not claimed as new**. Lawrence–Wilson [3] establishes that there are \(42\) pairs of disjoint hexagons and that the automorphism group is transitive on them, but does not determine which hexagon-product tori span top configuration homology, their integral lattice, or the homology representations. Related published computations on **ordered** Heawood two-particle spaces concern mod-two ranks rather than the unordered integral torus basis and the full automorphism character. Computations for the Heawood matching or independence complexes concern different topological objects, while two-particle representation calculations for the Petersen and dodecahedral graphs concern different graph spaces. These distinctions use implications, not just title differences.

## Limitations
The result concerns the unordered **two-particle** space of the original (unsplit) fourteen-vertex Heawood graph. It does not determine the fundamental group, integral \(G\)-module splitting, cup-product ring, ordered-space \(G\)-representations, or spaces of three or more particles. The discovered geometric torus basis is not claimed \(G\)-stable as a set. The character proof uses rational semisimplicity and does not imply that the integral rank-fourteen lattice splits as two integral summands. Potential coverage by unindexed literature remains a bibliographic risk.

## References
[1] K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180v1 (first publicly posted 12 March 2009), especially Lemma 1.1 and Sections 1–2. https://arxiv.org/pdf/0903.2180

[2] K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648v1 (2011), especially Lemma 3.15 and Theorem 3.16. https://arxiv.org/pdf/1101.2648

[3] E. D. Lawrence and R. T. Wilson, *The Structure of the Heawood Graph*, arXiv:1907.11978v1 (2019), Proposition 2 and Theorem 3. https://arxiv.org/pdf/1907.11978

[4] M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300 (2010). https://arxiv.org/pdf/1005.2300
