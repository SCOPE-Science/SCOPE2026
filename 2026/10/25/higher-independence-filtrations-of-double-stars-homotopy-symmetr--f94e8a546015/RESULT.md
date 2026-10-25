# Higher independence filtrations of double stars: homotopy, symmetries, and persistence

## Finding
For integers \(a,b\ge1\), let \(T_{a,b}\) be the tree whose adjacent centers \(u,v\) have, respectively, disjoint sets \(A,B\) of \(a,b\) pendant neighbors. Put \(L=A\sqcup B\) and \(N=a+b\). For an integer \(r\ge1\), let \(K_r=\operatorname{Ind}_r(T_{a,b})\), the complex of vertex subsets for which each connected component of the induced tree has at most \(r\) vertices.

**Theorem.** The complete integral homotopy classification is
\[
 K_r\simeq
 \begin{cases}
 \mathrm{pt},&r=1\text{ or }r\ge N+2,\\
 \displaystyle\bigvee^{\binom{N-1}{r-2}}S^{r-1},&2\le r\le N+1.
 \end{cases}
\]
In particular, the homotopy type depends on the **total** number of leaves, not how they are distributed between the centers.

Let \(G=\operatorname{Aut}(T_{a,b})\), let \(\mathbb Z^L\) be its leaf-permutation lattice and let \(U_L=\ker(\mathbb Z^L\xrightarrow{\mathrm{sum}}\mathbb Z)\). For \(2\le r\le N+1\), the only nonzero reduced integral homology, as an **integral \(G\)-module**, is
\[
 \widetilde H_{r-1}(K_r;\mathbb Z)
 \cong \bigwedge^{r-2} U_L\otimes\varepsilon_{uv},
\]
where \(\varepsilon_{uv}(g)=-1\) when \(g\) interchanges the two centers and \(+1\) otherwise. Thus \(G\cong S_a\times S_b\) if \(a\ne b\), and \(G\cong(S_a\times S_a)\rtimes C_2\) if \(a=b\). All other reduced integral homology groups vanish. With \(p_g\) the induced permutation of \(L\), the rational character is
\[
 \operatorname{tr}\!\left(g\mid\widetilde H_{r-1}(K_r;\mathbb Q)\right)
 =\varepsilon_{uv}(g)[t^{r-2}]
 \frac{\prod_{c\in\operatorname{Cyc}(p_g)}(1-(-t)^{|c|})}{1+t}.
\]

For every field \(F\), the inclusion filtration \(K_1\subseteq K_2\subseteq\cdots\subseteq K_{N+2}\) has precisely \(\binom{N-1}{r-2}\) positive-degree persistent bars \([r,r+1)\) in homological degree \(r-1\), for each \(2\le r\le N+1\), and no other reduced-homology bars. (Here \([r,r+1)\) denotes consecutive integer filtration indices, not metric lengths.)

## Assumptions and scope
All graphs and simplicial complexes are finite, all homology in the integral statement is reduced singular or simplicial homology over \(\mathbb Z\), and all homotopy equivalences concern geometric realizations. The parameters satisfy \(a,b\ge1\) and \(r\ge1\), with no upper bound on \(a,b\). A graph automorphism sends the centers to themselves or interchanges them, as dictated by their degrees; the induced leaf permutation preserves the two blocks or interchanges them. A wedge of zero spheres means a point. For skeleton calculations, \(\operatorname{sk}_{-1}\Delta(L)=\{\varnothing\}\) is the formal \((-1)\)-sphere, while any skeleton index at least \(N-1\) means the full simplex.

