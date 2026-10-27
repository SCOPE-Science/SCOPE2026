# Sharp Grundy-domination sensitivity of half graphs under every edge deletion

## Finding
For every integer \(n\ge3\), let the half graph \(H_n\) have distinct vertices \(x_1,\ldots,x_n,y_1,\ldots,y_n\) and edges \(x_i y_j\) exactly when \(1\le i\le j\le n\). For every edge \(e\) of \(H_n\), the Grundy domination number is
\[
\gamma_{\mathrm{gr}}(H_n-e)=
\begin{cases}
n+1,&e\in\{x_1y_1,x_ny_n\},\\
n+2,&e\in E(H_n)\setminus\{x_1y_1,x_ny_n\}.
\end{cases}
\]
In particular, **every nonpendant edge** is maximally sensitive under single-edge deletion: its removal attains the universal upper edge-deletion change of \(+1\), while the two pendant edges are stable. The baseline is \(\gamma_{\mathrm{gr}}(H_n)=n+1\). The restriction \(n\ge3\) is sharp: in \(H_2\), removing the middle edge instead changes the value from \(3\) to \(2\).

## Assumptions and scope
All graphs are finite, simple and undirected, with vertex names distinguished. A sequence \(S=(v_1,\ldots,v_k)\) of distinct vertices is *legal* when for every index \(t\), the closed neighborhood \(N[v_t]\) contains a vertex outside \(\bigcup_{s<t}N[v_s]\). It is *dominating* when the union of those closed neighborhoods is all vertices. Its maximum possible length is \(\gamma_{\mathrm{gr}}(G)\). A legal sequence of maximum length is automatically dominating, because another undominated vertex could be appended.

For the explicit sequences below, a consecutive increasing string \((y_a,\ldots,y_b)\) is empty when \(a>b\). All subscripts refer to the original graph, even after deleting an edge.

## Proof
**Baseline and universal upper bound.** The diagonal edges \(x_i y_i\) form a perfect matching, whereas each of the two shores is independent; hence \(\alpha(H_n)=n\). The graph is a chain graph. Brešar--Pandey--Sharma [1, Theorem 5] show that the Grundy domination number of a chain graph belongs to \(\{\alpha,\alpha+1\}\). The following sequence of length \(n+1\) is legal:
\[
(y_1,x_1,x_2,\ldots,x_{n-1},y_n).
\]
Indeed, \(y_1\) footprints itself, \(x_1\) footprints \(y_2\), each later \(x_r\) for \(2\le r\le n-1\) footprints itself, and \(y_n\) footprints \(x_n\). Thus \(\gamma_{\mathrm{gr}}(H_n)=n+1\). The atomic edge-deletion theorem of Brešar--Gologranc--Kos [2, Theorem 2.1] states, for any graph \(G\) and edge \(e\),
\[
\gamma_{\mathrm{gr}}(G-e)\le\gamma_{\mathrm{gr}}(G)+1.
\]
Therefore every deletion considered here has Grundy domination number at most \(n+2\). This published inequality is independently checked against its original proof: any loss of legality when one restores an edge can be repaired by discarding at most one entry from a longest legal sequence [2, Section 2.1].

**Nonpendant-edge lower bound.** Fix \(e=x_i y_j\), where \(1\le i\le j\le n\), excluding \((i,j)=(1,1),(n,n)\). We construct a legal dominating sequence of length \(n+2\). Every displayed sequence selects all \(n\) vertices on the \(y\)-shore and exactly two on the \(x\)-shore.

When \(i=1\) and \(2\le j<n\), use
\[
(y_1,x_1,x_{j+1},\ y_2,\ldots,y_{j-1},\ y_{j+1},y_j,\ y_{j+2},\ldots,y_n).
\]
The initial \(y_1\) is new; \(x_1\) reveals an unmarked \(y\)-vertex; \(x_{j+1}\) is itself new. The successive \(y_2,\ldots,y_{j-1}\) reveal fresh \(x\)-vertices, \(y_{j+1}\) reveals \(x_j\), and \(y_j\) reveals itself because its sole potential selected \(x\)-neighbor, \(x_1\), has lost the edge to \(y_j\). Each remaining \(y_r\) reveals \(x_r\).

When \(2\le i<j<n\), use
\[
(x_i,x_{j+1},\ y_1,\ldots,y_{i-2},\ y_i,y_{i-1},\ y_{i+1},\ldots,y_{j-1},\ y_{j+1},y_j,\ y_{j+2},\ldots,y_n).
\]
Both initially selected \(x\)-vertices are new. The early \(y_1,\ldots,y_{i-2}\) reveal themselves; \(y_i\) reveals \(x_{i-1}\), then \(y_{i-1}\) reveals itself. Intermediate increasing \(y\)-indices reveal their correspondingly indexed \(x\)-vertices. The entry \(y_{j+1}\) reveals \(x_j\), then \(y_j\) reveals itself because the deleted edge is its only edge to the two selected \(x\)-vertices. The rest reveal fresh \(x\)-vertices.

