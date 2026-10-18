# Clique-indexed independent-domination polynomial of every central graph
## Finding
Let \(G\) be any finite simple graph on \(n\ge1\) vertices, with \(m\) edges, and let \(C(G)\) be its central graph. For every set \(A\subseteq V(G)\), write \(e_A=|E(G[V(G)\setminus A])|\) and \(N_G(v)\) for the open neighborhood of \(v\). Define the admissible-clique family
\[
\mathscr A(G)=\{A\subseteq V(G):G[A]\text{ is a clique and }N_G(v)\ne A\text{ for every }v\notin A\}.
\]
The empty set counts as a clique. There is an explicit bijection between \(\mathscr A(G)\) and the independent dominating sets (equivalently, maximal independent sets) of \(C(G)\):
\[
 A\ \longleftrightarrow\ D_A=A\cup\{w_{uv}:uv\in E(G),\ u,v\notin A\},
\]
where \(w_{uv}\) is the subdivision vertex corresponding to edge \(uv\). Consequently, the **entire independent-domination polynomial** is
\[
\boxed{I(C(G);z)=\sum_{A\in\mathscr A(G)} z^{|A|+m-\sum_{v\in A}d_G(v)+\binom{|A|}{2}}.}
\]
All coefficients count actual distinct labeled vertex subsets; no multiplicity quotient is taken. For each fixed clique-number bound \(\omega(G)\le r\), the complete polynomial, its minimum and maximum exponents, and all optimum-set counts are computable in \(O(n^{r+2}+m)\) arithmetic operations by clique enumeration. In particular, for the complete graph \(K_n\), \(n\ge2\),
\[
I(C(K_n);z)=z^n+\sum_{a=0}^{n-2}\binom na z^{a+\binom{n-a}{2}},
\qquad i(C(K_n))=n-1,
\]
and exactly \(\binom n2\) minimum independent dominating sets exist.
## Assumptions and scope
The base graph is finite, simple, undirected, with \(n\ge1\), and may be disconnected or have isolated vertices. Its central graph subdivides every edge once and joins precisely those unordered pairs of original vertices that are nonadjacent in \(G\). Original vertices remain nonadjacent in \(C(G)\) if and only if they are adjacent in \(G\). Subdivision vertices have degree two and no subdivision-to-subdivision edges. Independent domination means an independent vertex subset meeting every closed neighborhood. The result is not about domination without independence, nor about iterated central graphs.
## Proof
Let \(D\) be an independent dominating set of \(C(G)\), and put \(A=D\cap V(G)\). Any pair in \(A\) must be nonadjacent in \(C(G)\), so \(A\) is a clique of \(G\). A subdivision vertex \(w_{uv}\) with an endpoint in \(A\) is adjacent to a selected original vertex and therefore cannot belong to \(D\). If neither endpoint lies in \(A\), the subdivision vertex has no selected original neighbor and no subdivision neighbors at all; domination forces \(w_{uv}\in D\). Thus \(D=D_A\), uniquely.

The selected set \(D_A\) is independent whenever \(A\) is a clique, since the selected subdivisions have both endpoints outside \(A\), and subdivisions are mutually nonadjacent. Every subdivision vertex is dominated: those with an endpoint in \(A\) are adjacent to it, and the others are selected. Consider an unselected original vertex \(v\notin A\). It has a neighbor inside \(A\) in \(C(G)\) precisely if \(va\notin E(G)\) for some \(a\in A\). It has a selected subdivision neighbor precisely if \(vu\in E(G)\) for some \(u\notin A\). Both routes fail simultaneously exactly when every \(a\in A\) is a neighbor of \(v\) in \(G\) and no \(u\notin A\) is such a neighbor: \(N_G(v)=A\). Hence \(D_A\) dominates if and only if \(A\in\mathscr A(G)\), proving the bijection.

For a clique \(A\), exactly \(m-\sum_{v\in A}d_G(v)+\binom{|A|}{2}\) original edges have both endpoints outside \(A\); here every edge inside \(A\) was subtracted twice and then restored once. This is \(|D_A|-|A|\), yielding the polynomial. If \(\omega(G)\le r\), enumerate at most \(\sum_{j=0}^r\binom nj=O(n^r)\) subsets, test the clique and neighborhood conditions and evaluate the exponent in \(O(n^2)\) operations per subset, using precomputed adjacency/degrees. This proves the stated bound.

For \(G=K_n\), all vertex subsets are cliques. For \(v\notin A\), \(N_G(v)=V(G)\setminus\{v\}\), so exactly the subsets of size \(n-1\) are inadmissible. All subsets of sizes \(0,\ldots,n-2\) and \(n\) are admissible, and their weights give the displayed formula. For \(n\ge2\), the smallest exponent \(a+\binom{n-a}{2}\) for \(a\le n-2\) is uniquely attained at \(a=n-2\), and equals \(n-1\); the extra term \(z^n\) is larger. Thus the minimum-set count is \(\binom n2\). For \(n=2\) the assertion follows directly as well.
## Verification
The accompanying standalone Python 3 program `verify.py` enumerates every finite simple labeled graph on \(1\le n\le4\) vertices and all graphs on five vertices having at most seven edges. For each, it directly enumerates independent dominating subsets of the *constructed central graph*, independently of the clique formula, and compares their entire coefficient profile with the formula. This comprises 1,043 graph cases. The recorded output is `ALL_OK cases 1043`. Exact integer arithmetic is used. This finite check tests boundary cases and the mapping but is not a substitute for the all-graph proof above.
## Relationship to prior work
Cabrera-Martínez, López-Carmona, Rios-Villamar, and Serrano-Díaz (2026, arXiv:2609.16357v1) introduced a current systematic study of **independent domination numbers** of central graphs; its abstract advertises bounds and closed numerical formulas. The present theorem concerns the complete independent-domination polynomial and the all-set bijection for arbitrary base graphs, including nonbipartite graphs with unrestricted clique number. A separately available triangle-free-base-graph enumeration is a covered special case, not part of the originality claim here. Results for higher central iterates and for total domination concern different parameters. The full text of the initiating 2026 paper could not be inspected, so overlap inside that manuscript remains a material literature risk.
## Limitations
The formula computes the central graph's independent-domination polynomial but does not assert general polynomial-time computability without a clique-number bound. It makes no claim of independent external validation or absolute novelty against inaccessible literature. For general graphs, the number of cliques may be exponential. Independent-set enumeration experiments do not establish the infinite theorem independently of the displayed proof.
## References
1. A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar, A. Serrano-Díaz, "Independent domination in central graphs", arXiv:2609.16357v1 (first public 2026-09-14), https://arxiv.org/abs/2609.16357.
2. W. Goddard and M. A. Henning, "Independent domination in graphs: a survey and recent results", *Discrete Mathematics* 313 (2013), 839–854, doi:10.1016/j.disc.2012.11.031.