## Proof
**1. An exact decomposition.** Let \(\Delta(S)\) denote the full simplex on a finite set \(S\), including its empty face, and let \(\langle u\rangle*X\) denote its cone on \(X\). For \(r\ge2\), define
\[
 X_r=\operatorname{sk}_{r-2}\Delta(A)*\Delta(B),\quad
 Y_r=\Delta(A)*\operatorname{sk}_{r-2}\Delta(B),\quad
 Z_r=\operatorname{sk}_{r-3}\Delta(L).
\]
A face with neither center may contain any leaves. A face containing \(u\) but not \(v\) may use at most \(r-1\) leaves of \(A\), because those leaves form one connected component with \(u\), while leaves in \(B\) are isolated; this gives \(\langle u\rangle*X_r\). Similarly the faces with \(v\) only give \(\langle v\rangle*Y_r\). If both centers are present, all selected leaves join their single connected component, so at most \(r-2\) leaves are permitted, giving \(\langle u,v\rangle*Z_r\). Hence the equality of simplicial complexes
\[
 K_r=\Delta(L)\ \cup\ (\langle u\rangle*X_r)
 \ \cup\ (\langle v\rangle*Y_r)
 \ \cup\ (\langle u,v\rangle*Z_r).\tag{1}
\]
This equality also covers \(r=2\), where \(Z_r\) has only the empty face.

**2. The contractible core and quotient.** Put
\[
 C_r=\Delta(L)\cup(\langle u\rangle*X_r)\cup(\langle v\rangle*Y_r).
\]
Because \(A\) and \(B\) are nonempty, \(X_r\) is a cone (it has the full \(\Delta(B)\) factor), as is \(Y_r\) (by \(\Delta(A)\)). Thus each is contractible. The first cone \(\langle u\rangle*X_r\) meets \(\Delta(L)\) in exactly \(X_r\). The second cone meets their union in exactly \(Y_r\). By the homotopy-pushout gluing lemma for simplicial inclusions, adjoining each cone along a contractible subcomplex preserves contractibility, so \(C_r\) is contractible.

The intersection of the last term in (1) with \(C_r\) is exactly \(\partial\langle u,v\rangle*Z_r\). Since \(C_r\subseteq K_r\) is a nonempty contractible simplicial subcomplex, collapsing it is a homotopy equivalence. Consequently
\[
 |K_r|\simeq |K_r|/|C_r|
 \cong |\langle u,v\rangle*Z_r|\big/|\partial\langle u,v\rangle*Z_r|.
 \tag{2}
\]
For \(r\ge3\), the last quotient is the unreduced suspension of the suspension of \(|Z_r|\). For \(r=2\), the quotient is an interval with its endpoints identified, namely \(S^1\).

**3. Homotopy and dimension.** When \(3\le r\le N+1\), put \(k=r-3\), so \(0\le k\le N-2\). Toggle a distinguished leaf in the face poset of \(\operatorname{sk}_k\Delta(L)\), pairing a face without that leaf with the face obtained by adding it whenever the latter remains in the skeleton. This is an acyclic matching: every matched edge toggles the same distinguished vertex. Allowing the empty face in the matching, its unmatched faces are exactly the \(\binom{N-1}{k+1}\) faces of size \(k+1\) not containing that leaf. The standard elementary discrete-Morse theorem therefore gives
\[
 |Z_r|\simeq\bigvee^{\binom{N-1}{r-2}}S^{r-3}.
\]
Together with (2), this proves the announced homotopy formula for \(3\le r\le N+1\); the \(r=2\) calculation gives its coefficient \(\binom{N-1}{0}=1\). If \(r\ge N+2\), every induced subgraph has at most \(N+2\le r\) vertices, so \(K_r\) is a full simplex. Finally, for \(r=1\) the face with both centers is absent. Repeating the first three terms of (1) with \(X_1=\Delta(B)\) and \(Y_1=\Delta(A)\) proves \(K_1\) contractible by the same gluing argument.

**4. Integral symmetry module.** The homotopy argument gives a corresponding canonical relative chain calculation, avoiding any need for an equivariant choice of contraction of \(C_r\). The relative chain complex \(C_*(K_r,C_r;\mathbb Z)\) is freely generated by oriented faces containing both \(u\) and \(v\). In degree \(q\), the map
\[
 [u,v,\ell_1,\ldots,\ell_{q-1}]\longmapsto
 [\ell_1,\ldots,\ell_{q-1}]
\]
identifies it with the augmented chain complex of \(Z_r\), shifted by two degrees. Terms obtained by deleting \(u\) or \(v\) vanish in relative chains. A center interchange reverses the ordered pair \([u,v]\) and hence multiplies this identification by \(-1\), whereas a leaf permutation acts through its natural oriented action. Because \(C_r\) is contractible and both complexes are connected, the long exact sequence of the pair gives the \(G\)-equivariant isomorphism
\[
 \widetilde H_{r-1}(K_r;\mathbb Z)
 \cong \widetilde H_{r-3}(Z_r;\mathbb Z)\otimes\varepsilon_{uv},
\]
including the augmented \(r=2\) convention.

