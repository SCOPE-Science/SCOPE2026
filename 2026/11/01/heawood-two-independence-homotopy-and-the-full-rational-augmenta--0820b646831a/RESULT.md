# Heawood two-independence homotopy and the full rational augmentation character

## Finding
Let \(H\) be the point–line incidence graph of the Fano projective plane. Label its point vertices by \(p_i\) and line vertices by \(\ell_j\), with indices in \(\mathbb Z/7\mathbb Z\), and put an edge \(p_i\ell_j\) precisely when \(i-j\in\{0,1,3\}\). Define \(X=\operatorname{Ind}_2(H)\) to have as its simplices exactly those vertex subsets whose induced graph components each have at most two vertices.

The **integral homotopy type** is
\[
X\simeq\bigvee^{13}S^5.
\]
Writing \(G=\operatorname{Aut}(H)\), the natural rational top-homology representation is the vertex-permutation augmentation module:
\[
\widetilde H_5(X;\mathbb Q)\cong_G
\ker\bigl(\mathbb Q^{V(H)}\xrightarrow{\sum}\mathbb Q\bigr),
\qquad |G|=336.
\]
All other reduced integral homology groups vanish, and \(\widetilde H_5(X;\mathbb Z)\cong\mathbb Z^{13}\). In particular, for the full action and its index-two point/line-preserving subgroup \(G^+\),
\[
\widetilde H_i(|X|/G;\mathbb Q)=0\quad(i\geq0),\qquad
\widetilde H_i(|X|/G^+;\mathbb Q)=
\begin{cases}\mathbb Q,&i=5,\\0,&i\ne5.\end{cases}
\]
The quotient statements are rational homology results, not assertions of contractibility or of integral quotient homology.

## Assumptions and scope
The graph is finite, simple, undirected, bipartite, and uses the seven distinct Fano lines \(L_j=\{j,j+1,j+3\}\) modulo seven. It has fourteen vertices, twenty-one edges, and girth six. A vertex subset lies in \(X\) if every vertex in it has at most one *selected* neighbor; this is equivalent, for any simple graph, to each component having at most two vertices. The automorphism action on simplices is induced by permuting graph vertices. All statements concern this one canonical graph and the first higher-independence parameter \(r=2\); no generalization to arbitrary incidence geometries is asserted.

## Proof
**Step 1: exhaustive face description.** For every integer bitmask \(m\) from \(1\) through \(2^{14}-1\), form the induced graph on the selected vertices and test the displayed degree-at-most-one condition. This visits *every* nonempty subset. Exactly \(2256\) pass, with numbers of faces in dimensions zero through six
\[
(14,91,322,651,728,392,58).
\]
There are \(70\) maximal five-simplices and \(58\) maximal six-simplices. The Euler characteristic is \(-12\), consistent with the claimed thirteen odd-dimensional spheres.

**Step 2: a complete acyclic discrete-Morse certificate.** Begin with the \(2256\) nonempty faces unpaired. In increasing vertex order \(0,1,\ldots,13\), pair every still-unpaired face \(\sigma\) not containing the current vertex \(v\) with \(\sigma\cup\{v\}\), provided both are still unpaired. There are exactly \(1121\) distinct face–coface pairs, and the unmatched faces are one vertex and thirteen five-simplices. The checker reconstructs all \(10150\) incidences between nonempty codimension-one faces, orients matched incidences upward and all remaining ones downward, and topologically sorts the directed graph. All \(2256\) faces are visited, establishing acyclicity globally. Forman's acyclic-matching theorem therefore gives a CW complex with just one zero-cell and thirteen five-cells. Its five-cell attaching maps land in a point; the complex is \(\bigvee^{13}S^5\), with no torsion or unresolved attaching maps.

**Step 3: complete symmetry group.** The seven line triples constitute the Fano \(2\)-\((7,3,1)\) design. Directly examine all \(7!\) point permutations and retain precisely those carrying every line triple to another line triple. There are \(168\), each uniquely extending to a bipartition-preserving graph automorphism. The involution \(p_i\leftrightarrow\ell_{-i}\) interchanges the two parts and preserves incidence. Together they produce \(336\) distinct automorphisms. Every graph automorphism either preserves or swaps the two intrinsic bipartition classes; therefore this enumeration is complete.

