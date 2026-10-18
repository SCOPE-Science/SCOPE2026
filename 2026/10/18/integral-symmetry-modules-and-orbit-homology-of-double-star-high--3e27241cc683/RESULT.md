# Integral symmetry modules and orbit homology of double-star higher-independence complexes

## Finding

Let \(D_{a,b}\) be the tree with two adjacent hubs \(u,v\), with \(a\geq1\) pendant vertices at \(u\) and \(b\geq1\) pendant vertices at \(v\). Write \(L=A\sqcup B\) for its \(m=a+b\) leaves, and put \(K_r=\operatorname{Ind}_r(D_{a,b})\) for every integer \(r\geq1\). Thus a simplex is a vertex subset all of whose induced connected components have at most \(r\) vertices. Let
\[
 U_L=\ker\!\left(\varepsilon:\mathbb Z^{L}\longrightarrow\mathbb Z,\quad e_\ell\longmapsto1\right).
\]
The automorphism group \(G=\operatorname{Aut}(D_{a,b})\) acts on \(L\) by permutation and on the ordered pair of hubs by a sign character \(\eta:G\to\{\pm1\}\): the character is \(-1\) precisely for elements interchanging the hubs (possible only if \(a=b\)).

**The integral equivariant result** is the following isomorphism of \(\mathbb Z[G]\)-modules, for every \(2\leq r\leq m+1\):
\[
 \boxed{\widetilde H_{r-1}(K_r;\mathbb Z)\ \cong_{\mathbb Z[G]}\ \eta\otimes\bigwedge^{r-2} U_L.}
\]
Every other reduced integral homology group vanishes. For \(r=1\) or \(r\geq m+2\), all reduced integral homology groups vanish. This determines **the entire integral automorphism representation at every threshold**; the rank alone is \(\binom{m-1}{r-2}\).

Let \(Q_r=|K_r|/G\) be the geometric orbit space under the full automorphism group. The equivariant calculation also determines its *reduced rational homology*, with all unlisted degrees zero:
\[
 \boxed{
 \begin{aligned}
 a\ne b:\quad &\widetilde H_j(Q_r;\mathbb Q)\cong\mathbb Q
 &&\text{exactly for }(r,j)=(2,1)\text{ or }(3,2);\\
 a=b:\quad &\widetilde H_j(Q_r;\mathbb Q)\cong\mathbb Q
 &&\text{exactly for }(r,j)=(3,2).
 \end{aligned}}
\]
In every other case the reduced rational homology is zero. In particular, for a fixed total number of leaves, exchanging an asymmetric leaf distribution for an equal split can remove the rational degree-one quotient class, even though the nonequivariant homotopy types remain the same.

**Prior-work boundary:** The nonequivariant homotopy formula \(K_r\simeq\bigvee^{\binom{m-1}{r-2}}S^{r-1}\) for \(2\leq r\leq m+1\), with contractible cases outside that range, is already contained in Deshpande and Singh's Theorem 3.10 (2021), specialized to two non-leaf vertices. **No novelty is asserted for that formula.** The new claim is the integral symmetry module and the resulting rational orbit-space classification.

## Assumptions and scope

All simplicial complexes are finite, and homology is reduced unless displayed otherwise. The integer conditions are \(a,b\geq1\) and \(r\geq1\), with no upper limit on \(a,b,r\). Here \(\bigwedge^0 U_L=\mathbb Z\). When \(a\ne b\), \(G=S_a\times S_b\). When \(a=b\), \(G=(S_a\times S_a)\rtimes C_2\), where the nontrivial factor swaps both hubs and both leaf blocks. The external sign \(\eta\) is the determinant of the two-hub permutation representation, not the sign of the leaf permutation. We do not claim integral homology of the orbit spaces, equivariant homotopy equivalence, or a classification of arbitrary trees.

## Proof

