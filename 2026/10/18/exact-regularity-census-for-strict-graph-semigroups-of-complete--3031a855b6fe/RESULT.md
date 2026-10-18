# Exact regularity census for strict graph semigroups of complete multipartite graphs

## Finding
Let \(r\geq3\) and let \(G=K_{n_1,\ldots,n_r}\), with every \(n_i\geq1\) and \(N=\sum_i n_i\). Write \(\mathrm{St}(G)\) for the finite semigroup of partial maps whose nonempty fibers are edges and whose images are independent sets, with the empty map included. The following gives **all rank-refined element, regular-element, and idempotent counts**.

For \(k\geq1\), set \(s_k=\sum_i\binom{n_i}{k}\) and
\[
 m_k=\sum_{\substack{a_{ij}\in\mathbb Z_{\geq0}\ (i<j),\;\sum_{i<j}a_{ij}=k\\ d_i=\sum_{j<i}a_{ji}+\sum_{i<j}a_{ij}\leq n_i}}
 \frac{\prod_{i=1}^{r}(n_i)_{d_i}}{\prod_{i<j}a_{ij}!},
 \qquad
 b_k=\sum_{i=1}^{r}\binom{n_i}{k}(N-n_i)_k
 -\sum_{i<j}\binom{n_i}{k}(n_j)_k.
\]
Here \((u)_k=u(u-1)\cdots(u-k+1)\), with \((u)_0=1\) and \((u)_k=0\) for \(k>u\), and likewise \(\binom uk=0\) for \(k>u\). Then the exact counts of maps, regular maps, and idempotents of rank \(k\) are respectively
\[
 \boxed{T_k=k!\,s_km_k,\qquad R_k=k!\,s_kb_k,\qquad E_k=\sum_i\binom{n_i}{k}(N-n_i)_k.}
\]
At rank zero all three counts equal one. At \(k>\min(\lfloor N/2\rfloor,\max_i n_i)\), all counts vanish.

**Regularity classification.** The entire semigroup \(\mathrm{St}(G)\) is regular exactly in the following cases:
\[
\boxed{
 r=3\ \text{and}\ (\min_i n_i=1\ \text{or}\ \max_i n_i\leq2),
 \quad\text{or}\quad
 r\geq4\ \text{and}\ \max_i n_i=1.
}
\]
In particular, \(K_{2,2,2}\) is a non-bipartite regular example, but \(K_{2,2,3}\) is not. The latter has \(1021\) strict maps, of which \(877\) are regular, and \(133\) are idempotents.

**Polynomial rarity.** For every fixed integer \(n\geq2\) and \(r\to\infty\), the semigroup associated to \(r\) parts each of size \(n\) satisfies
\[
\boxed{
 \frac{|\operatorname{Reg}\mathrm{St}(K_{\underbrace{n,\ldots,n}_{r}})|}{|\mathrm{St}(K_{\underbrace{n,\ldots,n}_{r}})|}
 \sim\frac{2^n n!}{n^n}\,r^{-(n-1)}.
}
\]
This is a polynomial, rather than exponential, decay law, with an explicit constant and exponent.

## Assumptions and scope
A complete multipartite graph has disjoint nonempty vertex parts \(V_1,\ldots,V_r\) of sizes \(n_1,\ldots,n_r\), with an edge exactly between vertices of distinct parts. The image of a partial map is its set of defined values; its rank is the image cardinality. The strict semigroup consists of exactly those maps arising by choosing a matching \(M\) of \(k\) graph edges, choosing an independent \(k\)-vertex image set \(I\), and assigning distinct vertices of \(I\) to the edges of \(M\), collapsing each edge to its assigned vertex. Regular means that some element \(g\) of the same semigroup obeys \(fgf=f\); idempotent means \(f^2=f\). All assertions are for finite labeled graphs and exact integer counts; no limiting claim is made when the part size grows with \(r\).

## Proof
**(1) Matching count.** For a matching of \(k\) edges, let \(a_{ij}\) be the number of edges between \(V_i\) and \(V_j\), and let \(d_i=\sum_{j\ne i}a_{\min(i,j),\max(i,j)}\). The \(d_i\) vertices incident to those edges in part \(i\) are distinct, hence \(d_i\leq n_i\). Choose ordered endpoints for all incident pair-types in \((n_i)_{d_i}\) ways. Simultaneously permuting the \(a_{ij}\) paired endpoints on both sides does not change the matching, so divide by \(a_{ij}!\) for each \(i<j\). Summing gives \(m_k\). Every independent nonempty vertex set of a complete multipartite graph lies in exactly one part, giving \(s_k\) choices for the image. Bijections from the \(k\) matching edges to the image set give \(k!\) strict maps, hence \(T_k\).

**(2) Regularity, with both directions reconstructed.** Fix a strict map \(f\) with domain matching \(M\) and image \(I\subseteq V_j\), both of size \(k\geq1\). If \(fgf=f\), then \(g\) chooses, for each \(y\in I\), one endpoint \(g(y)\) of the unique matching edge \(f^{-1}(y)\). These chosen endpoints are distinct and belong to the independent image set of the strict map \(g\). In a complete multipartite graph an independent set lies in one part, so **all edges of \(M\) meet one common part**.

Conversely suppose all edges of \(M\) meet the same part \(V_i\). Select one endpoint \(t_y\in V_i\) from each edge \(f^{-1}(y)\); these endpoints are independent. Every edge of \(M\) meets the complement of \(V_j\), so its \(k\) disjoint edges prove \(N-n_j\geq k\). Choose distinct \(k\) vertices outside \(V_j\) and pair them with the \(k\) vertices of \(I\), forming a matching \(M'\). Define \(g\) on each edge of \(M'\) to have the constant value \(t_y\) associated to its endpoint \(y\in I\). Then \(g\) has edge fibers and an independent image, so \(g\in\mathrm{St}(G)\), and \(fgf=f\). Thus the common-incident-part property is necessary and sufficient for regularity.

