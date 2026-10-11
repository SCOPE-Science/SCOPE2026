# Two collapsible independence complexes with identical Morse ensembles and different chromatic polynomials

## Finding

Let \(V=\{0,1,\ldots,10\}\) and let \(T_A,T_B\) be the finite simple graphs with edge sets
\[
\begin{aligned}
E(T_A)&=\{(0,1),(0,6),(1,2),(2,3),(3,4),(3,5),(6,7),(6,9),(7,8),(9,10)\},\\
E(T_B)&=\{(0,1),(0,6),(1,2),(2,3),(2,5),(3,4),(6,7),(6,10),(7,8),(8,9)\}.
\end{aligned}
\]
Put \(G_A=\overline{T_A}\) and \(G_B=\overline{T_B}\), where the complements are taken on \(V\). Both independence complexes \(\operatorname{Ind}(G_A)\) and \(\operatorname{Ind}(G_B)\) are collapsible one-dimensional simplicial complexes. They have **equal full Morse-ensemble polynomials**
\[
\Phi(G_A)=\Phi(G_B)
=\sum_{r=1}^{11} a_r z_0^{r}z_1^{r-1},
\qquad (a_1,\ldots,a_{11})
=(11,188,1051,2838,4295,3916,2223,788,169,20,1).
\]
Nevertheless their chromatic polynomials are different, with the exact identity
\[
\chi(G_B;q)-\chi(G_A;q)
=q(q-1)(q-2)(q-3)(q-4)(q-5).
\]
In particular, both graphs have chromatic number \(6\), but the numbers of proper colorings using six labeled colors are \(\chi(G_A;6)=1440\) and \(\chi(G_B;6)=2160\). Thus \(\Phi(G)\) does **not** determine the chromatic polynomial, even when the independence complex is a tree. This answers the chromatic-recovery question raised in Zheng's May 2026 paper negatively.

## Assumptions and scope

All graphs are undirected, finite, loopless, and simple. A tree is viewed as a one-dimensional abstract simplicial complex including every vertex and edge. Its face poset includes nonempty simplices. An acyclic matching on the vertex-edge face poset determines critical vertices and critical edges; its Morse-ensemble polynomial is the generating polynomial \(\mathcal{ME}_K(z_0,z_1)=\sum_M z_0^{c_0(M)}z_1^{c_1(M)}\) over all such matchings. For a graph \(G\), \(\Phi(G)=\mathcal{ME}_{\operatorname{Ind}(G)}\). The chromatic polynomial \(\chi(G;q)\) counts vertex colorings with \(q\) labeled colors in which adjacent vertices have different colors, whether or not each color is used. These conventions match the independent-complex and Morse-ensemble definitions of Zheng [1]. No infinite search or asymptotic claim is made.

## Proof

**1. Independence complexes and topology.** The two displayed graphs \(T_A,T_B\) each have \(11\) vertices and \(10\) edges, and are connected; the latter fact can be checked by traversing their explicitly displayed edges. Hence they are trees. An independent subset of \(G_i=\overline{T_i}\) is exactly a clique of \(T_i\). Since a tree has no triangles, its clique complex consists exactly of its vertices and edges. Therefore \(\operatorname{Ind}(G_i)=T_i\) as abstract simplicial complexes, for \(i\in\{A,B\}\). Every finite tree collapses to a vertex by successively removing a leaf edge together with its leaf vertex, proving collapsibility.

**2. Exact equality of all Morse-ensemble coefficients.** For any tree \(T\) on \(n\) vertices, a discrete Morse matching on its vertex-edge face poset corresponds to a spanning subforest \(F\subseteq E(T)\) with one root chosen in each component. For each forest \(F\), the number of root choices is \(\prod_C |V(C)|\), with the product over components. If \(c(F)\) is the number of components, the matching has exactly \(c(F)\) critical vertices and \(c(F)-1\) critical edges. The matrix-forest theorem (and, equivalently, the graph Morse-ensemble formula in [1, Theorem 4.2] or the rooted-forest formula in [2, Proposition 3.1 and Corollary 3.3]) therefore yields
\[
\mathcal{ME}_T(z_0,z_1)
=\sum_{F\subseteq E(T)}\Bigl(\prod_C |V(C)|\Bigr)
 z_0^{c(F)}z_1^{c(F)-1}
=z_1^{-1}\det(z_0z_1 I_n+L_T),
\]
where \(L_T\) is the ordinary combinatorial graph Laplacian. The apparent negative power cancels because a tree Laplacian has eigenvalue zero.