**1. Contractible one-hub subcomplex.** Put \(X\subseteq K_r\) equal to the subcomplex of faces not containing both hubs. Let \(\Delta^L\) be the full simplex on the leaves, contained in \(X\). Every face of \(X\setminus\Delta^L\) contains exactly one hub. A face with \(u\) but not \(v\) has the form \(\{u\}\cup F\) with \(F\subseteq L\) and \(|F\cap A|\leq r-1\); the analogous condition for a face containing \(v\) is \(|F\cap B|\leq r-1\). Fix leaves \(b_0\in B\) and \(a_0\in A\). Pair every \(u\)-containing face lacking \(b_0\) with that face after inserting \(b_0\), and pair every \(v\)-containing face lacking \(a_0\) with its enlargement by \(a_0\). These pairs are legal because opposite-block leaves are isolated from the chosen hub whenever the other hub is absent. Removing pairs in descending face-cardinality order gives elementary simplicial collapses: at the time of each removal, its lower member has the upper member as its only strict coface. No leaf-only face is removed, and every one-hub face is removed. Consequently \(X\searrow\Delta^L\) and \(|X|\) is contractible. Moreover, \(X\) is \(G\)-invariant; no equivariant collapse is required.

**2. Relative chain complex.** For a face containing both hubs, all its chosen vertices form one induced connected component. It is a face of \(K_r\) precisely when the remaining leaf subset \(F\subseteq L\) satisfies \(|F|\leq r-2\). For \(r\geq2\), the relative chains \(C_q(K_r,X;\mathbb Z)\) therefore have one generator \([u,v,\ell_1,\ldots,\ell_s]\) for each \(s=q-1\) and each \(F=\{\ell_1,\ldots,\ell_s\}\subseteq L\) of size at most \(r-2\). Choose the orientation with \(u,v\) first and the leaves ordered. Boundary terms deleting \(u\) or \(v\) lie in \(X\) and vanish in the relative complex; leaf-deletion terms have the signs of the *augmented* simplicial boundary of the leaf skeleton. Hence there is a degree-two shift of augmented chain complexes
\[
 C_q(K_r,X;\mathbb Z)\cong\widetilde C_{q-2}\bigl(\operatorname{skel}_{r-3}\Delta^L;\mathbb Z\bigr),
\]
where at \(r=2\), \(\operatorname{skel}_{-1}\Delta^L=\{\varnothing\}\) has its sole augmented generator in degree \(-1\). The action of \(g\in G\) on each oriented relative simplex multiplies by \(\eta(g)\) in addition to permuting the leaf orientation. Since \(X\) is invariant and contractible, the natural long exact sequence of the pair gives an equivariant isomorphism \(\widetilde H_q(K_r;\mathbb Z)\cong H_q(K_r,X;\mathbb Z)\) for every \(q\geq1\). (Both spaces are connected.)

**3. Exact integral cycle lattice.** Write \(P=\mathbb Z^{L}\) and \(\varepsilon:P\to\mathbb Z\) for coordinate sum. In degree \(k-1\), the augmented oriented chain group of the leaf simplex is \(\bigwedge^k P\), with boundary equal to contraction by \(\varepsilon\). Choose any leaf \(\ell_0\) to split \(P=U_L\oplus\mathbb Z e_{\ell_0}\). In \(\bigwedge^kP\), contraction by \(\varepsilon\) annihilates \(\bigwedge^kU_L\) and identifies the complementary factor \(e_{\ell_0}\wedge\bigwedge^{k-1}U_L\) with \(\bigwedge^{k-1}U_L\). Therefore its integral kernel is precisely \(\bigwedge^kU_L\); this equality is natural under every leaf permutation even though the splitting used to prove it is not. If \(2\leq r\leq m+1\), the leaf skeleton has top allowed cardinality \(k=r-2\). Its top reduced homology is this kernel \(\bigwedge^kU_L\), with lower reduced homology zero by exactness of the full simplex chain complex below the truncated top degree. Its rank is \(\binom{m-1}{k}\). Accounting for the relative degree shift and the two-hub orientation gives the asserted integral \(\eta\otimes\bigwedge^{r-2}U_L\) representation. For \(r=1\), no face contains both hubs, so \(K_1=X\) is contractible. For \(r\geq m+2\), all subsets are permitted and \(K_r\) is a simplex.

