# Edge-open-packing decomposition and exact polynomial for complete-graph subdivisions

## Finding
Let \(G=(V,E)\) be any finite simple graph. For each \(uv\in E\), let \(x_{uv}\) be a new vertex and replace \(uv\) by \(ux_{uv}\) and \(vx_{uv}\); call the resulting graph \(S(G)\). An *edge-open packing* is any set \(B\subseteq E(S(G))\) such that no two distinct selected edges have a third graph edge joining an endpoint of one to an endpoint of the other. Empty sets are included in the counting polynomial \(P_H(z)=\sum_{B\text{ edge-open packing}}z^{|B|}\).

Write \(V(M)\) for the endpoints of a matching \(M\) of \(G\), and \(U=V\setminus(V(M)\cup C)\). The following identity holds, without connectivity assumptions:
\[
P_{S(G)}(z)=\sum_{M\text{ matching in }G} z^{2|M|}
\sum_{C\subseteq V\setminus V(M)}
\prod_{c\in C}\left((1+z)^{|N_G(c)\cap U|}-1\right).
\tag{1}
\]
Here empty products equal \(1\). Consequently, writing \(\operatorname{mc}(H)\) for the largest number of edges across any bipartition of \(V(H)\),
\[
\rho_e^o(S(G))=\max_{M\text{ matching in }G}
\left(2|M|+\operatorname{mc}(G-V(M))\right).
\tag{2}
\]
For the complete graph, this specializes for every integer \(n\ge0\) to
\[
P_{S(K_n)}(z)=\sum_{k=0}^{\lfloor n/2\rfloor}
\frac{n!\,z^{2k}}{2^k k!(n-2k)!}
\sum_{c=0}^{n-2k}\binom{n-2k}{c}
\left((1+z)^{n-2k-c}-1\right)^c.
\tag{3}
\]
For \(n\ge5\), every maximum packing has no doubly selected subdivision vertex and consists of **all** incidence edges directed from one side to the other side of a balanced, ordered bipartition. Thus
\[
\rho_e^o(S(K_n))=\lfloor n^2/4\rfloor,
\quad \#\{\text{maximum packings}\}=
\begin{cases}\binom{n}{n/2},&n\text{ even},\\2\binom{n}{(n-1)/2},&n\text{ odd}.\end{cases}
\tag{4}
\]
The exceptional numbers of maximum packings are \(1\) at \(n=2\) and \(9\) at each of \(n=3,4\); \(n=0,1\) have the unique empty packing. The maximum sizes at \(n=2,3,4\) are respectively \(2,2,4\).

## Assumptions and scope
The graph is finite, undirected, simple, and may be disconnected or have isolated vertices. A matching may be empty. Each original edge is subdivided **exactly once**, and the polynomial is defined using labeled graph edges (so a graph automorphism does not identify packings). In \(G-V(M)\), all endpoints of edges of \(M\) are deleted. An *ordered* cut remembers which side supplies the original-vertex centers, a distinction needed for the extremal count.

## Proof
We classify each packing \(B\). If both incidence edges \(ux_{uv}\) and \(vx_{uv}\) are in \(B\), then no other selected edge can have original endpoint \(u\) or \(v\): otherwise the three-edge path through \(x_{uv}\) contains two selected nonconsecutive edges separated by the third selected edge. Such doubly occupied subdivision vertices correspond to a matching \(M\subseteq E(G)\). This matching is intrinsic to \(B\), and exactly \(2|M|\) selected edges use its subdivision vertices.

Delete the matched original endpoints and their associated selected incidences. Every remaining selected edge has precisely one original endpoint, and no subdivision vertex has two selected incidences. Let \(C\) be the set of remaining original vertices incident to at least one selected edge. Suppose \(cx_{cu}\) is selected with \(c\in C\). Then \(u\notin C\): if \(u\) were incident to a distinct selected edge, the third incidence \(ux_{cu}\) would join endpoints of these two selected edges. Also \(u\notin V(M)\) by the previous paragraph. Hence \(u\in U=V\setminus(V(M)\cup C)\). Conversely, choose any matching \(M\), any \(C\subseteq V\setminus V(M)\), and for each \(c\in C\) a nonempty subset of edges from \(c\) to \(U\). Select both incidence edges for all \(uv\in M\), plus each \(cx_{cu}\) for the chosen neighbors. Distinct chosen incidences are not joined by a third incidence: their original endpoints are either the same center, or lie among distinct centers, while their opposite original endpoints lie in \(U\); matched endpoints are disjoint from all of these. They therefore form an edge-open packing. The construction is mutually inverse to the extraction of \(M,C\) and the nonempty neighbor subsets. The latter contribute \((1+z)^{|N_G(c)\cap U|}-1\) independently, proving (1).

