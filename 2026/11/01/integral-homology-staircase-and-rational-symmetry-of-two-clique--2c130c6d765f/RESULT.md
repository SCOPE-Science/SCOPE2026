# Integral homology staircase and rational symmetry of two-clique sums

## Finding
Let \(A,B,C\) be pairwise disjoint finite vertex sets with \(|A|=a\ge1\), \(|B|=b\ge1\), and \(|C|=s\ge2\). Form the graph \(G\) by taking all edges within each of \(A\cup C\) and \(B\cup C\), and no edges between \(A\) and \(B\). Thus \(G\) is a clique sum of two complete graphs along their common \(s\)-vertex clique. For every integer \(t\ge3\), let \(X=\mathsf{CF}_t(G)\) consist of the vertex subsets containing no \(t\)-vertex clique of \(G\), and set \(k=t-1\).

For every integer \(i\ge0\), the reduced integral homology is torsion-free, with

\[
\operatorname{rank}\widetilde H_i(X;\mathbb Z)
=\sum_{\substack{0\le j\le\min(s,k)\\i=2k-j-1}}
\binom{s}{j}\binom{a-1}{k-j}\binom{b-1}{k-j}.
\]

A binomial coefficient \(\binom{n}{d}\) is zero when \(d<0\) or \(d>n\). In particular, all reduced homology vanishes outside the degrees \(2k-j-1\), \(0\le j\le\min(s,k)\). When \(a,b\ge t\) and \(s\ge t-1\), there is nonzero homology in **every one** of the \(t\) consecutive degrees \(t-2,t-1,\ldots,2t-3\).

The formula has a symmetry refinement. The natural \(S_a\times S_b\times S_s\) action preserves a filtration of each integral homology group whose associated graded terms in degree \(2k-j-1\) are

\[
\operatorname{Ind}^{S_s}_{S_j\times S_{s-j}}(\operatorname{sgn}_j\boxtimes\mathbf1)
\otimes\bigwedge^{k-j}U_A\otimes\bigwedge^{k-j}U_B,
\]

where \(U_A=\ker(\mathbb Z^A\xrightarrow{\sum}\mathbb Z)\) and similarly for \(U_B\). The induced module is the signed permutation lattice on \(j\)-element subsets of \(C\). Terms with vanishing exterior powers are zero. After tensoring with \(\mathbb Q\), the filtration splits as a representation; **no integral equivariant direct-sum splitting is claimed**.

For \((a,b,s,t)=(3,3,2,3)\), the nonzero reduced homology ranks are \(1,8,1\) in degrees \(1,2,3\). For \((4,4,3,4)\), they are \(1,27,27,1\) in degrees \(2,3,4,5\).

## Assumptions and scope
All graphs are finite and simple. Both private sets \(A,B\) are nonempty, the common set has \(s\ge2\) elements, and \(t\ge3\). A face \(F\subseteq A\sqcup B\sqcup C\) belongs to \(X\) exactly when

\[
|F\cap A|+|F\cap C|\le k,\qquad |F\cap B|+|F\cap C|\le k.
\]

The result determines ordinary integral homology and a rational symmetry representation, not a full homotopy type. It includes degenerate sizes for which the complex is contractible.

## Proof
**1. The common-clique filtration.** Give the augmented simplicial chains of \(X\) their usual integer orientations, including the empty face in degree \(-1\). For \(0\le j\le\min(s,k)\), let \(F_j\) be the subcomplex of faces using at most \(j\) vertices of \(C\). Take \(F_{-1}\) to be the void filtration level for augmented reduced chains. Since a face can have at most \(k\) common vertices, the final level is \(X\).

Fix \(J\subseteq C\) with \(|J|=j\). Among the faces whose common-vertex set is exactly \(J\), the private part is a face of

\[
Y_j=\operatorname{sk}_{k-j-1}(\Delta_A)*
\operatorname{sk}_{k-j-1}(\Delta_B),
\]

where \(\Delta_A,\Delta_B\) are full simplices on the indicated vertex sets, and \(\operatorname{sk}_{-1}(\Delta)=\{\varnothing\}\) is the augmented \((-1)\)-sphere. Orient vertices in the fixed block order \(C,A,B\). In the quotient of chain complexes \(\widetilde C_*(F_j)/\widetilde C_*(F_{j-1})\), every boundary term deleting a vertex of \(J\) vanishes. The remaining boundary is precisely the augmented simplicial boundary on \(Y_j\), shifted by \(j\). Hence

\[
H_i(F_j,F_{j-1};\mathbb Z)
\cong\bigoplus_{J\in\binom{C}{j}}\widetilde H_{i-j}(Y_j;\mathbb Z),
\]

where at \(j=0\) this denotes the reduced homology of \(F_0\), and the relative groups are understood in the augmented-chain sense. This identification is natural under permutations within \(A,B,C\); a permutation of \(J\) contributes its orientation sign.

**2. Integral homology of simplex skeletons.** For a set \(D\) of \(n\ge1\) vertices and \(d\ge0\), the augmented boundary complex of the full simplex is exact. Its chain groups identify with exterior powers of \(\mathbb Z^D\), and the boundary is contraction by the sum map \(\epsilon:\mathbb Z^D\to\mathbb Z\). Splitting \(\mathbb Z^D\cong\ker\epsilon\oplus\mathbb Z\) gives

