# Forced-colouring polynomials of complete multipartite graphs beyond one extra colour

## Finding

**Theorem (forced-completion classification, exact enumerator and minimum seed).** Let \(r\ge3\), let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with nonempty labeled parts \(V_i\) of sizes \(n_i\ge1\), and set \(N=\sum_i n_i\). Fix an integer palette size \(\lambda\ge r+2\). An initially partially coloured graph is *forced* when repeated applications of the following rule reach a proper total colouring: an uncoloured vertex seeing exactly \(\lambda-1\) different colours on its already coloured neighbours takes the unique missing colour. Zero applications are allowed.

For any proper total colouring \(\phi\), let \(t_i\) be the number of colours actually occurring on \(V_i\), let \(T=\sum_i t_i\), and let \(M=\{i:t_i=1\}\). Distinct parts use disjoint colour sets. A restriction of \(\phi\) is forcing **if and only if** either it is the whole colouring or all of the following hold:

1. \(T=\lambda\), so every palette colour occurs in the completed colouring.
2. Every part with \(t_i\ge2\) is already entirely coloured initially.
3. Every monochromatic part except possibly one contains an initially coloured vertex.

The forced completion is unique. Write \(\left\{\begin{smallmatrix}n\\t\end{smallmatrix}\right\}\) for a Stirling number of the second kind, \((\lambda)_T=\lambda!/(\lambda-T)!\), and \(A_i(x)=(1+x)^{n_i}-1\). For every profile \(\mathbf t=(t_1,\ldots,t_r)\) with \(1\le t_i\le n_i\), let \(M(\mathbf t)=\{i:t_i=1\}\) and define

\[
B_{\mathbf t}(x)=x^{\sum_{i\notin M(\mathbf t)}n_i}\left(\prod_{i\in M(\mathbf t)}A_i(x)+\sum_{j\in M(\mathbf t)}\prod_{i\in M(\mathbf t)\setminus\{j\}}A_i(x)\right).
\]

Empty products equal \(1\). The proper-colouring number is

\[
P_G(\lambda)=\sum_{\substack{1\le t_i\le n_i\\T\le\lambda}}(\lambda)_T\prod_{i=1}^{r}\left\{\begin{smallmatrix}n_i\\t_i\end{smallmatrix}\right\}.
\]

Let \(F_{G,\lambda}(x)=\sum_f x^{|\operatorname{dom}f|}\), summed over **all labeled forcing partial assignments**. Then the complete all-coefficient formula is

\[
\boxed{F_{G,\lambda}(x)=P_G(\lambda)x^N+\lambda!\!\sum_{\substack{1\le t_i\le n_i,\ T=\lambda\\M(\mathbf t)\ne\varnothing}}\left(\prod_i\left\{\begin{smallmatrix}n_i\\t_i\end{smallmatrix}\right\}\right)\bigl(B_{\mathbf t}(x)-x^N\bigr).}
\]

In Farr's random-partial-assignment model, each particular colour is assigned with probability \(p\), leaving a vertex blank with probability \(1-\lambda p\). Thus, for \(0\le p\le 1/\lambda\), the forced-colouring probability is the polynomial extension of

\[
\operatorname{FC}_{\lambda}(G;p)=(1-\lambda p)^N F_{G,\lambda}\left(\frac{p}{1-\lambda p}\right).
\]

There is also an exact minimum forcing-domain formula. Put \(k=\lambda-r\), \(c_i=n_i-1\), and

\[
\sigma(k)=\min\left\{\sum_{i\in H}c_i:\ H\subsetneq\{1,\ldots,r\},\ |H|\le k\le\sum_{i\in H}c_i\right\},
\]

with \(\min\varnothing=+\infty\). Then the least number of initially coloured vertices among forcing assignments is

\[
\boxed{s_{\lambda}(G)=\min\{N,\ r-1+\sigma(\lambda-r)\}.}
\]

This gives an integer-capacity subset-sum criterion for the existence of a forcing assignment with blanks. The theorem is new in scope for \(r\ge3\) and \(\lambda\ge r+2\); chromatic-palette, one-extra-colour, and bipartite cases were treated separately before.

