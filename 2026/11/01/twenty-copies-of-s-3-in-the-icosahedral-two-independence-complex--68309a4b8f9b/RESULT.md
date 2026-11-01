# Twenty copies of \(S^3\) in the icosahedral two-independence complex, with full symmetry

## Finding
Let \(I\) be the one-skeleton of the regular icosahedron and let \(X=\operatorname{Ind}_2(I)\) contain every vertex subset whose induced graph has connected components of order at most two. There is an integral homotopy equivalence
\[
X\simeq\bigvee^{20}S^3.
\]
The graph automorphism group is \(G\cong A_5\times C_2\). Let \(V_4\) and \(V_5\) denote the four- and five-dimensional rational irreducible representations of \(A_5\), and let \(\varepsilon\) be the nontrivial character of the central inversion group \(C_2\). The complete rational representation is
\[
\widetilde H_3(X;\mathbb Q)\cong
(\mathbf1\oplus V_4\oplus 2V_5)\boxtimes\mathbf1
\ \oplus\ V_5\boxtimes\varepsilon.
\]
All other reduced integral homology groups vanish. The central-inversion eigenspaces have ranks \(15\) and \(5\) over \(\mathbb Q\). In particular the full-group invariant subspace has dimension one, and the ordinary orbit space has rational reduced homology
\[
\widetilde H_j(X/G;\mathbb Q)\cong
\begin{cases}\mathbb Q,&j=3,\\0,&j\ne3.\end{cases}
\]
No integral equivariant homotopy equivalence is asserted.

## Assumptions and scope
All graphs are finite, simple and undirected. The graph \(I\) has twelve vertices and thirty edges. For a reproducible labeling, its vertices are numbered \(0,\ldots,11\), and the full edge list is the constant `EDGES` in `verify_icosahedral_dissociation.py`; that constant determines the graph without external data. Its degree is five at each vertex, it has twenty triangular faces, and its neighbors at each vertex induce a five-cycle. We use the convention that an induced component of size at most two is equivalent to an induced maximum degree at most one. The central involution exchanges each vertex with its graph-distance-three antipode. The action on chains uses increasing vertex order for orientations.

For the representation statement, the familiar order-\(60\) rotational subgroup is \(A_5\); adjoining antipodal inversion gives the full order-\(120\) automorphism group. The five rotational conjugacy classes are ordered by sizes \((1,15,20,12,12)\), with element orders \((1,2,3,5,5)\).

## Proof
A triple of vertices is forbidden precisely when one vertex is adjacent to the other two. There are exactly eighty distinct forbidden triples: the twelve five-valent centers produce \(12\binom{5}{2}=120\) counted triples, of which the twenty triangular triples were each counted three rather than once. Exhaustive enumeration of all \(2^{12}\) masks, independently checking both forbidden triples and induced maximum degree, gives exactly \(323\) nonempty faces and the dimension-indexed face vector
\[
(f_0,f_1,f_2,f_3)=(12,66,140,105).
\]
There are no higher-dimensional faces.

Construct a partial matching on nonempty faces by examining vertices in increasing order. At stage \(i\), pair each remaining face \(\sigma\) not containing \(i\) with \(\sigma\cup\{i\}\) whenever both still remain, then delete both. This yields \(149\) matched covering pairs and critical cells in dimensions \(0,1,2,3\) numbering \((1,0,2,22)\). An explicit topological sort of the full face-poset Hasse diagram with matched arrows reversed visits all \(323\) vertices and all \(972\) covering incidences. It establishes acyclicity, so Forman's discrete Morse theorem supplies a CW model with one zero-cell, two two-cells and twenty-two three-cells, with no cells in dimension one or above three.

For an exact attaching-map computation, orient simplices using increasing labels. Let \(\partial[u_0,\ldots,u_d]=\sum_j(-1)^j[u_0,\ldots,\widehat u_j,\ldots,u_d]\). For each matched pair \((\sigma,\tau)\) with \(\dim\sigma=2\) and \(\dim\tau=3\), eliminate the coefficient of \(\sigma\) in the boundary of any three-cell using the integral pivot \(\langle\partial\tau,\sigma\rangle=\pm1\). Since the matching is acyclic this elimination terminates and computes the signed integral Morse differential. With critical three-cells ordered by increasing bitmask, its twenty-two columns are
\[
\begin{split}
&(0,0),(0,0),(0,0),(-1,0),(1,0),(0,0),(-1,0),(0,0),\\
&(1,0),(0,0),(0,0),(0,-1),(-1,-1),(-1,0),(0,1),(0,1),\\
&(0,0),(0,1),(0,0),(0,-1),(0,0),(0,0).
\end{split}
\]
The columns with zero-based indices \(3\) and \(11\) have determinant \(+1\), proving that the integral Morse differential has Smith diagonal \((1,1)\) and kernel rank twenty. This also proves more than homology. The two-skeleton of the Morse model is \(S^2\vee S^2\), and attaching maps of its three-cells lie in \(\pi_2(S^2\vee S^2)\cong\mathbb Z^2\) via Hurewicz. Unimodular row and column operations correspond to homotopy equivalences among these attaching maps. The Smith diagonal \((1,1)\) cancels the two two-cells with two three-cells, leaving twenty freely attached three-cells. Hence \(X\simeq\bigvee^{20}S^3\) integrally.

