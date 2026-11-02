# Spanning-forest valuation formula and positive class-size polynomials at every congruence level of graphical groups

## Finding
Let \(\Gamma=(V,E)\) be any finite simple graph, \(m=|E|\), and \(\ell\ge1\). Let \(\mathcal O\) be a discrete valuation ring with uniformizer \(\pi\) and finite residue field of cardinality \(q\); put \(R=\mathcal O/(\pi^\ell)\). For each nonnegative integer \(s\), the number of conjugacy classes of size \(q^s\) of the standard graphical group \(\mathbf G_\Gamma(R)\) is a polynomial \(P_{\Gamma,\ell,s}(q)\) whose coefficients in \(q-1\) are nonnegative integers. The polynomial and its finite combinatorial construction are given explicitly below. Thus the same nonnegativity holds for the total class number for *every* graph and congruence level.

Write \(\mathcal A_\ell=\{0,\ldots,\ell\}^V\). For \(a\in\mathcal A_\ell\), a coordinate \(a_v=\ell\) represents the zero element modulo \(\pi^\ell\). For a nonempty forest \(F\subseteq E\), let \(d_F(v)\) denote its degree at \(v\), and let \(\mathcal C^+(F)\) denote its connected components containing an edge. Define
\[
 c_F(a)=\sum_{v:d_F(v)>0}(d_F(v)-1)a_v+
 \sum_{C\in\mathcal C^+(F)}\min_{v\in C}a_v.
\]
Let \(r=|V|-\#\{\text{connected components of }\Gamma\}\). Set \(\Delta_0(a)=0\) and, for \(1\le j\le r\),
\[
 \Delta_j(a)=\min_{F\subseteq E:\ F\text{ a forest},\ |F|=j}c_F(a),
 \qquad d_j(a)=\Delta_j(a)-\Delta_{j-1}(a).
\]
Then \(0\le d_1(a)\le\cdots\le d_r(a)\). Define
\[
 s_\ell(a)=\sum_{j=1}^{r}\max\{\ell-d_j(a),0\},\quad
 h_\ell(a)=\ell m-s_\ell(a),\quad
 b(a)=|\{v:a_v<\ell\}|,\quad
 e_\ell(a)=\sum_{v:a_v<\ell}(\ell-1-a_v).
\]
Both \(h_\ell(a)\) and \(e_\ell(a)\) are nonnegative integers. The claimed polynomial is
\[
 \boxed{P_{\Gamma,\ell,s}(Q)=
 \sum_{\substack{a\in\mathcal A_\ell\\s_\ell(a)=s}}
 (Q-1)^{b(a)}Q^{h_\ell(a)+e_\ell(a)}.}
\]
The total class-number polynomial is \(\sum_sP_{\Gamma,\ell,s}(Q)\). Every summand is visibly nonnegative after the substitution \(Q=1+T\). This formula is valid for connected and disconnected graphs, including isolated vertices and the empty edge set, and in residue characteristic two.

For a non-cograph example, let \(\Gamma=P_4\), the path with four vertices. At level \(\ell=2\),
\[
 k(\mathbf G_{P_4}(R))=q^4(6q^4-q^3-6q^2+q+1).
\]
Its expansion in \(T=q-1\) has coefficients, from degrees \(0\) through \(8\),
\(1,14,73,195,301,280,155,47,6\); all are positive.

## Assumptions and scope
The graphical group is the central extension with underlying set \(R^V\times R^E\), standard multiplication determined by the ordered-edge bilinear cocycle, and commutator
\[
 [(x,z),(y,w)]_e=x_uy_v-x_vy_u\qquad(e=\{u,v\},\ u<v).
\]
This is the usual graphical group scheme associated to \(\Gamma\), not a general group with the same commutator rank. The proof uses that \(\mathcal O\) is a DVR, so Smith normal form exists over \(\mathcal O\); no assumption of odd residue characteristic, unramifiedness, or connectedness is made. The graph and level are fixed, while \(q\) ranges over possible residue-field orders. The formula computes individual class-size strata as well as their sum.

## Proof
**1. Conjugation fibers.** For fixed \(x\in R^V\), conjugation changes only the central coordinate and its possible changes constitute the image of the \(R\)-linear map \(M_x:R^V\to R^E\) with edge row \(e=\{u,v\}\) having entries \(-x_v\) at column \(u\), \(x_u\) at column \(v\), and zero elsewhere. The number of conjugacy classes over this fixed \(x\) is \(|R|^m/|\operatorname{im}M_x|\), and every one of these classes has size \(|\operatorname{im}M_x|\). The total class count is their sum over \(x\).

**2. Units do not matter.** If \(x_v=c_v\pi^{a_v}\pmod{\pi^\ell}\), choose a unit \(c_v\in\mathcal O^\times\) for \(a_v<\ell\); when \(x_v=0\), take \(a_v=\ell\) and \(c_v=1\). Multiplying vertex columns and edge rows of \(M_x\) by the corresponding unit diagonal matrices reduces it modulo \(\pi^\ell\) to the matrix \(M_a\) obtained from the formal lift \(x_v=\pi^{a_v}\in\mathcal O\). Thus the image order and class sizes depend only on \(a\), including coordinates equal to \(\ell\).

**3. Forest minors.** Fix an arbitrary orientation of \(\Gamma\), and let \(B\) be its edge-by-vertex oriented incidence matrix, with each row having entries \(-1\) and \(+1\). Over the fraction field of \(\mathcal O\),
\[
 M_a=D_E B D_V^{-1},\quad
 (D_E)_{e,e}=\pi^{a_u+a_v},\quad
 (D_V)_{v,v}=\pi^{a_v}.
\]
Consequently, for edge set \(F\) and column set \(C\) of the same cardinality, the corresponding minor is
\[
 \det(M_a[F,C])=\det(B[F,C])\,
 \pi^{\sum_{\{u,v\}\in F}(a_u+a_v)-\sum_{v\in C}a_v}.
\]
The oriented incidence matrix is totally unimodular: its square minors are \(0,1,-1\). A minor \(\det B[F,C]\) is nonzero precisely when \(F\) is a forest and \(C\) contains every vertex incident to \(F\) except exactly one vertex from each nontrivial connected component. This characterization follows also by independently eliminating leaves of each tree: a component with \(t\) vertices contributes rank \(t-1\), and deleting one root column makes its reduced incidence matrix unimodular. Choosing the omitted root with minimum \(a_v\) in each component minimizes the valuation and gives exactly \(c_F(a)\).

**4. Smith exponents.** The minimum \(\pi\)-adic valuation of a nonzero \(j\)-minor over \(\mathcal O\) is therefore \(\Delta_j(a)\). Since the fraction-field rank is \(r=|V|-\#\mathrm{components}(\Gamma)\), Smith normal form gives nonzero elementary divisors \(\pi^{d_j(a)}\), \(j=1,\ldots,r\), with \(d_j(a)=\Delta_j(a)-\Delta_{j-1}(a)\). Reducing the Smith decomposition modulo \(\pi^\ell\) proves
\[
 |\operatorname{im}M_a|=q^{s_\ell(a)}.
\]
In particular \(0\le s_\ell(a)\le\ell m\) and \(h_\ell(a)\ge0\), even when some \(a_v=\ell\); no illicit division occurs in \(R\), because the diagonal factorization above took place over the DVR fraction field before reduction.

**5. Enumerate valuations.** For each \(0\le j<\ell\), there are exactly \((q-1)q^{\ell-j-1}\) elements of valuation \(j\) in \(R\); there is one zero element of valuation \(\ell\). Hence exactly \((q-1)^{b(a)}q^{e_\ell(a)}\) vectors have valuation profile \(a\). Each contributes \(q^{h_\ell(a)}\) classes, all of size \(q^{s_\ell(a)}\). Summing gives the boxed formula. Since \(Q^d=(1+(Q-1))^d\) for every nonnegative integer \(d\), the coefficientwise \((Q-1)\)-positivity is immediate. This proves the theorem.

## Verification
The standalone `verify.py` builds the spanning-forest minima and class-size profile without relying on precomputed polynomials; for comparison it independently enumerates actual commutator matrices and their integer-minor valuations on small rings and directly enumerates commuting ordered pairs. It checks non-cographs \(P_4\), \(C_5\), and a diamond graph, along with complete graphs, bipartite graphs, and cycles. The script reports `VERIFY_OK 44`, including characteristic two, level two, and positivity at levels one through three. The \(P_4\) level-two polynomial additionally matches the coefficient obtained from the published local zeta function of Rossmann and Voll. Exhaustive finite cases are evidence for, not a substitute for, the general proof above. Run with `python3 verify.py` (Python standard library only).

## Relationship to prior work
Rossmann and Voll, *Groups, graphs, and hypergraphs: average sizes of kernels of generic matrices with support constraints*, arXiv:1908.09589 (initially public 26 August 2019), establish polynomial class numbers for every graph and level, positive \((q-1)\)-coefficients for cographs (Theorem E), and ask explicitly in Question 1.7 which other graphs have this positivity. They tabulate local zeta functions for small graphs, including non-cographs. The present finite spanning-forest formula gives positive class-size polynomials for every graph and every finite level; its total class-number specialization answers that question affirmatively. It does **not** give a compact rational closed form of the complete zeta function or address analytic poles.

Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564 (initially public 12 July 2021), already proves \((q-1)\)-positivity of class-size polynomials for **every graph at level one** (Corollary C), and discusses the higher-congruence-level gap in Section 8. The level-one specialization is therefore prior work, not newly asserted. The contribution is the valuation-minor construction and all levels \(\ell\ge2\) for arbitrary graphs. Related character-degree enumeration for trees and cycles treats a different statistic and does not imply these class-size polynomials.

## Limitations
The explicit finite sum can be exponential in the vertex count and congruence level, so it is not a polynomial-time algorithm. The result does not claim new rationality, uniformity, or a compact denominator for the full class-counting zeta function, which were studied earlier. The theorem applies to standard graphical groups over quotients of DVRs; no assertion is made here about arbitrary principal-ideal rings without a DVR model. All claims have undergone self-review only; independent external mathematical audit and publication-priority verification remain outstanding. The possibility that a broader, previously published forest-minor or valuation-invariant theorem implies this special case is a residual novelty risk.

## References
1. T. Rossmann and C. Voll, *Groups, graphs, and hypergraphs: average sizes of kernels of generic matrices with support constraints*, arXiv:1908.09589, first posted 2019-08-26, Theorem E and Question 1.7, https://arxiv.org/html/1908.09589v2.
2. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564, first posted 2021-07-12, Corollary C and Section 8, https://arxiv.org/abs/2107.05564; published *Bull. London Math. Soc.* 54 (2022), 1923–1943, https://doi.org/10.1112/blms.12665.