## Assumptions and scope

All graph parts are nonempty and labeled, all available colours are distinguishable, and \(r\ge3\), \(\lambda\ge r+2\) are integers. Properness means no edge has equally coloured endpoints. The number of available colours may exceed \(N\); unused palette colours are then permitted in a proper total colouring, though they cannot appear in any nontrivial forcing completion. Counting weights refer to initially coloured vertices, not to forces performed. The formula uses no unspecified limiting process. The results also algebraically specialize to smaller palette sizes, but novelty is claimed **only** beyond one extra colour for genuine multipartite graphs.

## Proof

**Lemma 1 (restriction of every completion).** If a partial assignment forces a proper total colouring \(\phi\), the initial colours are a restriction of \(\phi\). In a complete multipartite graph, colour sets on different parts of a proper colouring are disjoint. Therefore \(1\le t_i\le n_i\), \(T\le\lambda\), and every such profile is realizable exactly when these inequalities hold.

**Lemma 2 (a forced vertex forces monochromaticity and full palette use).** If an uncoloured vertex \(v\in V_i\) is forced at any step, it sees \(\lambda-1\) distinct colours outside \(V_i\) and takes the last colour. In the final proper colouring, the colour set on \(V_i\) is disjoint from all outside-part colours, hence is contained in the single missing colour. Thus \(t_i=1\). The \(\lambda-1\) outside colours and the last colour all occur, so \(T=\lambda\). Consequently no vertex in a part with \(t_i\ge2\) can ever be forced; all such vertices must have been initially coloured.

**Lemma 3 (at most one seedless monochromatic part).** Assume a forcing restriction is not total. By Lemma 2 its completion uses all \(\lambda\) colours and all polychromatic parts are initially full. If two monochromatic parts were initially completely blank, their two distinct palette colours would be absent from the initially coloured vertices. At the initial step no vertex could therefore see \(\lambda-1\) different coloured-neighbour colours. No first forcing move would exist, a contradiction.

Conversely, suppose the three stated conditions hold. With every monochromatic part seeded, any remaining blank vertex is in a monochromatic part and already sees all \(\lambda-1\) other colours among its initially coloured neighbours, so it is forced. If exactly one monochromatic part \(V_j\) is completely seedless, a vertex in \(V_j\) sees all \(\lambda-1\) other colours, and is forced first; after that step every part is seeded, reducing to the previous case. The completed colouring is unique because each local move assigns the only allowable colour. Total proper assignments require no moves. This proves the classification, including all boundary cases.

**Enumeration.** Fix a profile \(\mathbf t\). To build proper total colourings, partition each labeled part \(V_i\) into \(t_i\) nonempty colour classes in \(\left\{\begin{smallmatrix}n_i\\t_i\end{smallmatrix}\right\}\) ways, then injectively assign \(T\) distinct palette colours to all those classes, in \((\lambda)_T\) ways. Summation gives \(P_G(\lambda)\). For a fixed completed colouring using all colours and having at least one monochromatic part, every polychromatic part contributes \(x^{n_i}\) (all initially coloured). A monochromatic part may contribute any nonempty seed subset, with polynomial \(A_i(x)\), except that exactly one such part may be seedless, contributing \(1\). These mutually exclusive alternatives give \(B_{\mathbf t}(x)\). Every total proper colouring was already counted once in \(P_G(\lambda)x^N\), so subtract its \(x^N\) monomial from the profile contribution. Each non-total forcing assignment has a **unique** forced completion, preventing double counting. This proves the boxed polynomial. Replacing the weight of a seed by \(p\) and an uncoloured vertex by \(1-\lambda p\) yields the probability identity for \(p<1/\lambda\); polynomial identity extends to the endpoint.

**Minimum domain.** Set \(H=\{i:t_i\ge2\}\) for a non-total forcing assignment. Since \(T=\lambda\), there are \(k=\lambda-r\) extra colours beyond one per part, allocated among the parts in \(H\). Each receives at least one and at most \(c_i=n_i-1\) extra colours. Thus \(H\subsetneq[r]\) and \(|H|\le k\le\sum_{i\in H}c_i\). The classification forces all \(\sum_{i\in H}n_i\) vertices in those parts to be seeded and at least one seed in all but one of the remaining \(r-|H|\) monochromatic parts. Hence every such assignment has at least

