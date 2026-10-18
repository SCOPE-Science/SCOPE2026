# Complete distance-edge-monitoring and minimal-probe enumerators for subdivided cliques

## Finding
For every integer \(n\ge3\), let \(H_n=S(K_n)\) be the graph obtained by subdividing each edge of the complete graph exactly once. Write \(D_n(x,y)\) for the polynomial whose coefficient of \(x^u y^f\) counts distance-edge-monitoring sets having \(u\) original vertices and \(f\) subdivision vertices. With \(q=\binom n2\), the entire polynomial is
\[
D_n(x,y)=\left(nx^{n-1}+x^n\right)(1+y)^q+\sum_{u=0}^{n-2}\binom nu x^u\sum_{j=0}^{n-u}(-1)^j\binom{n-u}{j}(1+y)^{\binom{n-j}{2}}.
\]
The corresponding polynomial \(M_n(x,y)\) counting **inclusion-minimal** distance-edge-monitoring sets satisfies
\[
M_n(x,y)=n![t^n]\exp\!\left(xt+\frac{yt^2}{2}+t(e^{yt}-1-yt)\right)-x^n+nx^{n-1}.
\]
Here \([t^n]\) is ordinary coefficient extraction from the displayed exponential generating series. In particular, possible cardinalities of inclusion-minimal monitoring sets are **exactly** \(\{\lceil n/2\rceil,\ldots,n-1\}\), and the coefficient of the smallest power in \(D_n(z,z)\) is
\[
\begin{cases}
9,&n=3,\\
\displaystyle\frac{n!}{2^{n/2}(n/2)!},&n\ge4\text{ even},\\
\displaystyle\frac{((n+1)/2)n!}{2^{(n-1)/2}((n-1)/2)!},&n\ge5\text{ odd}.
\end{cases}
\]
The underlying structural characterization, both size-enumerators, and the complete minimum-set multiplicities form one combined classification result. The scalar minimum alone is not claimed as an independently new theorem.

## Assumptions and scope
Graphs are finite, simple, connected, and unweighted. Original vertices of \(H_n\) are \(a_i\), indexed by \(i\in[n]\); subdivision vertices \(b_{ij}=b_{ji}\) correspond to the pairs \(\{i,j\}\). A monitoring set \(P\subseteq V(H_n)\) is one for which, for each graph edge \(e\), some \(p\in P\) and target vertex \(v\) satisfy \(d_{H_n-e}(p,v)>d_{H_n}(p,v)\). Infinite distances count as increased. A monitoring set is inclusion-minimal if deleting any one of its probes destroys this property. All assertions are quantified over every integer \(n\ge3\); the stated minimum-set expression treats the triangle-subdivision boundary separately.

For a probe set \(P\), put \(U=\{i:a_i\in P\}\) and \(F=\{\{i,j\}:b_{ij}\in P\}\). The underlying edge set \(F\subseteq E(K_n)\) has endpoint set \(V(F)\subseteq[n]\). No independence, connectivity, or minimality assumption on \(F\) is imposed when counting all monitoring sets.

## Proof
**1. Single-probe coverage.** For any connected graph, a fixed probe \(p\) detects an edge \(vw\) precisely when one endpoint, say \(w\), is at distance \(d(p,v)+1\) and \(v\) is its unique predecessor among neighbors at distance \(d(p,w)-1\). Indeed, uniqueness makes every shortest \(p,w\)-path use the edge. Conversely, if every shortest \(p,z\)-path uses \(vw\), choose the endpoint \(w\) encountered just after this edge on such a path. Any alternative shortest \(p,w\)-path avoiding the edge would concatenate with the remaining path to \(z\), contradicting the monitoring property.

