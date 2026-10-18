# Clique-prism two-independence topology and its full permutation character

## Finding

For each integer \(n\ge5\), let \(G_n=K_n\square K_2\) be the **clique prism**, whose vertex set consists of \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with a clique in each layer and matching edges \(a_i b_i\). Its two-independence complex \(X_n=\operatorname{Ind}_2(G_n)\) consists of subsets inducing connected components of order at most two. The integral homotopy type is

\[
X_n\simeq \bigvee^n S^1\ \vee\ \bigvee^{\beta_n}S^3,
\qquad
\beta_n=1-2n+2n(n-1)-n(n-1)(n-2)+\binom n2\binom{n-2}2
=\frac{n^4-10n^3+31n^2-30n+4}{4}.
\]

In particular, \(\pi_1(X_n)\cong F_n\), \(\widetilde H_1(X_n;\mathbb Z)\cong\mathbb Z^n\), \(\widetilde H_3(X_n;\mathbb Z)\cong\mathbb Z^{\beta_n}\), and every other reduced integral homology group is zero. The initial sphere multiplicities for \(n=5,6,7,8,9\) are \(1,19,71,181,379\).

The natural action of \(S_n\times C_2\), by simultaneous permutation of labels and swapping layers, has a complete rational homology character. For \(\sigma\in S_n\), write \(c_j=c_j(\sigma)\) for the number of its \(j\)-cycles, and let \(\tau\) denote the layer swap. Then

\[
\operatorname{tr}\bigl(\sigma\tau^e\mid H_1(X_n;\mathbb Q)\bigr)=(-1)^e c_1,\quad e\in\{0,1\},
\]
\[
\operatorname{tr}\bigl(\sigma\mid \widetilde H_3(X_n;\mathbb Q)\bigr)
=\sum_{a=0}^2\sum_{b=0}^2[x^a y^b](1-x-y)^{c_1}(1-x^2-y^2)^{c_2},
\]
\[
\operatorname{tr}\bigl(\sigma\tau\mid \widetilde H_3(X_n;\mathbb Q)\bigr)
=1-2c_2+4\binom{c_2}{2}-2c_4.
\]

Here \([x^a y^b]\) means ordinary polynomial coefficient extraction. In particular, layer exchange has trace exactly \(1\) on third homology, independent of \(n\). Integrally, \(H_1\) is the label-permutation lattice tensored with the negative character of layer exchange.

## Assumptions and scope

All graphs are finite, undirected, simple. The parameter is every integer \(n\ge5\). For a graph \(G\), a face of \(\operatorname{Ind}_2(G)\) is a vertex subset whose induced connected components each contain at most two vertices, including the empty face. Homotopy equivalence refers to geometric realizations. Group characters are defined over \(\mathbb Q\); the two displayed nonzero homology groups have integral lattices. The theorem does not assert any conclusion for \(n<5\), and does not claim that the underlying chessboard-core shellability is new.

## Proof

**1. Exact face classification.** For a selected subset \(F\), write \(A_F=\{i:a_i\in F\}\) and \(B_F=\{i:b_i\in F\}\). Each layer is a clique; therefore an allowable face satisfies \(|A_F|\le2\) and \(|B_F|\le2\). If both \(a_i,b_i\in F\), their matching edge joins the selected layer components. Any third selected vertex is adjacent to either \(a_i\) or \(b_i\), producing a component of size at least three. Thus this face must be the diagonal edge \(\{a_i,b_i\}\). In all other allowable faces, \(A_F\cap B_F=\emptyset\); conversely, every disjoint pair \((A_F,B_F)\) with cardinalities at most two is allowable, since no selected cross-layer matching edges occur. Define \(D_n\subset X_n\) by exactly these latter faces. Hence \(X_n\) is obtained from \(D_n\) by attaching the \(n\) diagonal edges along their endpoints; those edges occur in no higher-dimensional face.

**2. The chessboard core.** Regard \(A\) and \(B\) as rows of a two-row, \(n\)-column board, with at most two selected squares per row and at most one per column. This identifies \(D_n\) simplicially with the multiple chessboard complex \(\Delta^{2,2;\mathbf 1}_{n,2}\). Theorem 4.4 of Jojić–Vrećica–Živaljević (2014) says this complex is shellable when \(n\ge2+2+2-1=5\). Each maximal face has two vertices from each layer (extend any disjoint face using at least five columns), so \(D_n\) is pure three-dimensional; it is connected because its one-skeleton contains both cliques and every non-diagonal cross-layer edge. A pure shellable three-complex is homotopy equivalent to a wedge of three-spheres (possibly none). The exact numbers of simplices of dimensions zero, one, two, and three are
\[
f_0=2n,\qquad f_1=2n(n-1),\qquad f_2=n(n-1)(n-2),\qquad f_3=\binom n2\binom{n-2}2.
\]
Thus its only possible reduced Betti number is \(\beta_n=-\widetilde\chi(D_n)=1-f_0+f_1-f_2+f_3\), as claimed. Shellability gives integral wedge topology, so this is not an inference solely from field-valued Betti numbers.

**3. The added one-cells.** Attaching an edge along two vertices of a path-connected CW complex adds a free circle up to homotopy. Doing this for all \(n\) distinct diagonal edges (each has its two endpoints already in \(D_n\)) gives \(X_n\simeq D_n\vee\bigvee^n S^1\). The same cell-pair exact sequence shows \(H_1(X_n,D_n;\mathbb Z)\cong\mathbb Z^n\) with the oriented diagonal edges \([a_i,b_i]\) as generators; because \(H_1(D_n;\mathbb Z)=0\) and \(H_0(D_n;\mathbb Z)\to H_0(X_n;\mathbb Z)\) is an isomorphism, this is naturally \(H_1(X_n;\mathbb Z)\). A simultaneous label permutation permutes its generators, and row interchange reverses their orientations, proving the integral first-homology action and character.

