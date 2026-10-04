# Skew zero forcing sets of chain graphs factor by twin classes
## Finding
Let \(G=(A,B,E)\) be a finite connected chain graph. Thus the open neighborhoods of vertices on each side of the bipartition are linearly ordered by inclusion. Put \(u\sim v\) when \(N(u)=N(v)\), and let \(\mathcal T\) be the resulting open-neighborhood twin classes.

A set \(S\subseteq V(G)\) is a skew zero forcing set if and only if
\[
|T\setminus S|\le 1\qquad\text{for every }T\in\mathcal T.
\]
Hence, if
\[
\mathcal Z_-(G;x)=\sum_{S\text{ skew zero forcing}}x^{|S|},
\]
then
\[
\mathcal Z_-(G;x)=\prod_{T\in\mathcal T}\left(x^{|T|}+|T|x^{|T|-1}\right).
\]
In particular,
\[
Z^-(G)=|V(G)|-|\mathcal T|,
\]
and the number of minimum skew zero forcing sets is
\[
\prod_{T\in\mathcal T}|T|.
\]

## Assumptions and scope
Graphs are finite, simple, and connected. A chain graph is a bipartite graph \(G=(A,B,E)\) for which the neighborhoods on each bipartition side are nested by inclusion. The skew color-change rule allows a vertex of either color to force its unique white neighbor. The statement concerns every initial set, not only minimum sets.

Connectivity is used only to exclude isolated vertices and guarantee that every nonempty white singleton on one side has a neighbor from the other side. The classification can be extended componentwise with the usual treatment of isolated vertices, but that extension is not claimed here.

## Proof
Write \(W=V(G)\setminus S\) for the initially white vertices.

First suppose that \(W\) contains distinct vertices \(u,v\) from the same open-neighborhood twin class. Any vertex adjacent to one of \(u,v\) is adjacent to both, while every other vertex is adjacent to neither. Therefore no vertex has exactly one neighbor in \(\{u,v}\). As long as both \(u\) and \(v\) remain white, neither can be the unique white neighbor of any vertex. Thus they can never be forced, so \(S\) is not a skew zero forcing set. This proves necessity.

Conversely, suppose \(W\) contains at most one vertex from every open-neighborhood twin class. We show that if \(W\ne\varnothing\), then some vertex has exactly one neighbor in \(W\). If \(W\cap A\ne\varnothing\), choose \(a^*\in W\cap A\) with inclusion-maximal neighborhood among the white vertices in \(A\). If \(a^*\) is the only white vertex in \(A\), connectivity gives a vertex \(b\in N(a^*)\), and \(b\) has exactly one white neighbor in \(A\), namely \(a^*\). If there is another white vertex in \(A\), choose \(a'\) whose neighborhood is maximal among \((W\cap A)\setminus\{a^*}\). The twin-class hypothesis gives the strict inclusion \(N(a')\subsetneq N(a^*)\). Choose \(b\in N(a^*)\setminus N(a')\). Every other white vertex of \(A\) has neighborhood contained in \(N(a')\), so \(b\) has exactly one white neighbor, \(a^*\). Since \(G\) is bipartite, \(b\) has no neighbors in \(B\). Hence \(b\) can skew-force \(a^*\).

If \(W\cap A=\varnothing\), the same argument with the two sides interchanged produces a force of a white vertex in \(B\). After any such force, the smaller white set still contains at most one vertex from every twin class. Induction on \(|W|\) therefore forces all vertices. This proves sufficiency.

For a twin class \(T\), an admissible skew zero forcing set either contains all \(|T|\) vertices, contributing \(x^{|T|}\), or omits exactly one of the \(|T|\) vertices, contributing \(|T|x^{|T|-1}\). The choices are independent across classes, which gives the product formula. Its least exponent and corresponding coefficient give the final two corollaries.

## Verification
A standalone exhaustive checker constructs every canonical connected chain-graph degree profile through order \(10\). For every graph it tests every vertex subset against an independent implementation of the skew color-change process, compares the outcome with the twin-class criterion, compares every polynomial coefficient with the product formula, and checks the minimum exponent and the number of minimum sets. The run completed with:

`VERIFY_OK graph_profiles=511 subset_checks=349524 coefficient_checks=5119 max_order=10`

The finite computation checks small instances only; the theorem for arbitrary order follows from the proof above.

## Relationship to prior work
The skew color-change rule and its connection with minimum skew rank were introduced in the foundational minimum-skew-rank literature. DeAlba, arXiv:1404.1618, studies minimum skew zero forcing sets, includes matching-based results for bipartite graphs, characterizes complete multipartite graphs at the scalar level, and records \(Z^-(H_s)=0\) for the half-graph \(H_s\). The latter is the singleton-twin-class specialization of the present minimum-number formula, but it does not classify all initial sets or arbitrary chain graphs with repeated neighborhoods.

Cooper and Fickes, arXiv:2303.17419, develop skew zero forcing as a closure operator and study stalled-set matroids, complexity, trees, cycles, and several bipartite phenomena. Their accessible full text contains no occurrence of the terms “chain” or “Ferrers.” The present statement is an explicit all-set factorization for the nested-neighborhood class, not a claim that general closure theory is new.

## Limitations
No claim is made for bipartite graphs whose neighborhoods are not nested, for disconnected graphs with isolated vertices, or for variants of the skew color-change rule. The literature comparison cannot rule out every older source indexed under alternative terminology for chain graphs, such as Ferrers or difference graphs; this remains a residual originality risk. The half-graph scalar case is already known and is treated as prior coverage, not as a new consequence in isolation.

## References
1. IMA-ISU Research Group on Minimum Rank, “Minimum rank of skew-symmetric matrices described by a graph,” *Linear Algebra and its Applications* 432 (2010), 2457–2472. DOI: 10.1016/j.laa.2009.10.001.
2. L. M. DeAlba, “Some results on minimum skew zero forcing sets, and skew zero forcing number,” arXiv:1404.1618.
3. J. Cooper and G. Fickes, “Zero loci of nullvectors and skew zero forcing in graphs and hypergraphs,” arXiv:2303.17419.
