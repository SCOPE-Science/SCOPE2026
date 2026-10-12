# Super-domination polynomial of arbitrary heterogeneous pendant coronas

## Finding
Let \(G=(V,E)\) be an arbitrary finite simple graph with \(n=|V|\ge1\). To each base vertex \(v\) attach an independent bundle of \(r_v\ge1\) new vertices, each adjacent only to \(v\); call the resulting graph \(H\). Write \(R=\sum_{v\in V}r_v\) and \(M=n+R\). A super dominating set \(S\subseteq V(H)\) is one for which every \(w\in V(H)\setminus S\) admits \(u\in S\) with \(N_H(u)\cap (V(H)\setminus S)=\{w\}\). Let
\[
D_{sp}(H;x)=\sum_{S\,\mathrm{super\ dominating}}x^{|S|}.
\]
For \(U\subseteq V\), set \(N_G(U)=\bigcup_{u\in U}N_G(u)\), \(N_G[U]=U\cup N_G(U)\), and \(B_G(U)=N_G(U)\setminus U\). Empty products are one. Then, for every such \(G\) and every choice of positive pendant multiplicities,
\[
\boxed{D_{sp}(H;x)=x^R\sum_{U\subseteq V}x^{|B_G(U)|}\prod_{v\in V\setminus N_G[U]}(x+r_v).}
\]
The constant term of the factor after \(x^R\) is positive. Consequently the minimum size is \(\gamma_{sp}(H)=R\), and its exact multiplicity is
\[
\boxed{[x^R]D_{sp}(H;x)=\prod_{C\in\mathrm{Comp}(G)}\left(1+\prod_{v\in C}r_v\right).}
\]
A second structural consequence, with \(M=n+R\), is
\[
\boxed{[x^{M-2}]D_{sp}(H;x)=\binom M2-\sum_{v\in V}\left(\binom{r_v}2+r_v\right)-\sum_{\{u,v\}\in E}(r_u+r_v).}
\]
For common bundle size \(r_v=r\), this coefficient equals \(\binom{n(r+1)}2-n\binom r2-nr-2r|E|\). Thus the complete polynomial determines the edge count of the base when \(n\) and \(r\) are given. The minimum-set multiplicity is \(\prod_C(1+r^{|C|})\), and it equals \(2^{c(G)}\) for \(r=1\).

## Assumptions and scope
Graphs are finite, undirected, loopless, and without parallel edges. The base may be disconnected and may contain isolated vertices; its order is at least one. All pendant multiplicities are positive integers, possibly unequal. Each pendant is a degree-one vertex and pendant vertices are mutually nonadjacent, even within a bundle. The variable \(x\) is an indeterminate, not a fixed evaluation point. The sum counts labeled vertex *subsets* rather than the number of private-neighbor witness assignments. \(\mathrm{Comp}(G)\) denotes the vertex sets of the connected components of \(G\).

## Proof
For any candidate set \(S\subseteq V(H)\), write \(O=V(H)\setminus S\) for its omitted vertices, let \(U=O\cap V\) be the omitted original vertices, and let \(L_v\) be the private pendant bundle at \(v\).

**Local obstruction.** If two different vertices of \(L_v\) lie in \(O\), neither can have a selected private neighbor: their only possible witness is \(v\), which has at least two omitted neighbors. Hence every bundle contains at most one omitted pendant. If \(v\in U\), no pendant of \(L_v\) can be omitted, since that pendant has only the omitted vertex \(v\) as its neighbor. Finally, if one pendant of \(L_v\) is omitted, then \(v\in S\) must witness it. Therefore every base neighbor of \(v\) must be selected: \(N_G(v)\cap U=\varnothing\). These necessary conditions say that omitted pendants occur only at vertices \(v\in F(U):=V\setminus N_G[U]\), with at most one omitted pendant per such vertex. Note that an omitted base root cannot host an omitted pendant.

**Sufficiency.** Conversely, choose *any* \(U\subseteq V\) as the omitted base vertices. For each \(v\in F(U)\), choose either no omitted pendant, or exactly one of its \(r_v\) pendants; omit none from other bundles. Every omitted base vertex \(u\in U\) is witnessed by any one of its selected pendant neighbors, which exists because \(r_u\ge1\). Every omitted pendant at \(v\in F(U)\) is witnessed by its selected base vertex \(v\): there is exactly one omitted pendant in its bundle and, by the definition of \(F(U)\), it has no omitted base neighbor. Thus all omitted vertices have witnesses and the construction is super dominating. The two directions give a bijection, including the case \(U=\varnothing\).