For the two explicitly given graphs, exact integer arithmetic gives the identical characteristic polynomial
\[
\begin{aligned}
p(t)=\det(tI_{11}-L_{T_i})
={}&t^{11}-20t^{10}+169t^9-788t^8+2223t^7\\
&-3916t^6+4295t^5-2838t^4+1051t^3-188t^2+11t.
\end{aligned}
\]
This identity is reproduced by the stand-alone `verify.py` using Newton identities with exact integer matrix multiplication; the same program independently enumerates all \(2^{10}\) subforests of each tree and checks the weighted forest-expansion coefficients. Since the trees have equal Laplacian characteristic polynomials, the determinant formula gives equal Morse ensembles, with the displayed eleven coefficients. This proves equality of the *entire* critical-vector distribution, not merely equality at a specialization.

**3. Distinct chromatic polynomials.** A proper coloring of \(\overline{T}\) has color classes that are cliques of \(T\). For a tree, every class has size one or two; the size-two classes form a matching. Let \(m_j(T)\) count matchings of cardinality \(j\), including \(m_0(T)=1\). Choosing the \(j\) size-two classes leaves \(n-2j\) singleton classes, so there are \(n-j\) nonempty classes. Assigning distinct labeled colors to these classes gives
\[
\chi(\overline T;q)=\sum_{j=0}^{\lfloor n/2\rfloor}
 m_j(T)\,(q)_{n-j},\qquad
(q)_r=\prod_{s=0}^{r-1}(q-s).
\]
The explicit edge-subset check gives
\[
\begin{aligned}
(m_0(T_A),\ldots,m_5(T_A))&=(1,10,34,46,23,2),\\
(m_0(T_B),\ldots,m_5(T_B))&=(1,10,34,46,23,3).
\end{aligned}
\]
The lists differ only in their last component, so subtracting the two chromatic-polynomial formulas gives \(\chi(G_B;q)-\chi(G_A;q)=(q)_6\) exactly. At \(q=6\), all terms except \(j=5\) vanish, giving \(2\cdot 6!=1440\) and \(3\cdot 6!=2160\). The presence of a five-edge matching and impossibility of a six-edge matching show both graph chromatic numbers are \(11-5=6\). This completes the proof. \(\square\)

## Verification

Run `python3 verify.py` using the Python standard library. The program checks the tree property, independently computes both Laplacian characteristic polynomials with integer Newton identities, enumerates the \(2^{10}\) edge subsets of each tree to determine matching numbers, enumerates their rooted-forest weights independently, and directly counts proper six-colorings of both complement graphs by backtracking. Its successful final line is `VERIFY_OK`. The symbolic proof above gives the exact general counting identities; the finite program supplies reproducible certificates for the two fixed eleven-vertex objects.

## Relationship to prior work

Zheng [1], first posted May 23, 2026, defines the independence Morse ensemble \(\Phi\), proves its relation to graph Laplacian spectra, and explicitly asks whether \(\chi(G;q)\) is recoverable from \(\Phi(G)\) (v1 §8(1); v3 §7(4)). Those results do not state a counterexample: their examples establish the opposite-direction separation that the graph-level Morse ensemble does not determine \(\Phi\). Chari–Joswig [2] derive the rooted-forest/Laplacian enumeration of acyclic matchings on graphs, but they do not define Zheng's independence ensemble or compare it to chromatic polynomials. The present pair combines that topological enumeration with an exact, distinct matching-distribution witness to answer the newer recovery question. Classical spectral coincidences of trees supply context but a coincidence of Laplacian spectra alone does not establish the chromatic difference: the matching counts are separately determined above.

## Limitations

The theorem concerns two specified graphs of order eleven. It does not assert that they are smallest possible, that their higher homotopy data differ (both independence complexes are contractible), or that \(\Phi\) fails to recover all graph-coloring invariants: the exhibited pair has the same chromatic number. The claim depends on the definition of \(\Phi\) used in [1], and assumes ordinary simple graph coloring. Literature searches and same-model review do not amount to independent scholarly refereeing or a guarantee against unindexed equivalent work.

## References

[1] C. Zheng, *On the Morse Ensemble Polynomial of Simplicial Complexes*, arXiv:2605.24689v1 (first public 2026-05-23), and revision v3, §6 and §7. https://arxiv.org/html/2605.24689v1 ; https://arxiv.org/html/2605.24689v3 .

[2] M. K. Chari and M. Joswig, *Discrete Morse Complexes*, arXiv:math/0011234v1 (2000), Proposition 3.1 and Corollary 3.3. https://arxiv.org/pdf/math/0011234 . Published as *Complexes of discrete Morse functions*, Discrete Mathematics 302 (2005), 39–51.

[3] P. Chebotarev and E. Shamis, *The Matrix-Forest Theorem and Measuring Relations in Small Social Groups*, Automation and Remote Control 58 (1997), 1505–1514; foundational determinant/weighted-forest identity used in [1].