\[
\widetilde H_r(\operatorname{sk}_{d-1}(\Delta_D);\mathbb Z)
\cong\begin{cases}
\bigwedge^d\ker\epsilon,&r=d-1,\\
0,&r\ne d-1.
\end{cases}
\]

This also holds for \(d=0\), with reduced homology of \(\{\varnothing\}\) in degree \(-1\). The exterior lattice has rank \(\binom{n-1}{d}\); when \(d\ge n\), it vanishes and the skeleton is a full simplex. The integral join Künneth formula, including these augmented conventions, consequently gives

\[
\widetilde H_r(Y_j;\mathbb Z)
\cong\begin{cases}
\bigwedge^{k-j}U_A\otimes\bigwedge^{k-j}U_B,&r=2(k-j)-1,\\
0,&\text{otherwise}.
\end{cases}
\]

Every nonzero group is free abelian.

**3. Collapse by degree, without an assumption of vanishing attaching maps.** Use the integral spectral sequence of the finite filtered augmented chain complex. By Step 2, the \(j\)-th first-page column is supported only in the **total homological degree**
\[
d_j=j+2(k-j)-1=2k-j-1.\]
A homological differential \(d_r\) from filtration index \(j\) to \(j-r\), with \(r\ge1\), lowers total degree by one. But the only possibly nonzero group in the target column has degree \(d_{j-r}=d_j+r>d_j-1\). Thus every differential vanishes, for every page and all parameters. The spectral sequence converges to the reduced integral homology of \(X\). Its associated graded pieces are precisely the free groups of Step 2, one per \(j\) and each \(J\subseteq C\) of size \(j\). Since an extension of free abelian groups by free abelian groups splits as abelian groups, all resulting homology groups are free. Counting the subsets \(J\) and the ranks from Step 2 proves the displayed Betti formula and all asserted vanishing statements.

**4. Symmetry.** The filtration is preserved by \(S_a\times S_b\times S_s\). In each quotient, permutations of the common block act on the oriented \(j\)-element subsets with their permutation sign, while the two private groups act on the exterior augmentation lattices as in Step 2. This gives the stated integral associated-graded representation. Semisimplicity of finite-group representations over \(\mathbb Q\) splits the finite filtration after rationalization, yielding the full rational character. Specifically, for a permutation \(\sigma\), set

\[
P_\sigma(z)=\frac{\prod_{\ell\in L(\sigma)}(1-(-z)^\ell)}{1+z},\qquad
Q_\sigma(z)=\prod_{\ell\in L(\sigma)}(1-(-z)^\ell),
\]

where \(L(\sigma)\) is the multiset of cycle lengths. For \((\sigma_A,\sigma_B,\sigma_C)\), the trace on \(\widetilde H_{2k-j-1}(X;\mathbb Q)\) equals

\[
[z^j]Q_{\sigma_C}(z)\cdot[z^{k-j}]P_{\sigma_A}(z)
\cdot[z^{k-j}]P_{\sigma_B}(z).
\]

This follows because \(P\) is the exterior-character generating polynomial of the augmentation representation, and \(Q\) is the signed-subset-character polynomial. Only one index \(j\) contributes to a given degree.

## Verification
The accompanying `verify.py` constructs each graph independently from its two maximal cliques, enumerates all forbidden \(t\)-cliques, enumerates faces, and performs mod-two simplicial-boundary elimination. Eleven parameter cases passed, including the two examples above and limiting private-block sizes. For four parameter cases, it independently checked 492 signed Lefschetz traces against the displayed rational character formula. `verify_integral.py` used signed integer boundary matrices and Smith normal forms for four small examples; the calculated ranks matched and every nonzero Smith factor was one. Both scripts were executed successfully on the delivered versions. These finite tests do not replace the all-parameter integral proof.

## Relationship to prior work
Ghosh and Selvaraja (2026) systematically study clique-free complexes and prove shellability under graph-theoretic hypotheses, including a block-graph result, but do not determine the present integral homology ranks or rational characters for a nontrivial clique overlap. Khosh-Ahang and Moradi (2019) analyze clique ideals and related shellability questions, without the degree-by-degree overlapping-clique computation in the inspected text. Earlier one-vertex clique gluing is a different, simpler boundary case; the new assertion is for intersection size at least two, including the full consecutive-degree staircase. The proof here does not infer its ranks from an unspecified shelling.

## Limitations
No integral equivariant splitting of the filtration is established, only its integral associated graded and the rational representation. No wedge-of-spheres homotopy equivalence is claimed. The result does not extend automatically to an arbitrary clique-sum tree, other forbidden subgraphs, or the full graph automorphism group when two equal private blocks can be interchanged. Prior-literature comparisons are best-effort; equivalent formulations outside the inspected sources remain possible. No independent validation has been performed.

## References
- R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1 (first posted 2026-02-10), https://arxiv.org/abs/2602.09623.
- F. Khosh-Ahang and S. Moradi, *Some algebraic properties of t-clique ideals*, Communications in Algebra 47 (2019), DOI:10.1080/00927872.2018.1541462; author-posted full text: https://www.researchgate.net/publication/329870976_Some_algebraic_properties_of_t_-clique_ideals.
- S. Moradi, *t-clique ideal and t-independence ideal of a graph*, Communications in Algebra 46 (2018), DOI:10.1080/00927872.2017.1412445 (background; abstract checked).