In \(H_n\), distances and their predecessor multiplicities are explicit. From \(a_i\), every other original vertex \(a_j\) is joined by a unique shortest path \(a_i,b_{ij},a_j\). A subdivision vertex \(b_{jk}\) with neither index equal to \(i\) has two shortest paths from \(a_i\), via \(a_j\) and \(a_k\). Hence \(a_i\) detects exactly **both halfedges** of every subdivided edge of \(K_n\) incident with index \(i\). From \(b_{ij}\), each \(b_{ik}\) with \(k\ne j\) has a unique shortest path through \(a_i\), and similarly for \(j\); a remote original vertex is reached by two equally short routes through \(a_i\) and \(a_j\), while a subdivision vertex disjoint from \(\{i,j\}\) admits multiple shortest routes. Therefore \(b_{ij}\) detects exactly those halfedges having original endpoint \(a_i\) or \(a_j\). These distance assertions also cover \(n=3\), where the graph is a six-cycle.

Consequently, the halfedge joining \(a_i\) to \(b_{ij}\) is detected by \(P\) exactly when
\[
i\in U\quad\text{or}\quad j\in U\quad\text{or}\quad i\in V(F).
\]
If some \(i\notin U\cup V(F)\), every other index must belong to \(U\); conversely, that condition suffices. Thus the **complete necessary and sufficient criterion** is
\[
P\text{ monitors }H_n\quad\Longleftrightarrow\quad
U\cup V(F)=[n]\ \text{or}\ |U|\ge n-1.
\]

**2. Enumerating all monitoring sets.** For \(|U|=n-1\) or \(n\), all \(2^q\) choices of \(F\) work. These contribute \((nx^{n-1}+x^n)(1+y)^q\). For \(|U|=u\le n-2\), every one of the remaining \(n-u\) original labels must have positive degree in \(F\). By inclusion-exclusion over \(j\) missing labels, the weighted sum over allowable \(F\) is
\[
\sum_{j=0}^{n-u}(-1)^j\binom{n-u}{j}(1+y)^{\binom{n-j}{2}}.
\]
Multiplying by the \(\binom nu\) choices of \(U\) proves the formula for \(D_n(x,y)\).

**3. Inclusion-minimal monitoring sets.** When \(|U|=n-1\), every choice of \(F\) is dispensable, so precisely the \(n\) configurations \((U,\emptyset)\) are minimal. \(|U|=n\) is never minimal. If \(|U|\le n-2\), monitoring means that \(F\) covers all vertices of \(W=[n]\setminus U\). If a vertex in \(U\) is incident with any edge of \(F\), deleting that selected original probe preserves the complete-cover condition and hence monitoring. Such overlap cannot occur in a minimal probe set. Thus minimality forces all edges in \(F\) to have both endpoints in \(W\), and \(F\) must be an inclusion-minimal edge cover of \(K_W\). Conversely, an inclusion-minimal edge cover of \(W\), with no \(F\)-edge incident with \(U\), is an inclusion-minimal monitoring set: dropping any selected subdivision vertex uncovers a vertex in \(W\), while dropping a selected original vertex leaves at least two indices outside \(U\) and leaves the removed original index uncovered by \(F\).

An edge set in a complete graph is an inclusion-minimal edge cover precisely when its graph is a vertex-disjoint union of stars with at least two vertices per component. Every edge of a minimal cover must have a degree-one endpoint; this property rules out cycles and any path of three or more edges, so each connected component is a star. Conversely, every star-forest cover has no dispensable edge. The special configurations \(U=[n]\setminus\{i\}\), \(F=\emptyset\) are distinct from these star-forest configurations (which require \(|W|\ge2\)).

**4. Enumerating minimal monitoring sets.** A selected original vertex is a singleton component of weight \(xt\). A two-vertex star contributes \(yt^2/2\). A star of size \(k\ge3\) has \(k\) choices of center and weight \(y^{k-1}t^k/k!\). The corresponding labeled exponential generating function is
\[
\exp\!\left(xt+\frac{yt^2}{2}+\sum_{k\ge3}\frac{ky^{k-1}t^k}{k!}\right)=\exp\!\left(xt+\frac{yt^2}{2}+t(e^{yt}-1-yt)\right).
\]
Its \(n\)-label coefficient counts all singleton-plus-star partitions, including one inadmissible all-singleton object \(U=[n]\). Deleting that object and adding the \(n\) exceptional all-but-one-original monitoring sets proves \(M_n(x,y)\).

