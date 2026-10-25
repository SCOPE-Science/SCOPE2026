# Higher-independence homotopy and branch symmetries of unwhiskered subdivided stars

## Finding

Let \(m\ge2\) be an integer. Define the subdivided star \(T_m\) on vertices \(c,a_1,\ldots,a_m,b_1,\ldots,b_m\) with edges \(ca_i\) and \(a_ib_i\) for each \(i\). Its center has no adjacent leaves. For an integer \(r\ge1\), \(\operatorname{Ind}_r(T_m)\) is the simplicial complex of all vertex sets whose induced connected components each contain at most \(r\) vertices.

For every integer \(r\ge3\),
\[
\operatorname{Ind}_r(T_m)\simeq
\begin{cases}
\mathrm{pt},&3\le r\le m,\\
\displaystyle\bigvee^{\binom{m-1}{r-m-1}}S^{r-1},&m+1\le r\le 2m,\\
\mathrm{pt},&r\ge 2m+1.
\end{cases}
\]
All displayed equivalences are integral homotopy equivalences. In particular, the transition at \(r=m+1\) produces one \(m\)-sphere, the intermediate ranks form a binomial row, and the last noncontractible case \(r=2m\) is one sphere of dimension \(2m-1\).

Permuting the \(m\) arms defines an \(S_m\)-action. Put \(U_m=\ker(\mathbb Z^m\xrightarrow{\mathrm{sum}}\mathbb Z)\). When \(m+1\le r\le2m\), the complete nonzero reduced integral homology representation is
\[
\widetilde H_{r-1}(\operatorname{Ind}_r(T_m);\mathbb Z)
\cong_{\mathbb Z[S_m]}
\operatorname{sgn}_m\otimes\bigwedge^{r-m-1}U_m.
\]
This identifies the integral lattice, not merely the rational character or its rank.

## Assumptions and scope

The parameter \(m\) is any integer at least two and \(r\) is any integer at least three. The group acts by simultaneous permutations of the pairs \((a_i,b_i)\), fixing \(c\). A component's size is its number of vertices, including isolated singletons. The graph is not the fully whiskered star: the central vertex \(c\) has no leaf neighbor. The \(r=2\) case is not proposed as new, and arbitrary spiders with unequal arm lengths are not covered.

## Proof

Write \(A=\{a_1,\ldots,a_m\}\), \(B=\{b_1,\ldots,b_m\}\), and \(K=\operatorname{Ind}_r(T_m)\). Every subset of \(A\cup B\) is a face of \(K\), because deleting \(c\) leaves a disjoint union of edges. The link \(L=\operatorname{lk}_K(c)\) consists exactly of the subsets \(F\subseteq A\cup B\) satisfying
\[
\sum_{i:\,a_i\in F}\bigl(1+\mathbf 1_{b_i\in F}\bigr)\le r-1.
\]
Indeed, the left side counts the other vertices in the connected component of \(T_m[F\cup\{c\}]\) containing \(c\); the remaining \(b_i\) are isolated. Thus \(K=\Delta_{A\cup B}\cup(c*L)\), with intersection \(L\). Both pieces are contractible, so the homotopy pushout identifies \(K\simeq\Sigma L\). The Mayer–Vietoris connecting maps additionally give \(S_m\)-equivariant integral isomorphisms \(\widetilde H_j(K)\cong\widetilde H_{j-1}(L)\).

For each \(i\), let \(L_i\) denote the vertex-deletion subcomplex \(\{F\in L:a_i\notin F\}\). The vertex \(b_i\) is free in \(L_i\): adding or removing it changes none of the displayed weighted sum. Hence \(L_i\) is a cone. More generally, each nonempty intersection \(\bigcap_{i\in I}L_i\) is a cone on any \(b_i\) with \(i\in I\). Therefore the nerve lemma, applied to the finite cover by all \(L_i\), proves that \(U=\bigcup_{i=1}^mL_i\) is contractible: every intersection is nonempty and contractible, and the nerve is a full simplex.

If \(r\le m\), no face may contain all vertices of \(A\), because their contribution to the weighted sum is \(m>r-1\). Consequently \(L=U\) is contractible, and so is \(K\).

Suppose now \(m+1\le r\le2m\) and set \(k=r-m-1\), so \(0\le k\le m-1\). Define \(Y\) on \(B\) to consist of all subsets of cardinality at most \(k\). Here \(k=0\) means the simplicial complex containing just the empty face, geometrically the \((-1)\)-sphere for join purposes. The faces of \(L\) containing all of \(A\) have precisely at most \(k\) vertices of \(B\). Thus
\[
L=U\cup(\Delta_A*Y),\qquad U\cap(\Delta_A*Y)=\partial\Delta_A*Y.
\]
The first piece is contractible by the nerve argument, and the second is contractible as a join with a simplex. Their common subcomplex is a join of the boundary sphere \(\partial\Delta_A\cong S^{m-2}\) with \(Y\). The homotopy-pushout formula now gives
\[
L\simeq\Sigma(\partial\Delta_A*Y)\simeq\Sigma^mY,
\qquad K\simeq\Sigma^{m+1}Y.
\]
The truncated simplex \(Y\) is the \((k-1)\)-skeleton of the simplex on \(m\) vertices. It is homotopy equivalent to \(\bigvee^{\binom{m-1}{k}}S^{k-1}\), using the standard skeleton-collapse formula (for \(k=0\), interpret \(Y=\{\emptyset\}\)). Therefore \(K\simeq\bigvee^{\binom{m-1}{k}}S^{m+k}=\bigvee^{\binom{m-1}{r-m-1}}S^{r-1}\).

