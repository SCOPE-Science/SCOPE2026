# Integral homology of anchored configurations on every connected graph

## Finding

**Theorem.** Let \(G\) be a finite connected graph, viewed as a one-dimensional CW complex (multiple edges and loop edges are permitted). Let \(K\subseteq V(G)\) be a nonempty set of \(r\) distinct anchor vertices. For every integer \(n\geq r\), define the anchored configuration space
\[
\Sigma(G,K,n)=\{(x_1,\ldots,x_n)\in |G|^n:K\subseteq\{x_1,\ldots,x_n\}\}.
\]
Collisions among the labeled coordinates are allowed. Put \(b=|E(G)|-|V(G)|+1\) and \(d=n-r\). Every integral homology group \(H_i(\Sigma(G,K,n);\mathbb Z)\) is free abelian, and its rank depends only on \(b,r,n\).

For \(r\geq2\) and \(t\geq r\), set
\[
f(r,t)=\sum_{h=0}^{r-1}(-1)^h\binom rh(r-h-1)^t;
\]
set \(f(1,t)=0\). When \(d=0\), the only nonzero ordinary homology is
\[
H_0(\Sigma(G,K,r);\mathbb Z)\cong\mathbb Z^{r!}.
\]
When \(d\geq1\), the nonzero possible Betti numbers are exactly
\[
\beta_i=\binom ni b^i \quad (0\leq i<d),
\]
and
\[
\beta_d=\binom nd b^d r!+\sum_{j=0}^{d-1}\binom nj b^j f(r,n-j).
\]
Here \(0^0=1\), and \(H_i=0\) for \(i>d\). In particular, **anchored configurations of any finite connected graph have no integral homology torsion**.

More precisely, choose a spanning tree \(T\) of \(G\), fix \(a\in K\), and attach \(b\) one-cells as loops at \(a\), obtaining \(W=T\vee_a\bigvee^b S^1\). For the natural cellular product CW structure, there is an integral chain isomorphism
\[
C_*(\Sigma(W,K,n);\mathbb Z)
\cong \bigoplus_{j=0}^{n-r}
\left(C_{*-j}(\Sigma(T,K,n-j);\mathbb Z)\right)^{\oplus\binom nj b^j},
\]
using the standard degree-shift boundary convention. The spaces \(\Sigma(G,K,n)\) and \(\Sigma(W,K,n)\) are homotopy equivalent. This chain decomposition is the central structural assertion; the Betti formulas follow from the established tree theorem.

## Assumptions and scope

A product cell of \(G^n\) belongs to the anchored subcomplex if every vertex in \(K\) appears as an individual zero-dimensional coordinate cell. This is exactly the topological subset in the theorem. The coordinates are labeled and may coincide. The hypotheses require only finite connectedness and distinct vertices in \(K\); neither planarity nor graph simplicity is needed. The case \(n<r\) is excluded because the space is empty. All homology is ordinary, integral, and unreduced unless explicitly noted.

The first Betti number \(b\) is the cycle rank, not the number of simple cycles. The formula covers \(b=0\) (trees) and \(b=1\) (unicyclic graphs), but its new scope includes every \(b\geq2\). A graph with one vertex and no edges is permitted, using its trivial one-vertex spanning tree.

## Proof

**1. A homotopy equivalence fixing all anchors.** Let \(T\subseteq G\) be any spanning tree and choose \(a\in K\). For each edge \(e\) outside \(T\), choose an orientation from \(u_e\) to \(v_e\) and introduce a loop \(\lambda_e\) at \(a\) in \(W\). Define \(F:|G|\to |W|\) to be the identity on \(T\), and map the oriented edge \(e\) to the concatenation of the unique tree path from \(u_e\) to \(a\), then \(\lambda_e\), then the tree path from \(a\) to \(v_e\). Define \(Q:|W|\to |G|\) to be the identity on \(T\) and map \(\lambda_e\) to the tree path from \(a\) to \(u_e\), followed by \(e\), followed by the path from \(v_e\) to \(a\).

