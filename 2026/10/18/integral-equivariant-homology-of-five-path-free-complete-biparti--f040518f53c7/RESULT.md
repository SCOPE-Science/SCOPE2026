# Integral equivariant homology of five-path-free complete bipartite complexes

## Finding
For every pair of integers \(m,n\geq 3\), let \(G=K_{m,n}\) have its distinguished color classes \(L\) and \(R\), and let \(X_{m,n}\) be the simplicial complex of vertex subsets \(A\subseteq V(G)\) for which the induced graph \(G[A]\) has **no five-vertex path as a subgraph** (the forbidden path need not be induced). The color-preserving automorphism group \(\mathfrak S_m\times\mathfrak S_n\) acts on this complex.

Write \(E_r=\mathbb Z^r\) for the integral permutation lattice, \(\varepsilon_r:E_r\to\mathbb Z\) for coordinate summation, and \(I_r=\ker\varepsilon_r\). Define the equivariant surjection
\[
 d_r:\bigwedge^{2}E_r\longrightarrow I_r,\qquad
 d_r(e_i\wedge e_j)=e_j-e_i.
\]
Then all integral reduced homology of \(X_{m,n}\) vanishes except in degree three, and the surviving **integral equivariant lattice** has the canonical kernel description
\[
 \widetilde H_3(X_{m,n};\mathbb Z)
 \cong_{\mathbb Z[\mathfrak S_m\times\mathfrak S_n]}
 \ker\bigl(d_m\otimes d_n:\bigwedge^2E_m\otimes\bigwedge^2E_n\longrightarrow I_m\otimes I_n\bigr).
\]
In particular, this is a free abelian group of rank
\[
 \binom m2\binom n2-(m-1)(n-1).
\]

Over \(\mathbb Q\), let \(U_r=I_r\otimes\mathbb Q\), the standard \((r-1)\)-dimensional representation of \(\mathfrak S_r\). The **complete irreducible outer-product decomposition** is
\[
\begin{aligned}
\widetilde H_3(X_{m,n};\mathbb Q)\cong {}&
 (\textstyle\bigwedge^2U_m)\boxtimes U_n\\
 &\oplus U_m\boxtimes(\textstyle\bigwedge^2U_n)\\
 &\oplus(\textstyle\bigwedge^2U_m)\boxtimes(\textstyle\bigwedge^2U_n).
\end{aligned}
\]
The factors \(U_r\) and \(\bigwedge^2 U_r\) are the rational Specht modules for partitions \((r-1,1)\) and \((r-2,1,1)\), respectively. The three outer products are pairwise inequivalent irreducibles for all \(m,n\ge3\).

For arbitrary permutations \(g\in\mathfrak S_m\) and \(h\in\mathfrak S_n\), write \(f(g)\) for the number of fixed letters, and \(a(g)=[f(g)^2-f(g^2)]/2\). The character on degree-three homology is
\[
 \chi_3(g,h)=a(g)a(h)-[f(g)-1][f(h)-1].
\]
For example, when \(m=n=3\), the homology has rank five but a single transposition in the first factor acts with trace \(-3\); rank alone does not determine this representation.

## Assumptions and scope
The forbidden object is an ordinary five-vertex path appearing as a not-necessarily-induced subgraph of \(G[A]\). Equivalently, if \(a=|A\cap L|\) and \(b=|A\cap R|\), a face is permitted precisely when neither \((a\ge3,b\ge2)\) nor \((a\ge2,b\ge3)\) occurs. This equivalence uses the complete bipartite edges and alternation along a five-vertex path. The action treated is the color-preserving subgroup \(\mathfrak S_m\times\mathfrak S_n\); an additional color-swap symmetry when \(m=n\) is not classified here.

## Proof
**1. The lower-path subcomplex.** Let \(B\) consist of subsets satisfying \(a\le1\) or \(b\le1\); these are exactly the subsets avoiding a four-vertex path. Let \(A_R\) be the join of the full simplex on \(R\) with the discrete complex on \(L\), and define \(A_L\) symmetrically. Then \(B=A_R\cup A_L\). Each piece is contractible, and their intersection is precisely the one-dimensional complete bipartite graph \(K_{m,n}\). Both pieces and their intersection are invariant under the specified group. Equivariant Mayer–Vietoris identifies
\[
 \widetilde H_2(B;\mathbb Z)\cong H_1(K_{m,n};\mathbb Z)
 \cong I_m\otimes I_n,
\]
with all other reduced homology zero. For the second isomorphism, orient every cross edge from \(L\) to \(R\). The integral cycle space is the kernel of both row and column sums inside \(E_m\otimes E_n\), which equals \(I_m\otimes I_n\); the equality follows from the split-free row/column augmentation sequences. In particular \(B\) is simply connected: van Kampen applies to its two contractible pieces meeting in the connected graph \(K_{m,n}\).

**2. Exactly one relative layer.** The faces of \(X_{m,n}\setminus B\) have exactly two vertices from each color class. Every such face is a three-simplex, and each proper face belongs to \(B\). Therefore the relative chain complex \(C_*(X_{m,n},B;\mathbb Z)\) is concentrated in degree three and has
\[
 H_3(X_{m,n},B;\mathbb Z)
 \cong \bigwedge^2 E_m\otimes\bigwedge^2 E_n
\]
as a group module: oriented tetrahedra are ordered with the two left vertices preceding the two right vertices.