Let \(E=\mathbb Z^L\) with basis the leaves, and \(U_L=\ker(\varepsilon:E\to\mathbb Z)\) where \(\varepsilon\) sums coefficients. The augmented degree-\(j\) simplex chain group is \(\bigwedge^{j+1}E\), and its boundary is contraction with \(\varepsilon\). The full simplex chain complex is exact. For \(k=r-3\), the top cycles of its \(k\)-skeleton are therefore
\[
 \operatorname{im}\left(\partial_{k+1}:\bigwedge^{k+2}E\to\bigwedge^{k+1}E\right)
 =\bigwedge^{k+1}U_L.
\]
The equality follows by splitting \(E=U_L\oplus\mathbb Z e\) with \(\varepsilon(e)=1\). For \(k=-1\), the augmented reduced homology is \(\mathbb Z=\bigwedge^0 U_L\). This proves the integral module statement in every permitted case. The character formula follows from \(\det(I+t p_g\mid E)=\prod_c(1-(-t)^{|c|})\) and \(E\cong U_L\oplus\mathbf1\) rationally.

**5. Persistence.** The only nonzero reduced homology of \(K_r\) occurs in degree \(r-1\) for \(2\le r\le N+1\). The next complex has no homology in that same degree. Consequently every homology map induced by \(K_r\hookrightarrow K_{r+1}\) in positive degree is zero. Each nonzero group is free, so after base change to any field the intervals are exactly those stated, with no longer bars. This completes the proof.

## Verification
An independent-by-implementation exhaustive checker is supplied in `verify.py`, with its output in `verify_output.txt`. It constructs the original tree and every induced subgraph directly; tests all possible faces for \(1\le a,b\le3\) and \(1\le r\le a+b+2\); computes all reduced mod-two Betti numbers using exact bitwise Gaussian elimination; enumerates center-preserving and center-interchanging automorphisms; and compares signed invariant-face Lefschetz sums against the exterior-power character. It completed 54 parameter instances (4,174 nonempty faces aggregated over instances) and 892 symmetry-character comparisons. These finite tests supplement, rather than replace, the uniform integral argument above.

## Relationship to prior work
Deshpande and Singh (2020/2021) determine higher-independence homotopy for several families, including perfect rooted trees, and explicitly ask for sphere multiplicities for general trees (Question 2). The present double stars are caterpillar trees but are not in general perfect rooted trees. The smallest case \(a=b=1\) is the four-vertex path, whose nonequivariant classification is already contained in their path theorem and is included here only as a boundary case. Abdelmalek and coauthors (2021/2023) prove vertex decomposability for caterpillars; Ghosh and Selvaraja (2025) obtain shellability under tree-diameter hypotheses; Sawant (first publicly posted May 24, 2026) proves vertex decomposability for all trees. These qualitative conclusions imply the possibility of sphere wedges but do **not** give the binomial multiplicities, canonical integral automorphism modules, or complete filtration barcodes established here. The calculation is specific to the two-center tree and does not purport to solve the general-tree enumeration problem.

## Limitations
No homotopy classification is claimed for arbitrary caterpillars or trees of diameter at least four. The symmetry conclusion is integral at the homology-module level; it does not assert an equivariant wedge decomposition of spaces. The persistence statement concerns ordinary reduced homology with field coefficients at integer threshold parameters. Literature comparison is limited to the inspected sources and public searches; independent priority review has not been performed.

## References
1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first public version May 24, 2026, https://arxiv.org/abs/2605.25150.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first public version January 15, 2020; Journal of the Ramanujan Mathematical Society **36** (2021), 53–71, https://arxiv.org/abs/2001.05448.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863; International Journal of Algebra and Computation **33** (2023), 481–498, https://arxiv.org/abs/2106.10863.
4. A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614, first public version May 10, 2025, https://arxiv.org/abs/2505.06614.