For fixed \(M,C\), the largest packing selects every incidence from each \(c\in C\) to \(U\), of total size \(2|M|+|E_G(C,U)|\). Maximizing over all \(C\subseteq V\setminus V(M)\) is precisely \(\operatorname{mc}(G-V(M))\). This proves (2), even if an optimum cut contains an isolated vertex (which contributes no selected incidence).

When \(G=K_n\), the number of size-\(k\) matchings is \(n!/(2^k k!(n-2k)!)\). Removing matched endpoints leaves \(r=n-2k\) vertices. There are \(\binom rc\) choices of a \(c\)-vertex center set, each center having exactly \(r-c\) eligible neighbors. Substitution in (1) yields (3). For this family, (2) reduces to maximizing \(f_n(k)=2k+\lfloor(n-2k)^2/4\rfloor\) over \(0\le k\le\lfloor n/2\rfloor\). Its consecutive difference is \(f_n(k+1)-f_n(k)=3-(n-2k)\). The sequence decreases and then increases, so its maximum is at one of the two endpoints. For \(n\ge5\), \(f_n(0)=\lfloor n^2/4\rfloor>2\lfloor n/2\rfloor=f_n(\lfloor n/2\rfloor)\), with strict inequality throughout \(k>0\). Thus all optima have \(M=\varnothing\) and a maximum cut of \(K_n\). Its bipartitions have side sizes as equal as possible, and all crossing incidences are forced. The center side is distinguished, giving \(\binom n{n/2}\) or \(2\binom n{(n-1)/2}\) labeled optima; no two center sets produce the same packing because every vertex of the center side is incident to selected edges. Direct evaluation of the same formula gives the stated exceptional small orders.

## Verification
The included independent enumerators `verify_subdivision_general.py` and `verify_complete_subdivisions.py` calculate coefficient vectors by (1)/(3) and by a different method: enumerate all selected-incidence subsets and reject any pair of selected incidences connected by a third, distinct incidence. The general verifier covers **all labeled graphs on one through four vertices** and 32 deterministically sampled five-vertex graphs; the complete-graph verifier checks all coefficients through \(n=5\). Successful execution prints `ALL_CHECKS_OK` and `MATCH True`, respectively. For \(K_5\), the polynomial coefficient vector from degree zero through six is \((1,20,130,340,355,120,20)\). These finite tests are checks, not substitutes for the all-graph bijection and proof.

To replay with Python 3 standard library only, run `python3 verify_subdivision_general.py` and `python3 verify_complete_subdivisions.py` from the directory containing the extracted files. No external data or packages are needed.

## Relationship to prior work
The edge-open-packing definition and the induced-star observation were established by Chelladurai–Kalimuthu–Soundararajan (2022) and further developed by Brešar–Samadi (2024). The latter studies complexity, algorithms for trees, and bounds; Brešar–Dravec–Hedžet–Samadi (2024) studies trees and graph products. Neither the known general induced-star description nor the quoted results state the specific matching/center canonical decomposition (1), the matching-deletion maximum-cut reduction (2), or the complete-subdivision enumerator (3). The present proof derives these explicitly rather than treating a general induced-star characterization alone as a novel fact. Earlier injective edge-coloring results study decomposing **all** edges into packing color classes, a different problem from enumerating individual packing sets.

## Limitations
This theorem is about full one-subdivisions, not arbitrary subdivisions, multiple-edge base graphs, or edge packing in \(G\) itself. It does not claim an efficient exact algorithm for general \(G\): maximum cut appears in (2), and the all-graph sum may require exponential time. The exact form (3) and extremal census are for complete base graphs only. The literature comparison cannot eliminate possible unindexed earlier specializations, particularly under the terms induced-star packing, injective edge color class, or incidence-graph packing. Independent external review has not been performed.

## References
1. G. Chelladurai, K. Kalimuthu and S. Soundararajan, “Edge open packing sets in graphs,” RAIRO Operations Research 56 (2022), 3765–3776; https://doi.org/10.1051/ro/2022171.
2. B. Brešar and B. Samadi, “Edge open packing: complexity, algorithmic aspects, and bounds,” arXiv:2403.00750v1, first submitted 2024-03-01; https://arxiv.org/abs/2403.00750.
3. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, “Induced matching vs edge open packing: trees and product graphs,” arXiv:2406.04020v2 (2024); https://arxiv.org/abs/2406.04020.
4. F. Foucaud et al., “Complexity and algorithms for injective edge-coloring in graphs,” arXiv:2104.08003v1 (2021); https://arxiv.org/abs/2104.08003.