**Enumeration.** For fixed \(U\), vertices in \(U\) and the \(n-|U|\) other base vertices have prescribed selection status. At each vertex in \(F(U)\), exactly one of \(r_v+1\) possibilities applies: omit nothing (weight \(x\) when counting selections) or omit one of \(r_v\) leaves (weight \(r_v\)). The other private leaves must all be selected. If \(B=B_G(U)\), then \(V=U\sqcup B\sqcup F(U)\), so the fixed-\(U\) weighted count is
\[
x^{M-|U|-|F(U)|}\prod_{v\in F(U)}(x+r_v)
=x^{R+|B_G(U)|}\prod_{v\in F(U)}(x+r_v).
\]
Summing over \(U\) proves the polynomial identity, with no multiplicity overlap because \(U\) is recoverable from the selected set.

**Smallest cardinality and its multiplicity.** All summands are divisible by \(x^R\), and taking \(U=V\) gives \(x^R\), so \(\gamma_{sp}(H)=R\). A term contributes to \([x^R]\) exactly when \(B_G(U)=\varnothing\), meaning \(U\) is a union of connected components, and one always chooses an omitted pendant at every vertex outside \(U\). Such a component \(C\) contributes either \(1\) if it is in \(U\), or \(\prod_{v\in C}r_v\) if outside. Multiplying the independent component choices yields the displayed factorization.

**Coefficient of two omissions.** Every single vertex omission from \(H\) is permissible; for two omitted vertices, the above bijection fails exactly in one of three mutually exclusive cases: (i) two pendants from the same bundle, giving \(\sum_v\binom{r_v}{2}\); (ii) one base root and its own pendant, giving \(\sum_v r_v\); (iii) a base root \(u\) and a pendant attached at a distinct adjacent base vertex \(v\), giving \(\sum_{\{u,v\}\in E}(r_u+r_v)\). Two base vertices are always permitted, as are pendants at distinct roots. Subtracting forbidden pairs from \(\binom M2\) proves the last formula. It also holds for \(M=2\), when the coefficient is zero.

## Verification
The accompanying Python 3 standard-library script `verify_super_leafbundles.py` independently evaluates the graph-neighborhood definition for all selected subsets and compares exact degree distributions against the boundary-sum formula. It checks all labeled simple bases on one through four vertices with pendant multiplicities in \(\{1,2\}\), followed by seeded five- and six-vertex graphs with pendant multiplicities in the same set. It checks 1,150 instances and 2,435,884 individual candidate sets, the minimum-set component product, and the two-omission coefficient. All comparisons passed; sample exact polynomials and counts appear in `verification_output.txt`. Run with `python3 verify_super_leafbundles.py`. Finite verification corroborates but does not replace the proof for arbitrary base graphs and multiplicities.

## Relationship to prior work
Klein, Rodríguez-Velázquez, and Yi [1, Theorem 18] proved that the scalar super domination number of the ordinary corona \(G\odot N_r\) is \(nr\). That scalar special case is **prior work**; it does not state or imply the full distribution of super dominating subsets, their component-dependent minimum multiplicities, or the weighted coefficient encoding base edges. Ghanbari, Jäger, and Lehtilä [2] study the *neighborhood corona* operation, other products, and minimum-set counts for particular graph classes; the neighborhood corona is not the pendant construction here. Kaidash [3] introduces a super-domination polynomial and states polynomials for complete graphs, stars, complete bipartite graphs and a universal-vertex construction. Those base graph formulas are not a polynomial identity for all heterogeneous pendant coronas. A later chapter by Kaidash [4] discusses polynomials for unspecified families in its accessible abstract; its full chapter could not be compared, so potential implicit prior coverage is unresolved. The claimed contribution here is the complete pendant-corona enumerator and its consequences, not the earlier scalar value or the definition of the polynomial.

## Limitations
The formula relies on pendant bundles of **independent degree-one leaves**, at least one per base vertex. It does not apply without modification to private cliques, general attached rooted graphs, or bundles of size zero. For an arbitrary base graph it is an exact \(2^n\)-term expression, not a polynomial-time algorithm. The proof is mathematical and does not imply that a complete search of prior mathematics is possible. A relevant later chapter was accessible only as an abstract; an unindexed or implicitly equivalent previous counting formula is a residual originality risk. No independent validation has been performed.

## References
[1] D. J. Klein, J. A. Rodríguez-Velázquez, E. Yi, *On the super domination number of graphs*, arXiv:1705.00928 (first public 2 May 2017), Theorem 18, https://arxiv.org/abs/1705.00928.

[2] N. Ghanbari, G. Jäger, T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795 (first public 5 September 2022), https://arxiv.org/abs/2209.01795.

[3] P. A. Kaidash, *Investigation of a Super Domination Polynomial* [Russian], *Mathematics in the Modern World*, Vologda, 2023, pp. 31–33, https://publications.hse.ru/pubs/share/direct/863109231.pdf.

[4] P. A. Kaidash, *Super Domination Polynomial of a Graph*, MOTOR 2024 proceedings, DOI 10.1007/978-3-031-73365-9_6; first online 20 December 2024, https://doi.org/10.1007/978-3-031-73365-9_6.
