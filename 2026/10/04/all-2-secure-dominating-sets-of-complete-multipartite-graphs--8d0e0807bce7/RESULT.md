# All 2-secure dominating sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph, with parts \(X_1,\ldots,X_r\), and let \(S\subseteq V(G)\). Put \(s_i=|S\cap X_i|\), \(c_i=n_i-s_i\), and \(k=|S|\). Then \(S\) is a 2-secure dominating set if and only if \(k\ge2\) and \[k-s_i\ge\min\{c_i,3\}\qquad\text{for every }i.\] Thus simultaneous two-vertex security is controlled exactly by a three-guard cap outside each part. If \(a_k\) denotes the number of 2-secure dominating \(k\)-sets and \(M=\sum_{i:n_i\le3}n_i\), then \(a_0=a_1=0\), \(a_2=\binom N2\) when \(\max_i n_i\le2\) and \(a_2=0\) otherwise, and \(a_3=\binom M3\). For \(k=4\), \[a_4=\binom N4-\sum_{i:n_i\ge5}\left[\binom{n_i}4+(N-n_i)\binom{n_i}3+\binom{N-n_i}2\binom{n_i}2\right]+\sum_{\substack{i<j\\n_i,n_j\ge5}}\binom{n_i}2\binom{n_j}2.\] For every \(5\le k\le N\), \[a_k=\binom Nk-\sum_{i:n_i\ge k+1}\left[\binom{n_i}k+(N-n_i)\binom{n_i}{k-1}+\binom{N-n_i}2\binom{n_i}{k-2}\right].\]

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected, so \(r\ge2\), with partite classes \(X_1,\ldots,X_r\) and \(N=\sum_i n_i\). A set \(S\) is 2-secure dominating when, for every pair of distinct attacked vertices \(u_1,u_2\), there are distinct defenders \(v_1,v_2\in S\) with \(v_j\in N[u_j]\) such that
\[
(S\setminus\{v_1,v_2\})\cup\{u_1,u_2\}
\]
is dominating.

Write \(s_i=|S\cap X_i|\), \(c_i=n_i-s_i\), and \(k=|S|\). The polynomial \(D_{2s}(G;x)=\sum_k a_kx^k\) is used only as an enumerator for all 2-secure dominating sets.

## Proof
First suppose that \(S\) is 2-secure dominating. Necessarily \(k\ge2\). Fix a part \(X_i\).

If \(c_i=1\), then \(S\) cannot be contained in the proper subset \(S\cap X_i\), because such a set does not dominate the omitted vertex in \(X_i\). Hence \(|S\setminus X_i|\ge1\).

If \(c_i=2\), attack the two omitted vertices of \(X_i\). Their defenders must be distinct selected vertices outside \(X_i\), so \(|S\setminus X_i|\ge2\).

If \(c_i\ge3\), the same attack shows that at least two selected vertices lie outside \(X_i\). Equality cannot occur: the two outside vertices would be the only possible defenders, and after moving both into \(X_i\), at least one vertex of \(X_i\) would remain omitted while the moved set would be contained entirely in \(X_i\), so it would fail to dominate. Hence \(|S\setminus X_i|\ge3\). This proves
\[
k-s_i\ge\min\{c_i,3\}.
\]

Conversely, assume \(k\ge2\) and these inequalities hold for every part. Consider two distinct attacked vertices.

If both attacks lie in the same part \(X_i\), there are three cases. If both are already selected, use them as their own defenders. If exactly one is selected, use that vertex itself and one selected vertex outside \(X_i\). If at least two selected vertices remain outside \(X_i\), domination is immediate after the move; if exactly one was outside, the inequality forces \(c_i=1\), so the move fills \(X_i\) completely. If both attacked vertices are omitted, choose two defenders outside \(X_i\). If at least one outside selected vertex remains, the moved set meets two parts and dominates; if exactly two existed, the inequality forces \(c_i=2\), so the move fills \(X_i\) completely.