When \(2\le i=j<n\), use
\[
(x_i,x_{i+1},\ y_1,\ldots,y_{i-2},\ y_{i+1},y_{i-1},y_i,\ y_{i+2},\ldots,y_n).
\]
Here \(y_{i+1}\) first reveals \(x_{i-1}\), while \(y_{i-1}\) and \(y_i\) both reveal themselves. Later entries reveal new \(x\)-vertices. These observations check every entry directly against the *original* closed-neighborhood legality rule, rather than a surrogate conflict test.

For the central extreme edge \(x_1y_n\), use
\[
(y_{n-2},y_{n-3},\ldots,y_1,\ x_1,y_{n-1},x_{n-1},y_n).
\]
The initial descending \(y\)-vertices reveal themselves, \(x_1\) reveals \(y_{n-1}\), \(y_{n-1}\) reveals \(x_{n-1}\), \(x_{n-1}\) reveals \(y_n\), and \(y_n\) reveals \(x_n\). This construction works already when \(n=3\).

Finally, the involution \(x_r\mapsto y_{n+1-r}\), \(y_r\mapsto x_{n+1-r}\) is an automorphism of \(H_n\). It sends deletion of \(x_i y_n\) with \(2\le i<n\) to deletion of \(x_1y_{n+1-i}\), already covered by the first case. The reflected sequences complete all nonpendant edges. Every sequence has \(n+2\) distinct entries and dominates all vertices; the universal upper bound gives equality.

**Pendant edges.** By the same involution it suffices to delete \(x_1y_1\). This isolates \(y_1\). The remaining connected graph \(C\) is a chain graph with \(n\) vertices on the \(x\)-shore and \(n-1\) on the \(y\)-shore. For \(n\ge3\), its \(k=n-1\) ordered \(x\)-neighborhood twin classes have sizes \(1,\ldots,1,2\), and its \(k\) \(y\)-classes each have size one. Substitution into the explicit chain-graph algorithm [1, Algorithm 1] gives: boundary candidate \(\lvert Y\rvert+\lvert X_1\rvert=n\); each interior candidate \(\sum_{r\le t}\lvert X_r\rvert+\lvert Y\rvert-\sum_{r\le t}\lvert Y_r\rvert+1=n\) for \(1\le t<k\); final candidate \(\lvert X\rvert=n\) because the largest-neighborhood class has size two. Therefore \(\gamma_{\mathrm{gr}}(C)=n\), also witnessed by taking all \(x\)-vertices in any order. Since Grundy domination adds across connected components and \(\gamma_{\mathrm{gr}}(K_1)=1\), the deleted graph has value \(n+1\).

For \(n=2\), the half graph is a four-vertex path: deleting either pendant edge gives one isolated vertex and a three-vertex path, with value \(3\), while deleting the middle edge gives two disjoint edges, with value \(2\). This confirms the stated boundary.

## Verification
The accompanying standalone `check_halfgraph.py` directly builds the original adjacency and closed neighborhoods. It checks **4,900** explicit witnesses for all nonpendant edges at orders \(3\le n\le30\), then independently computes exact Grundy maxima with memoization over covered-vertex bitmasks for **119** individual edge deletions and baselines at \(2\le n\le8\). Every witness is checked for distinct entries, fresh footprints, full domination and its exact intended length. The attached `verification_output.txt` is the actual stdout of the verifier. These finite computations test premises and boundary cases; they are not substituted for the general mathematical proof.

## Relationship to prior work
The sharp universal \(\pm1\) edge-deletion bounds are from [2]; they do not specify which edges in a half graph attain which bound. The efficient chain-graph algorithm, and its dichotomy \(\gamma_{\mathrm{gr}}\in\{\alpha,\alpha+1\}\), are from [1]; the deleted nonpendant-edge graphs generally cease to be chain graphs. Work on equality between Grundy domination and independence [3] treats different structural classes and does not give this edge-by-edge sensitivity profile. Thus the new statement is an exact equality-case analysis of the atomic-change bound for a canonical strict Ferrers graph family, not a claim to the general upper bound or the chain-graph baseline.

## Limitations
The result concerns deletion of exactly one edge of the strict half graph, not arbitrary Ferrers graphs, multiple deletions or arbitrary edge additions. Search cannot establish absolute bibliographic uniqueness. The proof uses published general results [1,2] whose stated hypotheses are explicitly verified above. No independent external audit is asserted.

## References
[1] B. Brešar, A. Pandey, G. Sharma, *Computation of Grundy dominating sequences in (co-)bipartite graphs*, arXiv:2310.10566v1, first public 2023-10-16, especially Theorem 5 and Algorithm 1. https://arxiv.org/html/2310.10566v1

[2] B. Brešar, T. Gologranc, T. Kos, *Dominating sequences under atomic changes with applications in Sierpiński and interval graphs*, arXiv:1603.05116v1, first public 2016-03-16, Theorem 2.1. https://arxiv.org/html/1603.05116v1

[3] G. Bacsó, B. Brešar, K. Kuenzel, D. F. Rall, *Graphs with equal Grundy domination and independence number*, arXiv:2212.01335v1, first public 2022-12-02. https://arxiv.org/html/2212.01335v2
