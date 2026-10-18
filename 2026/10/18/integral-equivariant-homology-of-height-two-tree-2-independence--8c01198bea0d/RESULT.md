# Integral equivariant homology of height-two tree \(2\)-independence complexes

## Finding

Let \(a\geq 2\) and \(b_1,\ldots,b_a\geq1\) be integers. Construct the height-two tree \(T(\mathbf b)\) with root \(c\), neighbors \(u_1,\ldots,u_a\), and exactly \(b_i\) terminal leaves \(L_i\) adjacent to \(u_i\). Let \(K=\operatorname{Ind}_2(T(\mathbf b))\) consist of the vertex sets whose induced forest has every connected component of size at most two. Equivalently, \(K\) is the three-vertex-path-free complex.

Write \(A_b=\ker(\mathbb Z[L]\xrightarrow{\varepsilon}\mathbb Z)\), for a set \(L\) of \(b\) elements and the map \(\varepsilon\) sending each basis element to \(1\). The full tree automorphism group is \(G=\left(\prod_i S_{L_i}\right)\rtimes\prod_b S_{m_b}\), with \(m_b=|\{i:b_i=b\}|\); it permutes leaves independently within each arm and permutes arms of equal size.

There is a natural integral \(G\)-module isomorphism
\[
\widetilde H_j(K;\mathbb Z)\cong
\begin{cases}
\bigotimes_{i=1}^{a}A_{b_i},&j=2a-1,\\
0,&j\ne2a-1.
\end{cases}
\]
Here within-arm leaf permutations act on the corresponding augmentation factors. An arm permutation sends factors to the corresponding new arms **without a sign**. In particular,
\[
K\simeq \bigvee^{\prod_{i=1}^a(b_i-1)}S^{2a-1};
\]
if the multiplicity is zero, \(K\) is contractible.

More explicitly, let \(g\in G\) induce an arm permutation \(\sigma\). For every cycle \(C=(i_1,\ldots,i_t)\) of \(\sigma\), let \(\phi_C\) be the leaf permutation of \(L_{i_1}\) obtained by composing the leaf bijections around that cycle. Then the character on the only potentially nonzero rational reduced homology group is
\[
\chi_K(g)=\prod_{C\in\operatorname{Cycles}(\sigma)}\left(|\operatorname{Fix}(\phi_C)|-1\right).
\]
This expression is zero if some \(b_i=1\). For identical branch sizes, it computes the full character for the wreath-product action \(S_b\wr S_a\).

## Assumptions and scope

Graphs are finite, simple and undirected. The root has at least two children, and every child has at least one leaf. The root is the unique graph-theoretic center (all longest leaf-to-leaf paths between distinct branches have length four); therefore the displayed group is the full automorphism group, not merely a chosen subgroup. Reduced homology is integral unless a coefficient field is indicated. The statement is a nonequivariant homotopy classification together with a natural **equivariant homology** classification, not an equivariant homotopy classification.

## Proof

**1. Delete the root.** Put \(K_0=\operatorname{del}_K(c)\) and \(Y=\operatorname{lk}_K(c)\). Deleting \(c\) leaves the disjoint union of the \(a\) stars on \(\{u_i\}\cup L_i\); hence
\[
K_0=K_1*\cdots*K_a,\qquad K_i=\operatorname{Ind}_2(K_{1,b_i}).
\]
Writing \(L=\bigcup_iL_i\), the root link has the **exact** simplicial presentation
\[
Y=\Delta(L)\ \cup\ \bigcup_{i=1}^{a}\left(u_i*\Delta(L\setminus L_i)\right).
\]
Indeed, a face that contains \(c\) can contain at most one \(u_i\); if that center \(u_i\) is present, no terminal leaf of its branch can be present, since \(c,u_i,\ell\) would be an induced three-vertex path. In the absence of arm centers, any choice of leaves is allowed.

Each \(L\setminus L_i\) is nonempty because \(a\ge2\) and all \(b_j\ge1\). On realizations there is a \(G\)-equivariant deformation retract \(|Y|\to|\Delta(L)|\): fix the leaf simplex and slide each apex \(u_i\) linearly to the barycenter of the simplex on \(L\setminus L_i\). On each cone this affine homotopy agrees with the identity on the shared base, and the barycenter assignment commutes with the graph symmetries. Thus \(Y\) is nonempty and contractible.

The decomposition \(K=K_0\cup(c*Y)\), with intersection \(Y\), is a CW cofibration. Attaching a cone on a contractible nonempty subcomplex does not change its homotopy type, so the inclusion \(K_0\hookrightarrow K\) is a homotopy equivalence of underlying spaces. Equivariantly, the Mayer–Vietoris long exact sequence for this \(G\)-invariant union shows that inclusion induces an isomorphism of integral \(G\)-modules on all reduced homology. No equivariant null-homotopy of \(Y\) is asserted or needed.

**2. Compute each star factor.** The star complex has the presentation
\[
K_i=\Delta(L_i)\cup\left(u_i*L_i^{(0)}\right).
\]
The first summand is a simplex and the second is the graph containing the \(b_i\) spokes from \(u_i\) to the leaves. Contracting \(\Delta(L_i)\) shows \(K_i\simeq\bigvee^{b_i-1}S^1\) when \(b_i\ge2\), while \(K_i\) is contractible for \(b_i=1\). The augmentation kernel description is canonical: orient each spoke from \(u_i\) to its leaf and use the Mayer–Vietoris boundary map for the union of the leaf simplex and the star of spokes. Its reduced \(H_0\) connecting homomorphism has kernel precisely \(A_{b_i}\), so \(\widetilde H_1(K_i;\mathbb Z)\cong A_{b_i}\) as an \(S_{L_i}\)-lattice; other reduced homology vanishes.