For \(r\ge2m+1\), every vertex subset has induced connected components of at most the total \(2m+1\) vertices; hence \(K\) is the full simplex and is contractible. This proves every nonequivariant case and its exact boundary.

It remains to identify the natural integral action. The two applications of Mayer–Vietoris above are natural for the branch-permutation group because every union and intersection is invariant, and all of their contractible pieces have vanishing positive reduced integral homology. Thus the only nonzero reduced homology is the shifted homology of \(\partial\Delta_A*Y\). The top integral homology of \(\partial\Delta_A\) is the orientation-sign lattice \(\operatorname{sgn}_m\). Write \(E=\mathbb Z^B\) with its permutation action. The simplicial chain group of \(Y\) in degree \(k-1\) is \(\bigwedge^kE\); its top-cycle lattice is the kernel of the contraction by the augmentation \(\varepsilon:E\to\mathbb Z\). Since \(E=\ker\varepsilon\oplus\mathbb Zb_1\) as abelian groups and \(\varepsilon(b_1)=1\), this kernel is naturally \(\bigwedge^k\ker\varepsilon=\bigwedge^kU_m\), including \(k=0\) as the trivial lattice. The integral join Künneth formula has no torsion because these groups are free. It yields precisely the sign-twisted exterior-power representation stated above. No extension or rationalization is used.

## Verification

The supplied standalone `verify_spider.py` reconstructs faces directly by checking connected component sizes on the original tree, not by using the preceding link decomposition. It computes all augmented simplicial boundary ranks over \(\mathbb F_2\) for \(2\le m\le6\), across every \(2\le r\le2m+2\). Its \(45\) complete Betti-vector comparisons agree with the formula (including the previously established \(r=2\) boundary). It also enumerates all branch permutations for \(2\le m\le5\) and computes signed simplicial Lefschetz traces from permutation-fixed faces; all \(1436\) comparisons agree with the trace of \(\operatorname{sgn}_m\otimes\bigwedge^{r-m-1}U_m\), or with zero in contractible cases. `verify_output.txt` gives the actual replay output. These finite computations are corroboration only: the all-parameter integral homotopy and representation claims follow from the preceding proof.

## Relationship to prior work

Deshpande and Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types* (arXiv:2001.05448), Theorems 3.8 and 3.10, determine homotopy types for fully whiskered connected graphs and, more generally, connected graphs in which **every nonleaf vertex is adjacent to a leaf**. Our tree is excluded: its center \(c\) has degree \(m\ge2\) but no leaf neighbors. Their Theorem 5.6 treats perfect uniform-branching trees; here all intermediate vertices have exactly one child, so for \(m\ge2\) the tree is not a perfect \(m\)-ary height-two tree. No formula in those stated classes yields this binomial row or the integral \(S_m\)-lattice.

Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees* (arXiv:2605.25150; first released May 24, 2026), proves vertex decomposability for every tree, hence a general wedge-of-spheres existence theorem. The precise sphere ranks, sharp contractibility threshold for the center-unwhiskered family, and branch-permutation homology representation do not follow from mere vertex decomposability. Deshpande, Shukla and Singh, *Distance \(r\)-Domination Number and \(r\)-Independence Complexes of Graphs* (arXiv:2001.06775), give connectivity and general chordal wedge-existence bounds, not this parameter-specific representation.

A calculation for \(r=2\) in a more general diameter-four tree class is not part of the novelty asserted here. The ordinary discrete-Morse complexes of the same underlying trees, and their branch actions, are different simplicial complexes from \(\operatorname{Ind}_r\).

## Limitations

The theorem does not cover arbitrary rooted trees, unequal arm lengths, or higher independence complexes on other graph products. It does not establish an equivariant **homotopy** splitting—only the stated ordinary integral homotopy type and the equivariant integral homology lattice. The computational checks use \(\mathbb F_2\) Betti vectors and integral signed Lefschetz traces for finite samples; they are not substitutes for the integral infinite-family proof. As with any literature comparison, unindexed results may exist; the nearest explicit stronger family theorem was examined and found inapplicable owing to its positive-leaf-adjacency hypothesis.

## References

1. Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, Theorems 3.8, 3.10, 5.6; https://arxiv.org/html/2001.05448v2.
2. Rutuja Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first public version May 24, 2026; https://arxiv.org/abs/2605.25150.
3. Priyavrat Deshpande, Samir Shukla and Anurag Singh, *Distance \(r\)-Domination Number and \(r\)-Independence Complexes of Graphs*, arXiv:2001.06775; https://arxiv.org/abs/2001.06775.