**4. Equivariant top-degree homology.** Inclusions induce natural isomorphisms \(H_3(D_n;\mathbb Q)\cong H_3(X_n;\mathbb Q)\). For any simplicial automorphism \(g\) of \(D_n\), define the signed fixed-face sum
\[
P(g)=\sum_{F\in D_n,\ gF=F}(-1)^{|F|}\,\operatorname{sgn}(g|F),
\]
where the empty face contributes \(1\) and \(\operatorname{sgn}(g|F)\) is the sign of the induced permutation of the ordered vertices of \(F\). The simplicial Lefschetz trace identity, with the empty face included, gives \(P(g)=\operatorname{tr}(g\mid\widetilde H_3(D_n;\mathbb Q))\), because all other reduced homology is zero.

For \(g=\sigma\) with no row interchange, each fixed label contributes choices empty, row \(A\), or row \(B\), hence a factor \(1-x-y\). A two-cycle of labels may be wholly occupied in row \(A\) or row \(B\), each with orientation sign minus and two used squares, giving \(1-x^2-y^2\). No orbit of length greater than two fits into the capacity-two rows. Multiplication and restriction to exponents at most two in each variable yields the first top-character formula.

For \(g=\sigma\tau\), an odd label-cycle cannot support a nonempty fixed face without occupying both rows in some column. The two alternate selections along a label two-cycle each have one vertex per row and orientation sign minus, giving \(1-2xy\). The two alternate selections along a four-cycle occupy two vertices per row, with orientation sign minus, giving \(1-2x^2y^2\). Longer even cycles exceed row capacities. The capacity-restricted product is \((1-2xy)^{c_2}(1-2x^2y^2)^{c_4}\); collecting its terms of degree at most two in each variable gives \(1-2c_2+4\binom{c_2}2-2c_4\). This exhausts all conjugacy classes and completes the proof.

## Verification

The self-contained Python checker `verify_clique_prism.py` reconstructs graph edges, determines admissible faces directly from connected components, and compares them against the face classification independently for each \(5\le n\le9\). It calculates complete reduced simplicial homology over \(\mathbb F_2\) using exact boundary-matrix elimination, yielding vectors \((0,n,0,\beta_n)\) throughout those five cases. It separately enumerates the chessboard-core faces, computes signed simplicial Lefschetz sums for **all** \(240\) pairs of permutations and row swaps at \(n=5\), and for \(120\) deterministically selected pairs at \(n=6\). Every comparison with the closed character formulas passes. Reproduce with `python3 verify_clique_prism.py` using only the Python standard library. The finite checks corroborate the algebra and sign conventions; the all-parameter assertions follow from the complete arguments above.

## Relationship to prior work

Jojić–Vrećica–Živaljević (2014), Theorem 4.4, proves shellability of the **multiple chessboard core** \(D_n\), which directly covers that ingredient of Step 2 and is explicitly credited; its theorem does **not** classify the graph-theoretic complex \(X_n\) with its diagonal one-cells or supply the stated full \(S_n\times C_2\) homology character. Sawant (2026) studies vertex-decomposable higher-independence complexes **of trees**; the clique prism has cliques and cycles. A previously recorded classification of the **open-neighborhood complex** of \(K_n\square K_2\) concerns a different face predicate: subsets sharing an external open neighbor rather than induced-component sizes. Earlier work by Karaguezian–Reiner–Wachs (2001) and by Wachs (2003) studies broader bounded-degree graph and chessboard homology; accessible metadata do not resolve every potential equivalence, and this remains a bibliographic risk. No equivalent or stronger explicit conclusion for the full \(X_n\) and its full natural action was identified in the accessible comparisons.

## Limitations

The decomposition holds for \(n\ge5\), not for all smaller parameters. It does not give integral irreducible decomposition of third homology, only its complete rational character and its free abelian rank. The core's shellability is prior mathematics, not an original theorem. The available searches and full-text inspections cannot rule out unindexed results, and potentially relevant older bounded-degree-complex papers could not all be inspected in full. Computational tests range only over \(5\le n\le9\); a finite test alone would not establish the infinite claim. No independent validation is claimed.

## References

1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first public 2026-05-24. https://arxiv.org/abs/2605.25150
2. D. Jojić, S. Vrećica and R. Živaljević, *Multiple chessboard complexes and the colored Tverberg problem*, arXiv:1412.0386, first public 2014-12-01, especially Definition 1.4 and Theorem 4.4. https://arxiv.org/abs/1412.0386
3. D. B. Karaguezian, V. Reiner and M. L. Wachs, *Matching Complexes, Bounded Degree Graph Complexes, and Weight Spaces of GLn-Complexes*, J. Algebra 239 (2001), 77–92. https://doi.org/10.1006/jabr.2000.8654
4. M. L. Wachs, *Topology of matching, chessboard, and general bounded degree graph complexes*, Algebra Universalis 49 (2003), 345–385. https://doi.org/10.1007/s00012-003-1825-1
5. *Open-neighborhood complexes of clique prisms: a mixed-dimensional sphere decomposition*, published mathematical record, identifier `d1fca5b06808`, full result available at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-open-neighborhood-complexes-of-clique-prisms-a-mixed-dimensional--d1fca5b06808