**4. Quotient rational homology.** A finite simplicial group action has rational quotient homology equal to the invariants of rational homology; one may barycentrically subdivide to remove inversions before applying averaging/transfer. Under \(S_a\times S_b\), the rational augmentation space splits as
\[
 U_L\otimes\mathbb Q\ \cong\ (U_A\otimes\mathbb Q)\oplus(U_B\otimes\mathbb Q)\oplus\mathbb Q\,w,
\]
where \(w\) has constant coefficients within each leaf block and opposite total block sums. For each symmetric group on a leaf block, every positive exterior power of its standard augmentation module has no invariants: it is a direct summand of the corresponding exterior power of the full permutation module, and a transposition of two letters in any oriented subset forces invariant coefficients to vanish (the degree-one augmentation also has no invariants). Thus the invariant exterior powers of \(U_L\) under \(S_a\times S_b\) have dimension one for degrees \(0\) and \(1\), and zero for all higher degrees. This gives the unbalanced quotient statement. If \(a=b\), the additional automorphism interchanges leaf blocks and sends \(w\mapsto-w\), while its exchange of the hubs also contributes the factor \(\eta=-1\). Consequently it kills the degree-zero exterior invariant and preserves the degree-one invariant. This proves the balanced quotient statement.

## Verification

The accompanying standard-library Python script `check_bistar.py` independently constructs faces from induced-graph component searches, compares them with the explicit two-hub face criterion, and verifies an explicit descending-order sequence of elementary collapses to the leaf simplex. It also computes complete reduced mod-two simplicial homology, signed Lefschetz traces for graph automorphisms, exterior-character predictions, and invariant ranks of full-automorphism quotients. The recorded run `check_output.txt` reports 112 face-model parameter triples, 6,210 elementary collapse pairs, 84 complete homology calculations, 266 character comparisons, and 36 quotient calculations, all passing. These finite checks test the proof but are not substituted for the all-parameter argument.

## Relationship to prior work

Deshpande and Singh, *Higher independence complexes of graphs and their homotopy types* (first public version 2020; Theorem 3.10 of the 2021 version), give a more general non-equivariant homotopy formula for graphs with every non-leaf vertex carrying a pendant leaf. For the double star, that theorem gives exactly the known wedge rank stated above. Its discrete-Morse argument selects individual leaves and does not determine the automorphism action or the rational homology of orbit spaces. Abdelmalek and collaborators prove vertex decomposability for caterpillar higher-independence complexes (Theorem 3.12), Ghosh and Selvaraja give shellability criteria, and Sawant proves vertex decomposability for all trees (Theorem 3.6). These results explain wedge behavior but do not identify the \(\mathbb Z[G]\)-lattice or the hub-exchange sign. The present equivariant computation refines, rather than republishes, the older homotopy classification.

## Limitations

The novelty assertion concerns the integral representation and quotient ranks **only**, not the sphere-wedge formula already in prior literature. The proof gives no integer torsion classification for quotient spaces, no equivariant homotopy splitting, and no representation formula for trees with more than two non-leaf vertices. Published and indexed literature comparisons do not logically prove global novelty; a specialized or unindexed equivalent equivariant result may exist. There has been no independent scientific audit.

## References

1. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448v2 (2021), Theorem 3.10, https://arxiv.org/html/2001.05448v2. Earliest arXiv version 2020-01-15.
2. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1 (2026-05-24), Theorem 3.6, https://arxiv.org/html/2605.25150v1.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, Theorem 3.12, https://arxiv.org/abs/2106.10863.
4. A. Ghosh and S. Selvaraja, *Chordality and Shellability of Higher Independence Complexes*, arXiv:2505.06614 (2025), Theorem 5.16, https://arxiv.org/abs/2505.06614.
