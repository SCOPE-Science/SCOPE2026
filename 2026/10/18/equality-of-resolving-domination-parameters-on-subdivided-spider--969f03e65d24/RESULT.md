# Equality of resolving-domination parameters on subdivided spider trees

## Finding
Let \(T=S(\ell_1,\ldots,\ell_t)\) be a tree with one vertex of degree \(t\ge3\), every other vertex of degree at most two, and \(t\) internally disjoint arms of edge lengths \(\ell_i\ge2\). For a vertex set required simultaneously to dominate and resolve vertices, write \(\gamma_{md}(T)\) for its minimum cardinality. For a vertex set required simultaneously to distinguish every two edges by vertex-to-edge distance and to dominate every edge within vertex-to-edge distance at most one, write \(\gamma_{emd}(T)\).

Put
\[
U=\sum_{i=1}^t\left\lceil\frac{\ell_i-1}{3}\right\rceil,\qquad s=\#\{i:\ell_i=2\},
\]
and define \(\eta=0\) exactly when no \(\ell_i\) is congruent to \(1\pmod3\) and at least one \(\ell_i\) is congruent to \(2\pmod3\); otherwise \(\eta=1\). Define \(\epsilon=1\) exactly when every \(\ell_i\) is congruent to \(0\) or \(1\pmod4\); otherwise \(\epsilon=0\). Then
\[
\boxed{\gamma_{md}(T)=U+\eta}
\]
and
\[
\boxed{\gamma_{emd}(T)=\min\left\{
1+\sum_i\left\lceil\frac{\ell_i-2}{4}\right\rceil+\max\{s-1,0\},\quad
\sum_i\left\lceil\frac{\ell_i}{4}\right\rceil,\quad
\sum_i\left\lceil\frac{\ell_i-1}{4}\right\rceil+\epsilon
\right\}.}
\]
In particular,
\[
\boxed{\gamma_{md}(T)=\gamma_{emd}(T)\ \Longleftrightarrow\ 
\ell_i\in\{2,3\}\text{ for every }i,\text{ and at least one }\ell_i=2.}
\]
For example, when all \(t\) arms have length \(5\), the two parameters are \(2t\) and \(t+1\), giving an unbounded gap \(t-1\). This is a classification within subdivided spiders, not a characterization of all trees.

## Assumptions and scope
Graphs are finite, simple, undirected and connected. The center is \(c\); arm \(i\) has vertices \(v_{i,1},\ldots,v_{i,\ell_i}\) at distances \(1,\ldots,\ell_i\) from \(c\), with \(v_{i,0}=c\) and edges \(e_{i,j}=v_{i,j-1}v_{i,j}\). Distances between a vertex \(v\) and edge \(xy\) are \(d(v,xy)=\min\{d(v,x),d(v,y)\}\). Edge domination is \(\min_{v\in S}d(v,e)\le1\) for every edge \(e\); this is vertex-edge domination, **not** vertex-cover domination. Resolution means that every pair of distinct vertices (respectively edges) has distinct distance vectors to \(S\). There are at least three arms, each with at least two edges. No statement is made for unit-length arms, non-spider trees or different edge-domination conventions.

## Proof
**Resolving-arm lemma.** For either vertex resolution or edge resolution, \(S\) resolves exactly when its noncentral vertices meet at least \(t-1\) different arms. If two arms are missed, their depth-one vertices (and separately their first edges) have identical distances to every landmark. Conversely, with at most one missed arm, vertices on the same arm are distinguished by a landmark on another arm. For vertices on different arms, a landmark on a third arm separates unequal depths; if the depths coincide, a landmark on one of those arms separates them. When the two compared arms are the only represented arms, landmarks on both arms cannot simultaneously fail: equality of the first landmark's distances requires the first depth to exceed the second, while equality at the second requires the reverse. The same proof works for edges: for a selected vertex at depth \(a\) on arm \(i\), the distance to \(e_{i,j}\) is \(\min\{|a-j|,|a-j+1|\}\), while the distance to an edge \(e_{k,h}\) on another arm is \(a+h-1\). Equal distances for a landmark on the first arm force \(j>h\), and equal distances for a landmark on the second arm force \(h>j\); both are impossible. This also handles equal-index cross-arm edges and establishes sufficiency.