\[
\sum_{i\in H}n_i+(r-|H|-1)=r-1+\sum_{i\in H}c_i
\]

seeds. Conversely, for every such \(H\), distribute \(k\) extra colours so that each part in \(H\) receives between one and \(c_i\) extras; this is possible precisely by the inequalities. Choose any surjective proper colouring with that profile, seed all vertices in \(H\), seed one vertex in each monochromatic part except one, and force the rest. Its domain meets the lower bound. Finally, full proper assignments always exist and have \(N\) seeds, even if \(\lambda>N\). Minimizing over these cases proves the formula.

## Verification

A standalone standard-library-only program, `verify_forced_multipartite.py`, independently enumerates random-model states by looping over **every** assignment of either a blank or one of \(\lambda\) colours at each vertex, checks properness directly, applies the iterative rule, and compares every seeded-domain coefficient with an independently implemented Stirling-profile formula and the exact minimum domain. On 15 multipartite part-size profiles it completed 48 palette-profile checks, including \(r\ge3\) and \(\lambda\ge r+2\), and counted 54,346 forcing assignments, with every comparison equal.

For \(G=K_{2,2,3}\) and \(\lambda=5\), the coefficient list from degree zero through seven is \((0,0,0,0,600,1800,2280,1620)\); in particular the minimum forcing domain has size \(4\). Direct brute-force and the exact general formula agree. The finite evidence corroborates, but does not replace, the all-size proof above. Run `python3 verify_forced_multipartite.py` with Python 3 and no additional packages.

## Relationship to prior work

G. E. Farr's 2026 paper defines the local forced-colouring function, gives a general chromatic-polynomial endpoint relation and a closed formula for connected bipartite graphs with two colours, and explicitly discusses the greater difficulty of the case with more colours than the chromatic number. It does not classify forcing assignments of complete multipartite graphs with \(r\ge3\) and \(\lambda\ge r+2\). Farr and Morgan's 2024 precursor introduces the function and its general counting formalism, but contains no theorem with this multipartite and palette scope.

Previously published graph-family results already give the complete multipartite case \(\lambda=r\), the multipartite case \(\lambda=r+1\), and the bipartite case \(r=2\) for arbitrary palette size. They are **not** claimed here. Their statements do not imply the many-polychromatic-part case arising when \(\lambda\ge r+2\), nor the displayed capacity subset-sum minimum across all such profiles. For clarity, the profile formula specializes consistently to these known boundary cases. An unrelated black-white zero-forcing parameter on multipartite graphs has different dynamics and does not imply the present forcing-colour enumerator.

## Limitations

The theorem is specific to complete multipartite graphs and Farr's neighbourhood-palette rule. It is not a formula for arbitrary graph joins, for unique extendability without the iterative rule, or for improper partial assignments. For \(\lambda>N\) no non-total restriction can force because the complete colouring cannot use the full palette; the formula correctly reduces to the chromatic-polynomial total-colouring term and minimum \(N\). Exhaustive checks cover only the finite listed sizes. Searches and inspected primary papers do not establish a universal absence of equivalent unindexed work; independent validation has not been performed.

## References

1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, first publicly submitted 15 September 2026, https://arxiv.org/abs/2609.17108v1 (full 29-page paper inspected).
2. G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746v1, first publicly submitted 22 June 2024, https://arxiv.org/abs/2406.15746v1 (full 38-page paper inspected).
3. *Forced colourings of complete multipartite graphs at the chromatic palette size*, public research record 2026/10/4, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-forced-colourings-of-complete-multipartite-graphs-at-the-chromat--ab08eebc2655 (full RESULT inspected).
4. *Forced three-colouring polynomial of complete bipartite graphs*, public research record 2026/10/4, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-forced-three-colouring-polynomial-of-complete-bipartite-graphs--3fb93c858f69 (full RESULT inspected).