**3. Join, orientations and characters.** The integral join Künneth theorem (all factors have free homology) gives
\[
\widetilde H_{2a-1}(K_0;\mathbb Z)\cong\bigotimes_i\widetilde H_1(K_i;\mathbb Z)\cong\bigotimes_i A_{b_i},
\]
with zero reduced homology elsewhere. Under interchange of two join factors carrying homology classes of degree one, the graded join twist is \((-1)^{(1+1)(1+1)}=+1\). Thus permuting equal-size branches creates no sign. The trace of a cyclic permutation of tensor factors, each linked by linear bijections, equals the trace of their composite on one factor. For \(A_b\), a leaf permutation with \(f\) fixed leaves has trace \(f-1\), by subtracting the one-dimensional trivial summand of \(\mathbb Z[L]\). Multiply across disjoint branch cycles to obtain the displayed character formula. Because each \(K_i\) is a wedge of circles or contractible, their join is a wedge of \((2a-1)\)-spheres with the given multiplicity, including the contractible case.

**4. Independent finite Morse formulation of the homotopy calculation.** Choose one distinguished leaf in each \(L_i\). Sequentially match every still-unmatched face not containing the chosen leaf with its union with that leaf whenever this is a face. Standard sequential element matchings are acyclic (Deshpande–Singh, Proposition 2.10), and a direct argument shows the only critical faces in the augmented face poset are precisely those containing **all** centers \(u_i\), **no** root, and exactly one *non-distinguished* leaf per branch. The conditions are independent across branches; there are \(\prod_i(b_i-1)\) critical faces, all of cardinality \(2a\). Every root-containing face has at least one absent center, so a leaf in that branch is toggleable; every root-free face missing any center is likewise toggleable; and a root-free face with all centers survives exactly when it has one non-distinguished leaf per branch. This proves the homotopy multiplicity again, including zero, without extrapolating from finite experiments.

## Verification

The accompanying `verify_height_two.py` independently enumerates all subsets of a selected range of these trees and applies the induced-component size criterion. It constructs the staged distinguished-leaf matching, checks its critical faces and all directed-Hasse incidences for acyclicity, calculates all reduced mod-two boundary ranks by exact elimination, and independently computes signed fixed-simplex traces of automorphisms. The cases are branch profiles \((1,1),(1,3),(2,2),(2,3),(2,2,3),(2,3,2),(3,3),(2,2,2),(3,3,3)\). The largest has 13 vertices, 2,432 augmented faces, and 11,984 Hasse incidences. Tests cover a within-arm leaf transposition and equal-arm swaps; the exact mathematical proof above establishes the general group action, not just those tests.

Reproduce with `python3 verify_height_two.py` using the standard library. Finite enumeration validates these instances, **not** the universal quantifiers; the preceding argument supplies the proof for all positive branch sizes and all \(a\ge2\).

## Relationship to prior work

Rutuja Sawant's 2026 theorem proves vertex decomposability of \(\operatorname{Ind}_r(T)\) for **all** trees and \(r\), but does not give the exact integral automorphism representation or the character formula. It provides the recent motivating structural setting, not evidence that a wedge-of-spheres assertion for trees is new.

Deshpande and Singh's 2020/2021 results are particularly close: Theorem 5.6 calculates nonequivariant homotopy types for **perfect** \(m\)-ary trees, including the balanced height-two examples in the present family. Those balanced **homotopy types are prior results**. Their Theorem 3.10 requires every nonleaf to have an adjacent leaf; the central vertex here has no adjacent leaf, so that separate theorem does not cover these height-two trees. Neither theorem gives the integral group module and complete character formula for the full leaf- and branch-permutation action; the present classification additionally handles nonuniform branch profiles.

Ghosh and Selvaraja (2025, Theorem 4.8) already prove shellability for every tree of diameter at most five, **including every tree here** (diameter four). Thus shellability, and the mere existence of a wedge decomposition, are known for the entire family; this theorem adds exact multiplicities and the integral symmetry module and character. Abdelmalek and collaborators study shellability and vertex decomposability of higher independence complexes, including caterpillars, without this natural representation. Their earlier general-tree shellability proof has a noted gap, as discussed in Sawant (2026); no part of the present proof relies on that disputed argument. The distinction between a known sphere-wedge **existence** result, known balanced multiplicities, and an explicit equivariant integral representation is essential.

## Limitations

The theorem assumes a depth-two tree with at least two branches and at least one leaf in each. It does not classify arbitrary trees, higher independence parameter \(r\ne2\), or integral equivariant homotopy types. The isomorphism is natural on homology; the constructed contraction of the root link is equivariant, but the nonequivariant cone-attachment argument does not assert a \(G\)-equivariant homotopy equivalence. The group character is a consequence of the integral module and is not an assertion about a particular integral eigenbasis. Full scientific priority beyond indexed and inspected sources is not certified.

## References

1. Rutuja Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150v1, first posted 24 May 2026; Theorem 3.6 and introduction. https://arxiv.org/abs/2605.25150
2. Priyavrat Deshpande and Anurag Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (first posted 2020; journal publication 2021); Theorems 3.10, 5.6, and Proposition 2.10. https://arxiv.org/abs/2001.05448
3. Arka Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614, 2025; Theorem 4.8 (diameter at most five). https://arxiv.org/abs/2505.06614
4. Fred M. Abdelmalek, Priyavrat Deshpande, Shuchita Goyal, Amit Roy, and Anurag Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, International Journal of Algebra and Computation 33 (2023), 481–498. https://arxiv.org/abs/2106.10863