**5. Extremal cardinalities.** A star-forest configuration with \(c\) nontrivial star components has exactly \(n-c\) probes, since each component of \(k\) vertices contributes \(k-1\) probes and each singleton contributes one. Its number of nontrivial components lies between one and \(\lfloor n/2\rfloor\). Conversely, for every integer in that range choose \(c-1\) disjoint two-vertex stars and one final star on the remaining vertices (with no singleton), attaining all values \(n-c\). The exceptional \(n\) configurations have size \(n-1\) and do not alter the spectrum.

For even \(n=2r\ge4\), the unique minimum-type structures are perfect matchings consisting of \(r\) disjoint two-vertex stars, counted by \(n!/(2^rr!)\). For odd \(n=2r+1\ge5\), either one original vertex is selected and the others form \(r\) pairs, or all probes are subdivision vertices and the forest has one three-vertex star and \(r-1\) pairs. These two families have respectively \(n!/(2^rr!)\) and \(rn!/(2^rr!)\) members. At \(n=3\), all three exceptional original pairs also have minimum size two, adding three to the preceding six constructions, giving nine. This completes the proof.

## Verification
The accompanying `verify.py` builds every \(S(K_n)\) adjacency list for \(3\le n\le6\). For each probe and graph edge it recomputes shortest-path distances with and without that edge, rather than assuming the structural lemma. It then enumerates all \(2^{n+\binom n2}\) probe subsets, tests the displayed necessary-and-sufficient criterion, and checks every coefficient of both enumerating polynomials and minimum-set counts. In total it checks \(2,131,008\) probe subsets. The program's exact output is embedded in `verification_output.txt`. Exhaustive finite checks are not a proof of the infinite statement; the graph-theoretic and enumerative arguments above supply that proof.

## Relationship to prior work
Distance-edge-monitoring and the shortest-path predecessor perspective were introduced by Foucaud, Kao, Klasing, Miller, and Ryan (arXiv:2011.00029, first public 2020-10-30). Yang, Klasing, Mao, and Deng subsequently studied structural bounds for the minimum monitoring number (arXiv:2211.04920). The particularly relevant work by Ji, Guo, Cheng, Klasing, and Mao, *The distance-edge-monitoring numbers of subdivision graphs* (Discrete Applied Mathematics 372 (2025), 37–47; DOI:10.1016/j.dam.2025.03.015), concerns this graph-construction class and may determine the scalar optimum or related coverage properties. That work is not claimed as unrelated, and the scalar optimum here is not offered as a stand-alone originality claim. The present asserted contribution is the exact two-weight distribution of **all** monitoring sets, a classification and two-weight enumerator for **all inclusion-minimal** monitoring sets, and the exact structural minimum-set multiplicities. A scalar optimum does not mathematically determine those distributions. The full text of the 2025 study was not accessible for a decisive comparison, creating a material priority risk.

## Limitations
The theorem applies to one-subdivisions of simple complete graphs with \(n\ge3\), unweighted distances, edge-failure monitoring, and probes restricted to graph vertices. It does not address arbitrary subdivisions, additional edge failures, weighted distances, or robust monitoring. Finite testing is limited to \(3\le n\le6\). Earlier work might already contain an equivalent structural lemma or enumeration under other terminology, notably the unavailable 2025 subdivision-graph study; the enumerative novelty remains subject to independent full-text priority verification. This document does not assert an independent mathematical audit.

## References
1. F. Foucaud, M.-Y. Kao, R. Klasing, T. Miller, and P. Ryan, *Monitoring the edges of a graph using distances*, arXiv:2011.00029 (first posted 2020-10-30), https://arxiv.org/abs/2011.00029 .
2. C. Yang, R. Klasing, Y. Mao, and X. Deng, *On the distance-edge-monitoring numbers of graphs*, arXiv:2211.04920 (first posted 2022-11-09), https://arxiv.org/abs/2211.04920 .
3. Z. Ji, Z. Guo, E. Cheng, R. Klasing, and Y. Mao, *The distance-edge-monitoring numbers of subdivision graphs*, Discrete Applied Mathematics **372** (2025), 37–47, https://doi.org/10.1016/j.dam.2025.03.015 .
