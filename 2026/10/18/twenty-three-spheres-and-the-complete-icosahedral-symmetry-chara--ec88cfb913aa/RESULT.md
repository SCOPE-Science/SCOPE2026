# Twenty three-spheres and complete icosahedral symmetry in a two-independence complex

## Finding

Let \(I\) be the one-skeleton of the regular icosahedron and \(X=\operatorname{Ind}_2(I)\) its two-independence complex. There is an integral homotopy equivalence
\[
X\simeq\bigvee^{20}S^3.
\]
Moreover, writing the full graph automorphism group as \(\operatorname{Aut}(I)\cong A_5\times C_2\), its rational third-homology representation is
\[
\widetilde H_3(X;\mathbb Q)\cong
(\mathbf1\oplus W_4\oplus W_5^{\oplus2})\boxtimes\mathbf1
\;\oplus\;W_5\boxtimes\varepsilon.
\]
Here \(W_4,W_5\) are the unique rational irreducible representations of \(A_5\) of degrees four and five, and \(\varepsilon\) is the nontrivial character of the central antipodal \(C_2\). In particular, the invariant rational homology has dimension one; the antipodal \(+1\) and \(-1\) eigenspaces have dimensions fifteen and five.

## Assumptions and scope

Everything concerns a single finite simple graph. To specify it without geometric coordinates, take two poles \(N,S\), upper vertices \(u_i\), and lower vertices \(\ell_i\), with \(i\in\mathbb Z/5\mathbb Z\). Join \(N\) to each \(u_i\), \(S\) to each \(\ell_i\), consecutive vertices in each pentagon, and \(u_i\) to \(\ell_i\) and \(\ell_{i-1}\). This is the 12-vertex, 30-edge regular icosahedral graph. Both supplied computations implement this graph, with an explicit permutation identifying their two vertex labelings.

A face of \(X\) is a vertex subset \(U\subseteq V(I)\) for which every connected component of the induced graph \(I[U]\) has at most two vertices. Equivalently every selected vertex has at most one selected neighbor. This complex also equals the three-vertex-path-free complex when paths mean not-necessarily-induced subgraphs. No assertion is made about the different triangle-free, ordinary-independence, matching, cut, or neighborhood complexes.

## Proof

**Finite homotopy certificate.** In the labeled edge-list model of `verify_morse_character.py`, the nonempty faces are precisely the masks \(s\in\{1,\ldots,4095\}\) such that each selected vertex has at most one selected neighbor. Exact enumeration gives the face vector \((12,66,140,105)\), so \(X\) is three-dimensional and has 323 nonempty faces. Consider the ordered vertices
\[
(7,4,5,2,9,3,6,0,10,1,8,11).
\]
At each pivot \(v\), pair every as-yet-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), provided the latter remains unmatched. The algorithm constructs 151 disjoint cover pairs. Exactly one vertex and twenty three-simplices remain critical, with no critical cells in dimensions one or two.

For a direct acyclicity verification, orient each Hasse cover downward except the 151 matched covers, which are reversed. All 972 directed covers are built explicitly; Kahn's topological sort visits all 323 faces, so this directed graph contains no cycle. Thus the partial matching is acyclic. By the discrete-Morse theorem, \(X\) has a CW model with one zero-cell and twenty three-cells and no other cells. Every three-cell is attached to the zero-skeleton by a constant map, proving the stated integral sphere wedge (not just its Betti numbers). Since the matching covers every simplex and every possible cover, this is an exhaustive finite proof for the specified graph.

**Full symmetry character.** The verifier enumerates every adjacency-preserving bijection of the twelve graph vertices by exhaustive backtracking and obtains exactly 120 automorphisms. The vertex at distance three from any given vertex is unique, defining the central antipodal involution \(z\). The standard icosahedral symmetry identification yields the direct product \(A_5\times\langle z\rangle\).

For an automorphism \(g\), define \(T_d(g)\) as the sum of signs of the induced vertex permutations over the \(g\)-setwise-fixed \(d\)-simplices. Because \(H_0(X;\mathbb Q)=\mathbb Q\) and higher rational homology is concentrated in degree three, Hopf's trace formula gives
\[
\operatorname{tr}(g\mid H_3(X;\mathbb Q))
=1-\sum_{d=0}^{3}(-1)^dT_d(g).
\]
Every term is an exact integer count. For the rotation classes \((1,2A,3A,5A,5B)\) of \(A_5\), the traces are \((20,4,-1,0,0)\). For their products with \(z\), the traces are \((10,2,1,0,0)\). These exhaust the group: the corresponding class sizes are \((1,15,20,12,12)\), each copied to the other antipodal coset.

The positive and negative antipodal characters, obtained by taking the half-sum and half-difference, are respectively \((15,3,0,0,0)\) and \((5,1,-1,0,0)\). The standard \(A_5\) character table identifies them as \(\mathbf1\oplus W_4\oplus W_5^{\oplus2}\) and \(W_5\). This proves the asserted representation and its invariant-dimension and eigenspace consequences. The last calculation concerns rational representations; it does not assert an integral direct-sum lattice splitting at the prime two.

## Verification

Run `python3 verify_morse_character.py` and `python3 crosscheck_mod2.py` using Python 3.10 or later. Both use only the standard library and contain every graph edge and arithmetic rule required. Their expected deterministic terminal outputs are embedded as `verify_morse_character.out` and `crosscheck_mod2.out`. The first exhaustively checks graph identification, all 323 faces, the 151-pair discrete-Morse matching, all 972 Hasse covers, all 120 graph automorphisms and all icosahedral character values. The second uses the independent double-pentagon graph model and row-reduces every simplicial boundary over \(\mathbb F_2\); its boundary ranks are \((11,55,85)\), yielding reduced Betti vector \((0,0,0,20)\). These field checks corroborate the homotopy proof but alone would not establish the integral wedge decomposition.

## Relationship to prior work

Deshpande and Singh [1] develop higher-independence complexes and compute homotopy types for complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect rooted trees; none of those family results applies to the icosahedral graph. Sawant [2] proves vertex decomposability for higher-independence complexes of trees and explicitly identifies the three-vertex-path-free construction with two-independence. Ghosh and Selvaraja [3] prove shellability under block-graph and other structural hypotheses, not for this nonchordal icosahedral graph. The present computation specifies a new natural finite graph instance and determines the complete rational automorphism character, which is not determined by knowing the nonequivariant sphere count. Standard group data for full icosahedral symmetry are recorded in [4].

## Limitations

The result is for the twelve-vertex icosahedral graph only; no classification for arbitrary planar triangulations or regular graphs follows. The symmetry decomposition is over \(\mathbb Q\); the integral homology group is free, but the integral representation lattice is not classified here. The certificate is a finite exhaustive calculation whose interpretation uses standard discrete-Morse and Lefschetz theorems. No independent verification of this finding has been performed, and unindexed work could overlap.

## References

[1] P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first public January 15, 2020, https://arxiv.org/abs/2001.05448.

[2] R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150, first public May 24, 2026, https://arxiv.org/abs/2605.25150.

[3] A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614, first public May 10, 2025, https://arxiv.org/html/2505.06614v3.

[4] GroupNames, *\(C_2\times A_5\): the icosahedral full symmetry group*, https://www.people.maths.bris.ac.uk/~matyd/GroupNames/97/C2xA5.html.