For an automorphism \(g\), let \(\operatorname{sgn}(g|_\sigma)\) be the orientation sign if it preserves a simplex \(\sigma\) setwise, and zero otherwise. Because only reduced degree-three homology survives, the signed simplicial Lefschetz formula gives the exact character
\[
\chi(g)=1-\sum_{\varnothing\ne\sigma\in X}
(-1)^{\dim\sigma}\operatorname{sgn}(g|_\sigma).
\]
The two explicit edge-preserving permutations in the verifier generate \(120\) distinct automorphisms. This is the full group: an automorphism is determined by an image of a chosen vertex, an image of one of its five neighbors and an orientation of the induced pentagonal neighbor cycle, yielding the upper bound \(12\cdot5\cdot2=120\). Direct group multiplication identifies the order-\(60\) commutator subgroup and the central inversion.

On the five rotational classes, the characters of the central-even and central-odd rational homology subspaces are respectively
\[
(15,3,0,0,0),\qquad(5,1,-1,0,0).
\]
Their inner products with the irreducible character table of \(A_5\) give multiplicities, in the order of dimensions \(1,3,3',4,5\), of
\[
(1,0,0,1,2),\qquad(0,0,0,0,1).
\]
Thus the displayed full-group representation follows. Averaging the trace over the group gives \(\dim \widetilde H_3(X;\mathbb Q)^G=1\). Rational homology of a finite group orbit space is the invariant rational homology (equivalently, apply the cellular chain invariants after barycentric subdivision), giving the quotient assertion.

## Verification
`verify_icosahedral_dissociation.py` uses only Python's standard library and reproduces every finite statement above from the thirty explicit edges. It checks all \(4096\) subsets by two predicates, the complete \(972\)-arc matching acyclicity certificate, the full signed integer Morse differential and a determinant-one minor, three independent field-boundary-rank calculations, the complete order-\(120\) automorphism group generated by two listed permutations, conjugacy invariance of its signed Lefschetz character and exact rational character multiplicities. `verification_output.txt` is the saved standard output; a fresh execution has been compared with it byte-for-byte. The three field checks independently give reduced Betti ranks \((0,0,0,20)\) in degrees zero through three. They are corroboration, not the integral homotopy proof.

## Relationship to prior work
Conant and Thistlethwaite (arXiv:0808.0739; first public version August 5, 2008) treat the hypergraph independence complex and its Alexander dual. For the present graph, the forbidden length-two vertex triples define an eighty-hyperedge hypergraph, so this is an instance of that framework. Their inspected definitions, examples and graph-complex discussion do not compute this particular icosahedral object or its representation.

Deshpande and Singh (arXiv:2001.05448; first version January 15, 2020) define general higher-independence complexes and classify complete multipartite, fully whiskered, path, cycle and perfect rooted-tree families. These classes do not include the icosahedral graph. Published calculations of the icosahedral ordinary independence complex, matching complex, open-neighborhood complex and three-cut complex use different face conditions. Their homotopy types or homology characters do not imply the present classification. Searches under “two-independence,” “dissociation,” “forbidden triple” and “icosahedral graph” found no direct covering result; absence of a search hit is not a proof of historical novelty.

## Limitations
The theorem applies to one specified graph and higher-independence parameter two. The full rational symmetry character is determined, but not the integral symmetry-module isomorphism class or equivariant homotopy type. The orbit-space conclusion is rational only; no assertion is made about integral quotient torsion or contractibility. Priority remains subject to independent full-literature examination, including unindexed sources.

## References
1. J. Conant and O. Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739 (initial public posting 2008-08-05), https://arxiv.org/abs/0808.0739 .
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (initial public posting 2020-01-15), https://arxiv.org/abs/2001.05448 .
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
4. J.-P. Serre, *Linear Representations of Finite Groups*, Springer, for finite-group rational character theory.