**3. The connecting map.** For left vertices \(i,j\) and right vertices \(p,q\), the oriented boundary of the relative tetrahedron \([i,j,p,q]\) is
\[
 [j,p,q]-[i,p,q]+[i,j,q]-[i,j,p].
\]
The first two triangles belong to \(A_R\), and the last two to \(A_L\). Passing through the Mayer–Vietoris connecting isomorphism of Step 1 yields, up to a uniform sign fixed by conventions, the oriented rectangular cycle
\[
 (e_j-e_i)\otimes(f_q-f_p).
\]
Thus the connecting homomorphism in the long exact sequence of \((X_{m,n},B)\) is precisely \(d_m\otimes d_n\), up to that harmless global sign. This is an identification of **equivariant integral homomorphisms**, not merely a rank calculation.

**4. Integral surjectivity and homology.** Fix the last basis vector in each class. The images of
\[
 (e_i\wedge e_m)\otimes(f_j\wedge f_n),
 \qquad 1\le i<m,\quad1\le j<n,
\]
form a signed integral basis of \(I_m\otimes I_n\). Hence the connecting map is onto and admits a unit minor of order \((m-1)(n-1)\). The pair sequence gives \(\widetilde H_2(X_{m,n};\mathbb Z)=0\), identifies degree-three homology with the stated kernel, and yields zero in every other reduced degree. Its kernel is a subgroup of a free abelian group, hence free; the displayed rank follows. The quotient \(X_{m,n}/B\) has only relative three-cells, and \(B\) is simply connected, so the claimed vanishing includes the fundamental-group-level boundary required for the standard nonequivariant sphere-wedge interpretation. The *equivariant* assertion is instead the stronger, explicitly stated lattice identification.

**5. Rational irreducibles and character.** Over \(\mathbb Q\), splitting the permutation module by the invariant all-ones vector gives \(E_r\otimes\mathbb Q\cong\mathbf1\oplus U_r\), and therefore \(\bigwedge^2(E_r\otimes\mathbb Q)\cong U_r\oplus\bigwedge^2U_r\). The map \(d_r\) is the identity, up to scalar, on the first summand and zero on the second. Tensoring the two decompositions and removing the \(U_m\boxtimes U_n\) image yields the three announced irreducibles. The exterior-square character identity \(\chi_{\wedge^2 E_r}(g)=[f(g)^2-f(g^2)]/2\) and exactness give the character formula.

## Verification
The included `verify_p5.py` reconstructs the complexes by exhaustive vertex-subset enumeration and tests every subset against the forbidden-path size criterion. Exact finite-field reductions for \((m,n)=(3,3),(3,4),(4,4),(3,5),(4,5),(5,5)\) agree with the theorem in characteristics \(2,3,5,101\). The included, separately structured `verify_char.py` computes signed fixed-simplex Lefschetz traces for every element of the product groups for \((3,3),(3,4),(4,4)\), namely \(36+144+576=756\) elements, and verifies the predicted complete character against a second independent expression from the three irreducible summands. Both scripts were executed successfully. These checks are finite corroborations; the proof of the statement for every \(m,n\ge3\) is Steps 1–5.

## Relationship to prior work
Taylan's 2015 framework defines devoid complexes and proves homotopy classifications for forbidden paths on path and cycle graphs and for the three-vertex-path condition on forests. It supplies historical motivation but not this complete-bipartite equivariant lattice. Deshpande, Goyal and Sawant (2026) explicitly report the nonequivariant homotopy types of path-free complexes of complete bipartite graphs; **their sphere-wedge and Betti-number conclusions are treated as existing coverage**, not as new here. Their accessible abstract does not state the color-preserving symmetric-group representation; the full manuscript could not be materially inspected, leaving a bibliographic risk. Bate, Everitt, Ford and Ramos compute other homology representations, centered on complete-hypergraph matching complexes and general asymptotic representation stability, not this explicit integral kernel. The new claim is only the specified integral equivariant lattice and its full rational character decomposition.

## Limitations
The extra graph automorphism exchanging the two color classes when \(m=n\) is not included. No modular irreducible decomposition, ring structure, equivariant stable homotopy type, or higher-path analogue is claimed. Bibliographic searches cannot rule out mathematically equivalent work outside the indexed literature; in particular, the full text of the July 2026 closely related paper was not available for inspection, so no absolute priority is asserted. There has been no independent scientific audit.

## References
1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754 (first posted 2015-01-27). https://arxiv.org/abs/1501.06754
2. P. Deshpande, S. Goyal and R. Sawant, *On a complete characterization of path-free complexes associated with complete multipartite graphs*, arXiv:2607.05358 (first posted 2026-07-06). https://arxiv.org/abs/2607.05358
3. M. Bate, B. Everitt, S. Ford and E. Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750 (first posted 2023-12-21). https://arxiv.org/abs/2312.13750