**(3) Count common-part matchings.** The matchings of size \(k\) whose every edge meets \(V_i\) number \(\binom{n_i}{k}(N-n_i)_k\): select \(k\) vertices in \(V_i\) and inject them into the complementary vertices. The intersection of the corresponding conditions for distinct parts \(V_i,V_j\) consists exactly of matchings entirely between those two parts, counted by \(\binom{n_i}{k}(n_j)_k\). No matching with \(k\geq1\) can have every edge incident to three distinct parts simultaneously. Inclusion-exclusion therefore yields \(b_k\). Since regularity depends only on the matching, \(R_k=k!s_kb_k\).

**(4) Idempotents.** If \(f^2=f\), every image vertex must lie in its own fiber, since \(f(y)=y\) for \(y\) in the image. These are one chosen endpoint from every matching edge; their independence forces them into a common part \(V_i\). Conversely any \(k\)-element subset of \(V_i\), together with an injection from it into the complement, determines a unique idempotent by collapsing each selected edge onto its endpoint in \(V_i\). Different choices give different maps. This proves \(E_k\).

**(5) Which graphs are regular?** With three parts, a matching having no common incident part must contain edges of all three pair-types \(\{1,2\},\{1,3\},\{2,3\}\). Such a matching requires at least two vertices in each part and has at least three edges. Conversely, when all three part sizes are at least two, choose three disjoint edges of these three types; if some part has size at least three, choose an independent image of size three there to construct a nonregular strict map. If any part is a singleton, such a matching is impossible; if the largest part has size at most two, no image of size three exists. For \(r\geq4\), if all parts are singletons every independent image has size at most one and hence every strict map is regular. If some part has size at least two, choose two disjoint edges between four different parts, and use two vertices of the nonsingleton part as independent image; the resulting strict map fails the common-part criterion. This proves the classification.

**(6) Asymptotic.** Fix \(n\geq2\) and take all \(n_i=n\), so \(N=nr\) and possible ranks satisfy \(k\leq n\). For fixed \(k\leq n\), the complete graph has \((N)_{2k}/(2^k k!)\) matchings of size \(k\). Matchings containing an edge within one of the \(r\) parts contribute only \(O(r^{2k-1})\), since there are \(O(r)\) such forbidden edges and \(O(r^{2k-2})\) ways to choose other edges. Therefore
\[
 m_k=\frac{n^{2k}}{2^k k!}r^{2k}+O(r^{2k-1}).
\]
Here \(s_k=r\binom nk\). The top rank hence dominates the total with
\[
 |\mathrm{St}(G)|=\frac{n^{2n}}{2^n}r^{2n+1}+O(r^{2n}).
\]
For the common-part matching count, the exact formula gives
\[
 b_n=r(N-n)_n-\binom r2(n)_n
 =n^n r^{n+1}+O(r^n),
\]
while for \(1\leq k<n\), the bound \(b_k=O(r^{k+1})\) holds. Thus the regular top-rank term dominates and
\[
 |\operatorname{Reg}\mathrm{St}(G)|=n!n^n r^{n+2}+O(r^{n+1}).
\]
The ratio of these two expressions proves the displayed asymptotic, indeed with relative error \(O(1/r)\). No probabilistic approximation or unproved independence hypothesis is used.

## Verification
Run the included standalone `verify.py` under Python 3 (no third-party libraries). The program independently enumerates all matchings and independent images on fifteen graph profiles, compares each rank of \(T_k,R_k,E_k\) against the closed integer formulas, and checks the regularity trichotomy. It additionally constructs every strict partial map and tests existence of an explicit inner inverse \(g\) by exhaustive composition on four profiles. All checks passed. Representative output: \(K_{2,2,2}\) has \((253,253,61)\) total/regular/idempotent maps, while \(K_{2,2,3}\) has \((1021,877,133)\). Finite enumeration supports, but is not a substitute for, the six proof steps above.

## Relationship to prior work
Margolis and Rhodes (arXiv:2609.39370, first made public September 30, 2026) introduce the strict subsemigroup as used here, prove the general matching/transversal/covering characterization (their Theorem 7.1), and investigate regularity for paths, cycles, and bipartite graphs. The present theorem **does not claim that general criterion** as new. Its subject is the *evaluated, exact multipartite rank census*, complete non-bipartite regularity classification, and sharp fixed-part-size polynomial rarity constant, none of which is stated by that paper. Their earlier arXiv:2005.02606 gives singular-map counts for the equal-size complete bipartite case, which is not being re-claimed. The bipartite equal-size specialization is consistent with it.

## Limitations
This concerns the edge-fiber strict subsemigroup, **not** the full Margolis–Rhodes monoid, nor the older convention that adjoins graph automorphisms to strict singular maps. It is an exact theorem for complete multipartite graphs with at least three parts, not a classification of all graphs in the source's open problem. The asymptotic fixes \(n\geq2\) while the number of parts grows. Literature coverage cannot establish absolute novelty; a hidden earlier multipartite enumeration remains possible. Independent auditing has not been performed.

## References
1. Stuart Margolis and John Rhodes, *The Margolis-Rhodes Monoid of a Graph*, arXiv:2609.39370, first public September 30, 2026, especially Lemma 3.3 and Theorem 7.1. https://arxiv.org/abs/2609.39370
2. Stuart Margolis and John Rhodes, *Degree 2 Transformation Semigroups as Continuous Maps on Graphs*, arXiv:2005.02606, especially Example 2.11 for complete bipartite graphs. https://arxiv.org/abs/2005.02606