**Vertex domination.** Every vertex-dominating set intersects every arm: its terminal vertex of depth at least two can only be dominated by vertices of that arm. Therefore its vertex-resolving condition is automatic by the lemma. If \(c\in S\), the vertices at depths \(2,\ldots,\ell_i\) of arm \(i\) require exactly \(\lceil(\ell_i-1)/3\rceil\) further selections. This is sharp by the length-three coverage interval of each selected vertex; greedy selections attain it. The total is \(1+U\). If \(c\notin S\), arm \(i\) requires \(\lceil\ell_i/3\rceil\) selections to dominate its own vertices; also the center needs some depth-one selection. A minimum dominating set of the length-\(\ell\) arm path includes its first vertex exactly when \(\ell\not\equiv0\pmod3\). Indeed for lengths divisible by three, covering all vertices with the minimum number forces the unique depth sequence \(2,5,8,\ldots\); for other residues an endpoint-first optimal sequence exists. When all lengths are multiples of three, one extra vertex is necessary and sufficient. Thus the center-absent total is \(\sum_i\lceil\ell_i/3\rceil+\mathbf1_{\{\forall i:\ell_i\equiv0\ (\mathrm{mod}\ 3)\}}\). Comparing with \(1+U\), and using \(\lceil\ell/3\rceil-\lceil(\ell-1)/3\rceil=\mathbf1_{\{\ell\equiv1\ (\mathrm{mod}\ 3)\}}\), gives \(U+\eta\).

**Vertex-edge domination.** A vertex on arm \(i\) at depth \(a\ge1\) dominates exactly the edges of its own arm with indices in \([a-1,a+2]\cap[1,\ell_i]\), and, only if \(a=1\), the first edges of all other arms. The center dominates precisely the first two edges of each arm. One noncentral vertex can cover at most four consecutive arm edges.

If the center is selected, the \(\ell_i-2\) edges at indices \(3,\ldots,\ell_i\) independently require exactly \(\lceil(\ell_i-2)/4\rceil\) arm selections. Every arm of length greater than two is thereby represented; among the \(s\) arms of length two, at most one may remain unrepresented because of the resolving-arm lemma. Filling \(\max\{s-1,0\}\) such arms gives the first displayed candidate, attainable with suitable depth placements.

If the center is absent and no depth-one vertex is selected, each arm must cover all its own \(\ell_i\) edges, requiring and attaining \(\lceil\ell_i/4\rceil\) selections; depth-two, depth-six, and later regularly spaced vertices give suitable covers, with the last position adjusted toward the terminal edge. This is the second candidate. Finally, suppose there is at least one selected depth-one vertex. It covers the first edge of every arm. Each arm must still cover its edges at indices \(2,\ldots,\ell_i\), at cost \(\lceil(\ell_i-1)/4\rceil\). On any designated arm, forcing a depth-one selection costs \(1+\lceil\max\{\ell_i-3,0\}/4\rceil\), which exceeds that baseline by one precisely for \(\ell_i\equiv0,1\pmod4\), and otherwise equals it. Choosing a least-cost designated arm gives the third candidate, with surcharge \(\epsilon\). All three configurations have at least \(t-1\) represented arms, so the resolving condition is satisfied. Any admissible set belongs to one of these exhaustive cases, proving the second formula.

**Equality classification.** Write \(C=\sum_i\lceil(\ell_i-1)/4\rceil\) and \(\Delta=U-C\ge0\). Then \(\gamma_{emd}(T)\le C+\epsilon\). For integers \(\ell\ge2\), equality \(\lceil(\ell-1)/3\rceil=\lceil(\ell-1)/4\rceil\) occurs exactly for \(\ell\in\{2,3,4,6,7,10\}\). If \(\eta=1\), the bound \(C+\epsilon\) is strictly below \(U+1\) whenever \(\Delta\ge1\) or \(\epsilon=0\). The remaining case \(\Delta=0,\epsilon=1\) forces every arm length to be \(4\); the second edge-domination candidate is then \(t\) while \(\gamma_{md}(T)=t+1\).

