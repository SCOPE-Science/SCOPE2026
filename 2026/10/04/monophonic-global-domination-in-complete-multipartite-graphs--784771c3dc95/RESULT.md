# Monophonic global domination in complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), partite sets \(X_1,\ldots,X_r\), and \(m_i=|M\cap X_i|\). A set \(M\subseteq V(G)\) is monophonic global dominating if and only if \(m_i\ge1\) for every \(i\) and one of the following holds: at least two indices satisfy \(m_i\ge2\); exactly one index \(j\) satisfies \(m_j\ge2\) and then \(m_j=n_j\); or every part is a singleton and \(M=V(G)\). Consequently, if \(q=|\{i:n_i\ge2\}|\) and \(N=\sum_i n_i\), then \[\overline{\gamma}_m(G)=\begin{cases}N,&q\le1,\\ r+1,&q\ge2\text{ and some }n_i=2,\\ r+2,&q\ge2\text{ and every non-singleton part has size at least }3.\end{cases}\] The same classification yields an exact generating polynomial and exact counts of minimum sets.

For counting, set
\[
A_i(z)=(1+z)^{n_i}-1,\qquad B_i(z)=n_i z,\qquad C_i(z)=A_i(z)-B_i(z),
\]
and let \(q=|\{i:n_i\ge2\}|\). The generating polynomial whose coefficient of \(z^k\) is the number of monophonic global dominating sets of size \(k\) is
\[
\mathcal M_G(z)=\prod_i A_i(z)-\mathbf 1_{q>0}\prod_i B_i(z)-\sum_{i:n_i\ge2} C_i(z)\prod_{j\ne i}B_j(z)+\sum_{i:n_i\ge2}z^{n_i}\prod_{j\ne i}B_j(z).
\]
The number of minimum sets is \(1\) when \(q\le1\). If \(q\ge2\) and some part has size \(2\), it is
\[
\sum_{i:n_i=2}\prod_{j\ne i}n_j.
\]
If \(q\ge2\) and every non-singleton part has size at least \(3\), it is
\[
\sum_{\substack{i<j\\ n_i,n_j\ge2}}\binom{n_i}{2}\binom{n_j}{2}\prod_{h\notin\{i,j\}}n_h+\sum_{i:n_i=3}\prod_{j\ne i}n_j.
\]

## Assumptions and scope
All graphs are finite and simple. A monophonic path is an induced path. For vertices \(u,v\), the monophonic interval \(J[u,v]\) is the set of vertices on induced \(u\)-\(v\) paths, and \(M\) is monophonic when \(J[M]=V(G)\). A global dominating set dominates both \(G\) and its complement. The graph \(G=K_{n_1,\ldots,n_r}\) is connected, so \(r\ge2\) and every \(n_i\ge1\).

## Proof
The complement of \(G\) is the disjoint union of the cliques on \(X_1,\ldots,X_r\). Hence \(M\) dominates the complement exactly when it meets every part. If it meets every part, it also dominates \(G\), because any omitted vertex in \(X_i\) is adjacent to every selected vertex in another part. Thus global domination is exactly \(m_i\ge1\) for all \(i\).

Vertices from different parts are adjacent, so their monophonic interval consists only of the endpoints. If \(u,v\in X_j\), then for each \(w\notin X_j\), \(u-w-v\) is induced. No induced path in a complete multipartite graph has more than two edges: any four-vertex path would acquire a cross-part chord. Hence
\[
J[u,v]=\{u,v\}\cup(V(G)\setminus X_j).
\]
Therefore an omitted vertex in \(X_i\) is covered exactly when some different part contains at least two selected vertices. Let \(B=\{i:m_i\ge2\}\). If \(|B|\ge2\), every omission is covered by a pair from another large-selected part. If \(|B|=1\), say \(B=\{j\}\), omissions outside \(X_j\) are covered, but an omission in \(X_j\) cannot be, so \(m_j=n_j\). If \(B=\varnothing\), no omission can be covered, so \(M=V(G)\), which forces every part to be a singleton. This proves the classification.

The polynomial follows by choosing a nonempty subset in each part, subtracting profiles with zero or exactly one part contributing at least two selected vertices, and restoring the valid profiles where that unique part is selected in full. The minimum and its counts follow by minimizing these profiles: with at least two non-singleton parts, either one size-two part is selected in full for size \(r+1\), or two parts contribute two vertices each for size \(r+2\); a full size-three part gives the second additional type at size \(r+2\).

## Verification
The included `verify.py` independently constructs each complete multipartite graph, enumerates induced paths directly, forms monophonic intervals, tests domination in the graph and complement, and checks every vertex subset. It confirms the classification, minimum value, and minimum-set count for all 87 complete multipartite isomorphism types of orders two through nine, totaling 22,932 tested vertex subsets.

## Relationship to prior work
Selvi and Flower introduced monophonic global domination and determined the parameter for several standard families. Their Theorem 2.12 treats complete bipartite graphs. The present formula recovers its intended cases and extends them to arbitrary complete multipartite graphs while also classifying every feasible set and counting sets by size.

A 2025 paper on monophonic polynomials of joins gives general information about monophonic sets under joins, but its accessible abstract does not address the added requirement of domination in both a graph and its complement. A 2026 paper with the same monophonic-global-domination title has an abstract describing bounds, extremal graphs, realization, and corona products; its full text was not available in the inspected public source, so possible differently phrased overlap remains a residual risk. Targeted database and literature searches for complete-multipartite monophonic global domination did not locate an equivalent theorem or enumerator.

## Limitations
The result is restricted to connected complete multipartite graphs. The finite exhaustive verification is corroborative and does not replace the all-orders proof. The inaccessible full text of the 2026 same-topic paper leaves a specific residual risk of unobserved overlap.

## References
1. V. Selvi, V. Sujin Flower, “The monophonic global domination number of a graph,” J. Math. Comput. Sci. 11 (2021), 6007–6017, DOI 10.28919/jmcs/6225.
2. R. N. Paluga, “Monophonic Polynomial of the Join of Graphs,” Journal of the Indonesian Mathematical Society 31 (2025), DOI 10.22342/jims.v31i1.1686.
3. V. Selvi, J. John, V. Sujin Flower, “On the Monophonic Global Domination Number of a Graph,” Ukrainian Mathematical Journal 78 (2026), DOI 10.1007/s11253-026-02601-9.