The composites \(QF\) and \(FQ\) are each homotopic to the identity **relative to every point of \(T\)**. Indeed, their paths on each non-tree edge or added loop reduce to the original edge or loop by deleting an immediate traversal of a tree path followed by its reverse; these path homotopies fix the endpoints, and the maps are already the identity on \(T\). Hence \(F,Q\) are homotopy inverses fixing \(K\) throughout both homotopies. Applying them to all coordinates simultaneously restricts to maps between anchored spaces: if a coordinate equals an anchor, that coordinate stays equal to the same anchor under every map and homotopy. Thus
\[
\Sigma(G,K,n)\simeq\Sigma(W,K,n).
\]
This argument is relative to \(K\) and does not invoke an invalid ordinary configuration-space invariance theorem: collisions are allowed and are essential to the restriction.

**2. Splitting the integral cellular chains.** Give each tree edge and each added loop its usual one-cell CW structure. The product CW cells of \(W^n\) are indexed by a choice of a vertex or edge for each coordinate. A cell lies in \(\Sigma(W,K,n)\) precisely when every anchor occurs among its vertex coordinates. In particular, at most \(n-r\) coordinates can be occupied by a loop one-cell.

For each subset \(J\subseteq\{1,\ldots,n\}\) and choice \(\ell:J\to\{1,\ldots,b\}\), consider the cells whose loop coordinates are exactly those in \(J\), with loop label \(\ell(j)\) in coordinate \(j\). Every remaining coordinate is a tree vertex or tree edge, and the anchor condition on those \(n-|J|\) coordinates is precisely the definition of \(\Sigma(T,K,n-|J|)\). The cellular boundary of every loop one-cell is zero **over \(\mathbb Z\)** because both of its endpoints are the same vertex \(a\). Consequently the cellular differential never changes \(J\) or its loop labels. The chain group therefore splits into integral subcomplexes indexed by \((J,\ell)\).

Choose orientations by placing loop factors first and then the remaining tree factors in increasing coordinate order. The Koszul shuffle sign identifies each subcomplex, with its differential, with the \(|J|\)-fold degree shift of the anchored tree cellular chain complex. There are \(\binom nj b^j\) choices of \((J,\ell)\) for \(j=|J|\), giving the displayed **integral** chain isomorphism. The zero-boundary assertion is valid for CW loops even though the resulting CW structure need not be regular.

**3. Tree homology input, including boundary cases.** Kozlov's Stirling-complex theorem (Theorem 2.5 in the 2022 open-access version) establishes, for \(r\geq2\),
\[
\Sigma(T,K,m)\simeq\bigvee^{f(r,m)} S^{m-r}\qquad(m\geq r).
\]
For \(m=r\), the right side means a disjoint collection of \(r!\) points, equivalently \(f(r,r)=r!-1\) zero-spheres in a wedge. If \(r=1\), the unique-path contraction of \(T\) to its single anchor, applied coordinatewise, contracts \(\Sigma(T,K,m)\) and fixes that anchor. Hence, for \(m>r\), all these tree spaces have \(H_0\cong\mathbb Z\), plus a free group of rank \(f(r,m)\) in degree \(m-r\), and no other homology. For \(m=r\), they have \(H_0\cong\mathbb Z^{r!}\).

**4. Extract all degrees.** Write \(d=n-r\). When \(n=r\), no loop one-cell can occur, and the anchored space consists of the \(r!\) possible vertex assignments. When \(d\geq1\), a summand with exactly \(j<d\) loop coordinates contributes one class in degree \(j\) from the tree's connected \(H_0\), plus \(f(r,n-j)\) classes in total degree \(j+(n-j-r)=d\). The summands with \(j=d\) contribute \(r!\) classes in degree \(d\). Counting the \(\binom nj b^j\) summands in each case proves precisely the two displayed formulas. Since every tree homology group is free and the splitting is integral, no torsion occurs in any degree. \(\square\)

