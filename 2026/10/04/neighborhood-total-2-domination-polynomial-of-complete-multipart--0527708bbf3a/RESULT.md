# Neighborhood total \(2\)-domination polynomial of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), partite classes \(V_1,\ldots,V_r\), and \(N=\sum_i n_i\). For \(S\subseteq V(G)\), put \(s_i=|S\cap V_i|\) and \(s=|S|\). A neighborhood total \(2\)-dominating set means that every vertex outside \(S\) has at least two neighbors in \(S\), and the graph induced by the open neighborhood \(N(S)\) has no isolated vertices.

For \(r\ge3\), \(S\) is neighborhood total \(2\)-dominating if and only if \(s\ge2\) and
\[
s_i<n_i\quad\Longrightarrow\quad s-s_i\ge2
\]
for every \(i\). For \(r=2\), the same inequalities characterize the feasible sets after adding the condition that \(S\) meets both partite classes.

For \(2\le s\le N\), define
\[
Q_{i,s}(y)=y^{n_i}+\sum_{j=0}^{\min\{n_i-1,s-2\}}\binom{n_i}{j}y^j.
\]
Then the number \(d_{2nt}(G,s)\) of neighborhood total \(2\)-dominating sets of cardinality \(s\) is
\[
d_{2nt}(G,s)=[y^s]\prod_{i=1}^r Q_{i,s}(y)
-\mathbf 1_{r=2}\sum_{i=1}^2\mathbf 1_{s=n_i}.
\]
Consequently the exact cardinality enumerator is
\[
D_{2nt}(G;x)=\sum_{s=2}^{N}d_{2nt}(G,s)x^s.
\]
The minimum cardinality follows as
\[
\gamma_{2nt}(G)=
\begin{cases}
N,&r=2\text{ and }\min_i n_i=1,\\
3,&r=2\text{ and }\min_i n_i=2,\\
4,&r=2\text{ and }\min_i n_i\ge3,\\
2,&r\ge3\text{ and }\bigl(\exists i:n_i=2\text{ or at least two }n_i=1\bigr),\\
3,&r\ge3\text{ otherwise.}
\end{cases}
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. All part sizes are positive integers and \(r\ge2\). The polynomial counts vertex subsets, not labeled functions. The result concerns neighborhood total \(2\)-domination in the sense introduced by C. Sivagnanam: the outside vertices are \(2\)-dominated and the subgraph induced by \(N(S)\) has no isolated vertices.

## Proof
For a vertex \(v\in V_i\setminus S\), every vertex of \(S\) outside \(V_i\) is adjacent to \(v\), while no vertex of \(S\cap V_i\) is adjacent to \(v\). Hence
\[
|N(v)\cap S|=s-s_i.
\]
Thus the \(2\)-domination requirement is exactly the family of inequalities \(s_i<n_i\Rightarrow s-s_i\ge2\).

It remains to determine when \(G[N(S)]\) has no isolated vertices. If \(S\) meets at least two parts, every vertex has a selected neighbor in a different part, so \(N(S)=V(G)\). Since \(G\) is connected and has at least two parts, it has no isolated vertices.

If \(S\) meets exactly one part, say \(V_i\), then the \(2\)-domination inequalities force \(S=V_i\) and \(n_i\ge2\): otherwise an omitted vertex in \(V_i\) has no selected neighbor. In this case \(N(S)=V(G)\setminus V_i\). This induced graph has no isolated vertices exactly when at least two partite classes remain, that is, exactly when \(r\ge3\). This proves the set classification.

Fix a cardinality \(s\). In a non-full part, the inequality is equivalent to \(s_i\le s-2\), so the allowed occupancies are \(0,1,\ldots,\min\{n_i-1,s-2\}\); a full part contributes the separate occupancy \(n_i\). Multiplying the corresponding binomial-weighted part polynomials and extracting \([y^s]\) counts all profiles satisfying the \(2\)-domination inequalities. When \(r=2\), the only counted profiles that fail the neighborhood condition are the two possible one-part sets \(S=V_i\), and each exists at its own size \(n_i\); subtracting the displayed indicators yields the coefficient formula.

For the minimum, the bipartite cases follow directly from the classification: a star needs every vertex; a part of size \(2\) plus one vertex of the other part gives size \(3\); and when both parts have size at least \(3\), two vertices are needed from each part. For \(r\ge3\), a size-\(2\) set works exactly when it is a whole part of size \(2\), or consists of two whole singleton parts. If neither possibility occurs, one vertex from each of any three distinct parts is a feasible size-\(3\) set, and no size-\(2\) set can satisfy the classification.

## Verification
The standalone `verify.py` reconstructs every nondecreasing complete-multipartite profile of order at most \(10\), builds adjacency explicitly, and checks every vertex subset against the literal definition. It independently checks the profile criterion, every enumerator coefficient, and the minimum formula. Its replay result is:

`VERIFY_OK profiles=128 subset_checks=64916 criterion_checks=64916 valid_sets=48021 coefficient_checks=923 gamma_checks=128 max_order=10`

The exhaustive computation is a finite stress test. The theorem for arbitrary part sizes follows from the symbolic proof above.

## Relationship to prior work
Sivagnanam introduced neighborhood total \(2\)-domination and gave the defining condition, the value \(\gamma_{2nt}(K_n)=2\), the star value, and the complete-bipartite minimum values: \(3\) when one nonstar part has size \(2\), and \(4\) when both parts have size at least \(3\). The inspected full text contains no occurrence of “multipartite”; its complete-bipartite statement is a minimum-cardinality result rather than an all-set classification or cardinality enumerator. The bipartite branch of the theorem above therefore recovers those known minima and is not claimed as new by itself.

The new content retained here is the arbitrary complete-multipartite classification of every feasible set together with the exact coefficient formula for every cardinality. General neighborhood-total-domination results and other domination variants do not imply this condition because they impose different neighborhood multiplicities or different induced-subgraph requirements.

## Limitations
The result is restricted to connected complete multipartite graphs. It does not enumerate minimal neighborhood total \(2\)-dominating sets separately, although the full enumerator determines their possible cardinalities only indirectly. Literature searches cannot prove uniqueness: an obscure or poorly indexed statement under equivalent terminology may exist. The closest inspected primary source gives only complete-bipartite minimum values and no complete-multipartite all-set theorem.

## References
C. Sivagnanam, “Neighborhood Total 2-Domination in Graphs,” *International Journal of Mathematical Combinatorics* 4 (2014), 108–119. DOI: 10.5281/zenodo.826659.

C. Sivagnanam and G. Mahadevan, “Neighborhood Total 2-Domination Number and Connectivity,” *International Journal of Mathematical Combinatorics* 4 (2015), 18–24.