**Step 4: the character.** For each of these \(336\) permutations \(g\), compute the alternating signed trace on nonempty simplicial chains using all fixed simplices with their orientation signs. Since the only nonzero reduced rational homology is in degree five, the simplicial Lefschetz identity gives
\[
\operatorname{tr}(g\mid\widetilde H_5(X;\mathbb Q))
=1-\sum_{\substack{\emptyset\ne\sigma\in X\\g\sigma=\sigma}}
(-1)^{\dim\sigma}\operatorname{sgn}(g\mid\sigma).
\]
For *every* automorphism this equals \(\#\operatorname{Fix}_{V(H)}(g)-1\), the character of the vertex-permutation augmentation representation. Since rational representations of finite groups are semisimple, equality of all ordinary characters proves the asserted \(\mathbb QG\)-module isomorphism. This does **not** establish an integral \(\mathbb ZG\)-module isomorphism.

**Step 5: rational homology of orbit spaces.** The full group acts transitively on all fourteen graph vertices, while \(G^+\) has the two seven-element point/line orbits. Thus the augmentation module has invariant dimensions zero for \(G\) and one for \(G^+\). Barycentric subdivision removes simplex inversions; over characteristic zero, passage to coinvariants under a finite group is exact. Hence the rational homology of a finite simplicial quotient is the invariant rational homology, giving the orbit-space statements.

## Verification
Running `python3 verify_heawood_ind2.py` using the Python standard library rebuilds the complex and reproduces every finite step above. It additionally computes mod-two simplicial boundary ranks in degrees zero through six as \((0,13,78,244,407,321,58)\), yielding mod-two Betti numbers \((1,0,0,0,0,13,0)\), an independent check on the acyclic-matching conclusion. The program checks all \(336\) automorphisms individually rather than sampling conjugacy classes.

The complete tuple of class signatures (permutation order, whether the bipartition is swapped, number of fixed graph vertices, top-homology trace; multiplicity) is
`(1,0,14,13;1), (2,0,6,5;21), (2,1,0,-1;28), (3,0,2,1;56), (4,0,2,1;42), (6,1,0,-1;56), (7,0,0,-1;48), (8,1,0,-1;84)`.
The character sums are zero over the full group and \(168\) over the preserving subgroup.

## Relationship to prior work
Deshpande and Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types* (arXiv:2001.05448; first public January 15, 2020), defines the same \(r\)-independence construction and classifies complete multipartite, fully whiskered, path, cycle, and perfect rooted-tree families. None includes the Fano incidence graph. Deshpande, Shukla and Singh, *Distance \(r\)-Domination Number and \(r\)-Independence Complexes of Graphs* (arXiv:2001.06775), proves general vanishing bounds and a chordal-graph wedge criterion, neither of which supplies the exact Heawood classification or its automorphism character. Abdelmalek, Deshpande, Goyal, Roy and Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes* (arXiv:2106.10863), investigates trees and chordal graphs, whereas the Heawood graph contains induced six-cycles and is nonchordal.

Other known graph complexes on the Heawood graph are different simplicial constructions. In particular, the ordinary independence complex \(\operatorname{Ind}_1(H)\), the ordinary matching complex (whose vertices are graph edges), the perfect-matching complex, and the two-matching complex must not be identified with \(\operatorname{Ind}_2(H)\). A targeted search of public research records and accessible literature found no theorem implying the full homotopy type plus rational automorphism character here; see the accompanying review for explicit comparison scope and residual risk.

## Limitations
This is a classification for one distinguished finite graph, not an infinite-family theorem. The rational module identification is proved by exact character equality, but neither an explicit integral equivariant isomorphism nor a \(G\)-equivariant CW wedge decomposition is claimed. Rational acyclicity of the full quotient does not imply its integral acyclicity or contractibility. Exact searches cannot rule out unpublished or unindexed equivalent work, and independent external review has not been performed.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448v2 (first public January 15, 2020), https://arxiv.org/html/2001.05448v2 .
2. P. Deshpande, S. Shukla and A. Singh, *Distance \(r\)-Domination Number and \(r\)-Independence Complexes of Graphs*, arXiv:2001.06775v1 (January 19, 2020), https://arxiv.org/html/2001.06775v1 .
3. F. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863 (June 21, 2021), https://arxiv.org/abs/2106.10863 .
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145; standard discrete-Morse matching theorem as invoked in reference 1.