## Verification

The independent-from-the-formula finite checker in `verify_anchored.py` enumerates all anchored cubical cells of each listed finite graph, constructs boundary matrices directly by replacing one oriented edge coordinate by its endpoints, computes ranks by binary Gaussian elimination, and compares resulting mod-two Betti numbers with the stated formula. It covers 14 cases including trees, a cycle with a pendant edge, a wedge of two triangles, four-vertex complete graphs, and one-vertex and one-anchor boundary cases. Running `python3 verify_anchored.py` returned `VERIFY_OK 14 exact cubical boundary-rank comparisons`.

Examples include \(\beta(\Sigma(K_4,\{0,1\},4))=(1,12,121)\), \(\beta(\Sigma(C_3,\{0,1\},4))=(1,4,17)\), \(\beta(\Sigma(G_{\mathrm{two\ triangles}},\{1,3\},4))=(1,8,57)\), and \(\beta(\Sigma(K_4,\{0,1,2\},4))=(1,85)\). These **finite mod-two tests do not establish torsion-freeness**; that follows from the integral chain splitting and the published tree homotopy theorem. The direct checker uses combinatorial cells of the original graphs and therefore also tests the nontrivial relative graph reduction indirectly.

## Relationship to prior work

Kozlov, *Stirling complexes* (first public 2022), proves the tree case and the formula for \(f(r,m)\), including an appendix extending the result to contractible ambient complexes. That theorem supplies an essential input but does not treat noncontractible graphs with positive cycle rank. Kozlov, *Homology and Euler characteristic of generalized anchored configuration spaces of graphs* (arXiv:2309.17149; published 2024), proves an Euler characteristic formula for arbitrary connected graphs and computes the full homology in the circle case. The Euler formula alone does not imply the integral homology decomposition or absence of torsion in positive cycle rank.

Mamun, Nalikka, and Ramos, *Universality in the algebra and topology of cographs* (arXiv:2609.04554, first posted 2026-09-03), define these anchored spaces in Definition 4.13, prove finite generation and a universal torsion-exponent bound over cographs in Corollary 4.18, and explicitly identify the existence of integral torsion in arbitrary anchored graph configuration spaces as unknown. The theorem above settles that specific question negatively and strengthens finite generation to explicit integral ranks for every connected finite graph. Its proof uses neither cograph restrictions nor representation stability.

## Limitations

The result concerns **ordered/labeled particles with collisions allowed and with every selected anchor required to be occupied**. It does not apply to collision-free graph braid configuration spaces, to spaces requiring only some fixed number of anchors to be occupied, or automatically to the unordered quotient. It calculates additive integral homology, not cup products, equivariant homology representations, or the full homotopy type for cyclic graphs. It uses the established homotopy classification of the tree case as an input rather than reproving it. The literature check includes the relevant published primary material and indexed result comparisons, but cannot exclude all unpublished or unindexed equivalent statements. Independent validation has not been performed.

## References

1. A. Mamun, J. Nalikka, E. Ramos, *Universality in the algebra and topology of cographs*, arXiv:2609.04554v1 (submitted 2026-09-03), Section 4.3.1, Definition 4.13, Corollary 4.18 and following discussion. https://arxiv.org/html/2609.04554v1
2. D. N. Kozlov, *Stirling complexes*, *Journal of Applied and Computational Topology* **7** (2023), 57–74; first available 2022-09-24, Theorems 2.1, 2.5 and Appendix Theorem A.1. https://doi.org/10.1007/s41468-022-00096-4
3. D. N. Kozlov, *Homology and Euler characteristic of generalized anchored configuration spaces of graphs*, *Journal of Applied and Computational Topology* **8** (2024), 1053–1068; arXiv:2309.17149, Theorem 2.1, Theorem 4.4 and Corollary 4.6. https://doi.org/10.1007/s41468-024-00167-8