If the attacks lie in distinct parts, let \(A=N[u_1]\cap S\) and \(B=N[u_2]\cap S\). Each is nonempty. Moreover every vertex of \(S\) belongs to \(A\cup B\), because a vertex can fail to be adjacent to at most the attacked vertex in its own part, while the other attack lies in a different part. Since \(|S|\ge2\), the two sets admit distinct representatives. After the corresponding move, both attacked parts are represented, so the new set dominates. The criterion is therefore necessary and sufficient.

For enumeration, let \(a_k\) count the valid \(k\)-subsets. At size two, the criterion holds for every pair exactly when all parts have size at most two; otherwise no pair works. At size three, a selected vertex can lie in a part of size at most three, and every three-subset of the union of those small parts is valid, giving \(a_3=\binom M3\).

Now let \(k\ge4\). A \(k\)-subset violates the criterion at part \(X_i\) exactly when \(n_i\ge k+1\) and at most two selected vertices lie outside \(X_i\). For a fixed such part, the bad subsets are counted by
\[
\binom{n_i}k+(N-n_i)\binom{n_i}{k-1}+\binom{N-n_i}2\binom{n_i}{k-2}.
\]
For \(k\ge5\), two distinct bad-part events cannot occur simultaneously because each would contain at least \(k-2\) selected vertices, and \(2(k-2)>k\). This gives the stated formula.

When \(k=4\), two bad-part events can intersect only in a set consisting of two selected vertices from each of two parts of sizes at least five. Inclusion-exclusion therefore adds
\[
\sum_{i<j,\ n_i,n_j\ge5}\binom{n_i}2\binom{n_j}2,
\]
which proves the quadratic correction in \(a_4\).

## Verification
The included checker independently reconstructs every complete multipartite graph of orders two through ten. For every vertex subset it first tests domination directly, then checks every unordered pair of attacked vertices and searches all ordered pairs of distinct defenders satisfying the closed-neighborhood requirement. It compares the result with the structural inequality and with every coefficient in the closed enumerator.

## Relationship to prior work
Lad, Reddy, and Kumar introduced 2-secure domination in 2017 and proved NP-completeness even for split and bipartite graphs. Their full paper establishes the simultaneous two-attack model and complexity, but does not classify complete multipartite 2-secure dominating sets.

Kumar and Reddy's 2020 full preprint makes the distinct-attacker and distinct-defender convention explicit, lists MSC \(05C69\), and develops further complexity and approximation results. Full-text searches in that paper for complete bipartite, multipartite, and polynomial formulations do not reveal the statement proved here.

A similarly named 2022 parameter, secure 2-domination, is different: it starts from a 2-dominating set and requires security under one replacement. It is not an equivalent formulation of 2-secure domination, which starts from domination and defends two simultaneous attacks.

Targeted semantic-database and literature searches for 2-secure domination together with complete multipartite, complete bipartite, polynomial, all-set, and simultaneous-two-attack terminology did not locate the three-guard criterion or the coefficient formulas above.

## Limitations
The theorem is specific to connected complete multipartite graphs. The exact coefficients are not claimed for the distinct 2022 secure 2-domination invariant. Finite verification through order ten is corroborative only; the all-orders result follows from the proof. Search coverage cannot exclude differently phrased or non-indexed prior enumerative work.

## References
1. D. Lad, P. Venkata Subba Reddy, J. Pavan Kumar, “Complexity Issues of Variants of Secure Domination in Graphs,” Electronic Notes in Discrete Mathematics 63 (2017), 77–84, DOI 10.1016/j.endm.2017.11.001.
2. J. Pavan Kumar, P. Venkata Subba Reddy, “Algorithmic Aspects of 2-Secure Domination in Graphs,” arXiv:2002.02408v1, 5 February 2020.
3. I. Boufelgha, M. Ahmia, M. Guettiche, “Secure 2-domination in graphs,” Research Square preprint, posted 15 November 2022, DOI 10.21203/rs.3.rs-1968931/v1.
