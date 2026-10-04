# Zero forcing graphs of complete multipartite graphs via singleton compression
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph. If every part is singleton, so \(G=K_N\), then \(\mathscr Z(G)\cong K_N\). Otherwise, let \(m_1,\ldots,m_p\ge2\) be the non-singleton part sizes and let \(q\) be the number of singleton parts. Form the compressed complete multipartite graph \(H\) with part sizes \(m_1,\ldots,m_p\) and, when \(q>0\), one additional part of size \(q\). Then the token-jumping zero forcing reconfiguration graph is exactly the line graph \[\mathscr Z(G)\cong L(H).\] Equivalently, the minimum zero forcing sets are exactly the complements of pairs \(\{x,y\}\) lying in distinct original parts and not both in singleton parts, and two such minimum sets are adjacent exactly when their omitted pairs share one vertex. Consequently \[|V(\mathscr Z(G))|=\sum_{i<j}n_i n_j-\binom q2.\] For noncomplete \(G\), \(\mathscr Z(G)\) is connected and has diameter \(1\) exactly for stars, and diameter \(2\) otherwise.

## Assumptions and scope
All graphs are finite and simple. The zero forcing graph \(\mathscr Z(G)\) has as vertices the minimum zero forcing sets of \(G\), with two minimum sets adjacent when their symmetric difference has size two.

Let \(G=K_{n_1,\ldots,n_r}\) be connected. Let \(q\) denote the number of singleton parts, and let \(m_1,\ldots,m_p\ge2\) be the sizes of the non-singleton parts.

## Proof
Suppose first that \(G\) is complete. Then every minimum zero forcing set has size \(N-1\) and is the complement of one vertex. Any two such complements differ by one exchanged vertex, so \(\mathscr Z(G)\cong K_N\).

Now assume that \(G\) is not complete. We first classify its minimum zero forcing sets directly. If at least three vertices are initially white and a first force is possible from a blue vertex in part \(X_i\), then exactly one white vertex lies outside \(X_i\). After that vertex is forced, at least two white vertices remain in \(X_i\). Every blue vertex in \(X_i\) then has no white neighbor, while every blue vertex outside \(X_i\) has at least two white neighbors. The process stalls. Therefore every zero forcing set has at most two white vertices, so \(Z(G)\ge N-2\).

Let the two white vertices be \(x,y\). If they lie in the same part, every blue vertex outside that part sees both whites and every blue vertex inside sees neither, so no force occurs. If they lie in two singleton parts, there is no blue vertex in either of those parts, while every blue vertex in any other part sees both whites, so again no force occurs.

Conversely, suppose \(x\) and \(y\) lie in distinct parts and at least one of those parts, say the part containing \(x\), has another vertex \(u\). Then \(u\) is blue and has the unique white neighbor \(y\), so \(u\) forces \(y\). The newly blue vertex \(y\) then has the unique white neighbor \(x\), and forces it. Thus \(V(G)\setminus\{x,y\}\) is zero forcing. Since \(G\) is noncomplete, such a pair exists, so \(Z(G)=N-2\). This proves that the minimum zero forcing sets are exactly the stated complements.

Define \(H\) on the same vertex set by joining two vertices exactly when they lie in distinct original parts and are not both singleton vertices. Merging all singleton parts of \(G\) into one independent part shows that
\[
H\cong K_{m_1,\ldots,m_p,q},
\]
with the \(q\)-part omitted when \(q=0\).

The map
\[
\phi:E(H)\to V(\mathscr Z(G)),\qquad \phi(\{x,y\})=V(G)\setminus\{x,y\}
\]
is a bijection. For edges \(e,f\) of \(H\), the symmetric difference of their complementary minimum zero forcing sets is exactly \(e\triangle f\). Hence those two minimum sets are adjacent in \(\mathscr Z(G)\) exactly when \(|e\cap f|=1\), which is precisely adjacency in the line graph. Therefore \(\mathscr Z(G)\cong L(H)\).

The order formula is \(|E(H)|\): start with all cross-part pairs of \(G\) and remove the \(\binom q2\) pairs between singleton parts.

The graph \(H\) is connected, so its line graph is connected. If \(G\) is a nontrivial star, then \(H\) is the same star and its line graph is complete, so the diameter is one. Otherwise \(H\) has two disjoint edges. Any two disjoint edges of a complete multipartite graph have an endpoint-crossing edge joining one endpoint of the first to one endpoint of the second, so their distance in \(L(H)\) is two. Every pair of line-graph vertices is at distance at most two by the same argument, proving diameter two.

## Verification
The included checker independently enumerates every vertex subset through the first successful zero-forcing layer for every connected complete multipartite isomorphism type of orders \(2\) through \(10\). It simulates the standard color-change rule directly and compares the resulting minimum zero forcing sets with the omitted-pair classification.

It then constructs the token-jumping adjacency relation from symmetric differences and compares it entry-by-entry with the line graph of the compressed complete multipartite graph. The order and diameter consequences are checked independently.

## Relationship to prior work
The 2020 paper introducing zero forcing reconfiguration defines \(\mathscr Z(G)\), studies token jumping among minimum zero forcing sets, and computes the zero forcing graphs of paths, cycles, complete graphs, and stars. Its full text contains no complete-multipartite or complete-bipartite treatment and no line-graph description for this family.

The 2023 paper on zero- and total-forcing-dense graphs proves that every nonstar complete multipartite graph is zero-forcing-dense and, when noncomplete, has zero forcing number \(N-2\). Its proof constructs enough minimum sets to establish density but does not classify all minimum zero forcing sets and does not study their reconfiguration graph. The theorem here uses an exact all-minimum-set classification to identify the entire reconfiguration graph as a classical line graph. The complete-graph and star cases from the 2020 paper are recovered as boundary cases rather than claimed anew.

## Limitations
The theorem concerns token-jumping reconfiguration of minimum standard zero forcing sets. It does not address token sliding, TAR reconfiguration, positive-semidefinite forcing, skew forcing, or reconfiguration among nonminimum zero forcing sets. The exhaustive computation through order ten is corroborative only; the arbitrary-order statement follows from the proof. Search coverage cannot exclude a differently phrased or non-indexed complete-multipartite reconfiguration result.

## References
1. J. Geneson, R. Haas, L. Hogben, “Reconfiguration graphs of zero forcing sets,” arXiv:2009.00220v1, 1 September 2020; Discrete Applied Mathematics 329 (2023), 126–139, DOI 10.1016/j.dam.2023.01.027.
2. R. Davila, M. A. Henning, R. Pepper, “Zero and total forcing dense graphs,” Discussiones Mathematicae Graph Theory 43(3) (2023), 619–634, DOI 10.7151/dmgt.2389. Public author manuscript uploaded 23 January 2021.