If \(\eta=0\), no length is \(1\pmod3\) and at least one is \(2\pmod3\). When \(\epsilon=1\), each arm contributes at least one to \(\Delta\): the only zero-contribution length congruent to \(0\) or \(1\pmod4\) is \(4\), which is excluded by the \(\eta=0\) condition. Hence \(\Delta\ge t\ge3\) and the gap is strict. When \(\epsilon=0\) and \(\Delta\ge1\), the gap is again strict. The remaining possibility \(\Delta=0\) forces all lengths to lie in \(\{2,3,6\}\), with at least one equal to \(2\). If \(k\ge1\) arms have length \(6\), then \(U=t+k\) while the center-selected edge-domination candidate is exactly \(t\), giving strict inequality. Otherwise every arm has length \(2\) or \(3\), with at least one of length \(2\): here \(\gamma_{md}(T)=t\), and \(\gamma_{emd}(T)=t\) because a center-selected resolving set needs the center plus landmarks on at least \(t-1\) arms, while a center-absent edge-dominating set must meet all \(t\) arms. This proves the equivalence.

## Verification
The companion `verify_spider.py` builds graphs, computes all-pairs vertex distances by breadth-first search, computes edge distances independently as endpoint minima, and tests **every vertex subset** for simultaneous domination and resolving. It checks the resolving-arm equivalence on every vertex subset in four mixed spiders (2,688 subsets), confirms both closed formulas for 51 small spiders with three or four arms, and checks the modular equality classification on 42,294 additional arm profiles with between three and five arms and arm lengths through \(20\). Run `python verify_spider.py` without third-party dependencies. These finite computations check implementations and boundary cases; the infinite theorem follows from the preceding interval and resolving-arm proofs, not from enumeration.

## Relationship to prior work
Ikhlaq, Hayat and Siddiqui (2022, arXiv:2211.09327v1) introduced \(\gamma_{emd}\), proved a general tree inequality against \(\gamma_{md}\), and explicitly asked for trees on which equality holds. Their results for paths, cycles and graph products do not give the two formulas or equality condition here. Classical tree metric-dimension results give the branch-resolving part but not the interaction with vertex-edge domination. The 2023 notion termed *dominant edge metric dimension* in Tavakoli et al. uses a **vertex-cover** requirement, rather than vertex-edge domination, and is mathematically distinct. Recent work on distance-\(k\) resolving domination of balanced spiders addresses a different domination radius and does not supply the vertex-edge formula or arbitrary-arm equality condition. The overlap assessment is limited by indexing and accessible material; it is not a declaration of exhaustive global novelty.

## Limitations
The characterization applies only to spiders with at least three arms and **all** arms of length at least two. A spider with a unit-length arm may have different optimal landmark patterns and is outside scope. Other trees, weighted graphs, edge-cover domination instead of vertex-edge domination, and independent validation are not addressed. Published and indexed sources were compared, but unindexed equivalents remain possible.

## References
1. H. M. Ikhlaq, S. Hayat, H. M. A. Siddiqui, *Unique identification and domination of edges in a graph: The vertex-edge dominant edge metric dimension*, arXiv:2211.09327v1 (first public submission 2022-11-17), https://arxiv.org/html/2211.09327v1, Sections 2, 5–7.
2. L. Susilowati, I. Sa'adah, R. Z. Fauziyyah, A. Erfanian and Slamin, *The dominant metric dimension of graphs*, Heliyon 6 (2020), e03633, https://doi.org/10.1016/j.heliyon.2020.e03633.
3. M. Tavakoli, M. Korivand, A. Erfanian, G. Abrishami and E. T. Baskoro, *The dominant edge metric dimension of graphs*, Electronic Journal of Graph Theory and Applications 11 (2023), https://doi.org/10.5614/ejgta.2023.11.1.16 (distinct vertex-cover definition).
